# Load the packages
import sklearn as sk
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.preprocessing import scale
from sklearn.model_selection import train_test_split
from sklearn import cluster
from sklearn import metrics
import pandas as pd
import pickle

from KNN_Digits.visualization import visualize
from KNN_Digits.configuration import config


# Load the data from the sklearn dataset
digits = load_digits()
data = scale(digits.data)

# Print out the some properties of the dataset
print("The shape of the data set: ", data.shape)
print("The first data in the set: ", data[1])
# plt.imshow(digits.images[1], cmap="bone")
# plt.show()

# visualize.print_digits(digits.images, digits.target)


def run_training():
    # Train Test split
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test, img_train, img_test = train_test_split(
        digits.data, digits.target, digits.images.reshape(-1, 64),
        test_size=0.2, random_state=2021)

    pd.DataFrame(X_train).to_csv(config.DATA_PATH + config.IMAGE[0])
    pd.DataFrame(X_test).to_csv(config.DATA_PATH + config.IMAGE[1])
    pd.DataFrame(y_train).to_csv(config.DATA_PATH + config.LABEL[0])
    pd.DataFrame(y_test).to_csv(config.DATA_PATH + config.LABEL[1])

    # Now let's use the K-means clustering to cluster the data
    from sklearn import cluster
    model = cluster.KMeans(init="k-means++", n_clusters=config.CLUSTER_NUM,
                           random_state=config.RANDOM_STATE)
    model.fit(X_train)

    # Let's save the model
    pickle.dump(model, open(config.SAVED_MODEL_PATH +
                            "default_knn_model.sav", 'wb'))


if __name__ == "__main__":
    run_training()
