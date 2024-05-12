import tkinter as tk
from tkinter import messagebox
from scipy.stats import f

class FScoreCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fスコア計算")
        self.geometry("800x400")  

        self.degrees_label_1 = tk.Label(self, text="自由度1:", font=('Meiryo UI', 14))
        self.degrees_label_1.place(x=200, y=50)

        self.degrees_entry_1 = tk.Entry(self, font=('Meiryo UI', 14), bd=5)
        self.degrees_entry_1.place(x=300, y=50)

        self.degrees_label_2 = tk.Label(self, text="自由度2:", font=('Meiryo UI', 14))
        self.degrees_label_2.place(x=200, y=100)

        self.degrees_entry_2 = tk.Entry(self,  font=('Meiryo UI', 14), bd=5)
        self.degrees_entry_2.place(x=300, y=100)

        self.probability_label = tk.Label(self, text="上側確率:", font=('Meiryo UI', 14))
        self.probability_label.place(x=200, y=150)

        self.probability_entry = tk.Entry(self,  font=('Meiryo UI', 14), bd=5)
        self.probability_entry.place(x=300, y=150)

        self.calculate_button = tk.Button(self, text="計算", font=('Meiryo UI', 14), command=self.calculate_f_score)
        self.calculate_button.place(x=400, y=200)

        self.result_label = tk.Label(self, text="", font=('Meiryo UI', 14))
        self.result_label.place(x=250, y=300)

    def calculate_f_score(self):
        try:
            degrees_1 = int(self.degrees_entry_1.get())
            degrees_2 = int(self.degrees_entry_2.get()) 
            probability = float(self.probability_entry.get())
            f_score = f.ppf(1 - probability, degrees_1, degrees_2) 
            self.result_label.config(text=f"自由度({degrees_1}、{degrees_2})、確率 {probability} のFスコア: {f_score:.4f}")
        except ValueError:
            self.result_label.config(text="有効な自由度と確率を入力してください")

def main():
    app = FScoreCalculatorApp()
    app.mainloop()

if __name__ == "__main__":
    main()