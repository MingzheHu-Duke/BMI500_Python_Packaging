import pandas as pd
import pickle
from kmeans_Digits.configuration import config


def run_test(_data, _label):
    """Do the prediction with the pretrained model

    Args:
        _data: Numpy array (n, 64)
        _label: Numpy array (n, 1)

    Returns:
        The predition result (group labels)

    """
    if _data.shape[1] != 64:
        print("The number of features is incorrect!")
        return
    if _data.shape[0] != _label.shape[0]:
        print("The lengths of features and labels do not match!")
        return
    if _label.ndim != 1:
        print("Warning! You should flatten the labels first!")
    # Load the pretrained knn model
    loaded_model = pickle.load(open(config.SAVED_MODEL_PATH +
                                    "default_knn_model.sav", 'rb'))

    # Do the prediction
    y_pred = loaded_model.predict(_data)
    print("The prediction result is: ", y_pred)
    print("{} digits have been clustered!".format(len(y_pred)))
    return y_pred


if __name__ == "__main__":
    X_test = pd.read_csv(config.DATA_PATH + config.IMAGE[1],
                         index_col=0).to_numpy()
    y_test = pd.read_csv(config.DATA_PATH + config.LABEL[1],
                         index_col=0).to_numpy().flatten()
    run_test(X_test, y_test)