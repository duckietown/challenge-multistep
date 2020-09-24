
AIDO_REGISTRY ?= docker.io
PIP_INDEX_URL ?= https://pypi.org/simple

update-reqs:
	pur --index-url $(PIP_INDEX_URL) -r requirements.txt -f -m '*' -o requirements.resolved
	aido-update-reqs requirements.resolved
