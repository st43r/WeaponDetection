import cv2
from collections import defaultdict
from ultralytics import YOLO
import os

def get_object_count(video_path: str, path_to_model:str) -> dict:
    model = YOLO(path_to_model)

    cap = cv2.VideoCapture(video_path)

    frame_i = 0
    classes_count = defaultdict(set)

    while cap.isOpened():

        success, frame = cap.read()

        if success:
            results = model.track(frame, persist=True, verbose=False)

            for cls, track_id, xyxyn in zip(results[0].boxes.cls, results[0].boxes.id, results[0].boxes.xyxyn):
                if xyxyn[0] > 0.1 and xyxyn[2] < 0.8:
                    classes_count[int(cls.data)].add(int(track_id.data))

            frame_i += 1

        else:
            break

    cap.release()

    return classes_count

def count_numbers_in_brackets(input_str: str) -> str:
    sets = input_str.strip().split("\n")
    counts = []
    for s in sets:
        numbers = eval(s)
        counts.append(len(numbers))
    return "\n".join(map(str, counts))
def count_to_txt(data: dict, video_path: str) -> str:
    values = []
    for value_set in data.values():
        values.append("{%s}" % ", ".join(map(str, value_set)))
    values_str = "\n".join(values)
    count_str = count_numbers_in_brackets(values_str)
    output_file_path = video_path + "output.txt"
    with open(output_file_path, 'w') as file:
        file.write(count_str)

    return output_file_path