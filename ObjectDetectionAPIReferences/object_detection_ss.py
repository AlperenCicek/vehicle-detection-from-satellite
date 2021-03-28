import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'    # Suppress TensorFlow logging
import tensorflow as tf
from object_detection.utils import label_map_util
from object_detection.utils import config_util
from object_detection.utils import visualization_utils as viz_utils
from object_detection.builders import model_builder

tf.get_logger().setLevel('ERROR')           # Suppress TensorFlow logging (2)

# Enable GPU dynamic memory allocation
gpus = tf.config.experimental.list_physical_devices('GPU')
for gpu in gpus:
    tf.config.experimental.set_memory_growth(gpu, True)

# Load pipeline config and build a detection model
configs = config_util.get_configs_from_pipeline_file("exported-models/my_model_faster_rcnn_resnet50_v1_640x640_Unfinished6ClassedDataset106_RHF_RVF_4batches_13k/pipeline.config")
model_config = configs['model']
detection_model = model_builder.build(model_config=model_config, is_training=False)

# Restore checkpoint
ckpt = tf.compat.v2.train.Checkpoint(model=detection_model)
ckpt.restore(os.path.join("exported-models/my_model_faster_rcnn_resnet50_v1_640x640_Unfinished6ClassedDataset106_RHF_RVF_4batches_13k/checkpoint", 'ckpt-0')).expect_partial()

@tf.function
def detect_fn(image):
    """Detect objects in image."""

    image, shapes = detection_model.preprocess(image)
    prediction_dict = detection_model.predict(image, shapes)
    detections = detection_model.postprocess(prediction_dict, shapes)

    return detections, prediction_dict, tf.reshape(shapes, [-1])


# %%
# Load label map data (for plotting)
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Label maps correspond index numbers to category names, so that when our convolution network
# predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility
# functions, but anything that returns a dictionary mapping integers to appropriate string labels
# would be fine.
category_index = label_map_util.create_category_index_from_labelmap("annotations/label_map.pbtxt",
                                                                    use_display_name=True)

# %%
# Define the video stream
# ~~~~~~~~~~~~~~~~~~~~~~~
# We will use `OpenCV <https://pypi.org/project/opencv-python/>`_ to capture the video stream
# generated by our webcam. For more information you can refer to the `OpenCV-Python Tutorials <https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html#capture-video-from-camera>`_
import cv2

#cap = cv2.VideoCapture(0)

# %%
# Putting everything together
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~
# The code shown below loads an image, runs it through the detection model and visualizes the
# detection results, including the keypoints.
#
# Note that this will take a long time (several minutes) the first time you run this code due to
# tf.function's trace-compilation --- on subsequent runs (e.g. on new images), things will be
# faster.
#
# Here are some simple things to try out if you are curious:
#
# * Modify some of the input images and see if detection still works. Some simple things to try out here (just uncomment the relevant portions of code) include flipping the image horizontally, or converting to grayscale (note that we still expect the input image to have 3 channels).
# * Print out `detections['detection_boxes']` and try to match the box locations to the boxes in the image.  Notice that coordinates are given in normalized form (i.e., in the interval [0, 1]).
# * Set ``min_score_thresh`` to other values (between 0 and 1) to allow more detections in or to filter out more detections.
import numpy as np
import win32api
import pyautogui
from PIL import ImageGrab
import time
def click_coordinates():
    for pos in range(2):
        state_prev = win32api.GetKeyState(0x01)
        while True:
            state_current = win32api.GetKeyState(0x01)
            if state_current != state_prev:
                pos = pyautogui.position()
                print("**Positions set: ", pos)
                return pos

def conversionOfCoordinates(coord, w, h):
    return  int(coord[0] * h), int(coord[1] * w), int(coord[2] * h), int(coord[3] * w)

def set_pos():
    print("Set the area to process")
    print("Upper corner")
    mouse_posX1, mouse_posY1 = click_coordinates()
    print("Lower corner")
    time.sleep(0.8)
    mouse_posX2, mouse_posY2 = click_coordinates()
    x = int(mouse_posX1)
    y = int(mouse_posY1)
    w = int(mouse_posX2)
    h = int(mouse_posY2)
    return x, y, w, h

x, y, w, h = set_pos()

while True:
    # Read frame from camera
    
    wholeScreen = ImageGrab.grab((x, y, w, h))
    """
    cv2.imshow("temp", np.array(wholeScreen))
    cv2.waitKey(0)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
    """

    image_np = np.array(wholeScreen)
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)

    # Things to try:
    # Flip horizontally
    # image_np = np.fliplr(image_np).copy()

    # Convert image to grayscale
    # image_np = np.tile(
    #     np.mean(image_np, 2, keepdims=True), (1, 1, 3)).astype(np.uint8)

    input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
    detections, predictions_dict, shapes = detect_fn(input_tensor)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()
    image_np_with_detections = cv2.cvtColor(image_np_with_detections, cv2.COLOR_BGR2RGB)
    img, coordinates, classOfVehicles = viz_utils.visualize_boxes_and_labels_on_image_array(
          image_np_with_detections,
          detections['detection_boxes'][0].numpy(),
          (detections['detection_classes'][0].numpy() + label_id_offset).astype(int),
          detections['detection_scores'][0].numpy(),
          category_index,
          use_normalized_coordinates=True,
          max_boxes_to_draw=500,
          min_score_thresh=.30,
          agnostic_mode=False)
    try:
        print("---CLASS & COORDINATES OF FRAME---")
        for i in range(0, len(classOfVehicles)):
            print(classOfVehicles[i], " : ", conversionOfCoordinates(coordinates[i], w, h))
    except:
        print(".....")
    # Display output
    cv2.imshow('object detection', image_np_with_detections)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()