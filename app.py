import streamlit as st
import random
import matplotlib.pyplot as plt
import time

st.set_page_config(page_title="KrishiBondhu AI System", layout="wide")

# ---------------- STATE ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = 40

if "history" not in st.session_state:
    st.session_state.history = []

if "mode" not in st.session_state:
    st.session_state.mode = "Farmer"

threshold = 50

# ---------------- HEADER ----------------
st.title("🌱 KrishiBondhu Smart Agriculture System")

mode = st.radio("Select Mode", ["Farmer Mode 👨‍🌾", "Expert Mode 🧑‍🔬"])

st.session_state.mode = mode

st.divider()

# ---------------- LIVE SIMULATION ----------------
# Natural environment change (this makes it "live")
change = random.randint(-3, 3)
st.session_state.moisture += change

# Buttons (user interaction)
col1, col2 = st.columns(2)

with col1:
    if st.button("🌧️ Simulate Rain"):
        st.session_state.moisture += 20

with col2:
    if st.button("☀️ Simulate Heat"):
        st.session_state.moisture -= 20

# clamp values
st.session_state.moisture = max(0, min(100, st.session_state.moisture))

m = st.session_state.moisture

# ---------------- MODE LOGIC ----------------
if st.session_state.mode == "Farmer Mode 👨‍🌾":

    if m < 30:
        status = "💧 সেচ দিন (পানি প্রয়োজন)"
        advice = "মাটি খুব শুকনো, দ্রুত সেচ দিন।"
    elif m < 70:
        status = "🌿 স্বাভাবিক অবস্থা"
        advice = "বর্তমানে মাটি ঠিক আছে।"
    else:
        status = "🌧️ অতিরিক্ত আর্দ্রতা"
        advice = "সেচ বন্ধ রাখুন।"

else:

    if m < 30:
        status = "CRITICAL DRY CONDITION"
        advice = "Soil moisture critically low. Irrigation system must be activated immediately."
    elif m < 70:
        status = "STABLE CONDITION"
        advice = "Soil is within optimal agricultural range."
    else:
        status = "HIGH MOISTURE LEVEL"
        advice = "Risk of over-irrigation. Drainage recommended."

# ---------------- HISTORY ----------------
st.session_state.history.append(m)
if len(st.session_state.history) > 40:
    st.session_state.history.pop(0)

# ---------------- DASHBOARD ----------------
colA, colB = st.columns(2)

with colA:
    st.metric("Soil Moisture", f"{m}%")
    st.progress(m / 100)

with colB:
    st.subheader("System Status")
    st.write(status)
    st.info(advice)

# ---------------- LIVE GRAPH ----------------
st.subheader("📊 Live Moisture Graph")

fig, ax = plt.subplots()
ax.plot(st.session_state.history, linewidth=2)
ax.set_ylim(0, 100)
ax.set_xlabel("Time")
ax.set_ylabel("Moisture")

st.pyplot(fig)

# ---------------- AUTO REFRESH ----------------
time.sleep(1)
st.rerun()