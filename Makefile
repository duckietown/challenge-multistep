

define-challenge:
	dts challenges define --config MS-regular.challenge.yaml
	dts challenges define --config MS-ipfs.challenge.yaml



define-challenge-no-cache:
	dts challenges define --config MS-regular.challenge.yaml --no-cache
	dts challenges define --config MS-ipfs.challenge.yaml    --no-cache
