import tkinter as tk
from tkinter import messagebox
from scipy.stats import t

class TScoreCalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tスコア計算")

        #GUI画面の幅と位置の設定
        self.geometry("800x400")
        self.geometry("+300+200")

        #自由度
        self.degrees_label = tk.Label(self, text="自由度", font=('Meiryo UI', 14))
        self.degrees_label.place(x=200, y=50)

        #自由度入力欄
        self.degrees_entry = tk.Entry(self, font=('Meiryo UI', 14), bd=5)
        self.degrees_entry.place(x=300, y=50)

        #確率
        self.probability_label = tk.Label(self, text="上側確率", font=('Meiryo UI', 14))
        self.probability_label.place(x=200, y=135)

        # 確率入力欄
        self.probability_entry = tk.Entry(self, font=('Meiryo UI', 14), bd=5)
        self.probability_entry.place(x=300, y=135)

        #計算ボタン
        self.calculate_button = tk.Button(self, text="計算", font=('Meiryo UI', 14), command=self.calculate_t_score)
        self.calculate_button.place(x=400, y=200)

        #結果表示
        self.result_label = tk.Label(self, text="", font=('Meiryo UI', 14))
        self.result_label.place(x=250, y=300)

    def calculate_t_score(self):
        try:
            degrees = float(self.degrees_entry.get())
            probability = float(self.probability_entry.get())
            t_score = t.ppf(1 - probability, degrees)
            self.result_label.config(text=f"自由度 {degrees}、確率 {probability} のtスコア: {t_score:.4f}")
        except ValueError as e:
            messagebox.showerror("エラー", str(e))

def main():
    app = TScoreCalculatorApp()
    app.mainloop()

if __name__ == "__main__":
    main()