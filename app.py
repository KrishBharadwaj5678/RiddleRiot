import streamlit as st
import requests

st.set_page_config(
    page_title="Riddle Riot",
    page_icon="icon.png",
    menu_items={
        "About":"Experience the excitement of solving riddles and brain teasers. Join the riot of fun and test your problem-solving skills."
    }
)

st.write("<h2 style='color:#3FBA8C;'>Challenge Your Mind with Intriguing Puzzles.</h2>",unsafe_allow_html=True)

btn=st.button("Generate Riddle")

if btn:
    api_url = 'https://api.api-ninjas.com/v1/riddles'
    response = requests.get(api_url, headers={'X-Api-Key': '2jWCY0dASiPZc7RLybXvXA==R9oC0XPKPWiGJ6k6'})
    try:
        if response.status_code == requests.codes.ok:
            data=response.json()
            title=data[0]["title"]
            question=data[0]["question"]
            answer=data[0]["answer"]
            st.write(f"<p style=color:#46B5E3;font-size:32px;>Title: {title}</p>",unsafe_allow_html=True)
            st.write(f"<p style=font-size:22px;>Question: {question}</p>",unsafe_allow_html=True)
            with st.expander("Show Answer"):
                st.write(f"<p style=font-size:20px;>{answer}</p>",unsafe_allow_html=True)
    except:
        st.toast("Internet Error 🔌")
