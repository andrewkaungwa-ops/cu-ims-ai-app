import streamlit as st
import pickle

# Load the trained model
model = pickle.load(open("student_score_model.pkl", "rb"))

# Title of the web app
st.set_page_config(page_title="AI Student Performance Predictor", page_icon="🎓", layout="centered")
st.title("🎓 AI Student Performance Predictor")

# Section: User Inputs
st.header("Student Details")
study_hours = st.number_input("Weekly Self Study Hours", min_value=0.0, max_value=100.0, step=0.5)
absence_days = st.number_input("Number of Absence Days", min_value=0, max_value=365, step=1)

# Button to run prediction
if st.button("Analyze Performance"):

    # Predict numeric score
    prediction = model.predict([[study_hours, absence_days]])
    score = prediction[0]

    # Display numeric score
    st.subheader("Predicted Final Score:")
    st.write(round(score, 2))

    # Show progress bar
    st.progress(min(int(score), 100))

    # Determine and display backlog risk
    st.subheader("Backlog Risk Level:")
    if score < 50:
        st.error("🔴 High Risk of Backlog")
        st.write("Recommendation: Immediate improvement needed. Increase study hours and reduce absences.")
    elif score < 65:
        st.warning("🟠 Moderate Risk of Backlog")
        st.write("Recommendation: Moderate performance. Try to study more consistently and maintain attendance.")
    else:
        st.success("🟢 Low Risk of Backlog")
        st.write("Recommendation: Good performance. Keep up the effort!")

# Footer
st.markdown("---")
st.markdown("Developed by Your Name | AI Student Score Predictor System")
