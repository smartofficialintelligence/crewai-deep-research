import requests

def fetch_citations(query):
    url = f"https://api.crossref.org/works?query={query}&rows=5"
    response = requests.get(url)
    return response.json()['message']['items'] if response.status_code == 200 else {"error": "Failed to fetch citations"}

# Add other citation-related functions here.