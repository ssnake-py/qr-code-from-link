import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import ImageTk, Image

# Create window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x500")
root.resizable(False, False)

# Generate QR function
def generate_qr():
    link = entry.get()

    if not link.strip():
        messagebox.showerror("Error", "Paste a link first.")
        return

    # Create QR
    qr = qrcode.make(link)

    # Save temporarily
    qr.save("qrcode.png")

    # Display image
    img = Image.open("qrcode.png")
    img = img.resize((250, 250))

    qr_img = ImageTk.PhotoImage(img)

    image_label.config(image=qr_img)
    image_label.image = qr_img

    status_label.config(text="QR code generated!")

# Title
title = tk.Label(
    root,
    text="QR Code Generator",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

# Input
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Button
generate_button = tk.Button(
    root,
    text="Generate QR",
    font=("Arial", 12),
    command=generate_qr
)
generate_button.pack(pady=10)

# Image display
image_label = tk.Label(root)
image_label.pack(pady=20)

# Status
status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack()

root.mainloop()
