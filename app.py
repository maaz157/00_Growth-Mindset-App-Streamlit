import streamlit as st 

st.set_page_config(page_title="Growth Mindset Project", page_icon="🌟")

st.title("Growth Mindset Challenge: 🌿")

st.header("✨ Welcome To Your Growth Journey!")
st.write("Embrace challenges, unlock your true potential, and begin your growth mindset adventure today! 🌈")

# Quote section
st.header("💭 Today's Growth Mindset Quote")
st.write("“Happiness is not something ready made. It comes from your own actions.” - Dalai Lama")

if st.button('Inspire Me with Another Quote'):
    st.write("“Believe you can and you're halfway there.” - Theodore Roosevelt")

# Challenge section
st.header("🛠️ What's Your Challenge Today?")
user_input = st.text_input("Describe the challenge you're facing:")

if st.button('Submit Challenge'):
    if user_input:
        st.success(f" You are facing: {user_input}. Keep striving and never give up! 💪")
    else:
        st.warning("Please enter your challenge to proceed! 🌟")

# Reflection section
st.header("📝 Reflect on Your Challenge")
reflection = st.text_area("Write your reflection here:")

if st.button('Submit Reflection'):
    if reflection:
        st.success(f" 🌟 Wonderful Insight! Your reflection: {reflection}")
    else:
        st.info("Taking time to reflect helps you grow! 🌱")

# Achievement section
st.header("🎉 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently achieved:")

if st.button('Celebrate My Achievement'):
    if achievement:
        st.success(f"🏅 Congratulations! You Achieved: {achievement}")
    else:
        st.info("Every achievement matters, big or small! 🎈")

# Removed balloon effect

# Footer
st.write("- - -")
st.write("🌟 Keep believing in yourself. Growth is a journey, not a destination! 🌻")

st.write("** Made by Maaz Zameer**")
st.write("Connect With Me On [LinkedIn](https://www.linkedin.com/in/maaz-zameer-322286361?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
