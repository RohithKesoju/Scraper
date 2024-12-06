from flask import Flask, request, jsonify
from utils import search_articles, fetch_article_content, concatenate_content, generate_answer
import os

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        user_query = data.get('query')
        if not user_query:
            return jsonify({"error": "No query provided"}), 400

        # Step 1: Search and scrape articles
        articles = search_articles(user_query)
        if not articles:
            return jsonify({"error": "No relevant articles found"}), 404

        # Step 2: Concatenate content from the scraped articles
        content = concatenate_content(articles)

        # Step 3: Generate an answer using the LLM
        answer = generate_answer(content, user_query)

        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5001)




# from flask import Flask, request
# import os

# # Load environment variables from .env file

# app = Flask(__name__)

# @app.route('/query', methods=['POST'])
# def query():
#     """
#     Handles the POST request to '/query'. Extracts the query from the request,
#     processes it through the search, concatenate, and generate functions,
#     and returns the generated answer.
#     """
#     # get the data/query from streamlit app
#     print("Received query: ", query)
    
#     # Step 1: Search and scrape articles based on the query
#     print("Step 1: searching articles")

#     # Step 2: Concatenate content from the scraped articles
#     print("Step 2: concatenating content")

#     # Step 3: Generate an answer using the LLM
#     print("Step 3: generating answer")

#     # return the jsonified text back to streamlit
#     return 

# if __name__ == '__main__':
#     app.run(host='localhost', port=5001)
