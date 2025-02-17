# Tunisian BAC Exams Scraper 🎓

A Python web scraper that downloads Tunisian Baccalaureate exam papers and their corrections from bacweb.tn. This tool helps students and teachers easily access past exam papers and their solutions.

## 🌟 Features

- Downloads exam papers and corrections from bacweb.tn
- Supports all sections (Math, Sciences, Economics, etc.)
- Organizes files by section, subject, and year
- Merges correction PDFs for easy studying
- Handles both principal and control session exams
- Automatically cleans up empty folders

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/tunisian-bac-scraper.git
cd tunisian-bac-scraper
```

2. Create and activate a virtual environment:
```bash
# For Linux/Mac
python -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## 📚 Supported Sections

- Mathematics (math)
- Experimental Sciences (sciences_exp)
- Economics (economie)
- Technical (technique)
- Literature (lettres)
- Sport (sport)
- Computer Science (informatique)

## 📝 Supported Subjects

- Mathematics (mathematiques)
- Computer Science (informatique)
- Technical Studies (technique)
- Physical Sciences (sciences_physiques)
- Natural Sciences (sciences_naturelles)
- Management (gestion)
- Economics & Management (economiegestion)
- English (anglais)
- French (francais)
- Philosophy (philosophie)
- German (allemand)
- Spanish (espagnol)
- Italian (italien)
- Algorithms (algorithmique)
- Database (base_de_donnee)

## 🚀 Usage

### To Download All Exams
```bash
python scrapers/bac_scraper.py
```

### To Merge Corrections for a Subject
```bash
python utils/pdf_utils.py
```


## 📁 Project Structure

```
tunisian-bac-scraper/
│── scrapers/
│    ├── __init__.py
│    └── bac_scraper.py
│── utils/
│    ├── __init__.py
│    ├── pdf_utils.py
│    └── file_utils.py
│  
├── mappings.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Configuration

You can modify the section and subject mappings in `mappings.py` to add or update supported exam types.


## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## ⚠️ Disclaimer

This tool is for educational purposes only. Please respect the website's terms of service and use the tool responsibly.


## 📧 Contact

If you have any questions or suggestions, feel free to open an issue or contact me directly.

---
Made with ❤️ for Tunisian students