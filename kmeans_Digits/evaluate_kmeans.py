import pandas as pd
import pickle
from kmeans_Digits.configuration import config
from sklearn import metrics


def run_test():
    """Run the evaluation function on test data

    Returns:
        The prediction result (group numbers)

    """
    # Load the pretrained knn model
    loaded_model = pickle.load(open(config.SAVED_MODEL_PATH +
                                    "default_knn_model.sav", 'rb'))

    # Load the test data
    X_test = pd.read_csv(config.DATA_PATH + config.IMAGE[1], index_col=0).to_numpy()
    y_test = pd.read_csv(config.DATA_PATH + config.LABEL[1], index_col=0).to_numpy().flatten()

    # Do the prediction
    y_pred = loaded_model.predict(X_test)

    # The test performance
    print("Adjusted rand score:{:.2}".format(metrics.adjusted_rand_score(y_test, y_pred)))
    print("Homogeneity score:{:.2} ".format(metrics.homogeneity_score(y_test, y_pred)))
    print("Completeness score: {:.2} ".format(metrics.completeness_score(y_test, y_pred)))
    return y_pred


if __name__ == "__main__":
    run_test()