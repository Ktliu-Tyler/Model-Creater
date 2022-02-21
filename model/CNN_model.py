import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Conv3D, MaxPooling3D, Dropout
from tensorflow.keras import optimizers, losses

def CNNModel():
	model = tf.keras.Sequential(name="CNN")
	model.add(Conv2D(filters=64, input_shape=( 30, 30, 1), kernel_size=(2, 2), activation="relu"))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Conv2D(filters=32, kernel_size=(2, 2), activation="relu"))
	model.add(MaxPooling2D(pool_size=(2, 2)))
	model.add(Flatten())
	model.add(Dense(units=128, activation="relu"))
	model.add(Dense(units=32, activation="relu"))
	model.add(Dense(units=64, activation="relu"))
	model.add(Dense(units=12, activation="relu"))
	model.add(Dense(units=24, activation="relu"))
	model.add(Dense(units=3, activation="softmax"))
	return model


if __name__ == "__main__":
	model = CNNModel()
	print(model.summary())
	model.save("./CNN_model.h5")

