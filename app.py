import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="কৃষিবন্ধু স্মার্ট মাঠ",
    layout="centered"
)

# ---------------- CUSTOM UI STYLE ----------------
st.markdown("""
<style>
.main-title {
    font-size:28px;
    font-weight:700;
}
.card {
    padding: 15px;
    border-radius: 12px;
    background-color: #f5f7fa;
    margin-bottom: 10px;
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

# ---------------- HEADER ----------------
st.markdown('<div class="main-title">🌾 কৃষিবন্ধু স্মার্ট মাঠ</div>', unsafe_allow_html=True)
st.caption("স্মার্ট কৃষি সহায়ক সিস্টেম")

# ---------------- TABS (APP-LIKE UI) ----------------
tab1, tab2, tab3 = st.tabs(["🏠 ড্যাশবোর্ড", "🎛️ নিয়ন্ত্রণ", "📊 বিশ্লেষণ"])

# ---------------- LIVE SIMULATION ----------------
st.session_state.moisture += random.randint(-2, 2)
st.session_state.moisture = max(0, min(100, st.session_state.moisture))
m = st.session_state.moisture

# ---------------- LOGIC ----------------
if m < 30:
    irrigation = True
    fert = "🚨 মাটি শুষ্ক — সেচ ও সার দিন"
elif m < 70:
    irrigation = False
    fert = "🌿 স্বাভাবিক অবস্থা"
else:
    irrigation = False
    fert = "🌧️ অতিরিক্ত আর্দ্রতা — সেচ বন্ধ"

# ---------------- HISTORY ----------------
st.session_state.history.append(m)
if len(st.session_state.history) > 40:
    st.session_state.history.pop(0)

# ================= TAB 1: DASHBOARD =================
with tab1:

    st.subheader("🌱 বর্তমান অবস্থা")

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("মাটির আর্দ্রতা", f"{m}%")
    st.progress(m / 100)
    st.markdown('</div>', unsafe_allow_html=True)

    if irrigation:
        st.success("💧 সেচ চালু আছে")
    else:
        st.info("🌱 সেচ বন্ধ আছে")

    st.markdown(f"**{fert}**")

# ================= TAB 2: CONTROL =================
with tab2:

    st.subheader("🎛️ নিয়ন্ত্রণ প্যানেল")

    mode = st.radio("মোড নির্বাচন", ["Farmer Mode 👨‍🌾", "Expert Mode 🧑‍🔬"])
    st.session_state.mode = mode

    col1, col2 = st.columns(2)

    with col1:
        if st.button("🌧️ বৃষ্টি"):
            st.session_state.moisture += 20

    with col2:
        if st.button("☀️ গরম"):
            st.session_state.moisture -= 20

    st.markdown("---")

    if mode == "Expert Mode 🧑‍🔬":
        st.code(f"Moisture Level: {m}%\nIrrigation: {'ON' if irrigation else 'OFF'}")

# ================= TAB 3: ANALYTICS =================
with tab3:

    st.subheader("📊 আর্দ্রতা বিশ্লেষণ")

    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(st.session_state.history, linewidth=2)
    ax.set_ylim(0, 100)
    ax.set_xlabel("সময়")
    ax.set_ylabel("আর্দ্রতা (%)")

    st.pyplot(fig)

# ---------------- AUTO REFRESH ----------------
time.sleep(1)
st.rerun()
