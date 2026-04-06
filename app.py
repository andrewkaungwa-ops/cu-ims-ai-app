import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("ims_model.pkl", "rb"))

st.set_page_config(page_title="CU IMS AI Assistant", layout="centered")

st.title("🎓 Chandigarh University IMS AI Assistant")
st.subheader("Predict Student Performance & Backlog Risk")

st.markdown("Enter student details below:")

# Inputs
attendance = st.slider("Attendance (%)", 0, 100, 75)
internal = st.slider("Internal Marks (out of 40)", 0, 40, 25)
assignment = st.slider("Assignment Score (out of 10)", 0, 10, 6)
midterm = st.slider("Midterm Marks (out of 30)", 0, 30, 20)
study_hours = st.slider("Study Hours per Week", 0, 20, 10)
gpa = st.slider("Previous GPA", 0.0, 10.0, 7.0)
participation = st.selectbox("Participation", ["No", "Yes"])
backlogs = st.slider("Previous Backlogs", 0, 5, 1)
late = st.slider("Late Submissions", 0, 10, 2)
class_test = st.slider("Class Test Average", 0, 100, 70)

# Convert participation
participation_val = 1 if participation == "Yes" else 0

# Predict
if st.button("🔍 Predict Risk"):

    data = np.array([[attendance, internal, assignment, midterm,
                      study_hours, gpa, participation_val,
                      backlogs, late, class_test]])

    prediction = model.predict(data)[0]

    # Map result
    if prediction == 0:
        risk = "High Risk ❌"
        st.error("⚠️ Student is at HIGH risk of backlog!")

        st.markdown("### 📌 Recommendations:")
        st.write("- Increase study hours immediately")
        st.write("- Attend all classes")
        st.write("- Reduce late submissions")
        st.write("- Seek academic support")

    elif prediction == 1:
        risk = "Low Risk ✅"
        st.success("🎉 Student is performing well!")

        st.markdown("### 📌 Recommendations:")
        st.write("- Maintain consistency")
        st.write("- Keep attending classes")
        st.write("- Aim for higher GPA")

    else:
        risk = "Medium Risk ⚠️"
        st.warning("⚠️ Student is at MEDIUM risk")

        st.markdown("### 📌 Recommendations:")
        st.write("- Increase study time slightly")
        st.write("- Improve assignment scores")
        st.write("- Reduce absences")

    st.subheader(f"Predicted Result: {risk}")
