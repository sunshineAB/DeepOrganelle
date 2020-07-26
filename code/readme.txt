Deep learning framework for organelle fluorescent image classification

Some code references:
Identifying Medical Diagnoses and Treatable Diseases by Image-Based Deep. 
DOI: http://dx.doi.org/10.17632/rscbjbr9sj.2#file-b267c884-6b3b-43ff-a992-57960f740d0f

Tensorflow pre-trained model code references:
"TensorFlow-Slim image classification model library" N. Silberman and S. Guadarrama, 2016.
https://github.com/tensorflow/models/tree/master/research/slim

DenseNet weights reference:
https://github.com/fchollet/deep-learning-models/releases/tag/v0.8

How do I get set up?
1) Install the following:

Python 3.6
Tensorflow 1.14.0
Keras 2.2.4
pycharm

2) Clone this repository

3) Untar the downloaded file

DataSet:
"DeepOrganelleDataset.zip" is the data set. Before using it, you need to divide the data set into training set, 
validation set and test set first. Then you can use "dataArgument.py" for data argument. Script "dataArgument.py"
will divide each image into 4 parts, and rotate and flip them, which can be increase by 32 times.

How to augment data:
Modify the path in "dataArgument.py", This method will first divide the data set into 4 parts, then rotate and flip.
Atfer data argument, the amount of data will be increased by 32 times.

How to train:
Open the ".py" file (such as "train_densenet_201.py") of the corresponding model, and modify the correct path, 
and then you can train this model. If you want to change the data set. please modify the "--images" in the code.

Generate ROC and confusion_matrix
First run "predict.py" repeatedly to generate prediction data for all pre-trained models. Then chose the pre-trained
 model and run "ROC.py" and "confusion_matrix.py", you can get the ROC and confusion_matrix for each model.

How to visualization:
First, open directory of "CNN", and run "CNN/train.py" to train the CNN model.
Hidden Layer Output Visualization:
--Modify the correct path and run "CNN/hidden_layer_output_visualization.py", you will get the hidden layer output 
   of each channel and the feature map with maximum activation.

Feature Visualization:
--Choose one images and feed to "CNN/feature_visualization.py", you will get the activation feature of the top
  16 activation values.

Grad-CAM:
--Modify the correct path and run "CNN/Grad-CAM.py", you will get all images of Grad-CAM. After adjusting the
  code, you will get the corresponding heatmap.

