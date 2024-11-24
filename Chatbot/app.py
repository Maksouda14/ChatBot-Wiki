import streamlit as st
import wikipedia

# Initialize the Streamlit app
st.title("Chatbot with Wikipedia Integration")

# Initial greeting message
initial_message = "Hello! I am a chatbot that can help you with any topic. Feel free to ask anything, and I will retrieve the answer from Wikipedia!"

# Function to fetch the response from Wikipedia
def get_wikipedia_response(query):
    try:
        wiki_summary = wikipedia.summary(query, sentences=2)

        # Check for irrelevant content
        irrelevant_phrases = ["political", "destruction", "denazification", "unauthorized use of music"]
        if any(phrase in wiki_summary.lower() for phrase in irrelevant_phrases):
            return "Sorry, I could not find relevant information for your query."

        return wiki_summary
    
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is ambiguous. Here are some possible topics: {', '.join(e.options)}"
    
    except wikipedia.exceptions.PageError:
        return "Sorry, I could not find a page for that query."
    
    except wikipedia.exceptions.HTTPTimeoutError:
        return "Sorry, there was a timeout while fetching data from Wikipedia."

# Streamlit app interface
st.write(initial_message)

# Input box for user query
user_input = st.text_input("Ask me anything!")

if user_input:
    # Display user query
    st.write(f"**You:** {user_input}")
    
    # Get and display bot response
    response = get_wikipedia_response(user_input)
    st.write(f"**Bot:** {response}")
