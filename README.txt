#📄 PDF to Word Converter (OCR-based GUI Tool)

This project provides a user-friendly GUI application that converts scanned PDFs into editable Word documents using **Tesseract OCR** and **Poppler**. It supports multiple languages like **Hindi**, **Telugu**, **Tamil**, **Malayalam**, and **English**.

---

## 🚀 Features

- 📤 Upload scanned PDF files  
- 🌐 Choose from multiple languages for accurate OCR  
- 🧠 Text-only output (ignores embedded images)  
- 🖥️ Easy-to-use **Tkinter** GUI  
- 📄 Output in `.docx` (Microsoft Word) format  
- 🧩 Portable `.exe` file for Windows (via PyInstaller)  

---

## 📦 Folder Structure

pdf_to_word_app/
├── pdf_to_word_gui.py # Main Python GUI app
├── tesseract/ # Tesseract OCR binary (for portability)
│ └── tesseract.exe
├── poppler/ # Poppler binary (with /bin subfolder)
│ └── bin/
│ └── pdftoppm.exe, etc.
├── README.md # This file
└── dist/
└── pdf_to_word_gui.exe # Standalone Windows executable (optional)

yaml
Copy
Edit

---

## 🖥️ Requirements

### For Python Script:
- Python 3.6+

Install dependencies:
```bash
pip install pytesseract pdf2image python-docx pillow
For .exe Build (Optional):
PyInstaller

Ensure tesseract.exe and poppler/bin/ are bundled properly.

⚙️ How to Run
✅ Run from Python script:
``` bash

python pdf_to_word_gui.py
🛠️ Run as Executable:
Download pdf_to_word_gui.exe from the dist/ folder.

Double-click to launch the app — no Python needed!

🧠 OCR Language Support
Select your OCR language in the app:

Hindi (हिंदी) → hin

Telugu (తెలుగు) → tel

Tamil (தமிழ்) → tam

Malayalam (മലയാളം) → mal

English → eng

📬 Output
A .docx file will be saved in the same folder as the original PDF, named like:

Copy
Edit
samplefile_output.docx
👤 Author
Ande Gayathri
📧 gayathriande20@gmail.com
🔗 LinkedIn

🛡️ License
MIT License – feel free to use, share, and improve.

