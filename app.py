import streamlit as st
import random
import pandas as pd
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="কৃষিবন্ধু স্মার্ট মাঠ",
    layout="wide"
)

# -----------------------------
# CSS
# -----------------------------
st.markdown("""
<style>
.block-container { padding-top: 3rem; }

.header-box {
    background: linear-gradient(90deg, #1b4332, #2d6a4f);
    padding: 30px;
    border-radius: 12px;
    text-align: center;
}

.header {
    font-size: 34px;
    font-weight: bold;
    color: white;
}

.subheader {
    font-size: 16px;
    color: #d8f3dc;
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
# PLACEHOLDERS (IMPORTANT)
# -----------------------------
water_box = st.empty()
fertilizer_box = st.empty()
chart_box = st.empty()
advice_box = st.empty()

# -----------------------------
# INITIAL GRAPH DATA
# -----------------------------
history_water = [random.randint(40,80) for _ in range(5)]
history_fert = [random.randint(40,80) for _ in range(5)]

# -----------------------------
# LIVE LOOP
# -----------------------------
while True:

    # simulate changing values
    soil_moisture = random.randint(20, 100)
    fertility = random.randint(20, 100)

    # update history
    history_water.append(soil_moisture)
    history_fert.append(fertility)

    history_water = history_water[-6:]
    history_fert = history_fert[-6:]

    # ---------------- WATER UI ----------------
    with water_box.container():
        st.subheader("💧 সেচ (Water Level)")
        st.progress(soil_moisture)

        if soil_moisture < 40:
            st.error("🚨 এখনই পানি দিন!")
        elif soil_moisture < 70:
            st.warning("⚠️ অল্প পানি প্রয়োজন")
        else:
            st.success("✅ পানি ঠিক আছে")

        st.write(f"বর্তমান আর্দ্রতা: {soil_moisture}%")

    # ---------------- FERTILIZER UI ----------------
    with fertilizer_box.container():
        st.subheader("🌿 সার (Fertilizer Level)")
        st.progress(fertility)

        if fertility < 40:
            st.error("🚨 এখনই সার দিন!")
        elif fertility < 70:
            st.warning("⚠️ কিছুটা সার প্রয়োজন")
        else:
            st.success("✅ সার ঠিক আছে")

        st.write(f"বর্তমান উর্বরতা: {fertility}%")

    # ---------------- GRAPH ----------------
    df = pd.DataFrame({
        "Water": history_water,
        "Fertilizer": history_fert
    })

    chart_box.line_chart(df)

    # ---------------- SMART ADVICE ----------------
    with advice_box.container():
        st.subheader("🧠 স্মার্ট পরামর্শ")

        if soil_moisture < 40 and fertility < 40:
            st.error("⚠️ পানি ও সার দুটোই দিন!")
        elif soil_moisture < 40:
            st.warning("💧 পানি দিন")
        elif fertility < 40:
            st.warning("🌿 সার দিন")
        else:
            st.success("🌱 সব ঠিক আছে")

    # refresh every 2 seconds
    time.sleep(2)
