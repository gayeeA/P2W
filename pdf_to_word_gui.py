import pytesseract
from pdf2image import convert_from_path
from docx import Document
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import sys
# Configure paths
# Get current directory
base_dir = os.path.dirname(os.path.abspath(__file__))

# Use relative paths
# tesseract_cmd_path = os.path.join(base_dir, "tesseract", "tesseract.exe")
# poppler_bin_path = os.path.join(base_dir, "poppler", "bin")
# base_dir = os.path.dirname(os.path.abspath(__file__))
# poppler_path = os.path.join(base_dir, "poppler", "bin")
# pytesseract.pytesseract.tesseract_cmd = os.path.join(base_dir, "tesseract", "tesseract.exe")

if getattr(sys, 'frozen', False):
    # Running as a bundled .exe from PyInstaller
    base_dir = sys._MEIPASS
else:
    # Running as a script
    base_dir = os.path.dirname(os.path.abspath(__file__))

# Use relative paths
tesseract_cmd_path = os.path.join(base_dir, "tesseract", "tesseract.exe")
poppler_path = os.path.join(base_dir, "poppler", "bin")

# Language map
lang_map = {
    'Hindi (हिंदी)': 'hin',
    'Telugu (తెలుగు)': 'tel',
    'Tamil (தமிழ்)': 'tam',
    'Malayalam (മലയാളം)': 'mal',
    'English': 'eng'
}

def select_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    pdf_path.set(filepath)

def convert_pdf_to_word():
    file_path = pdf_path.get()
    language_name = lang_choice.get()
    ocr_lang = lang_map.get(language_name, 'eng')

    if not file_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    try:
        pages = convert_from_path(file_path, poppler_path=poppler_path)
        doc = Document()
        for i, img in enumerate(pages):
            text = pytesseract.image_to_string(img, lang=ocr_lang)
            doc.add_paragraph(text.strip())
        output_file = os.path.splitext(file_path)[0] + '_output.docx'
        doc.save(output_file)
        messagebox.showinfo("Success", f"✅ File saved: {output_file}")
    except Exception as e:
        messagebox.showerror("Conversion Failed", str(e))

# GUI
root = tk.Tk()
root.title("Scanned PDF to Word Converter (Text Only)")

pdf_path = tk.StringVar()
lang_choice = tk.StringVar(value='Hindi (हिंदी)')

tk.Label(root, text="📄 Select PDF File:").grid(row=0, column=0, padx=10, pady=10, sticky='w')
tk.Entry(root, textvariable=pdf_path, width=50).grid(row=0, column=1, padx=10)
tk.Button(root, text="Browse", command=select_pdf).grid(row=0, column=2, padx=10)

tk.Label(root, text="🌐 Select Language:").grid(row=1, column=0, padx=10, pady=10, sticky='w')
lang_menu = ttk.Combobox(root, textvariable=lang_choice, values=list(lang_map.keys()), state='readonly')
lang_menu.grid(row=1, column=1, padx=10, sticky='w')

tk.Button(root, text="Convert to Word", command=convert_pdf_to_word, bg='green', fg='white').grid(row=2, column=1, pady=20)

root.mainloop()

