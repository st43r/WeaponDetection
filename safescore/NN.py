from collections import defaultdict
from pathlib import Path
import cv2
from ultralytics import YOLO
from ensemble_boxes import *

PAD = 0.1

def process_video(video_path: str):
    OUT_PATH = Path("/media/images/")

    # Load the YOLOv8 model
    model = YOLO('yolov8l.pt')
    model_weapon = [
        YOLO('safescore/best6.pt'),
        YOLO('safescore/best7.pt'),
        YOLO('safescore/best8.pt'),
    ]

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    track_history = defaultdict(int)
    frame_i = 0
    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True, verbose=True, imgsz=960, stream=False)

            # Visualize the results on the frame
            annotated_frame = results[0][results[0].boxes.cls == 0].plot()

            humans = []
            for bbox in results[0].boxes:
                if bbox.cls != 0:
                    continue
                x1, y1, x2, y2 = bbox.xyxy[0].int()
                _, _, w, h = bbox.xywh[0].int()

                x1 = max(0, int(x1 - PAD * w))
                x2 = min(frame.shape[1], int(x2 + PAD * w))
                y1 = max(0, int(y1 - PAD * h))
                y2 = min(frame.shape[0], int(y2 + PAD * h))

                humans.append([frame[y1:y2, x1:x2], [x1, y1], bbox])

            for human_img, origin, bbox_h in humans:
                weapons = [model.predict(human_img, verbose=False, imgsz=320) for model in model_weapon]

                boxes_list = []
                scores_list = []
                labels_list = []
                iou_thr = 0.5
                skip_box_thr = 0.0001
                sigma = 0.1
                for weapon_r in weapons:
                    boxes_list.append(weapon_r[0].boxes.xyxyn.cpu().numpy())
                    scores_list.append(weapon_r[0].boxes.conf.cpu().numpy())
                    labels_list.append(weapon_r[0].boxes.cls.cpu().numpy())

                boxes, scores, labels = weighted_boxes_fusion(boxes_list, scores_list, labels_list, iou_thr=iou_thr,
                                                              skip_box_thr=skip_box_thr)

                for box, score in zip(boxes, scores):
                    if score < 0.5:
                        continue
                    x1, y1, x2, y2 = box

                    x1 *= human_img.shape[1]
                    y1 *= human_img.shape[0]
                    x2 *= human_img.shape[1]
                    y2 *= human_img.shape[0]
                    x1 += origin[0]
                    y1 += origin[1]
                    x2 += origin[0]
                    y2 += origin[1]

                    annotated_frame = cv2.rectangle(
                        annotated_frame,
                        (int(x1), int(y1)),
                        (int(x2), int(y2)),
                        (255, 0, 0),
                        4
                    )
                    track_history[int(bbox_h.id)] += 1

            cv2.imwrite(str(OUT_PATH / f"{frame_i:05d}.jpg"), annotated_frame)
            yield annotated_frame, results[0].boxes, track_history
            # cv2.imshow("Weapon", annotated_frame)
            # cv2.waitKey(1)
            frame_i += 1
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()