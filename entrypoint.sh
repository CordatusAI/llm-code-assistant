#!/bin/bash

ollama serve &
streamlit run app.py --server.headless true
