FROM duckietown/aido2-base-python3:z2

WORKDIR /solution

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY solution.py .
CMD python solution.py
