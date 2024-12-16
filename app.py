import streamlit as st
import requests
import uuid
import json

# Define your Gemini API endpoint URL and API Key (Bearer Token)
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?"  # Replace with actual Gemini API URL
API_KEY = "AIzaSyAhCDnQ00Z4VlWJu_onQYl7_LIf4D7-I28"  # Replace with your actual Gemini API Key


# Function to send message to Gemini API and get the LLM response
def send_message_to_gemini(session_id, user_message):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    # Define the payload for the Gemini API request
    payload = {
        "sessionId": session_id,
        "chartInput": user_message
    }

    # Send the POST request to the Gemini API endpoint
    response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(payload))

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the response from the JSON body
        response_data = response.json()
        # Assuming Gemini's response includes a field "output" or similar
        return response_data.get("Output", "No response from LLM.")
    else:
        return f"Error: Unable to get response from Gemini API. Status Code: {response.status_code}"


# Streamlit UI components
def main():
    st.title("Gemini LLM Chat Interface")
    session_id = str(uuid.uuid4())  # Generate a random session ID for each user

    # Create a text input field for the user to enter their message
    user_message = st.text_input("Enter your message:")

    if user_message:
        # Send message to Gemini API and get the LLM response
        response = send_message_to_gemini(session_id, user_message)

        # Display the response from the LLM
        st.write(f"LLM Response: {response}")


if __name__ == "__main__":
    main()
