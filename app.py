import streamlit as st
import random
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="KrishiBondhu Dashboard", layout="centered")

# ----------------------------
# Initialize session state
# ----------------------------
if "moisture" not in st.session_state:
    st.session_state.moisture = 40

if "history" not in st.session_state:
    st.session_state.history = []

threshold = 50

# ----------------------------
# UI Title
# ----------------------------
st.title("🌱 KrishiBondhu Smart Irrigation System")
st.caption("A low-cost intelligent irrigation simulation for rural Bangladesh")

# ----------------------------
# Control Panel
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🌵 Simulate Dry Soil"):
        st.session_state.moisture -= 20

with col2:
    if st.button("🌧️ Simulate Rain"):
        st.session_state.moisture += 20

# ----------------------------
# Automation Logic
# ----------------------------
if st.session_state.moisture < threshold:
    status = "💧 Irrigation ON"
    status_color = "red"
    st.session_state.moisture += random.randint(3, 7)
else:
    status = "🌱 Irrigation OFF"
    status_color = "green"
    st.session_state.moisture -= random.randint(2, 5)

# Keep values in range
st.session_state.moisture = max(0, min(100, st.session_state.moisture))

# Save history
st.session_state.history.append(st.session_state.moisture)
if len(st.session_state.history) > 25:
    st.session_state.history.pop(0)

# ----------------------------
# Display Metrics
# ----------------------------
st.subheader("Soil Moisture Level")
st.progress(st.session_state.moisture / 100)

st.metric("Current Moisture", f"{st.session_state.moisture}%")

st.markdown(f"### Status: :{status_color}[{status}]")

# ----------------------------
# Live Graph
# ----------------------------
st.subheader("📊 Moisture Trend Over Time")

fig, ax = plt.subplots()
ax.plot(st.session_state.history, linewidth=2)
ax.set_ylim(0, 100)
ax.set_ylabel("Moisture %")
ax.set_xlabel("Time Steps")

st.pyplot(fig)

# ----------------------------
# Auto refresh simulation
# ----------------------------
time.sleep(1)
st.rerun()