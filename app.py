import streamlit as st
import random
import matplotlib.pyplot as plt

st.set_page_config(page_title="কৃষি সহায়ক ড্যাশবোর্ড", layout="wide")

# ---------------- STATE ----------------
if "moisture" not in st.session_state:
    st.session_state.moisture = 40

if "history" not in st.session_state:
    st.session_state.history = []

threshold = 50

# ---------------- TITLE ----------------
st.title("🌱 কৃষিবন্ধু স্মার্ট সেচ ও কৃষি সহায়ক সিস্টেম")
st.caption("বাংলাদেশের কৃষকদের জন্য পানি ও সার ব্যবস্থাপনা সহায়ক ড্যাশবোর্ড")

st.divider()

# ---------------- PROBLEM & SOLUTION ----------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 সমস্যা")
    st.write("কৃষিতে অতিরিক্ত পানি ব্যবহার এবং সঠিক সময়ে সার ও সেচ নির্ধারণের অভাব।")

with col2:
    st.subheader("💡 সমাধান")
    st.write("মাটির অবস্থা অনুযায়ী স্বয়ংক্রিয় সেচ ও কৃষি পরামর্শ ব্যবস্থা।")

st.divider()

# ---------------- CONTROL ----------------
st.subheader("⚙️ সিস্টেম কন্ট্রোল")

c1, c2 = st.columns(2)

with c1:
    if st.button("🌵 শুকনো মাটি সিমুলেট করুন"):
        st.session_state.moisture -= 20

with c2:
    if st.button("🌧️ বৃষ্টি সিমুলেট করুন"):
        st.session_state.moisture += 20

# ---------------- LOGIC ----------------
m = st.session_state.moisture

if m < threshold:
    status = "💧 সেচ চালু আছে"
    color = "red"
    st.session_state.moisture += random.randint(3, 6)
elif m > 70:
    status = "🌱 সেচ বন্ধ (আর্দ্রতা বেশি)"
    color = "green"
    st.session_state.moisture -= random.randint(2, 4)
else:
    status = "🌿 স্বাভাবিক অবস্থা"
    color = "blue"

st.session_state.moisture = max(0, min(100, st.session_state.moisture))

# ---------------- FERTILIZER ADVISORY ----------------
moisture = st.session_state.moisture

if moisture < 30:
    advice = "⚠️ মাটি শুষ্ক — পানি ও সার প্রয়োগ প্রয়োজন"
elif moisture < 60:
    advice = "🌿 স্বাভাবিক অবস্থা — নিয়মিত পরিচর্যা করুন"
else:
    advice = "💧 আর্দ্রতা বেশি — আপাতত সার প্রয়োগ প্রয়োজন নেই"

# ---------------- HISTORY ----------------
st.session_state.history.append(moisture)
if len(st.session_state.history) > 30:
    st.session_state.history.pop(0)

# ---------------- DASHBOARD ----------------
st.divider()
st.subheader("📊 বর্তমান অবস্থা")

col3, col4 = st.columns(2)

with col3:
    st.metric("মাটির আর্দ্রতা", f"{moisture}%")

with col4:
    st.markdown(f"### অবস্থা: **{status}**")

st.progress(moisture / 100)

st.info(advice)

# ---------------- GRAPH ----------------
st.divider()
st.subheader("📈 আর্দ্রতা পরিবর্তন বিশ্লেষণ")

fig, ax = plt.subplots()
ax.plot(st.session_state.history, linewidth=2)
ax.set_ylim(0, 100)
ax.set_xlabel("সময়")
ax.set_ylabel("আর্দ্রতা (%)")

st.pyplot(fig)