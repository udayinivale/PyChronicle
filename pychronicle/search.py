from pychronicle.viewer import (
    get_execution_steps,
    get_variables
)


def search_variable(db_path, run_id, variable_name):

    steps = get_execution_steps(db_path, run_id)

    results = []

    for step_number, line_number in steps:

        variables = get_variables(
            db_path,
            run_id,
            step_number
        )

        for name, value in variables:

            if name.lower() == variable_name.lower():

                results.append(
                    (step_number, line_number, value)
                )

    return results