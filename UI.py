import tkinter as tk
import tkinter.ttk as ttk


class UI:
    def __init__(self):
        self.window = tk.Tk()
        self.WIDTH = 850
        self.HEIGHT = 360
        self.window.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.window.title('Model Creater')
        self.font = ("Microsoft Yahei", 9)# times new roman

        self._varDeclare()
        self._createframe()
        self._option()
        self._createScreen()

    def _varDeclare(self):
        self.modelStruct = []
        self.layerList = ["Conv2D", "Conv3D", "Dense", "MaxPooling2D", "MaxPooling3D", "Flatten", "Dropout"]
        self.activationList = ["relu", "softmax", "sigmoid", "tanh"]
        self.entry_Var_1 = tk.StringVar()
        self.entry_Var_1.set("")
        self.entry_Var_3 = tk.StringVar()
        self.entry_Var_3.set("")
        self.entry_Var_5 = tk.StringVar()
        self.entry_Var_5.set("Enter Input Shape")
        self.label_Var_4 = tk.StringVar()
        self.label_Var_4.set("Haven't set")
        self.check_Var_1 = tk.BooleanVar()
        self.allDirPath = []
        self.optimizerVar = tk.StringVar()
        self.optimizerVar.set("")
        self.lossVar = tk.StringVar()
        self.lossVar.set("")
        self.metricsVar = tk.StringVar()
        self.metricsVar.set("")

    def _createframe(self):
        self.optionFrame = tk.LabelFrame(self.window, text="Option", font=("Microsoft Yahei", 15, "bold"), bg="gray",
                                     fg="white", bd=5, relief=tk.GROOVE)
        self.optionFrame.place(x=0, y=0, width=self.WIDTH//3, height=self.HEIGHT//3*2)
        self.optionFrame2 = tk.LabelFrame(self.window, font=("Microsoft Yahei", 15, "bold"), bg="gray",
                                         fg="white", bd=5, relief=tk.GROOVE)
        self.optionFrame2.place(x=0, y=self.HEIGHT//3*2, width=self.WIDTH // 3, height=self.HEIGHT//3)

        self.screenFrame = tk.LabelFrame(self.window, text="Your Model", font=("Microsoft Yahei", 15, "bold"), bg="gray",
                                     fg="white", bd=5, relief=tk.GROOVE)
        self.screenFrame.place(x=self.WIDTH//3, y=0, width=self.WIDTH//3*2, height=self.HEIGHT)

    def _option(self):
        self.label_1 = tk.Label(self.optionFrame, text="Model Name", font=self.font, width=11)
        self.label_1.grid(row=0, column=0, padx=10, pady=5, ipady=2)
        self.label_2 = tk.Label(self.optionFrame, text="Choice Layer", width=11, font=self.font)
        self.label_2.grid(row=1, column=0, padx=10, pady=5, ipady=2)
        self.label_3 = tk.Label(self.optionFrame, text="Layer Option", width=11, font=self.font)
        self.label_3.grid(row=2, column=0, padx=10, pady=5, ipady=2)
        # self.label_4 = tk.Label(self.optionFrame, textvariable=self.label_Var_4, width=20, font=self.font)
        # self.label_4.grid(row=5, column=1, columnspan=2, padx=10, pady=5, ipady=2)

        self.entry_1 = tk.Entry(self.optionFrame, width=20, textvariable=self.entry_Var_1,font=self.font)
        self.entry_1.grid(row=0, column=1, padx=10, pady=5, ipady=2, columnspan=2)
        self.entry_2 = ttk.Combobox(self.optionFrame, value=self.layerList, width=17, font=self.font)
        self.entry_2.grid(row=1, column=1, padx=10, pady=5, ipady=2, columnspan=2)
        self.entry_3 = tk.Entry(self.optionFrame, width=4, textvariable=self.entry_Var_3, font=self.font)
        self.entry_3.grid(row=2, column=1, padx=10, pady=5, ipady=1, columnspan=1)
        self.entry_4 = ttk.Combobox(self.optionFrame, value=self.activationList, width=10, font=self.font)
        self.entry_4.grid(row=2, column=2, padx=10, pady=5, ipady=1, columnspan=1)
        self.entry_5 = tk.Entry(self.optionFrame, width=20, textvariable=self.entry_Var_5, font=self.font)
        self.entry_5.configure(state="disable")
        self.entry_5.grid(row=3, column=1, padx=10, pady=5, ipady=1, columnspan=2)
        self.entry_6 = ttk.Combobox(self.optionFrame, value=self.allDirPath, width=17, font=self.font)
        self.entry_6.grid(row=6, column=1, padx=10, pady=5, ipady=2, columnspan=2)
        self.entry_6.current(0)

        self.check_1 = tk.Checkbutton(self.optionFrame, text="First Layer", variable=self.check_Var_1, command=self.changeBox,
                         onvalue=1, offvalue=0, width=8, font=self.font)
        self.check_1.grid(row=3, column=0, padx=10, pady=8, ipady=1, columnspan=1)

        self.button_1 = tk.Button(self.optionFrame2, text="Add", width=15, font=self.font)
        self.button_1.grid(row=0, column=0, columnspan=1, padx=10, pady=8, ipadx=1)
        self.button_2 = tk.Button(self.optionFrame2, text="Delete", width=15, font=self.font)
        self.button_2.grid(row=0, column=1, columnspan=1, padx=10, pady=8, ipadx=1)
        self.button_3 = tk.Button(self.optionFrame2, text="Confirm", width=15, font=self.font)
        self.button_3.grid(row=1, column=0, columnspan=2, padx=10, pady=8, ipadx=1)
        self.button_4 = tk.Button(self.optionFrame, text="Load Path", width=11, font=self.font)
        self.button_4.grid(row=6, column=0, columnspan=1, padx=10, pady=5, ipady=2)
        # self.button_4 = tk.Button(self.optionFrame, text="Compile", command=self._createCWindow,width=11, font=self.font)
        # self.button_4.grid(row=5, column=0, columnspan=1, padx=10, pady=5, ipady=2)


    def _createScreen(self):
        self.scrol_y = tk.Scrollbar(self.screenFrame, orient=tk.VERTICAL)
        self.screen = tk.Listbox(self.screenFrame, yscrollcommand=self.scrol_y.set, selectbackground="gold",
                                selectmode=tk.BROWSE, height=self.HEIGHT,
                                font=self.font, bg="silver", fg="navyblue", bd=5, relief=tk.GROOVE)
        self.scrol_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrol_y.config(command=self.screen.yview)
        self.screen.pack(fill=tk.BOTH)

    def changeBox(self):
        if self.check_Var_1.get():
            self.entry_5.configure(state="normal")
            self.entry_Var_5.set("( 30, 30, 1)")
        else:
            self.entry_Var_5.set("Enter Input Shape")
            self.entry_5.configure(state="disable")

    def Loop(self):
        self.window.mainloop()


if __name__ == "__main__":
    win = UI()
    win.Loop()
