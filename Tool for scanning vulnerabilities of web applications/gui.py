import tkinter as tk
from tkinter import messagebox
from scanner import scan_urls

def start_scan():
    urls = entry_urls.get("1.0", "end-1c").splitlines()
    if not urls:
        messagebox.showerror("Error", "Please enter URL.")
        return

    result = scan_urls(urls)

    if result:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "\n".join(result))
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "No vulnerabilies.")

root = tk.Tk()
root.title("Vulnerability Scan")
root.geometry("600x400")

frame = tk.Frame(root)
frame.pack(pady=10)

label = tk.Label(frame, text="Enter URLs (one per line):")
label.pack()

entry_urls = tk.Text(frame, height=5, width=50)
entry_urls.pack()

start_button = tk.Button(root, text="Start Scan", command=start_scan)
start_button.pack(pady=10)

output_text = tk.Text(root, height=10, width=70)
output_text.pack()

root.mainloop()
