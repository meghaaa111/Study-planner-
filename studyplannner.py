import streamlit as st
import google.generativeai as genai

# === Configuration ===
genai.configure(api_key="AIzaSyBFWADVbjtG8W2hdrQ5EznCRkSxszIII_Q")  # 🔁 Replace with your real API key
model = genai.GenerativeModel("models/gemini-2.0-flash")

# === Streamlit UI Setup ===
st.set_page_config(page_title="🎓 Study Guide Generator", layout="centered")
st.title("📘 Smart Study Guide Generator")
st.markdown("Powered by **Gemini 2.0 Flash** — Generate personalized study guides instantly!")

# === Form for Inputs ===
with st.form("study_guide_form"):
    exam_name = st.text_input("📝 Exam Name", placeholder="e.g., JEE, NEET, Board Exams")
    time_left = st.text_input("⏳ Time Left for Exam", placeholder="e.g., 45 days, 2 months")
    strengths = st.text_area("✅ Your Strengths", placeholder="e.g., Algebra, Diagrams, Definitions")
    weaknesses = st.text_area("⚠️ Your Weaknesses", placeholder="e.g., Time management, Organic Chemistry")
    topic = st.text_input("📚 Specific Topic to Study", placeholder="e.g., Laws of Motion, French Revolution")
    format_type = st.selectbox("🗂️ Preferred Format", ["Bullet Points", "Paragraph", "Mixed"])
    language = st.selectbox("🌐 Language", ["English", "Tamil", "Hindi"])
    generate = st.form_submit_button("Generate Study Guide ✨")

# === Output Section ===
if generate:
    with st.spinner("Generating your personalized study guide..."):
        prompt = f"""
        You are an expert tutor. Help a student who is preparing for the "{exam_name}" which is in {time_left}.
        The student is good at: {strengths}.
        The student struggles with: {weaknesses}.
        Create a personalized study guide on the topic: "{topic}".
        The format should be {format_type.lower()} and the output language should be {language}.
        Include the following:
        - Key concepts (explain clearly)
        - Tips to overcome weaknesses
        - Example problems if applicable
        - Quick summary or memory tricks
        - Mistakes to avoid
        Limit it to 6–10 impactful points or sections.
        """
        try:
            response = model.generate_content(prompt)
            st.success("✅ Study Guide Ready!")
            st.subheader("🧠 Your Personalized Study Guide:")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"❌ Error: {e}")

# === Footer ===
st.markdown("---")
st.caption("🚀 Built with ❤️ using Streamlit + Gemini 2.0 Flash | Developer: [Your Name]")
