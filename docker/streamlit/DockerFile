# Lite-Version Python
FROM python:3.12-slim

# Set working directory.
WORKDIR /home

COPY ./requirements.txt ./
COPY ./src ./src/
COPY ./models ./models/
COPY ./config/ ./config/

RUN \
apt-get update && \
apt-get upgrade -y && \
apt-get autoremove -y && \
apt-get clean -y && \
pip install --upgrade pip && \
pip install wheel && \
pip install -r requirements.txt

# Expose the port the app runs on.
EXPOSE 8501

CMD ["streamlit", "run", "src/streamlit.py"]