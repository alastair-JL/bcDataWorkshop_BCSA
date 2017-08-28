# bcDataWorkshop_BCSA

This is the git repository of the BCSA team of the BC data workshop:
Javier Hernandez, Alastair Jamieson-Lane, Jie Jian,  Hans Oeri,  Yi Sui,  Shanzhao Wang


In this workshop we experimented with "Bottlenecking", a particular technique used in transfer learning. 
We have created a number of scripts, and Python notebook files, all of which we hope will be helpful to those who follow.

For those working at BCSafety who make use of this:
A Visual description of the work done in this repository can be found in
BC data Workshop BC Safety Authority.pdf

For far better fleshed out discussion of transfer learning and bottlenecking, please see: 
https://medium.com/@galen.ballew/transferlearning-b65772083b47


For the sake of USING the code here, the First file to look at is: BottleNeckingOfBCSA.ipynb
This Python notebook can be used to scrape the images from the AWS, and turn them into vectors (using the pretrained Neural network of your choice) before saving said vectors to an npy file.

Once this is done, you can move on to:
ModelingWithBottleneckedImages.ipynb

This file loads the image feature vectors formed before, and trains a basic model (Very quickly). Please play around with the size and shape of the model to be trained. 
So far, we have not been able to pin down a "good" model, but we hope that the bottlenecking technique will allow you to train new models quicker (thus making finding good ones far easier).
Some basic test metrics are avaliable at the end of this file for checking the accuracy, precision and recall of your model.
There is a "Data balancing" function midway through this file that can be used to undersample labels that are overrepresented in your data... although this will often dramatically shrink the size of your data if your training data is very inbalanced.

The remaining Python notebooks are used to explore the "Daisy vs Rose" dataset we have in our files. In particular, VGG16_BottleNeck_RoseDaisy.ipynb gives a second example of out bottlenecking techniques, while VGG16Notebook_DaisyRose.ipynb attempts to use direct transfer learning (training the upper layers with the entire original network still present)
These two notebooks are less polished, but may still be useful - in particular they demonstrate transfer learning working succesfully when we have a well labeled and easily classified data set.m

photoSort.py and s3Download.py are both helper functions. 
PhotoIndex-Table1.csv is the table provided by BCSA and gives the names of photo files which we need to access.


If you have further questions, probably the easiest point of contact is me (Alastair) at aja107@math.ubc.ca .