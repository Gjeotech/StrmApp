import streamlit as st
import requests
import uuid
import json

# Define the URL for the n8n webhook endpoint
WEBHOOK_URL = "https://g-jeotech.app.n8n.cloud/workflow/7yZFUcNWp9LpXfC7"  # Replace with your n8n webhook URL
BEARER_TOKEN = "7yZFUcNWp9LpXfC7"  # Replace with your actual bearer token


# Function to send message to n8n webhook and get response
def send_message_to_n8n(session_id, user_message):
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json",
    }

    payload = {
        "sessionId": session_id,
        "chartInput": user_message
    }

    response = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        # Extract the response from the webhook JSON
        response_data = response.json()
        return response_data.get("Output", "No response from LLM.")
    else:
        return "Error: Unable to get response from LLM."


# Streamlit UI components
def main():
    st.title("LLM Chat Interface")
    session_id = str(uuid.uuid4())  # Generate a random session ID for each user

    # Create a text input field for the user to enter their message
    user_message = st.text_input("Enter your message:")

    if user_message:
        # Send message to the webhook and get the LLM response
        response = send_message_to_n8n(session_id, user_message)

        # Display the response from the LLM
        st.write(f"LLM Response: {response}")


if __name__ == "__main__":
    main()
