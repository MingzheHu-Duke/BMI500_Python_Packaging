# Let's visualize some of the images
import matplotlib.pyplot as plt


def print_digits(images, _labels, _num=10):
    """Visualize the hand written digits together with the label

    Args:
        images: numpy array of the hand written digits images
        _labels: The corresponding labels of the images
        _num: Number of images to display

    Returns:
        None

    """
    fig = plt.figure(figsize=(16, 16))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, hspace=0.05,
                        wspace=0.05)
    i = 0
    while i < _num and i < images.shape[0]:
        # plot the images in a matrix of 20x20
        p = fig.add_subplot(12, 12, i + 1, xticks=[], yticks=[])
        p.imshow(images[i], cmap=plt.cm.bone)
    # label the image with the target value
        p.text(0, 14, str(_labels[i]))
        i = i + 1
    plt.show()

