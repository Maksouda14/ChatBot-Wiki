# Wikipedia-based Chatbot

A simple chatbot that fetches information from Wikipedia based on user queries. Built with **Streamlit** for easy deployment.

## Features

- **Wikipedia Integration**: Fetches summaries from Wikipedia based on user input.
- **Simple Chat Interface**: A straightforward and interactive chat window.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Maksouda14/ChatBot-Wiki.git
   cd ChatBot-Wiki

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Open the provided URL (usually `http://localhost:8501`) to start interacting with the chatbot.


## Screenshot

![Chatbot Interface](Chatbot/chatbotScreen.png)

## Notes

This is a primitive version of the chatbot that retrieves information from Wikipedia based on basic prompts. It functions primarily with simple questions or topics, and it responds with the first few sentences from the Wikipedia summary of the topic.

### Current Limitations:
- The chatbot currently handles basic prompts and may not respond effectively to more complex or nuanced queries.
- It does not have advanced conversation management or the ability to engage in a multi-turn conversation.
- The system relies on Wikipedia summaries and may occasionally provide incomplete or vague information, especially if the query is ambiguous or has multiple meanings.
- Error handling is basic and may not cover all edge cases.

### Future Improvements:
- The addition of more advanced natural language processing capabilities to handle more complex queries.
- Incorporating features like multi-turn conversations, context retention, and more interactive user experiences.
- Integration with other knowledge sources to enhance the chatbot's ability to provide more accurate and detailed responses.


