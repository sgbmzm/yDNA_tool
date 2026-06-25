'''
Tm Wallace – חישוב מהיר לפי ספירת A/T ו־G/C (כלל אצבע)
Tm GC – נוסחה אמפירית לפי אחוז GC ואורך הרצף
Tm NN – החישוב הכי מדויק (Nearest Neighbor, תרמודינמיקה)
'''
import tkinter as tk
from tkinter import messagebox
from Bio.SeqUtils import MeltingTemp as mt
from Bio.Seq import Seq
import re

def clean_seq(seq):
    """מסיר תווים לא חוקיים ומשאיר רק ACGT"""
    seq = seq.upper()
    seq = re.sub(r'[^ACGT]', '', seq)
    return seq

def calculate():
    raw = entry.get()
    seq = clean_seq(raw)

    if len(seq) == 0:
        messagebox.showerror("Error", "הרצף ריק או לא תקין")
        return

    try:
        seq_obj = Seq(seq)

        tm_wallace = mt.Tm_Wallace(seq_obj)
        tm_gc = mt.Tm_GC(seq_obj)
        tm_nn = mt.Tm_NN(seq_obj)

        result_text.set(
            f"Clean sequence: {seq}\n\n"
            f"Tm Wallace: {tm_wallace:.2f} °C\n"
            f"Tm GC: {tm_gc:.2f} °C\n"
            f"Tm NN: {tm_nn:.2f} °C"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# ---------------- GUI ----------------
root = tk.Tk()
root.title("DNA Tm Calculator")
root.geometry("500x300")

tk.Label(root, text="הכנס רצף DNA:").pack()

entry = tk.Entry(root, width=60)
entry.pack(pady=5)

tk.Button(root, text="חשב Tm", command=calculate).pack(pady=10)

result_text = tk.StringVar()
tk.Label(root, textvariable=result_text, justify="left").pack()

root.mainloop()