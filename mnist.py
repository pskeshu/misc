# hello world program to train a model to identify digits from MNIST database

import tensorflow as tf
import matplotlib.pyplot as plt
from keras.models import Sequential, load_model
from keras.layers import Dense, Conv2D, Dropout, Flatten, MaxPooling2D
import numpy as np


def train_model():
    model = Sequential()
    model.add(Conv2D(50, kernel_size=(3, 3), input_shape=input_shape))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation="relu"))
    model.add(Dropout(0.2))
    model.add(Dense(10, activation="softmax"))

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    model.fit(x=x_train, y=y_train, epochs=40)
    model.save("mnist_50_conv_dropout-0.2.h5")
    model.evaluate(x_test, y_test)
    return model


(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


x_train = x_train.reshape(*x_train.shape, 1)
x_test = x_test.reshape(*x_test.shape, 1)

input_shape = (28, 28, 1)

x_train = x_train.astype('float32')
x_test = x_test.astype('float32')

x_train /= 255
x_test /= 255

try:
    model = load_model("mnist_50_conv_dropout-0.2.h5")
except:
    model = train_model()

fig, ax = plt.subplots(4, 4, figsize=(8, 8), dpi=100)

for a in ax.reshape(-1):
    image_index = np.random.randint(0, 10000)
    pred = model.predict(x_test[image_index].reshape(1, 28, 28, 1))
    a.imshow(x_test[image_index].reshape(28, 28), cmap='Greys')
    a.set_title(f"prediction : {pred.argmax()}", fontsize=10)
    a.grid(False)
    a.set_xticks([])
    a.set_yticks([])
plt.tight_layout()
plt.show()
