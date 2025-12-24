import streamlit as st
from datetime import date

st.set_page_config(page_title="New Dad Mental Health Check-In", layout="centered")

st.title("🍼 New Dad Mental Health Check-In")
st.caption("Daily self-check tool – simple, fast, no judgment")

st.divider()

# --- DAILY QUICK CHECK ---
st.header("Daily Quick Check")
checks = {
    "Slept at least 3–4 total hours (even if broken)": False,
    "Ate at least 2 solid meals": False,
    "Drank water intentionally": False,
    "Moved my body (walk, lift, stretch)": False,
    "Had one positive interaction with partner or baby": False,
    "Took medication as prescribed": False,
}

checked_count = 0
for label in checks:
    checks[label] = st.checkbox(label)
    if checks[label]:
        checked_count += 1

if checked_count <= 2:
    st.warning("Low recovery inputs today → expect mood/anxiety noise")
else:
    st.success("Foundational needs mostly met")

st.divider()

# --- EMOTIONAL STATE ---
st.header("Emotional State")
emotional_state = st.radio(
    "Which best fits right now?",
    [
        "Calm / Engaged",
        "Tired but coping",
        "Irritable but aware",
        "Overwhelmed",
        "Numb / Disconnected",
        "Anxious / Racing thoughts",
    ],
)

st.divider()

# --- SLEEP VS ANXIETY ---
st.header("Sleep Deprivation vs Anxiety")
nap_helped = st.checkbox("I feel better after rest or a nap")
spiraling = st.checkbox("My thoughts feel spiraling or catastrophic")

if nap_helped and not spiraling:
    st.info("Likely sleep deprivation – be gentle with yourself")
elif spiraling:
    st.warning("Possible anxiety signal – monitor closely")

st.divider()

# --- SIGNAL ZONES ---
st.header("Signal Zone")
zone = st.selectbox(
    "Which zone best fits today?",
    ["Green – Stable", "Yellow – Monitor", "Red – Reach out"],
)

if zone.startswith("Green"):
    st.success("Stay the course")
elif zone.startswith("Yellow"):
    st.warning("Track for 7–10 days – no panic")
else:
    st.error("Reach out to your doctor or support system")

st.divider()

# --- MEDICATION AWARENESS ---
st.header("Medication Awareness")
current_dose = st.text_input("Current Zoloft dose (mg)")
dose_change = st.checkbox("Dose change in last 6 weeks")
blunting = st.checkbox("Emotional blunting / numbness present")

if dose_change:
    st.info("Dose changes take weeks – avoid snap decisions")

st.divider()

# --- SUMMARY ---
st.header("Daily Summary")
if st.button("Save Today’s Check-In"):
    st.success("Check-in saved (local session). Screenshot if needed.")

st.caption(f"Date: {date.today()}")

st.markdown("---")
st.markdown(
    "**Reminder:** Sleep deprivation lies. Exhaustion amplifies everything. This phase is temporary."
)    
