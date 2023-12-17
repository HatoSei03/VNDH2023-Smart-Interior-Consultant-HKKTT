# [VNDH2023 - HKKTT] Smart Interior Consultant

## Problem Overview

This solution provides users a tool ehancing their shopping experience in the IKEA environment

- Generate interior design based on user's style
- Recommend some IKEA items matched with their need

## Features

- Generate design based on user's prompt
- List related IKEA items

## Techniques Overview
- Language: `python`
- API Platform: `HuggingFace`
- Foundation model: `Stable Diffusion XL base 1.0`, `YOLO v8`
- Database: `MySQL`
- External libraries: `PyTorch`, `PIL`,...

## Data Flow
Step-by-step processing

- Cleaning Data
- Collecting images

### Cleaning data
- Remove records not having enough 3 size
- Remove records having "no-meaning" URL
- Reindex

### Collecting images
- Collect useful IKEA items' images from their URL
- These images used for training text-to-image model

### Labeling images
- Label some attributes: category, color
- These labels used for object detection and classification

### Final datasets

After the previous steps, we have 2 datasets:
- full cleaned dataset
- image dataset: images used for model training

## AI Model
### Text-To-Image
- Foundation model: `Stable Diffusion XL base 1.0`
- Training dataset customized fit to IKEA furniture items
- Generate recommend desgin picture based on user's prompt

### Object Detection & Classification
- Foundation model: `YOLO v8`
- Used to list IKEA furnitutre items matched with the recommeded desgin

## Built With

List the major frameworks/libraries used to bootstrap the project. For example:

- [Flask](http://flask.palletsprojects.com/en/1.1.x/) - The web framework used
- [TensorFlow](https://www.tensorflow.org/) - ML framework
- [Pillow](https://pillow.readthedocs.io/en/stable/) - Image processing library

## Authors

This solution is in the scope of VNDH 2023 Competition

Author group:
- Le Ngoc Thao (leader)
- Tran Trung Hieu
- Vo Cao Tri
- Vo Minh Khoi
- Van Tuan Kiet
