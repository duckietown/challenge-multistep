#!/usr/bin/env python

from duckietown_challenges import wrap_solution, ChallengeSolution, ChallengeInterfaceSolution, InvalidEnvironment


class Solver(ChallengeSolution):
    def run(self, cis):
        assert isinstance(cis, ChallengeInterfaceSolution)

        step_name = cis.get_current_step()

        basename = 'myfile.txt'
        contents = 'from step1'
        STEP1 = 'step1'
        STEP2 = 'step2'

        if step_name == STEP1:
            cis.set_solution_output_file_from_data(basename, contents)
        elif step_name == STEP2:
            read = cis.get_completed_step_solution_file_contents(STEP1, basename)
            if read != contents:
                msg = 'Wrong contents'
                raise InvalidEnvironment(msg)
        else:
            msg = 'invalid step %s' % step_name
            raise InvalidEnvironment(msg)

        cis.set_solution_output_dict({})


if __name__ == '__main__':
    wrap_solution(Solver())
