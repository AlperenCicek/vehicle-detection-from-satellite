# vehicle-detection-from-satellite

This repository covers vehicle detection on images taken from satellite.

With The project I developed on Tensorflow 2.4 Object Detection API and Colab, you can detect and classify vehicle classes such as cars, minivans, vans, pickups, buses and trucks from satellite images!

The links to the documentation that includes the necessary setups on behalf of Tensorflow and you will need if you want to do your training on Colab are as follows;

https://tensorflow-object-detection-api-tutorial.readthedocs.io/en/latest/index.html

https://medium.com/swlh/tensorflow-2-object-detection-api-with-google-colab-b2af171e81cc


Also I used Faster R-CNN ResNet50 V1 640x640 as model on this project. If you want use another model from modelzoo, You can download from this link;

https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md#coco-trained-models

You can directly proceed to the training phase by using the datasets that I have prepared and labeled in the "annotations" folder before the relevant trainings. If you want to access the pictures in the dataset directly, you can contact me.


Some of the screenshots taken while the project was running (Detection frames come from Simulation, Google Earth and Test Datasets);


![#1](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-1-min.PNG)
![#2](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-2-min.PNG)
![#3](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-3-min.PNG)
![#4](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-4-min.PNG)
![#5](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/SS-28.03.2021-5-min.PNG)



Some of screenshots taken from label process;


![#LabelProcessSS](https://github.com/AlperenCicek/vehicle-detection-from-satellite/blob/main/example-images/LabelProcessSS-min.PNG)