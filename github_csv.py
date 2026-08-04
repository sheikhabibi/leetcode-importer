import pandas as pd
from urllib.parse import urlparse


class GitHubCSV:

    def __init__(self, url: str):
        self.url = url

    def get_questions(self):
        df = pd.read_csv(self.url)

        # Find the URL column automatically
        url_col = None
        for col in df.columns:
            if "link" in col.lower() or "url" in col.lower():
                url_col = col
                break

        if url_col is None:
            raise Exception("Couldn't find URL column in CSV")

        questions = []

        for url in df[url_col].dropna():
            
            path = urlparse(url).path.rstrip("/")
            slug = path.split("/")[-1]

            questions.append({
                "url": url,
                "slug": slug
            })

        return questions