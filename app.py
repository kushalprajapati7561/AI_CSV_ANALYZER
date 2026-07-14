import streamlit as st

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# Load CSS
# -----------------------------
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.image(
        "https://img.icons8.com/color/96/resume.png",
        width=80
    )

    st.title("AI Resume Analyzer")

    st.markdown("---")

    selected_role = st.selectbox(
        "🎯 Target Job Role",
        [
            "Data Analyst",
            "Python Developer",
            "Machine Learning Engineer",
            "Data Scientist",
            "Business Analyst"
        ]
    )

    st.markdown("---")

    st.info(
        """
        Upload your resume and receive:

        ✅ ATS Score

        ✅ Skill Analysis

        ✅ Missing Skills

        ✅ Improvement Suggestions
        """
    )

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <h1 class='title'>
        📄 AI Resume Analyzer
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p class='subtitle'>
        Upload your resume and discover how well it matches your target role.
    </p>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Upload Section
# -----------------------------
st.markdown(
    "<h3 class='section-title'>📤 Upload Resume</h3>",
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose PDF or DOCX file",
    type=["pdf", "docx"]
)

# -----------------------------
# Dashboard Preview
# -----------------------------
if uploaded_file:

    st.success("Resume uploaded successfully!")

    # Demo Data
    ats_score = 82
    skills_found = 12
    missing_skills = 4

    # -----------------------------
    # KPI Cards
    # -----------------------------
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "📊 ATS Score",
            f"{ats_score}%"
        )

    with col2:
        st.metric(
            "🛠 Skills Found",
            skills_found
        )

    with col3:
        st.metric(
            "⚠ Missing Skills",
            missing_skills
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------
    # ATS Score Card
    # -----------------------------
    st.markdown(
        f"""
        <div class="score-box">
            <h2>ATS Resume Score</h2>
            <h1>{ats_score}%</h1>
            <p>Good Match for {selected_role}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------
    # Skills Section
    # -----------------------------
    col4, col5 = st.columns(2)

    with col4:
        st.subheader("✅ Detected Skills")

        skills = [
            "Python",
            "SQL",
            "Pandas",
            "NumPy",
            "Power BI",
            "Excel"
        ]

        for skill in skills:
            st.markdown(
                f"<span class='skill-box'>{skill}</span>",
                unsafe_allow_html=True
            )

    with col5:
        st.subheader("❌ Missing Skills")

        missing = [
            "Tableau",
            "Machine Learning",
            "Statistics",
            "Azure"
        ]

        for skill in missing:
            st.markdown(
                f"<span class='missing-skill'>{skill}</span>",
                unsafe_allow_html=True
            )

    st.markdown("---")

    # -----------------------------
    # Resume Preview
    # -----------------------------
    st.subheader("📄 Resume Preview")

    st.text_area(
        "Extracted Resume Content",
        "Resume text will appear here...",
        height=250
    )

    st.markdown("---")

    # -----------------------------
    # Suggestions
    # -----------------------------
    st.subheader("💡 Improvement Suggestions")

    st.warning(
        "Add Tableau to improve Data Analyst profile."
    )

    st.warning(
        "Add Machine Learning projects."
    )

    st.warning(
        "Include quantified achievements in projects."
    )

    st.success(
        "Strong Python and SQL foundation detected."
    )

else:

    st.info(
        "Upload a resume to start analysis."
    )

