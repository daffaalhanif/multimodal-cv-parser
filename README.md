# Multimodal CV Parser

An AI-powered application that extracts structured information from CV documents (PDF or image) using GPT-4o and outputs the result as JSON.

---

## Features

- Upload CV in PDF or image format (JPG, PNG)
- Multi-page PDF support
- Extracts name, experience, education, and skills
- Automatically classifies hard skills and soft skills
- Structured JSON output with Pydantic validation
- Simple and interactive UI built with Gradio

---

## Tech Stack

- **LLM:** GPT-4o via LangChain + OpenAI
- **Validation:** Pydantic v2
- **UI:** Gradio
- **PDF Processing:** pdf2image + Poppler
- **Language:** Python 3.12.13

---

## Project Structure

```
multimodal-cv-parser/
├── app.py                    # Main application and Gradio UI
├── parser/
│   ├── multimodal_parser.py  # GPT-4o API call and JSON extraction
│   └── validator.py          # Output validation against schema
├── models/
│   └── schema.py             # Pydantic schema definition
├── utils/
│   └── file_handler.py       # File conversion to base64
├── requirements.txt
├── .env.example
└── .python-version
```

---

## Prerequisites

Install Poppler on your system before running the application:

| OS | Command |
|---|---|
| Mac | `brew install poppler` |
| Linux (Ubuntu/Debian) | `sudo apt-get install poppler-utils` |
| Windows | Download from [poppler-windows](https://github.com/oschwartz10612/poppler-windows/releases), then add `bin/` to PATH |

---

## Requirements

- Python 3.12.13
- Poppler (see Prerequisites above)
- OpenAI API key

---

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/daffaalhanif/multimodal-cv-parser.git
cd multimodal-cv-parser
```

**2. Create and activate virtual environment**
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
```

Open `.env` and fill in your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

---

## Running the Application

```bash
python app.py
```

Open your browser and go to `http://127.0.0.1:7860`

---

## Usage

1. Upload a CV file (PDF, JPG, or PNG)
2. Click **Analisis CV**
3. View the structured JSON output on the right

---

## Output Format

```json
{
  "nama": "John Doe",
  "experience": [
    {
      "posisi": "Software Engineer",
      "start": "Jan 2020",
      "end": "Present",
      "description": "Built backend systems using Go and Kubernetes."
    }
  ],
  "education": [
    {
      "degree": "Bachelor",
      "univ": "ITB",
      "start": null,
      "end": "2018",
      "field": "Computer Science"
    }
  ],
  "skills": {
    "hardskills": ["Python", "Go", "Kubernetes"],
    "softskills": ["Leadership", "Communication"]
  }
}
```

---

## Contributors

- [@daffaalhanif](https://github.com/daffaalhanif)
- [@HMAgiel](https://github.com/HMAgiel)
- [@syifamedina](https://github.com/syifamedina)
