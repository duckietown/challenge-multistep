ARG AIDO_REGISTRY
FROM ${AIDO_REGISTRY}/duckietown/aido-base-python3:daffy-aido4

WORKDIR /solution

COPY requirements.* ./
RUN pip install -r requirements.txt

COPY solution.py .
CMD python solution.py
