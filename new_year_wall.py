import streamlit as st
import pandas as pd
from datetime import datetime, date
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="🎆 New Year Community Wall", layout="centered")

# 🎨 Background gradient & text styling
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #1CD8D2, #93EDC7); /* futuristic gradient */
}
h1, h2, h3, p, .css-1d391kg {
    color: #222222;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 🎆 Fireworks + floating stars + flowers
components.html("""
<style>
@keyframes floatY {
    0% {transform: translateY(0);}
    50% {transform: translateY(-15px);}
    100% {transform: translateY(0);}
}
@keyframes flyDiagonal {
    0% {transform: translate(0,0);}
    100% {transform: translate(100vw, -100vh);}
}
@keyframes firework {
    0% {opacity: 0; transform: scale(0);}
    50% {opacity: 1; transform: scale(1.5);}
    100% {opacity: 0; transform: scale(0);}
}
.floating {
    position: fixed;
    font-size: 30px;
    animation: floatY 4s ease-in-out infinite;
    z-index: 1;
}
.star {
    position: fixed;
    font-size: 25px;
    animation: flyDiagonal linear infinite;
    z-index: 0;
}
.firework {
    position: fixed;
    font-size: 40px;
    animation: firework 2s ease-in-out infinite;
    z-index: 0;
}
</style>

<!-- Floating flowers -->
<div class="floating" style="left:10%; top:20%;">🌸</div>
<div class="floating" style="left:50%; top:10%;">🌸</div>
<div class="floating" style="left:90%; top:30%;">🌸</div>

<!-- Flying futuristic stars (watermark) -->
<div class="star" style="left:15%; top:85%; color:#00FFFF; animation-duration:20s;">⭐</div>
<div class="star" style="left:35%; top:60%; color:#FF00FF; animation-duration:18s;">⭐</div>
<div class="star" style="left:55%; top:40%; color:#FF9900; animation-duration:22s;">⭐</div>
<div class="star" style="left:75%; top:30%; color:#00FFCC; animation-duration:16s;">⭐</div>

<!-- Fireworks -->
<div class="firework" style="left:20%; top:60%; color:#FF0000;">🎆</div>
<div class="firework" style="left:50%; top:30%; color:#00FF00;">🎇</div>
<div class="firework" style="left:70%; top:70%; color:#0000FF;">🎆</div>
""", height=600)

# 🎄 Two-paragraph title
st.markdown("""
<h1 style='text-align:center; color:#222222;'>🎄 Christmas</h1>
<h1 style='text-align:center; color:#222222;'>→ New Year Community Wall 🎆</h1>
""", unsafe_allow_html=True)

st.subheader("Reflect together. Rise together.")

# 🌍 Public notice
st.warning("🌍 This is a PUBLIC community wall. All posts are visible to everyone.")

# 🎆 Countdown
new_year = date(date.today().year + 1, 1, 1)
days_left = (new_year - date.today()).days
st.success(f"⏳ {days_left} days to New Year!")

# 📁 Data file
DATA_FILE = "community_posts.csv"
if not os.path.exists(DATA_FILE):
    pd.DataFrame(columns=["Name", "Gratitude", "Goals", "Word", "Time"]).to_csv(DATA_FILE, index=False)

# ✍️ Post form
with st.form("post_form"):
    st.subheader("📝 Share Your New Year Reflection")
    name = st.text_input("Your Name or Nickname")
    gratitude = st.text_area("🙏 What are you grateful for this year?")
    goals = st.text_area("🎯 Your goals for the New Year")
    word = st.text_input("🧠 Your word for the year (optional)")
    submit = st.form_submit_button("Post to Community 🚀")

if submit and name and goals:
    df = pd.read_csv(DATA_FILE)
    df.loc[len(df)] = [name, gratitude, goals, word, datetime.now().strftime("%Y-%m-%d %H:%M")]
    df.to_csv(DATA_FILE, index=False)
    st.success("🎉 Your post is live on the community wall!")

# 📜 Display posts in stylish cards
st.markdown("---")
st.subheader("🌟 Community Posts")
df = pd.read_csv(DATA_FILE).iloc[::-1]
for _, row in df.iterrows():
    st.markdown(f"""
    <div style="
        background: rgba(255, 255, 255, 0.85);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.15);
    ">
        <strong>🎆 {row['Name']}</strong><br>
        🙏 <em>{row['Gratitude']}</em><br>
        🎯 <strong>Goals:</strong> {row['Goals']}<br>
        🧠 <strong>Word:</strong> {row['Word']}<br>
        ⏰ {row['Time']}
    </div>
    """, unsafe_allow_html=True)

# 🔐 Footer
st.caption("Built with ❤️ for the season of new beginnings.")
st.caption("Please avoid sharing private or sensitive information.")
