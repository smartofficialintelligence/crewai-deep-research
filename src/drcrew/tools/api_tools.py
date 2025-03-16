import requests

def fetch_academic_papers(query):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&fields=title,authors,year,url"
    response = requests.get(url)
    return response.json() if response.status_code == 200 else {"error": "Failed to fetch papers"}

def fetch_twitter_data(query):
    # Add Twitter API logic here.
    pass
