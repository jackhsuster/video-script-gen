from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.utilities import WikipediaAPIWrapper

# import os

def generate_script(subject, video_length, creativity, api_key):
    # 1. 產生標題
    title_template = ChatPromptTemplate.from_messages(
        [
           ("human", f"我想要製作一部關於{subject}的影片，可以幫我想一個標題嗎？"),
         
        ]
    )
    script_template = ChatPromptTemplate.from_messages(
        [
            ("human",
             """"你是一位短視頻頻道的部落客。根據以下標題和相關訊息，為短視頻頻道寫一個視頻腳本。
               影片標題：{title}，影片長度：{duration}分鐘，產生的腳本的長度盡量遵循影片長度的要求。
               要求開頭抓住限球，中間提供乾貨內容，結尾有驚喜，腳本格式也請依照【開頭、中間，結尾】分隔。
               整體內容的表達方式要盡量輕鬆有趣，吸引年輕人。 腳本內容可以結合以下維基百科搜尋出的信息，
               但僅作為參考，只結合相關的即可，對不相關的進行忽略：
             ```{wikipedia_search}```"""
             )
        ]            
            
    )
    
    model = ChatOpenAI(openai_api_key=api_key, temperature=creativity)
    title_chain = title_template | model
    script_chain = script_template | model

    title = title_chain.invoke({"subject": subject}).content

    search = WikipediaAPIWrapper(lang="zh-tw")

    search_result = search.run(subject)

    script = script_chain.invoke({"title": title, 
                                  "duration": video_length, 
                                  "wikipedia_search": search_result}).content
    
    return search_result, title , script

# print(generate_script("平行宇宙", 1, 0.3, os.getenv("OPENAI_API_KEY")))





   