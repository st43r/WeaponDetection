from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class CsvReport(models.Model):
    title = models.CharField(max_length=200)
    csv_file = models.FileField(upload_to='csv_reports/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Analytics(models.Model):
    csv_file = models.ForeignKey(CsvReport, on_delete=models.CASCADE)
    date = models.DateField()
    tree = models.IntegerField()
    glass = models.IntegerField()
    plastic = models.IntegerField()
    metal = models.IntegerField()


class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id} uploaded on {self.created_at}"

class DetectedObject(models.Model):
    track_id = models.IntegerField(unique=True)
    image_path = models.CharField(max_length=255)