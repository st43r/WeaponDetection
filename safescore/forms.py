from django import forms
from .models import Video
from .models import CsvReport

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

class CsvForm(forms.ModelForm):
    class Meta:
        model = CsvReport
        fields = ('title', 'csv_file')