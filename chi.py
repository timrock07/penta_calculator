import tkinter as tk
from tkinter import messagebox
from scipy.stats import chi2

class ChiSquaredCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("χ²スコア計算")
        self.geometry("800x400")  # GUIのサイズを変更

        self.degrees_label = tk.Label(self, text="自由度:", font=('Meiryo UI', 14))
        self.degrees_label.place(x=200, y=50)

        self.degrees_entry = tk.Entry(self, font=('Meiryo UI', 14), bd=5)
        self.degrees_entry.place(x=300, y=50)

        self.probability_label = tk.Label(self, text="上側確率:", font=('Meiryo UI', 14))
        self.probability_label.place(x=200, y=150)

        self.probability_entry = tk.Entry(self, font=('Meiryo UI', 14), bd=5)
        self.probability_entry.place(x=300, y=150)

        self.calculate_button = tk.Button(self, text="計算", font=('Meiryo UI', 14), command=self.calculate_chi_squared_score)
        self.calculate_button.place(x=400, y=250)

        self.result_label = tk.Label(self, text="", font=('Meiryo UI', 14))
        self.result_label.place(x=250, y=350)

    def calculate_chi_squared_score(self):
        try:
            degrees = int(self.degrees_entry.get())
            probability = float(self.probability_entry.get())
            chi_squared_score = chi2.ppf(1 - probability, degrees)
            self.result_label.config(text=f"自由度 {degrees}、上側確率 {probability} のχ²スコア: {chi_squared_score:.4f}")
        except ValueError:
            self.result_label.config(text="有効な自由度と確率を入力してください")

def main():
    app = ChiSquaredCalculatorApp()
    app.mainloop()

if __name__ == "__main__":
    main()