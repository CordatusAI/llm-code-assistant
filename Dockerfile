FROM ollama/ollama

COPY templates /app/templates
COPY app.py /app/app.py
COPY logo.png /app/logo.png
COPY entrypoint.sh /app/entrypoint.sh

WORKDIR /app
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install streamlit ollama && \
    rm -rf /root/.cache

ENTRYPOINT [ "/app/entrypoint.sh" ]