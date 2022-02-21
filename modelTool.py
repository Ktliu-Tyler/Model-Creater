import os

class ModelTool:
    def __init__(self, modelName):
        print("[RECOMMAND] Now your are using Keras to create model!")
        self.modelName = modelName
        self.model = None
        self.modelList = []

    def createSetting(self):
        w = f"import tensorflow as tf\n"\
            f"from tensorflow.keras.layers import Dense, Flatten, Conv2D,"\
            f" MaxPooling2D, Conv3D, MaxPooling3D, Dropout\n"\
            f"from tensorflow.keras import optimizers, losses" \
            f"\n" \
            f"\n"\
            f"def {self.modelName}Model():\n"\
            f"\tmodel = tf.keras.Sequential(name=\"{self.modelName}\")\n"
        return w

    def createDense(self, units, activation):
        w = f"\tmodel.add(Dense(units={units}, activation=\"{activation}\"))\n"
        return w

    def createFlatten(self):
        w = f"\tmodel.add(Flatten())\n"
        return w

    def createMaxPooling2D(self, pool_size):
        w = f"\tmodel.add(MaxPooling2D(pool_size={pool_size}))\n"
        return w

    def createConv2D(self, units, kernel_size,activation):
        w = f"\tmodel.add(Conv2D(filters={units}, kernel_size={kernel_size}, activation=\"{activation}\"))\n"
        return w

    def createConv3D(self, units, kernel_size,activation):
        w = f"\tmodel.add(Conv2D(filters={units}, kernel_size={kernel_size}, activation=\"{activation}\"))\n"
        return w

    def createDropout(self, rate):
        w = f"\tmodel.add(Dropout(rate={rate}))\n"
        return w

    def Adam(self, option):
        w = f"\topt = optimizers.Adam({option})"
        return w

    def SGD(self, option):
        w = f"\topt = optimizers.SGD({option})"
        return w

    def Adadelta(self, option):
        w = f"\topt = optimizers.Adadelta({option})"
        return w

    def writeEnd(self):
        w = f"\treturn model\n" \
            f"\n" \
            f"\n" \
            f"if __name__ == \"__main__\":\n" \
            f"\tmodel = {self.modelName}Model()\n" \
            f"\tprint(model.summary())\n" \
            f"\tmodel.save(\"./{self.modelName}_model.h5\")"
        return w

    def writeAll(self, allw, path):
        path = os.path.join(f"{path}", f"{self.modelName}_model.py")
        with open(path, "w") as f:
            print("=========================The model structure=====================\n")
            for i in allw:
                f.write(i)
                print(i)
            print("=================================================================\n")
        return allw








