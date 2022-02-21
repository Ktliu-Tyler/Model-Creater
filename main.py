from UI import UI
from modelTool import ModelTool
from tkinter import *
from tkinter import filedialog as fd


class modelCreator:
    def __init__(self):
        self.window = UI()
        self.modelNameList = []
        self.modelList = []
        self.model = None
        self.bttSetting()
        self.index = -1
        self.modelDic = {'layers':[]}

    def bttSetting(self):
        self.window.button_1.configure(command=self.add)
        self.window.button_2.configure(command=self.delete)
        self.window.button_3.configure(command=self.confirmModel)
        self.window.button_4.configure(command=self.openDir)
        self.window.screen.bind('<<ListboxSelect>>', self.getIndex)

    def add(self):
        modelName = self.window.entry_1.get()
        if modelName != "":
            if modelName in self.modelNameList:
                self.model = self.modelList[self.modelNameList.index(modelName)]
                print(f"[RECOMMAND] Using model {modelName} Model!")
            else:
                self.modelDic['layers'] = []
                self.model = ModelTool(modelName)
                w = self.model.createSetting()
                self.modelDic['layers'].append(w)
                self.modelNameList.append(modelName)
                self.modelList.append(self.model)
                self.window.screen.insert(0, f"model = keras.Sequential(\"{modelName}\")")
                print(f"[RECOMMAND] Create {modelName} Model!")

            self.window.entry_1.configure(state="disable")
            if self.window.entry_3.get() != "":
                units = self.window.entry_3.get()
                if self.window.check_Var_1.get():
                    if self.window.entry_5.get() != "":
                        units += f", input_shape={self.window.entry_5.get()}"
                    else:
                        print("[WARNING] Please enter the input shape!")

                if self.window.entry_4.get() != "":
                    activation = self.window.entry_4.get()
                    if self.index == -1:
                        print(len(self.modelDic['layers']))
                        index = len(self.modelDic['layers'])
                    else:
                        index = self.index + 1
                    if self.window.entry_2.get() == "Dense":
                        w = self.model.createDense(units, activation)
                        self.modelDic['layers'].insert(index, w)
                        self.window.screen.insert(index, w)
                        print(f"[RECOMMAND] Create Dense!")
                    elif self.window.entry_2.get() == "Conv2D":
                        w = self.model.createConv2D(units, (2, 2), activation)
                        self.modelDic['layers'].insert(index, w)
                        self.window.screen.insert(index, w)
                        print(f"[RECOMMAND] Create Dense!")
                    elif self.window.entry_2.get() == "Conv3D":
                        w = self.model.createConv2D(units, (2, 2, 3), activation)
                        self.modelDic['layers'].insert(index, w)
                        self.window.screen.insert(index, w)
                        print(f"[RECOMMAND] Create Dense!")
                    elif self.window.entry_2.get() == "MaxPooling2D":
                        w = self.model.createMaxPooling2D((2, 2))
                        self.modelDic['layers'].insert(index, w)
                        self.window.screen.insert(index, w)
                        print(f"[RECOMMAND] Create Dense!")
                    elif self.window.entry_2.get() == "Flatten":
                        w = self.model.createFlatten()
                        self.modelDic['layers'].insert(index, w)
                        self.window.screen.insert(index, w)
                        print(f"[RECOMMAND] Create Flatten!")
                    elif self.window.entry_2.get() == "Dropout":
                        w = self.model.createDropout(0.3)
                        self.modelDic['layers'].insert(index, w)
                        self.window.screen.insert(index, w)
                        print(f"[RECOMMAND] Create Dense!")
                    else:
                        print("[WARNING] Please choice the Layers!")
                else:
                    print("[WARNING] Please choice the activation!")
            else:
                print("[WARNING] Please enter the units!")

    def delete(self):
        print(self.index)
        if self.index != -1:
            index = self.index
            self.modelDic['layers'].pop(index)
            self.window.screen.delete(index)

    def reset(self):
        self.window.entry_2.current(0)
        self.window.entry_Var_3.set("")
        self.window.entry_1.configure(state="normal")
        self.window.entry_Var_1.set("")
        self.window.screen.delete(0, END)
        self.modelDic['layers'] = []

    def getIndex(self, event):
        try:
            object = event.widget
            self.index = int(object.curselection()[0])
            print(self.index)
        except:
            pass

    def confirmModel(self):
        modelName = self.window.entry_1.get()
        if modelName != "":
            if self.window.entry_6.get() != "Choice loading path":
                try:
                    w = self.model.writeEnd()
                    self.modelDic['layers'].append(w)
                    path = self.window.entry_6.get()
                    self.model.writeAll(self.modelDic['layers'], path)
                    print(f"[RECOMMAND] Save model successfully!(at {path})")
                    self.reset()

                except:
                    print("[WARNING] Can't save the model!")
            else:
                print("[WARNING] Please choice a loading path!")


    def openDir(self):
        self.dirPath = fd.askdirectory()
        print(f"[RECOMMAND] FIND PATH: {self.dirPath}")
        self.window.allDirPath.append(self.dirPath)
        self.window.entry_6["value"] = self.window.allDirPath


    def mainloop(self):
        self.window.Loop()


if __name__ == '__main__':
    creator = modelCreator()
    creator.mainloop()
