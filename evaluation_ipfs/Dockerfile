ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy-aido4


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip list

COPY . .

ENTRYPOINT ["python3", "eval_ipfs.py"]
