import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# ---------------- PAGE CONFIG (RESPONSIVE) ----------------
st.set_page_config(
    page_title="ক্ষেত নিয়ন্ত্রণ সিস্টেম",
    layout="centered"   # BEST for mobile + laptop balance
)

# ---------------- OPTIONAL MOBILE TIGHT CSS ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 1rem;
    padding-left: 1rem;
    padding-right: 1rem;
}
</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = 45

if "history" not in st.session_state:
    st.session_state.history = []

if "mode" not in st.session_state:
    st.session_state.mode = "Farmer"

threshold = 50

# ---------------- HEADER ----------------
st.title("🌾 ক্ষেত নিয়ন্ত্রণ স্মার্ট সিস্টেম")
st.caption("মাঠের সেচ ও সার ব্যবস্থাপনার জন্য একটি নিয়ন্ত্রণ প্যানেল")

st.divider()

# ---------------- MODE ----------------
mode = st.radio("মোড নির্বাচন করুন", ["Farmer Mode 👨‍🌾", "Expert Mode 🧑‍🔬"])
st.session_state.mode = mode

st.divider()

# ---------------- NATURAL CHANGE (LIVE SIMULATION) ----------------
st.session_state.moisture += random.randint(-3, 3)

# ---------------- CONTROLS (RESPONSIVE SAFE) ----------------
col1, col2 = st.columns(2)

with col1:
    if st.button("🌧️ বৃষ্টি"):
        st.session_state.moisture += 20

with col2:
    if st.button("☀️ গরম"):
        st.session_state.moisture -= 20

# clamp values
st.session_state.moisture = max(0, min(100, st.session_state.moisture))

m = st.session_state.moisture

# ---------------- LOGIC ----------------
irrigation = False

if m < 30:
    irrigation = True
    fert = "⚠️ সার প্রয়োগ প্রয়োজন (মাটি খুব শুষ্ক)"
elif m < 70:
    fert = "🌿 সার স্বাভাবিক অবস্থায় আছে"
else:
    fert = "🌧️ অতিরিক্ত আর্দ্রতা — সার প্রয়োজন নেই"

# ---------------- MODE OUTPUT ----------------
if st.session_state.mode == "Farmer Mode 👨‍🌾":

    if irrigation:
        status = "💧 সেচ চালু হয়েছে"
    else:
        status = "🌱 সেচ বন্ধ আছে"

    advice = fert

else:

    status = f"IRRIGATION SYSTEM: {'ACTIVE' if irrigation else 'OFF'}"
    advice = f"Moisture: {m}% | Threshold Logic Applied"

# ---------------- HISTORY ----------------
st.session_state.history.append(m)
if len(st.session_state.history) > 40:
    st.session_state.history.pop(0)

# ---------------- DASHBOARD ----------------
st.subheader("🎛️ নিয়ন্ত্রণ প্যানেল")

st.metric("মাটির আর্দ্রতা", f"{m}%")
st.progress(m / 100)

st.success(status)
st.info(advice)

# ---------------- ALERT SECTION ----------------
st.subheader("🌱 কৃষি পরামর্শ")

if m < 30:
    st.error("🚨 জরুরি: সেচ ও সার প্রয়োগ করুন")
elif m < 70:
    st.warning("ℹ️ পর্যবেক্ষণ করুন")
else:
    st.success("✅ অতিরিক্ত আর্দ্রতা — সেচ বন্ধ রাখুন")

# ---------------- GRAPH (MOBILE FRIENDLY SIZE) ----------------
st.subheader("📊 মাঠের আর্দ্রতা পরিবর্তন")

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(st.session_state.history, linewidth=2)
ax.set_ylim(0, 100)
ax.set_xlabel("সময়")
ax.set_ylabel("আর্দ্রতা (%)")

st.pyplot(fig)

# ---------------- LIVE UPDATE ----------------
time.sleep(1)
st.rerun()
