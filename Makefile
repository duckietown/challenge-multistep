
update-reqs:
	$(MAKE) -C evaluation update-reqs
	$(MAKE) -C evaluation_ipfs update-reqs

define-challenge:  update-reqs
	dts challenges define --config MS-regular.challenge.yaml
	dts challenges define --config MS-ipfs.challenge.yaml



define-challenge-no-cache: update-reqs
	dts challenges define --config MS-regular.challenge.yaml --no-cache
	dts challenges define --config MS-ipfs.challenge.yaml    --no-cache
