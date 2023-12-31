# -*- coding: utf-8 -*-
"""app_p

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hSE-cOtt2iCKziyRZHm--kgEAT95sSWZ
"""

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
import os


with open("/content/gdrive/MyDrive/polycthemi.txt") as f:
   polycthemi_text = f.read()


text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, separator = "\n")
texts = text_splitter.split_text(polycthemi_text)

embeddings = OpenAIEmbeddings()

docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]).as_retriever()

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

docsearch = Chroma.from_texts(texts, embeddings, metadatas=[{"source": str(i)} for i in range(len(texts))]).as_retriever()

chain = load_qa_chain(OpenAI(temperature=0), chain_type="stuff")

if __name__ == "__main__":
    # make a gradio interface
    import gradio as gr

    gr.Interface(
        make_inference,
        [
            gr.inputs.Textbox(lines=2, label="Query"),
        ],
        gr.outputs.Textbox(label="Response"),
        title="Query My Document📄",
        description="Query My Material📄: is a tool that allows you to ask questions about a document. In this case  O.A. Alabi : -A Pediatrics presentation on Polycythermia. ",
    ).launch()