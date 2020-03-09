FROM duckietown/aido3-base-python3:daffy

WORKDIR /solution

COPY requirements.* ./
RUN pip install -r requirements.txt

COPY solution.py .
CMD python solution.py
