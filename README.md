[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  **V1.0**


# BMI500_Python_Packaging
This is the package of k means clustering models generated with sklearn package on sklean digits dataset.  
A description of this public dataset is here: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_digits.html  

**Run Time**: 0.32s  
**Minumum Memory Requirements:**: 114 MB

#Usage (Important):  
To download and install this package, there are two ways:  
**1. Install via PYPI:**  
pip install -i https://test.pypi.org/simple/ kmeans-Digits==1.0  

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
