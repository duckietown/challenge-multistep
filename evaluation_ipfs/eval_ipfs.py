#!/usr/bin/env python
import os
import traceback
import ipfsapi

from duckietown_challenges import ChallengeInterfaceEvaluator, InvalidEnvironment, scoring_context

basename = "mylogs"
contents = b"from step1 of evaluator"


def score_step1(cie: ChallengeInterfaceEvaluator):
    cie.set_evaluation_file_from_data("regular.txt", contents)

    d = cie.get_tmp_dir()
    dn = os.path.join(d, "mydata")
    fn = os.path.join(dn, "one.txt")
    if not os.path.exists(dn):
        os.makedirs(dn)
    with open(fn, "wb") as f:
        f.write(contents)

    # "docker.for.mac.host.internal"
    # API = "/ip4/127.0.0.1/tcp/5001",
    try:
        try:
            client = ipfsapi.connect("docker.for.mac.host.internal", 5001)
        except:
            msg = "Cannot connect to docker.for.mac.host.internal; trying 127.0.0.1"
            cie.info(msg)
            client = ipfsapi.connect("127.0.0.1", 5001)
        res = client.add(dn, recursive=False)
    except:
        msg = f"Cannot connect to ipfs server:\n{traceback.format_exc()}"
        raise InvalidEnvironment(msg)

    cie.info(res)
    qm = res[-1]["Hash"]
    # qm = res['']
    #
    # cmd = ['ipfs', '--api', API, 'add', '-r', '-q', dn]
    # res = subprocess.check_output(cmd)

    cie.info(qm)

    cie.set_evaluation_ipfs_hash(basename, qm)


def score_step2(cie: ChallengeInterfaceEvaluator):
    fn = cie.get_completed_step_evaluation_file(STEP1, "regular.txt")
    with open(fn, "rb") as f:
        read_back = f.read()

    if read_back != contents:
        msg = "Wrong contents for regular file regular.txt"
        raise InvalidEnvironment(msg)

    fn = cie.get_completed_step_evaluation_file(STEP1, os.path.join(basename, "one.txt"))
    with open(fn, "rb") as f:
        read_back = f.read()

    if read_back != contents:
        msg = "Wrong contents"
        raise InvalidEnvironment(msg)


STEP1 = "step1"
STEP2 = "step2"


def score(cie: ChallengeInterfaceEvaluator):
    step_name = cie.get_current_step()
    if step_name == STEP1:
        score_step1(cie)
    elif step_name == STEP2:
        score_step2(cie)
    else:
        msg = "invalid step %s" % step_name
        raise InvalidEnvironment(msg)

    cie.set_score("passed-%s" % step_name, 1)


if __name__ == "__main__":
    with scoring_context() as cie:
        score(cie)
