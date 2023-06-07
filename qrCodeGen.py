import qrcode
import tkinter as tk
from tkinter import messagebox as mb

def get_fields():
    text = link_entry.get()
    file_name = filename_entry.get()
    
    period = "."
    
    if period not in file_name:
        file_name = f"{file_name}.png"
    
    if text != "" & file_name != "":
        generate_qr_code(text, file_name)
        mb.showinfo("QR Code Created", f"QR Code saved as {file_name}")
    else:
        mb.showerror("Missing Link", "Error: A link is required to create a qr code.")
        

def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="green", back_color="black")
    img.save(file_name)

window = tk.Tk()
window.title("QR Code Generator")
window.geometry('500x200')

link_label = tk.Label(text="Link")
link_entry = tk.Entry(width=50)

filename_label = tk.Label(text="File Name")
filename_entry = tk.Entry(width=50)

create_qrcode = tk.Button(text="Create QR Code", command=get_fields)

link_label.pack()
link_entry.pack()
filename_label.pack()
filename_entry.pack()
create_qrcode.pack()


window.mainloop()





# window = tk.Tk()

# text = "https://www.youtube.com/watch?v=ZqS_lnqSgeY&list=LL&index=2"

# file_name = "qr_code.png"

# generate_qr_code(text, file_name)
# print(f"QR code saved as {file_name}")