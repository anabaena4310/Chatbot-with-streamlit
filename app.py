import streamlit as st
import requests

apikey = "DZZbHdU8i6DyNufqdG2UIvoHH0qtCewG"

chat_logs = []

st.title("Chatbot with streamlit")

st.subheader("メッセージを入力してから送信をタップしてください")

message = st.text_input("メッセージ")


def request(endpoint, apikey, query, callback):
    params = {'apikey': apikey,
              'query': query,
              }
    if callback is not None:
        params['callback'] = callback

    response = requests.post(endpoint, params)

    return response.json()


def send_pya3rt():
    ans_json = request('https://api.a3rt.recruit.co.jp/talk/v1/smalltalk',
                       apikey, message, None)
    ans = ans_json['results'][0]['reply']
    chat_logs.append('you: ' + message)
    chat_logs.append('AI: ' + ans)
    for chat_log in chat_logs:
        st.write(chat_log)


if st.button("送信"):
    send_pya3rt()
