import streamlit as st
from ollama import Client

# -----------------------------
# Ollama Cloud Client
# -----------------------------
client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": "Bearer bdc62b647a994959abd083479ff7d2aa.2vJqfrmjNJs3OVS8tiYVlj0g"
    }
)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="AI Coding Mentor",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Coding Mentor")
st.write("Enter your coding question or code below.")

# User input
user_input = st.text_area(
    "Enter your code/question:",
    height=250,
    placeholder="Example: Explain this Python code..."
)

# Button
if st.button("🚀 Ask AI Mentor"):

    if not user_input.strip():
        st.warning("Please enter some code or a question.")
    else:

        prompt = f"""
You are an AI Coding Mentor.

Help the student with the following input:

{user_input}

Your job is to:
1. Explain the code clearly.
2. Identify errors if present.
3. Give the corrected code if needed.
4. Explain why the error occurred.
5. Suggest improvements.

Keep the explanation beginner-friendly.
"""

        try:
            response = client.chat(
                model="gpt-oss:120b-cloud",
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            st.subheader("🤖 AI Mentor")

            # Get AI response
            answer = response["message"]["content"]

            st.write(answer)

        except Exception as e:
            st.error(f"Error: {e}")