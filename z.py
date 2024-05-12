import tkinter as tk
from tkinter import messagebox
from scipy.stats import norm

class ZScoreCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Zスコアの計算")
        self.geometry("800x400")

        self.create_widgets()

    def create_widgets(self):
        
        self.probability_label = tk.Label(self, text="上側確率もしくはZスコアを入力してください:", font=('Meiryo UI', 14))
        self.probability_label.place(x=50, y=50)

        self.probability_entry = tk.Entry(self, font=('Meiryo UI', 14), bd=5)
        self.probability_entry.place(x=400, y=50)

        self.calculate_zscore_button = tk.Button(self, text="上側確率⇒Zスコア", font=('Meiryo UI', 14), command=self.calculate_zscore)
        self.calculate_zscore_button.place(x=200, y=150)

        self.calculate_probability_button = tk.Button(self, text="Zスコア⇒上側確率", font=('Meiryo UI', 14), command=self.calculate_probability)
        self.calculate_probability_button.place(x=450, y=150)

        self.result_label = tk.Label(self, text="", font=('Meiryo UI', 14))
        self.result_label.place(x=250, y=250)

    def calculate_zscore(self):
        try:
            probability = float(self.probability_entry.get())
            if probability < 0 or probability > 1:
                raise ValueError("確率は0から1の間である必要があります")
            z_score = norm.ppf(1 - probability)
            self.result_label.config(text=f"上側確率 {probability} のZスコア: {z_score:.4f}")
        except ValueError as e:
            messagebox.showerror("エラー", str(e))

    def calculate_probability(self):
        try:
            z_score = float(self.probability_entry.get())
            probability = norm.cdf(z_score)
            self.result_label.config(text=f"Zスコア {z_score} の上側確率: {1-probability:.4f}")
        except ValueError as e:
            messagebox.showerror("エラー", str(e))

def main():
    app = ZScoreCalculatorApp()
    app.mainloop()

if __name__ == "__main__":
    main()