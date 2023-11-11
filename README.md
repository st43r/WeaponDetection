## <div align="center">Команда SafeScope</div>



## <div align="center">О нашем решении📝</div>
<p>Мы представляем модель для детекции людей и оружия по видео. В основе нашей модели был использоан ансамбль из трх моделей yolov8l обученных на размеченном датасете из ~44к фотографий: https://www.linksprite.com/gun-detection-datasets

Метрики:
<br>
<a href="https://ibb.co/V3jGsXC"><img src="https://i.ibb.co/vDwWS2d/photo-2023-11-11-19-22-52.jpg" alt="photo-2023-11-11-19-22-52" border="0"></a>
</p>

## <div align="center">Стэк технологий📑</div>
<div align="center">
  <a href="https://www.python.org/doc/"><img src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54"></a>
  <a href="https://pytorch.org/docs/stable/index.html"><img src="https://img.shields.io/badge/PyTorch-%23EE4C2C.svg?style=for-the-badge&logo=PyTorch&logoColor=white"></a>
  <a href="https://opencv.github.io/cvat/docs/"><img src="https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white"></a>
  <a href="https://www.djangoproject.com/"><img src="https://img.shields.io/badge/django-%23white.svg?style=for-the-badge&logo=django&logoColor=white"></a>
  <br>
  <a href="https://github.com/ultralytics/ultralytics/actions/workflows/ci.yaml"><img src="https://github.com/ultralytics/ultralytics/actions/workflows/ci.yaml/badge.svg"></a>
</div>

## <div align="center">Быстрый старт🎢</div>
<details open>
  
#### Установка зависимостей
<p>
Для работы необходим заранее установленный python 3.10+
</p>

<p>
Для запуска проекта необходимо установить зависимости. Необходимые для работы проекта библиотеки можно посмотреть в файле <a href="https://github.com/st43r/GarbageCounter/blob/main/requirements.txt">requirements.txt</a> и установить их вручную. Также можно воспользоваться командой:
</p>
  
```bash
$ pip install -r requirements.txt
```

</details>

## <div align="center">Концепт работы программы</div>
<p>
  Видеопоток с камер передается на обученную нейронную сеть, которая выделяет всех людей и оружие на фото.

