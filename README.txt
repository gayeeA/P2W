📝 P2W - PDF to Word Converter (OCR-based GUI Tool)





Convert scanned PDF files into editable Word documents with ease! P2W is a GUI application built using Python that leverages Tesseract OCR and Poppler to perform high-quality text extraction. It supports multiple Indian and global languages.

🚀 Features

📤 Upload scanned PDF files

🌐 Choose from multiple languages for accurate OCR

🧠 Text-only output (ignores embedded images)

🖥️ User-friendly Tkinter GUI

📄 Generates .docx (Microsoft Word) files

🧩 Windows executable via PyInstaller (no Python needed)

📁 Folder Structure

pdf_to_word_app/
├── pdf_to_word_gui.py          # Main Python GUI app
├── tesseract/                  # Tesseract OCR binary
│   └── tesseract.exe
├── poppler/                    # Poppler binary
│   └── bin/
│       └── pdftoppm.exe, etc.
├── README.md                   # Project documentation
└── dist/
    └── pdf_to_word_gui.exe     # Standalone executable

🖥️ Requirements

For Python Script:

Python 3.6+

Install dependencies:

pip install pytesseract pdf2image python-docx pillow

For Executable Build:

PyInstaller

Ensure tesseract.exe and poppler/bin are bundled properly

⚙️ How to Run

✅ Run from Source:

python pdf_to_word_gui.py

🛠️ Run Executable:

Download pdf_to_word_gui.exe from the dist/ folder

Double-click to launch (no Python required)

🌐 OCR Language Support

Select your language when using the app:

Hindi (हिंदी) → hin

Telugu (తెలుగు) → tel

Tamil (தமிழ்) → tam

Malayalam (മലയാളം) → mal

English → eng

📬 Output

Converted .docx files are saved in the same directory as the original PDF:

samplefile_output.docx

🤝 Contributing

We welcome contributions! Feel free to fork this repo and submit a pull request. For major changes, open an issue first to discuss what you’d like to change.

📄 License

This project is licensed under the MIT License.

📫 Contact

For support or questions, reach out via:

GitHub: @gayeeA

Email: your.email@example.com


