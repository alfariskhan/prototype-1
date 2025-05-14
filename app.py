# app.py

import streamlit as st

def get_scholarships(name, caste, community, religion, annual_income, first_graduate, disability):
    scholarships = []

    tn_scholarships = [
        {"name": "🎓 First Graduate Scholarship", "criteria": {"first_graduate": "Yes"}, "link": "https://www.tn.gov.in/scholarships"},
        {"name": "📜 SC/ST Scholarship", "criteria": {"community": ["SC", "ST"]}, "link": "https://www.tn.gov.in/scholarships"},
        {"name": "🏛️ BC/MBC Scholarship", "criteria": {"community": ["BC", "MBC", "BCM"]}, "link": "https://www.tn.gov.in/scholarships"},
        {"name": "🕌 Minority Scholarship", "criteria": {"religion": ["Muslim", "Christian", "Others"]}, "link": "https://www.tn.gov.in/scholarships"},
        {"name": "♿ Differently Abled Scholarship", "criteria": {"disability": "Yes"}, "link": "https://www.tn.gov.in/scholarships"},
        {"name": "💰 Income-based Scholarship", "criteria": {"annual_income": 200000}, "link": "https://www.tn.gov.in/scholarships"}
    ]

    for scholarship in tn_scholarships:
        match = True
        for key, value in scholarship["criteria"].items():
            if key == "community" and community not in value:
                match = False
            elif key == "religion" and religion not in value:
                match = False
            elif key == "annual_income" and annual_income > value:
                match = False
            elif key == "first_graduate" and first_graduate != value:
                match = False
            elif key == "disability" and disability != value:
                match = False
        if match:
            scholarships.append(f"{scholarship['name']} - [📎 Apply Here]({scholarship['link']})")

    return scholarships

# Streamlit UI
st.set_page_config(page_title="📘 DOCGUIDE - TN Scholarship Finder", layout="centered")
st.title("📘 DOCGUIDE - Tamil Nadu Scholarship Finder")

with st.form("scholarship_form"):
    name = st.text_input("👤 Name")
    caste = st.selectbox("🏷️ Caste", ["Adi Dravidar", "Nadar", "Vanniyar", "Chettiar", "Gounder", "Thevar", "Others"])
    community = st.selectbox("🆔 Community", ["OC", "BC", "MBC", "SC", "ST", "BCM"])
    religion = st.selectbox("☪️ Religion", ["Hindu", "Muslim", "Christian", "Others"])
    annual_income = st.number_input("💵 Annual Income (INR)", min_value=0)
    first_graduate = st.radio("🎓 First Graduate", ["Yes", "No"])
    disability = st.radio("♿ Disability", ["Yes", "No"])

    submitted = st.form_submit_button("🔍 Find Scholarships")

    if submitted:
        result = get_scholarships(name, caste, community, religion, annual_income, first_graduate, disability)
        if result:
            st.markdown("### 🎯 Eligible Scholarships:")
            for r in result:
                st.markdown(f"- {r}")
        else:
            st.error("❌ No scholarships available for the given criteria.")
