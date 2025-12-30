import streamlit as st
from groq import Groq

# ---------------- CONFIG ----------------
st.set_page_config(page_title="GradPrep AI", layout="centered")

# ---------------- API KEY ----------------
# Store your API key securely (for demo purpose shown here)
client = Groq(api_key="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")

# ---------------- UI ----------------
st.title("🎓 GradPrep – AI Interview Assistant")
st.write("Ask interview questions based on YOUR needs")

menu = st.sidebar.selectbox(
    "Navigation",
    ["Home", "AI Interview Practice", "Resume Guidance", "Progress"]
)

# ---------------- HOME ----------------
if menu == "Home":
    st.subheader("👋 Welcome Graduate")
    st.write("""
    This AI-powered app helps you:
    - Ask your own interview questions
    - Get AI-based answers & feedback
    - Improve communication & confidence
    - Prepare for real interviews
    """)

# ---------------- AI INTERVIEW ----------------
elif menu == "AI Interview Practice":
    st.subheader("🧠 AI Interview Practice")

    role = st.selectbox(
        "Select Interview Type",
        ["HR Interview", "Technical Interview", "Behavioral Interview"]
    )

    user_question = st.text_input(
        "Ask your interview question",
        placeholder="Example: How should I answer 'Tell me about yourself'?"
    )

    if st.button("Ask AI"):
        if user_question.strip() == "":
            st.warning("Please enter a question")
        else:
            with st.spinner("AI is thinking..."):
                prompt = f"""
                You are an experienced interviewer.
                Interview type: {role}
                Student question: {user_question}

                Provide:
                1. A strong interview-ready answer
                2. Explanation why this answer is good
                3. Tips to improve confidence
                """

                response = client.chat.completions.create(
                    # New supported model
                    model="llama-3.1-8b-instant",

                    messages=[{"role": "user", "content": prompt}]
                )

                st.subheader("🤖 AI Response")
                st.write(response.choices[0].message.content)

# ---------------- RESUME GUIDANCE ----------------
elif menu == "Resume Guidance":
    st.subheader("📄 Resume Guidance")
    st.write("""
    **AI Resume Tips**
    - Use role-specific keywords
    - Highlight projects & internships
    - Keep resume ATS-friendly
    - Use clear and concise points
    """)

# ---------------- PROGRESS ----------------
elif menu == "Progress":
    st.subheader("📊 Progress Tracker")
    st.progress(70)
    st.write("Interview Readiness Score: **70%**")
    st.info("Practice more questions to improve your score")
