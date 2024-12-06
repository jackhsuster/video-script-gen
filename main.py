import streamlit as st
from utils import generate_script

st.title("🎬影片腳本產生器🤖")

with st.sidebar:
    open_ai_key = st.text_input("輸入 OPENAI 金鑰", type="password")
    st.markdown("🔥[點我取得金鑰](https://platform.openai.com/account/api-keys)🔥")

subject = st.text_input("輸入影片主題")
video_length = st.number_input("輸入影片長度(分鐘)", min_value=0.5, step=0.1)
creativity = st.slider("💡請輸入影片腳本創意值 (數字越大創意越豐富)", min_value=0.0,value=0.2,max_value=1.0 ,step=0.1)  
submit = st.button("🚀開始產生腳本🚀")

if submit and  not open_ai_key:
   st.info("請輸入 OPENAI 金鑰")
   st.stop()

if submit and not subject:
   st.info("請輸入影片主題")
   st.stop()
   
if submit and not video_length>=0.1:
   st.info("影片長度需要大於0.1分鐘")

if submit:
   with st.spinner("🤖AI 智慧生成中🤖"):
      search_result,title,script = generate_script(subject, video_length, creativity, open_ai_key) 
   st.success("🎉腳本生成成功🎉")
   st.subheader("📝腳本內容📝")
   st.write(title)
   st.subheader("📚相關資訊📚")
   st.write(script)
   with st.expander("🔗維基百科搜尋結果🔗"):
      st.info(search_result)

