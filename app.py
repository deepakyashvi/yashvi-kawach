import streamlit as st

# 1. भाषाओं का डेटाबेस (आप इसमें और भी भाषाएँ जोड़ सकते हैं)
languages = {
    "Hindi": {
        "title": "यशवी AI कवच",
        "header": "Yashvi Enterprise द्वारा सुरक्षित",
        "label": "कॉल की बातचीत यहाँ लिखें:",
        "button": "सुरक्षा जांचें",
        "safe": "✅ बातचीत सुरक्षित लग रही है।",
        "scam": "🚨 सावधान! यह फ्रॉड कॉल हो सकता है।"
    },
    "English": {
        "title": "Yashvi AI Kavach",
        "header": "Secured by Yashvi Enterprise",
        "label": "Paste or type call conversation:",
        "button": "Check Security",
        "safe": "✅ Conversation seems safe.",
        "scam": "🚨 Warning! This might be a scam call."
    },
    "Marathi": {
        "title": "यशवी AI कवच",
        "header": "यशवी एंटरप्राइझ द्वारे सुरक्षित",
        "label": "कॉल संभाषण येथे लिहा:",
        "button": "सुरक्षा तपासा",
        "safe": "✅ संभाषण सुरक्षित वाटते.",
        "scam": "🚨 सावधान! हा फसवणुकीचा कॉल असू शकतो."
    }
}

# भाषा चुनने का विकल्प (Dropdown)
selected_lang = st.sidebar.selectbox("Language / भाषा चुनें", list(languages.keys()))
lang = languages[selected_lang]

st.title(f"🛡️ {lang['title']}")
st.subheader(lang['header'])

user_input = st.text_area(lang['label'], height=150)

if st.button(lang['button']):
    # आपका वही पुराना स्कैम चेकिंग लॉजिक यहाँ काम करेगा
    text = user_input.lower()
    if any(word in text for word in ["otp", "police", "arrest", "account", "verify"]):
        st.error(lang['scam'])
    else:
        st.success(lang['safe'])
