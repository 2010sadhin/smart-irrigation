import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="কৃষিবন্ধু মাঠসাথী",
    layout="wide"   # important for responsive width
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Make content centered but flexible */
.block-container {
    max-width: 1200px;
    padding: 1rem;
}

/* Card style */
.card {
    padding: 15px;
    border-radius: 12px;
    background-color: #f5f7fa;
    margin-bottom: 15px;
}

/* Responsive title */
.title {
    font-size: 32px;
    font-weight: 700;
}

@media (max-width: 768px) {
    .title {
        font-size: 22px;
    }
}

</style>
""", unsafe_allow_html=True)

# ---------------- STATE ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = 45

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- HEADER ----------------
st.markdown('<div class="title">🌾 কৃষিবন্ধু মাঠসাথী</div>', unsafe_allow_html=True)
st.caption("স্মার্ট কৃষি সহায়ক সিস্টেম")

st.divider()

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
if len(st.session_state.history) > 50:
    st.session_state.history.pop(0)

# ---------------- DASHBOARD GRID ----------------
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.metric("মাটির আর্দ্রতা", f"{m}%")
    st.progress(m / 100)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    if irrigation:
        st.success("💧 সেচ চালু আছে")
    else:
        st.info("🌱 সেচ বন্ধ আছে")

    st.write(fert)

    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- CONTROLS ----------------
st.subheader("🎛️ নিয়ন্ত্রণ")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🌧️ বৃষ্টি", use_container_width=True):
        st.session_state.moisture += 20

with c2:
    if st.button("☀️ গরম", use_container_width=True):
        st.session_state.moisture -= 20

with c3:
    if st.button("💧 সেচ দিন", use_container_width=True):
        st.session_state.moisture += 15

# ---------------- GRAPH ----------------
st.subheader("📊 আর্দ্রতা বিশ্লেষণ")

fig, ax = plt.subplots(figsize=(10, 4))  # wide for laptop, scales for mobile
ax.plot(st.session_state.history, linewidth=2)
ax.set_ylim(0, 100)
ax.set_xlabel("সময়")
ax.set_ylabel("আর্দ্রতা (%)")

st.pyplot(fig, use_container_width=True)

# ---------------- AUTO REFRESH ----------------
time.sleep(1)
st.rerun()
