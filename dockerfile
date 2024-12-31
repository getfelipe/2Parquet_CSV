FROM python:3.12.3-slim
RUN pip install streamlit pandas pyarrow
COPY ./app.py /app/app.py
WORKDIR /app
ENTRYPOINT ["streamlit", "run", "app.py"]