import streamlit as st
import random
import matplotlib.pyplot as plt
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="কৃষিবন্ধু স্মার্ট মাঠ", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

.block-container {
    padding-top: 1rem;
}

/* Header */
.header-box {
    background: linear-gradient(90deg, #1b4332, #2d6a4f);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 15px;
}

.header {
    font-size: 26px;
    color: white;
    font-weight: 700;
}

.subheader {
    font-size: 13px;
    color: #d8f3dc;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("""
<div class="header-box">
    <div class="header">🌱 কৃষিবন্ধু স্মার্ট মাঠ</div>
    <div class="subheader">মাঠের সেচ ও সার ব্যবস্থাপনার জন্য একটি আস্থাযোগ্য প্ল্যাটফর্ম</div>
</div>
""", unsafe_allow_html=True)

# ---------------- MODE ----------------
mode = st.radio("মোড:", ["👨‍🌾 Farmer", "🧠 Expert"], horizontal=True)

# ---------------- INIT STATE ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = [random.randint(65, 85) for _ in range(20)]

if "pump" not in st.session_state:
    st.session_state.pump = "OFF"

# ---------------- AUTO UPDATE ----------------
def auto_update():
    last = st.session_state.moisture[-1]

    # Natural change
    change = random.randint(-3, 2)
    new = max(35, min(100, last + change))

    # Smart irrigation logic
    if new < 50:
        st.session_state.pump = "ON"
        new += 3  # water increases moisture
    elif new > 80:
        st.session_state.pump = "OFF"

    st.session_state.moisture.append(new)
    st.session_state.moisture.pop(0)

auto_update()
current = st.session_state.moisture[-1]

# ---------------- STATUS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📊 মাটির অবস্থা")
    st.metric("আর্দ্রতা", f"{current}%")

with col2:
    st.subheader("💧 পাম্প অবস্থা")
    if st.session_state.pump == "ON":
        st.success("চালু")
    else:
        st.error("বন্ধ")

with col3:
    st.subheader("🌿 অবস্থা বিশ্লেষণ")

    if current < 50:
        st.error("🚨 মাটি শুকনো")
    elif current < 70:
        st.warning("⚠️ মাঝামাঝি")
    else:
        st.success("✅ ভালো অবস্থা")

# ---------------- SMART ADVICE ----------------
st.subheader("🤖 স্বয়ংক্রিয় সিদ্ধান্ত")

if current < 50:
    st.write("💧 সেচ স্বয়ংক্রিয়ভাবে চালু হয়েছে")
    st.write("🧪 ইউরিয়া প্রয়োগ করা যেতে পারে")
elif current > 85:
    st.write("🚫 অতিরিক্ত পানি — সেচ বন্ধ")
else:
    st.write("🌱 সবকিছু স্বাভাবিক চলছে")

# ---------------- GRAPH ----------------
st.subheader("📈 লাইভ ডেটা স্ট্রিম")

fig, ax = plt.subplots()
ax.plot(st.session_state.moisture)
ax.set_ylim(0, 100)
ax.set_ylabel("আর্দ্রতা (%)")

st.pyplot(fig)

# ---------------- EXPERT MODE ----------------
if mode == "🧠 Expert":
    st.subheader("🔬 সিস্টেম লজিক")

    st.write(f"Current Moisture: {current}")
    st.write(f"Pump Status: {st.session_state.pump}")

    st.write("Logic:")
    st.code("""
IF moisture < 50:
    pump = ON
IF moisture > 80:
    pump = OFF
""")

# ---------------- AUTO REFRESH ----------------
time.sleep(2)
st.rerun()
