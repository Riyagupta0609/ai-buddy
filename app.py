import streamlit as st
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

# Page configuration
st.set_page_config(
    page_title="AI Learning Buddy Riya",
    page_icon="🎓"
)

# Title
st.title("🎓 AI Learning Buddy Riya")

# Welcome message
st.markdown("""
Welcome! 👋

I'm **Riya**, your AI Learning Buddy.

I can help you with:

- 📖 Explain concepts
- 🌍 Give real-life examples
- 📝 Generate quizzes
- 💬 Answer your questions

Enter a topic below and choose a learning activity to get started.
""")

st.divider()

# User input
topic = st.text_input(
    "📚 Enter a Topic",
    placeholder="Example: JavaScript Functions"
)

# Activity selection
option = st.selectbox(
    "🎯 Choose Learning Activity",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Ask Anything"
    ]
)

# Riya Persona
RIYA_PERSONA = """
You are Riya, a friendly AI Learning Buddy.

Your personality:
- Friendly
- Patient
- Encouraging

Teaching Style:
- Explain concepts in simple English.
- Teach like a 15-year-old beginner.
- Explain step by step.
- Give one real-life analogy.
- Keep explanations engaging.
- End with one short question to check understanding.
"""

# Generate response
if st.button("🚀 Generate"):

    if topic.strip() == "":
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":

            prompt = f"""
{RIYA_PERSONA}

Explain the concept "{topic}" as if teaching a beginner.

Instructions:
- Use simple English.
- Explain step by step.
- Give one real-life analogy.
- Keep it short and engaging.
- End with one question to check understanding.
"""

        elif option == "Real-Life Example":

            prompt = f"""
{RIYA_PERSONA}

Give one clear real-life example of "{topic}".

Instructions:
- Choose an everyday situation.
- Explain how it relates to the topic.
- Keep it simple and easy to understand.
"""

        elif option == "Generate Quiz":

            prompt = f"""
{RIYA_PERSONA}

Create 5 multiple-choice questions on "{topic}".

Requirements:
- Each question must have 4 options (A, B, C, D).
- Only one option should be correct.
- After each question provide:
  - Correct Answer
  - Short Explanation
- Arrange questions from easy to difficult.
"""

        else:

            prompt = f"""
{RIYA_PERSONA}

Answer the following question:

{topic}

Use simple English.
Explain clearly.
Give examples whenever possible.
"""

        try:

            with st.spinner("Riya is preparing your lesson... 📖"):
                response = model.generate_content(prompt)

            st.success("Done!")

            st.subheader("📚 Riya's Response")

            st.markdown(response.text)

        except Exception as e:

            st.error(f"Error: {e}")

# Footer
st.divider()

st.caption("Made with ❤️ using Streamlit and Google Gemini")
