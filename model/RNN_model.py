import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D, Conv3D, MaxPooling3D, Dropout
from tensorflow.keras import optimizers, losses

def RNNModel():
	model = tf.keras.Sequential(name="RNN")
	model.add(Dense(units=256, input_shape=( 30, 30, 1), activation="relu"))
	model.add(Dense(units=128, activation="relu"))
	model.add(Dense(units=64, activation="relu"))
	model.add(Dense(units=128, activation="relu"))
	model.add(Dense(units=32, activation="relu"))
	model.add(Dense(units=16, activation="relu"))
	model.add(Dense(units=3, activation="softmax"))
	return model


if __name__ == "__main__":
	model = RNNModel()
	print(model.summary())
	model.save("./RNN_model.h5")