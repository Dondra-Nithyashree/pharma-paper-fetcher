import argparse
from paper_fetcher.fetch import fetch_papers, save_to_csv

parser = argparse.ArgumentParser(description="Fetch PubMed papers.")
parser.add_argument("-q", "--query", required=True, help="Search query")
parser.add_argument("-o", "--output", help="Output CSV file")

args = parser.parse_args()

results = fetch_papers(args.query)

if args.output:
    save_to_csv(results, args.output)
    print(f"Results saved to {args.output}")
else:
    for row in results:
        print(row)
