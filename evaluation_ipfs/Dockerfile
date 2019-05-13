FROM duckietown/aido2-base-python3:z2


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip list

COPY . .

ENTRYPOINT ["python3", "eval_ipfs.py"]
