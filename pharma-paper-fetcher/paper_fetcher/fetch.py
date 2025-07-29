from Bio import Entrez
import csv

Entrez.email = "your-email@example.com"  # Replace with your email

def fetch_papers(query, max_results=20):
    handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    id_list = record["IdList"]
    handle.close()

    results = []
    for pubmed_id in id_list:
        fetch_handle = Entrez.efetch(db="pubmed", id=pubmed_id, rettype="medline", retmode="text")
        abstract = fetch_handle.read()
        fetch_handle.close()
        # You'll need to extract structured data here using Medline parser or regex
        # For demo: just store IDs
        results.append({
            "PubMed ID": pubmed_id,
            "Title": "Example Title",
            "Date": "2022",
            "Non-academic Author(s)": "John Doe",
            "Company Affiliation(s)": "Pfizer",
            "Corresponding Email": "john@example.com"
        })

    return results

def save_to_csv(data, file_path):
    keys = data[0].keys()
    with open(file_path, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)
