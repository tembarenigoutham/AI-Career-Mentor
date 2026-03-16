import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from career_recommendation import recommend_career

# Page configuration
st.set_page_config(page_title="AI Career Mentor", page_icon="🚀", layout="wide")

# Custom UI styling
st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#4CAF50;
}
.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
}
.skill-box{
    padding:10px;
    margin:5px;
    border-radius:8px;
    background-color:#1f2937;
}
</style>
""", unsafe_allow_html=True)

# Title
st.markdown('<p class="main-title">🚀 AI Personal Career Mentor</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Upload your resume and discover the best career path using AI</p>', unsafe_allow_html=True)

st.divider()

# Upload section
uploaded_file = st.file_uploader("📄 Upload your Resume (PDF)", type=["pdf"])

if uploaded_file is not None:

    # Extract text from resume
    text = extract_text_from_pdf(uploaded_file)

    # Extract skills
    skills = extract_skills(text)

    # Resume score calculation
    score = len(skills) * 10
    if score > 100:
        score = 100

    # Career recommendation
    career = recommend_career(skills)

    # Layout
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 Resume Score")
        st.progress(score)
        st.write(f"{score} / 100")

    with col2:
        st.subheader("💼 Recommended Career")
        st.success(career)

    st.divider()

    # Skills section
    st.subheader("🧠 Extracted Skills")

    if len(skills) == 0:
        st.warning("No skills detected in the resume.")
    else:
        for skill in skills:
            st.markdown(f"<div class='skill-box'>✔ {skill}</div>", unsafe_allow_html=True)st