import streamlit as st
import ollama
import asyncio
from ollama import AsyncClient

out = ""
prompt = ""

async def chat(model_name,nprompt):
    global out 
    message = {'role': 'user', 'content': nprompt}
    response = await AsyncClient().chat(model= model_name, messages=[message])
    out = response['message']['content']

async def pull(model_name):
    global out 
    response = await AsyncClient().pull(model= model_name)
    out = response
    print(response)

APP_TITLE = 'LLM Code Assistant'
prompt_header_file = 'templates/prompt_header.txt'


models = [ x['model'] for x in ollama.list()['models']]

with open( prompt_header_file ) as fp:
    data = fp.readlines()

prompt_header = [x.split('|')[0] for x in data]
template_files = [x.split('|')[1] for x in data]
template_lists = []

for fname in template_files:
    with open('templates/'+fname.strip())  as fp:
        template_lists.append(fp.readlines())


with open('templates/code_llms.txt') as fp:
     code_llms = fp.readlines()

# App title
st.set_page_config(page_title=APP_TITLE)

source_code = None

with st.sidebar:
    width = 90
    st.markdown(f'<style> .sidebar {{width: 90%;}} </style>', unsafe_allow_html=True)
    st.image("logo.png")
    st.title(APP_TITLE)
    st.subheader('Available Models')
    selected_model = st.sidebar.selectbox('Choose a Model', models , key='selected_model')
    st.subheader('Prompt Header')
    selected_prompt_header = st.sidebar.selectbox('Choose a Prompt Header', prompt_header , key='selected_prompt_header')
    st.subheader('Prompt Templates')
    ix = prompt_header.index(selected_prompt_header)
    selected_prompt_template = st.sidebar.selectbox('Choose a Prompt Template', template_lists[ix] , key='selected_prompt_template')
    # prompt = st.text_area("Prompt Text ", selected_prompt_template)
    st.subheader('Source Code File ')
    file = st.file_uploader("Choose a file")
    if file is not None:
         source_code = file.getvalue().decode("utf-8")
        #  print(source_code)
    else:
         source_code = None

    st.subheader('Code Models')
    selected_pull_model = st.sidebar.selectbox('Pull a Model', code_llms , key='selected_pull_model') 
    if st.button('Pull Model') :
         asyncio.run(pull(selected_pull_model))


st.subheader('Prompt')
prompt = st.text_area("Prompt Text ", selected_prompt_template)
if st.button('Run LLM'):        
        if "[code snippet]" in prompt  and source_code is not None:
            prompt = prompt.replace("[code snippet]", source_code )
        # out = ollama.chat(model= selected_model, messages=[{'role': 'user', 'content': prompt}])['message']['content']
        asyncio.run(chat(selected_model, prompt))
st.subheader('Output of Models')
st.markdown(out)
