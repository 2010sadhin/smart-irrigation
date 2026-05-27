import streamlit as st

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

/* Reduce top gap */
.block-container {
    padding-top: 3rem;
}

/* Header container */
.header-box {
    background: linear-gradient(90deg, #1b4332, #2d6a4f);
    padding: 30px 20px;
    border-radius: 12px;
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
}

/* Title */
.header {
    font-size: 34px;
    font-weight: 700;
    color: white;
    margin: 0;
    line-height: 1.4;
}

/* Subtitle */
.subheader {
    font-size: 16px;
    color: #d8f3dc;
    margin-top: 10px;
}

/* Optional: center whole app content */
.main {
    text-align: center;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER UI
# -----------------------------
st.markdown("""
<div class="header-box">
    <div class="header">🌱 কৃষিবন্ধু স্মার্ট মাঠ</div>
    <div class="subheader">
        মাঠের সেচ ও সার ব্যবস্থাপনার জন্য একটি আস্থাযোগ্য প্ল্যাটফর্ম
    </div>
</div>
""", unsafe_allow_html=True)

# -----------------------------
# EMPTY BODY (CLEAN LOOK)
# -----------------------------
st.write("")
st.write("")
st.write("")
st.write("")

# Optional placeholder (remove if not needed)
st.markdown("### 🚧 Dashboard coming soon...")
