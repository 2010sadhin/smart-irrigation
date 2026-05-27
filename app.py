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
    margin: 0;
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
# SIMULATED SENSOR DATA
# -----------------------------
water_level = random.randint(20, 100)
fertilizer_level = random.randint(20, 100)

# -----------------------------
# METERS SECTION
# -----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("💧 পানি স্তর (Water Level)")
    st.progress(water_level)

    if water_level < 40:
        st.error("⚠️ এখনই পানি দিন")
    elif water_level < 70:
        st.warning("পানি প্রয়োজন হতে পারে")
    else:
        st.success("পানি পর্যাপ্ত আছে")

with col2:
    st.subheader("🌿 সার স্তর (Fertilizer Level)")
    st.progress(fertilizer_level)

    if fertilizer_level < 40:
        st.error("⚠️ এখনই সার প্রয়োগ করুন")
    elif fertilizer_level < 70:
        st.warning("সার প্রয়োজন হতে পারে")
    else:
        st.success("সার পর্যাপ্ত আছে")

# -----------------------------
# GRAPH DATA
# -----------------------------
st.write("")
st.subheader("📊 গত ৭ দিনের অবস্থা")

data = pd.DataFrame({
    "Day": ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"],
    "Water": [random.randint(30, 100) for _ in range(7)],
    "Fertilizer": [random.randint(30, 100) for _ in range(7)]
})

data.set_index("Day", inplace=True)

st.line_chart(data)
