import streamlit as st
import random
import time
import matplotlib.pyplot as plt

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="কৃষিবন্ধু সহায়ক", layout="wide")

# ---------------- CSS ----------------
st.markdown("""
<style>
.block-container {
    padding-top: 1.5rem;
    padding-left: 1rem;
    padding-right: 1rem;
}

.header-box {
    background: linear-gradient(90deg, #1b4332, #2d6a4f);
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 20px;
}

.header {
    font-size: 28px;
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
    <div class="header">🌱 কৃষিবন্ধু সহায়ক</div>
    <div class="subheader">বাংলাদেশ স্মার্ট কৃষি সহায়ক</div>
</div>
""", unsafe_allow_html=True)

# ---------------- MODE ----------------
mode = st.radio("মোড নির্বাচন:", ["👨‍🌾 Farmer Mode", "🧠 Expert Mode"], horizontal=True)

# ---------------- 64 DISTRICTS ----------------
districts = [
"ঢাকা","গাজীপুর","নারায়ণগঞ্জ","টাঙ্গাইল","কিশোরগঞ্জ","মানিকগঞ্জ","মুন্সিগঞ্জ",
"চট্টগ্রাম","কক্সবাজার","রাঙ্গামাটি","খাগড়াছড়ি","বান্দরবান","ফেনী","নোয়াখালী","লক্ষ্মীপুর",
"রাজশাহী","নাটোর","নওগাঁ","চাঁপাইনবাবগঞ্জ","পাবনা","সিরাজগঞ্জ",
"খুলনা","বাগেরহাট","সাতক্ষীরা","যশোর","নড়াইল","মাগুরা","কুষ্টিয়া","ঝিনাইদহ","মেহেরপুর",
"বরিশাল","ভোলা","পটুয়াখালী","পিরোজপুর","ঝালকাঠি","বরগুনা",
"সিলেট","মৌলভীবাজার","হবিগঞ্জ","সুনামগঞ্জ",
"রংপুর","দিনাজপুর","কুড়িগ্রাম","লালমনিরহাট","নীলফামারী","গাইবান্ধা","ঠাকুরগাঁও","পঞ্চগড়",
"ময়মনসিংহ","নেত্রকোনা","শেরপুর","জামালপুর",
"মাদারীপুর","শরীয়তপুর","গোপালগঞ্জ","রাজবাড়ী","ফরিদপুর",
"চাঁদপুর","কুমিল্লা","ব্রাহ্মণবাড়িয়া"
]

# ---------------- LOCATION ----------------
st.subheader("📍 আপনার জেলা নির্বাচন করুন")
district = st.selectbox("জেলা:", districts)

# ---------------- DISTRICT DATA ----------------
def get_advice(district):
    # simplified grouped logic
    coastal = ["ভোলা","পটুয়াখালী","বরগুনা","কক্সবাজার","সাতক্ষীরা","বাগেরহাট"]
    hilly = ["রাঙ্গামাটি","খাগড়াছড়ি","বান্দরবান"]
    north = ["রংপুর","দিনাজপুর","ঠাকুরগাঁও","পঞ্চগড়","নীলফামারী"]

    if district in coastal:
        return {"crop":"লবণ সহনশীল ধান","fert":"জৈব সার","water":"কম সেচ"}
    elif district in hilly:
        return {"crop":"আদা, হলুদ","fert":"কম্পোস্ট","water":"মাঝারি"}
    elif district in north:
        return {"crop":"গম, ভুট্টা","fert":"নাইট্রোজেন","water":"নিয়মিত"}
    else:
        return {"crop":"ধান, সবজি","fert":"ইউরিয়া","water":"মাঝারি"}

data = get_advice(district)

# ---------------- LIVE DATA ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = [random.randint(60, 90) for _ in range(20)]

def update():
    val = st.session_state.moisture[-1] + random.randint(-2,2)
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
    st.subheader("🌾 জেলা ভিত্তিক পরামর্শ")
    st.write("🌱 ফসল:", data["crop"])
    st.write("🧪 সার:", data["fert"])
    st.write("💧 সেচ:", data["water"])

# ---------------- CONTROL ----------------
st.subheader("🎛 নিয়ন্ত্রণ")

c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🌧 পানি দিন"):
        st.success("সেচ চালু")

with c2:
    if st.button("☀️ শুকানো"):
        st.info("শুকানো মোড চালু")

with c3:
    if st.button("💧 বন্ধ"):
        st.warning("সেচ বন্ধ")

# ---------------- GRAPH ----------------
st.subheader("📈 লাইভ গ্রাফ")

fig, ax = plt.subplots()
ax.plot(st.session_state.moisture)
ax.set_ylim(0,100)
ax.set_ylabel("আর্দ্রতা (%)")

st.pyplot(fig)

# ---------------- EXPERT ----------------
if mode == "🧠 Expert Mode":
    st.subheader("🔬 বিশ্লেষণ")
    st.write("জেলা:", district)
    st.write("বর্তমান আর্দ্রতা:", current)

    if current < 50:
        st.write("মাটি শুষ্ক")
    elif current > 85:
        st.write("অতিরিক্ত ভেজা")
    else:
        st.write("স্বাভাবিক")

# ---------------- REFRESH ----------------
time.sleep(2)
st.rerun()
