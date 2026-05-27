import streamlit as st
import random
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="কৃষিবন্ধু স্মার্ট মাঠ", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>

.block-container {
    padding-top: 1.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

/* Header */
.header-box {
    background: linear-gradient(90deg, #1b4332, #2d6a4f);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}

.header {
    font-size: 26px;
    color: white;
    font-weight: 700;
}

.subheader {
    font-size: 14px;
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
mode = st.radio("মোড নির্বাচন:", ["👨‍🌾 Farmer Mode", "🧠 Expert Mode"], horizontal=True)

# ---------------- LIVE DATA ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = [random.randint(60, 90) for _ in range(20)]

def update():
    if len(st.session_state.moisture) == 0:
        st.session_state.moisture = [70]

    val = st.session_state.moisture[-1] + random.randint(-2, 2)
    val = max(40, min(100, val))

    st.session_state.moisture.append(val)
    st.session_state.moisture.pop(0)

update()
current = st.session_state.moisture[-1]

# ---------------- STATUS ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 বর্তমান অবস্থা")
    st.metric("মাটির আর্দ্রতা", f"{current}%")

    if current < 50:
        st.error("🚨 পানি দিন")
    elif current < 70:
        st.warning("⚠️ অল্প পানি দরকার")
    else:
        st.success("✅ সব ঠিক আছে")

with col2:
    st.subheader("🌾 স্মার্ট পরামর্শ")

    if current < 50:
        st.write("🌱 ফসল: ধান / সবজি")
        st.write("🧪 সার: ইউরিয়া প্রয়োগ করুন")
        st.write("💧 সেচ: বেশি পানি দিন")
    elif current < 70:
        st.write("🌱 ফসল: সবজি")
        st.write("🧪 সার: কম্পোস্ট ব্যবহার করুন")
        st.write("💧 সেচ: মাঝারি পানি")
    else:
        st.write("🌱 ফসল: ধান")
        st.write("🧪 সার: এখন দরকার নেই")
        st.write("💧 সেচ: বন্ধ রাখুন")

# ---------------- CONTROL ----------------
st.subheader("🎛 নিয়ন্ত্রণ")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🌧 পানি দিন"):
        st.success("সেচ চালু হয়েছে")

with c2:
    if st.button("☀️ শুকানো"):
        st.info("শুকানোর মোড চালু")

with c3:
    if st.button("💧 বন্ধ"):
        st.warning("সেচ বন্ধ করা হয়েছে")

# ---------------- GRAPH ----------------
st.subheader("📈 লাইভ আর্দ্রতা গ্রাফ")

fig, ax = plt.subplots()
ax.plot(st.session_state.moisture)
ax.set_ylim(0, 100)
ax.set_ylabel("আর্দ্রতা (%)")

st.pyplot(fig)

# ---------------- EXPERT MODE ----------------
if mode == "🧠 Expert Mode":
    st.subheader("🔬 বিস্তারিত বিশ্লেষণ")

    st.write("বর্তমান আর্দ্রতা:", current)

    if current < 50:
        st.write("মাটি খুব শুষ্ক — জরুরি সেচ প্রয়োজন")
    elif current > 85:
        st.write("অতিরিক্ত ভেজা — পানি বন্ধ করুন")
    else:
        st.write("স্বাভাবিক অবস্থা")

# ---------------- SAFE REFRESH ----------------
if st.button("🔄 আপডেট করুন"):
    st.rerun()
