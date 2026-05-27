import streamlit as st
import random
import pandas as pd

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="কৃষিবন্ধু স্মার্ট মাঠ",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>
.block-container {
    padding-top: 3rem;
}

.header-box {
    background: linear-gradient(90deg, #1b4332, #2d6a4f);
    padding: 30px 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

.header {
    font-size: 34px;
    font-weight: 700;
    color: white;
}

.subheader {
    font-size: 16px;
    color: #d8f3dc;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<div class="header-box">
    <div class="header">🌱 কৃষিবন্ধু স্মার্ট মাঠ</div>
    <div class="subheader">
        মাঠের সেচ ও সার ব্যবস্থাপনার জন্য একটি আস্থাযোগ্য প্ল্যাটফর্ম
    </div>
</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# FAKE SENSOR DATA (for demo)
# -----------------------------
soil_moisture = random.randint(20, 100)
fertility = random.randint(20, 100)

# -----------------------------
# WATER METER
# -----------------------------
st.subheader("💧 সেচ (Water Level)")

st.progress(soil_moisture)

if soil_moisture < 40:
    st.error("🚨 এখনই পানি দিন!")
elif soil_moisture < 70:
    st.warning("⚠️ অল্প পানি প্রয়োজন")
else:
    st.success("✅ মাটি ভেজা আছে, এখন পানি লাগবে না")

st.write(f"বর্তমান আর্দ্রতা: {soil_moisture}%")

# -----------------------------
# FERTILIZER METER
# -----------------------------
st.subheader("🌿 সার (Fertilizer Level)")

st.progress(fertility)

if fertility < 40:
    st.error("🚨 এখনই সার প্রয়োজন!")
elif fertility < 70:
    st.warning("⚠️ কিছুটা সার দিতে হবে")
else:
    st.success("✅ সার পর্যাপ্ত আছে")

st.write(f"বর্তমান উর্বরতা: {fertility}%")

# -----------------------------
# GRAPH DATA
# -----------------------------
st.subheader("📊 গত কয়েক দিনের অবস্থা")

days = ["Day 1","Day 2","Day 3","Day 4","Day 5","Today"]

data = {
    "Water Level": [random.randint(30,90) for _ in range(6)],
    "Fertilizer Level": [random.randint(30,90) for _ in range(6)]
}

df = pd.DataFrame(data, index=days)

st.line_chart(df)

# -----------------------------
# FINAL ADVICE
# -----------------------------
st.subheader("🧠 স্মার্ট পরামর্শ")

if soil_moisture < 40 and fertility < 40:
    st.error("⚠️ জরুরি: পানি ও সার দুটোই দিন!")
elif soil_moisture < 40:
    st.warning("💧 শুধুমাত্র পানি দিন")
elif fertility < 40:
    st.warning("🌿 শুধুমাত্র সার দিন")
else:
    st.success("🌱 সব কিছু ঠিক আছে!")
