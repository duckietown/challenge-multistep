
DOCKER_REGISTRY ?= docker.io
PIP_INDEX_URL ?= https://pypi.org/simple


update-reqs:
	pur --index-url $(PIP_INDEX_URL) -r requirements.txt -f -m '*' -o requirements.resolved
	dt-update-reqs requirements.resolved




submit: update-reqs
	dts challenges submit --user-label "Template"

submit-bea: update-reqs
	dts challenges submit --user-label "Template" --impersonate 1639 --challenge all  --retire-same-label --buildx
