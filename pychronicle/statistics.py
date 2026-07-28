from pychronicle.viewer import (
    get_execution_steps,
    get_all_variables
)


def get_execution_statistics(db_path, run_id):

    steps = get_execution_steps(db_path, run_id)
    variables = get_all_variables(db_path, run_id)

    stats = {
        "total_steps": len(steps),
        "total_variables": len(variables),
        "unique_variables": len(
            set(variable[1] for variable in variables)
        )
    }

    return stats