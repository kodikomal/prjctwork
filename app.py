import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Academic Risk Classification System",
    page_icon="🎓",
    layout="wide"
)

# Sidebar - Student Details
st.sidebar.header("📋 Student Profile Input")
student_id = st.sidebar.text_input("Student Roll No. / ID", value="257")
attendance = st.sidebar.slider("Attendance Percentage (%)", 0, 100, 75)
cgpa = st.sidebar.slider("Current CGPA / Grade", 0.0, 10.0, 6.5, 0.1)
assignment_score = st.sidebar.slider("Avg Assignment Score (%)", 0, 100, 70)
backlogs = st.sidebar.number_input("Active Backlogs", min_value=0, max_value=10, value=0)

# Main Title & Header
st.title("🎓 AI-Driven Academic Risk Classification System")
st.caption("IBM SkillsBuild Project | Predictive Analytics for Student Performance & Dropout Prevention")
st.markdown("---")

# Main Dashboard layout
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Student ID", value=student_id)
with col2:
    st.metric(label="Attendance", value=f"{attendance}%")
with col3:
    st.metric(label="Current CGPA", value=f"{cgpa} / 10.0")

st.markdown("### 📊 Risk Assessment Analysis")

# Prediction Logic (Rule-based / ML Simulation)
if st.sidebar.button("Run Risk Assessment", type="primary"):
    # Calculating Risk Score
    risk_score = 0
    
    if attendance < 60:
        risk_score += 40
    elif attendance < 75:
        risk_score += 20

    if cgpa < 5.0:
        risk_score += 40
    elif cgpa < 6.5:
        risk_score += 20

    if backlogs > 2:
        risk_score += 30
    elif backlogs > 0:
        risk_score += 15

    if assignment_score < 50:
        risk_score += 20

    # Risk Classification
    st.markdown("---")
    if risk_score >= 50:
        st.error("🚨 **High Risk Level Detected!**")
        st.warning("⚠️ **Action Required:** Student requires immediate academic counseling and attendance intervention.")
    elif risk_score >= 25:
        st.warning("⚠️ **Moderate Risk Level Detected.**")
        st.info("💡 **Recommendation:** Regular monitoring and extra academicgit add app.py support advised.")
    else:
        st.success("✅ **Low Risk Level (Good Standing)**")
        st.write("🎉 Student is performing well academically.")

    # Data summary table
    st.markdown("### 📝 Input Summary")
    summary_df = pd.DataFrame({
        "Metric": ["Attendance", "CGPA", "Assignment Score", "Active Backlogs", "Calculated Risk Score"],
        "Value": [f"{attendance}%", cgpa, f"{assignment_score}%", backlogs, f"{risk_score} / 100"]
    })
    st.dataframe(summary_df, use_container_width=True)

else:
    st.info("👈 Adjust student parameters in the sidebar and click **Run Risk Assessment** to evaluate risk level.")