import requests
import json

# Define the keywords
keywords = [
    "glioblastoma", "biomarker", "molecular marker", "prognostic marker", "predictive marker",
    "MGMT methylation", "IDH1 mutation", "EGFR amplification", "PTEN mutation", "TERT promoter mutation",
    "IL-6", "VEGF", "microRNA", "long non-coding RNA", "circulating tumor DNA (ctDNA)",
    "circulating tumor cells (CTCs)", "glioma", "brain tumor", "cancer", "tumor", "diagnosis",
    "prognosis", "treatment", "therapy", "response", "survival", "recurrence", "resistance",
    "genomics", "proteomics", "transcriptomics", "epigenetics", "immunotherapy", "targeted therapy",
    "liquid biopsy", "blood-based biomarkers", "glioblastoma MGMT methylation", "IDH1 mutation glioblastoma prognosis",
    "EGFR amplification glioblastoma treatment response", "circulating tumor DNA glioblastoma biomarker",
    "microRNA glioblastoma biomarker", "immunotherapy glioblastoma biomarker"
]

# File to save the DOIs
output_file = "glioblastoma_biomarkers_dois.txt"

# CrossRef API endpoint
API_URL = "https://api.crossref.org/works"

# Open the output file
with open(output_file, "w") as file:
    # Iterate through each keyword
    for keyword in keywords:
        params = {
            "query": keyword,
            "rows": 100,  # Number of results per query (max is 1000)
        }
        print(f"Fetching results for keyword: {keyword}")

        try:
            # Make the API request
            response = requests.get(API_URL, params=params)
            response.raise_for_status()
            data = response.json()

            # Extract DOIs from the response
            items = data.get("message", {}).get("items", [])
            for item in items:
                doi = item.get("DOI")
                if doi:
                    # Write the DOI to the file
                    file.write(doi + "\n")
        except Exception as e:
            print(f"Error fetching data for keyword '{keyword}': {e}")

print(f"DOIs saved to {output_file}")
