# vehicle-detection-from-satellite

This repository covers vehicle detection on images taken from satellite.

With The project I developed on Tensorflow 2.4 Object Detection API / YOLOv4-Darknet and Colab, you can detect and classify vehicle classes such as cars, minivans, vans, pickups, buses and trucks from satellite images!

The links to the documentation that includes the necessary setups on behalf of Tensorflow 2.4 Object Detection API / YOLOv4-Darknet and you will need if you want to do your training on Colab are as follows;

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/index.html

https://github.com/AlexeyAB/darknet

https://medium.com/swlh/tensorflow-2-object-detection-api-with-google-colab-b2af171e81cc

Those who want to use YOLOv3 - YOLOv4 can follow this tutorial.

https://github.com/AlexeyAB/darknet


Also I used Faster R-CNN ResNet50 V1 640x640 as model on this project. If you want use another model from modelzoo, You can download from this link;

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md#coco-trained-models

You can directly proceed to the training phase by using the datasets that I have prepared and labeled in the "annotations" and xml folder before the relevant trainings (Tensorflow 2.4 Object Detection API). For YOLOv4-Darknet training, you can check txt folder. If you want to access the pictures in the dataset directly, you can contact me. (alperencicek1998@gmail.com)


Some of the screenshots taken while the project was running (Detection frames come from Simulation, Google Earth and Test Datasets, Tensorflow 2.4 Object Detection API - Faster R-CNN ResNet50 V1 640x640);


![#1](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-1-min.PNG)
![#2](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-2-min.PNG)
![#3](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-3-min.PNG)
![#4](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-4-min.PNG)
![#5](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-5-min.PNG)



Some of screenshots taken from label process;


![#LabelProcessSS](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/LabelProcessSS-min.PNG)
