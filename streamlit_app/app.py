import streamlit as st
import requests

st.title("LLM-based RAG Search System")

# Input for user query
query = st.text_input("Enter your query:")

if st.button("Search"):
    try:
        # Send the query to the Flask backend
        response = requests.post(
            "http://localhost:5001/query",
            json={"query": query}
        )
        if response.status_code == 200:
            result = response.json()
            st.success("Answer:")
            st.write(result.get("answer", "No answer available."))
        else:
            st.error(f"Error: {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        st.error(f"Connection Error: {e}")




# import streamlit as st
# import requests

# st.title("LLM-based RAG Search")

# # Input for user query
# query = st.text_input("Enter your query:")

# if st.button("Search"):
#     # Make a POST request to the Flask API
#     print("accessing ", "<Flask app string>", " with query ", query)
#     response = None # call the flask app and get response

#     # implement the flask call here
    
#     if response.status_code == 200:
#         # Display the generated answer
#         answer = response.json().get('answer', "No answer received.")
#         st.write("Answer:", answer)
#     else:
#         st.error(f"Error: {response.status_code}")
