# Pharma Paper Fetcher

This tool fetches PubMed research papers with non-academic authors (pharma/biotech) and returns results in CSV format.

## 🔧 Usage
```bash
python main.py -q "cancer AND drug development" -o papers.csv
```

## 🧪 Requirements
```bash
pip install -r requirements.txt
```

## 📂 Output Columns
- Title
- Publication Date
- Non-academic Author(s)
- Company Affiliation(s)
- Corresponding Email
