# Cursor Control with Hand Gesture using Yolo_v5
As with any Machine Learning project, the main challenge is to find the dataset. I couldn't find any proper dataset that I can use for this project. So I had to create my own dataset! It was very difficult to collect all these images and label them. I used more than 700 images for the training. Half of them are collected from Google, other half I clicked myself with my brother. After preparing dataset, the challenge was to train the data. I don't have powerful GPU to train this huge data. I invented that Google provides support for training dataset in Colab. They provide free GPU support. I took advantage of that and trained my dataset in Google Colab. I modified the script from Roboflow tutorial to train my dataset.
I was able to achieve 85% accuracy in training. If you like the project and want to improve the accuracy of the dataset, feel free to contact me. <br>
After training my custom dataset, I used the saved weights and modified the yolo_v5 to detect different gesture of hand.<br>
Here I used 5 types of gesture to control mouse movement. The picture below will illustrate the usage.<br>
![use of different sign]()
<br>
## Installation
To use this smoothly, GPU is almost necessary. To utilize the GPU, install CUDA first. It is highly recommended to use a virtual environment. Then follow the instruction below:<br>
- Clone this git repository
- Install all the files in requirements.txt file using `pip install -r requirements.txt`
- Now run the file using `python run_mouse_control.py`<br>

Default source is primary webcam. If you want to use phone camera or any other webcam, pass source arguments. <br>
Default image size is 640. To use different size pass img-size argument. Ex.<br>
`python run_mouse_control.py --source "give_source_here" --img-size any_size` <br>
If version of PyTorch does not match with CUDA version, upgrade PyTorch

## Instruction
