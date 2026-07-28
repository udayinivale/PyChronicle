from pychronicle.viewer import (
    get_execution_steps,
    get_variables
)


def search_variable(db_path, run_id, variable_name):
    """
    Search for a variable across all execution steps of a run.

    Returns:
        List of tuples:
        (step_number, line_number, variable_value)
    """

    steps = get_execution_steps(db_path, run_id)

    results = []

    for step in steps:
        step_number = step[0]
        line_number = step[1]

        variables = get_variables(
            db_path,
            run_id,
            step_number
        )

        for name, value in variables:
            if name.lower() == variable_name.lower():
                results.append(
                    (
                        step_number,
                        line_number,
                        value
                    )
                )

    return results