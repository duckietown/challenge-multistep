#!/usr/bin/env python

from duckietown_challenges import ChallengeInterfaceEvaluator, InvalidEnvironment, \
    scoring_context

basename = 'evaluator-file.txt'
contents = b'from step1 of evaluator'


def score_step1(cie: ChallengeInterfaceEvaluator):
    cie.set_evaluation_file_from_data(basename, contents)


def score_step2(cie: ChallengeInterfaceEvaluator):
    fn = cie.get_completed_step_evaluation_file(STEP1, basename)
    with open(fn, 'rb') as f:
        read_back = f.read()

    if read_back != contents:
        msg = 'Wrong contents'
        raise InvalidEnvironment(msg)


STEP1 = 'step1'
STEP2 = 'step2'


def score(cie: ChallengeInterfaceEvaluator):
    step_name = cie.get_current_step()
    if step_name == STEP1:
        score_step1(cie)
    elif step_name == STEP2:
        score_step2(cie)
    else:
        msg = 'invalid step %s' % step_name
        raise InvalidEnvironment(msg)

    cie.set_score('passed-%s' % step_name, 1)


if __name__ == '__main__':
    with scoring_context() as cie:
        score(cie)
