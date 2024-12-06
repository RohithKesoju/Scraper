import os
import requests
from bs4 import BeautifulSoup
import openai
from dotenv import load_dotenv

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def search_articles(query):
    """
    Searches for articles using the Serper API.
    """
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY}
    payload = {"q": query, "num": 5}
    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        results = response.json().get('organic', [])
        articles = [{"url": item["link"], "title": item["title"]} for item in results]
        return articles
    return []

def fetch_article_content(url):
    """
    Scrapes content from an article URL using BeautifulSoup.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = [p.get_text() for p in soup.find_all('p')]
    return "\n".join(paragraphs)

def concatenate_content(articles):
    """
    Concatenates content from a list of articles.
    """
    content = ""
    for article in articles:
        content += f"Title: {article['title']}\n"
        content += fetch_article_content(article["url"])
        content += "\n\n"
    return content

def generate_answer(content, query):
    """
    Generates an answer using OpenAI's GPT model.
    """
    openai.api_key = OPENAI_API_KEY
    prompt = f"Context:\n{content}\n\nUser Query: {query}\nAnswer:"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].text.strip()


# import os


# # Load API keys from environment variables
# SERPER_API_KEY = None
# OPENAI_API_KEY = None


# def search_articles(query):
#     """
#     Searches for articles related to the query using Serper API.
#     Returns a list of dictionaries containing article URLs, headings, and text.
#     """
#     articles = None
#     # implement the search logic - retrieves articles
#     return articles


# def fetch_article_content(url):
#     """
#     Fetches the article content, extracting headings and text.
#     """
#     content = ""
#     # implementation of fetching headings and content from the articles

#     return content.strip()


# def concatenate_content(articles):
#     """
#     Concatenates the content of the provided articles into a single string.
#     """
#     full_text = ""
#     # formatting + concatenation of the string is implemented here

#     return full_text


# def generate_answer(content, query):
#     """
#     Generates an answer from the concatenated content using GPT-4.
#     The content and the user's query are used to generate a contextual answer.
#     """
#     # Create the prompt based on the content and the query
#     response = None
    
#     # implement openai call logic and get back the response
#     return response
