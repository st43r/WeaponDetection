from django.shortcuts import render
from .models import Video, CsvReport
from django.shortcuts import render, redirect
from .models import Video
from .forms import VideoForm
from .forms import CsvForm
from .models import ImageModel
from .models import DetectedObject
from .NN import process_video

def home(request):
    latest_videos = Video.objects.all().order_by('-uploaded_at')[:2]
    csv_reports = CsvReport.objects.all().order_by('-uploaded_at')
    return render(request, 'home.html', {'latest_videos': latest_videos, 'csv_reports': csv_reports})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()
            process_and_analyze_video(video.video_file.path) # Фоновая обработка видео
            return redirect('home')
    else:
        form = VideoForm()
    return render(request, 'upload_video.html', {'form': form})

def process_and_analyze_video(video_path):
    track_history = {}
    for _, _, history in process_video(video_path):
        for track_id, count in history.items():
            track_history[track_id] = track_history.get(track_id, 0) + count

    for track_id, count in track_history.items():
        if count > 50:
            # Здесь вам нужно определить, как получить путь к изображению для данного track_id
            image_path = get_image_path_for_id(track_id)
            DetectedObject.objects.update_or_create(
                track_id=track_id,
                defaults={'image_path': image_path}
            )
    frequent_ids = {track_id: count for track_id, count in track_history.items() if count > 50}

    return frequent_ids

def get_image_path_for_id(track_id):
    # Базовый путь к папке с изображениями
    base_path = '/media/images/'

    # Формируем имя файла изображения
    image_filename = f"{track_id}.jpg"

    # Полный путь к изображению
    full_path = base_path + image_filename

    return full_path

def upload_csv(request):
    if request.method == 'POST':
        form = CsvForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # или любой другой URL, куда вы хотели бы перенаправить после успешной загрузки
    else:
        form = CsvForm()
    return render(request, 'upload_csv.html', {'form': form})

def analytics(request):
    reports = CsvReport.objects.all()
    data_for_charts = []

    for report in reports:
        with open(report.csv_file.path, 'r') as file:
            lines = file.readlines()
            data = {
                "title": report.title,
                "tree": int(lines[0].strip()),
                "glass": int(lines[1].strip()),
                "plastic": int(lines[2].strip()),
                "metal": int(lines[3].strip())
            }
        data_for_charts.append(data)

    return render(request, 'analytics.html', {"data_for_charts": data_for_charts})

def upload_image(request):
    if request.method == 'POST':
        image_file = request.FILES.get('image')
        new_image = ImageModel.objects.create(image=image_file)
        return render(request, 'upload_success.html', {'new_image': new_image})
    return render(request, 'upload.html')

def home(request):
    detected_objects = DetectedObject.objects.all()
    return render(request, 'home.html', {'detected_objects': detected_objects})