[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  **V1.0**


# BMI500_Python_Packaging  
**!If you could not install the package:**  
1. Check if you have the right python version  
2. Check if you have the latest pip version   
 
**If there are any missing support package:**   
Please install them manually, in case I missed any in the requirements.txt  

This is the package of k means clustering models generated with sklearn package on sklean digits dataset.  
A description of this public dataset is here: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html  

**Run Time**: 0.32s  
**Minumum Memory Requirements:**: 114 MB

## Usage (Important):  
**Minimum Python Requirement:** 3.7.12 (best if python 3.8)  
**Upgrade Your pip!** $pip install --upgrade pip  
  
Here is the video guide:  
[![IMAGE ALT TEXT](http://img.youtube.com/vi/XVJkmyreTvw/0.jpg)](http://www.youtube.com/watch?v=XVJkmyreTvw "Video Tutorial")

To download and install this package, there are two ways:  
<strike>**1. Install via PYPI:**</strike>  
<strike>pip install -i https://test.pypi.org/simple/ kmeans-Digits==1.0</strike>  

**2. Clone to local and install:**  
git clone https://github.com/MingzheHu-Duke/BMI500_Python_Packaging.git  
pip install -e BMI500_Python_Packaging/  

Here are the functions in the package you may want to call:   
**Import the Package:**  
\>>import kmeans_Digits  

**Train the base K means clustering model:**  
\>>from kmeans_Digits import train_kmeans  
\>>train_kmeans.run_training()  
This will train the base kmeans model with the training set and save the trained model locally  

**Evaluate the pretrained model:**
\>>from kmeans_Digits import evaluate_kmeans  
\>>evaluate_kmeans.run_test()  
This will evaluate the performance of our pretrained model on the test set

**Predict new data:**  
\>>from kmeans_Digits import predict  
\>>predict.run_test(_data, _label)  
This will do the prediction with our pretrained model. Notice that the _data and _label should be in the same structure  
as the sklean digits data.  
