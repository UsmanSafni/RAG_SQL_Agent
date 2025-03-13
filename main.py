# main.py
from streamlit_app import ChatUI
import streamlit as st

if __name__ == "__main__":
    ui = ChatUI()
    ui.render()