"""
Script for setting the configurations for training the Mask-RCNN model to our dataset.
Derives from the Config class of the original model and overrides values.
"""

import os
import sys

# Root directory of the project
ROOT_DIR = os.path.abspath("../../")

# Import Mask RCNN
sys.path.append(os.path.join(ROOT_DIR, "Mask_RCNN"))  # To find local version of the library
from mrcnn.config import Config


"""
Training Configurations for the Dataset
"""
class FMPAConfig(Config):

    NAME = "FMPA"

    IMAGES_PER_GPU = 1

    GPU_COUNT = 1

    # Number of classes (including background)
    NUM_CLASSES = 1 + 1  # Background +  RBCs

    # Number of training steps per epoch
    STEPS_PER_EPOCH = 338

    # Number of validation steps should be the same as the length of the validation dataset
    VALIDATION_STEPS = 101

    # Backbone network architecture
    BACKBONE = "resnet101" # 'resnet50' or 'resnet101'

    # Length of square anchor side in pixels
    RPN_ANCHOR_SCALES = (8, 16, 32, 64, 128) # (16, 32, 64, 128, 256)

    USE_MINI_MASK = False

    # Images are resized 
    IMAGE_MIN_DIM = 1024 # 1024 or 512
    IMAGE_MAX_DIM = 1024 # 1024 or 512

    # Each image only has handful of cells to be detected
    DETECTION_MAX_INSTANCES = 15

    # Learning rate and momentum
    LEARNING_RATE = 0.001
    LEARNING_MOMENTUM = 0.9

    # Skip detections with < 80% confidence
    DETECTION_MIN_CONFIDENCE = 0.8

    USE_MINI_MASK = False
    RUN_EAGERLY = False

"""
Inference Configurations for the Dataset
"""
class InferenceConfig(FMPAConfig):
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

    # Don't resize imager for inferencing
    IMAGE_RESIZE_MODE = "pad64"

    USE_MINI_MASK = False
    RUN_EAGERLY = False