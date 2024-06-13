# Cyclist Detection

A project developed using YOLOv8 for detecting cyclists and adding labels to live video. This project aims to provide a real-time detection system that enhances the safety of cyclists by utilizing advanced computer vision techniques.

## Project Overview

This project, developed in collaboration with @serapgunes, detects cyclists in real-time and overlays labels on them. Our future plans include migrating this project to a VR (Virtual Reality) platform as Mixed Reality to enhance its perspective and adapt it to real-time travel.

The goal of our project is to provide practical solutions with high-accuracy models and use technology innovatively to improve the safety of cyclists.

## Project Process

- We trained the model using 8,000 labeled data augmented by the Augmentation method and YOLOv8 model.
- During the training and testing process, 70% of the data was used for training, 20% for testing, and 10% for validation.

## Analysis and Results
![confusion_matrix](https://github.com/tetrakup/cyclist_detection/assets/97338156/b296f275-c918-42c6-83c1-09f6bf746090){:width="300px" height="300px"}

**Performance Metrics:**
- Accuracy: 84.6%
- Recall: 96.5%
- Precision: 87.3%
- F1 Score: 91.7%

![projeuygulama](https://github.com/tetrakup/cyclist_detection/assets/97338156/32a70baa-bf38-4268-835c-78a9c94811cc)


These results indicate that our model can detect cyclists with high accuracy and is successful in its task.



## Requirements

Make sure you have the following libraries installed. You can install them using the command:
```sh
pip install -r requirements.txt
```

"Stock footage used in the project introduction is provided by Videvo, downloaded from www.videvo.net."

