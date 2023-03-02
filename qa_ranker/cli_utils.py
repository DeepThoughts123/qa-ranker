import click


def validate_bool(ctx, param, value) -> bool:
    """
    Validate whether the value is boolean
    :return: Python boolean type
    """
    value = str(value)
    if value.lower() == "false":
        return False
    elif value.lower() == "true":
        return True
    else:
        raise click.BadParameter(
            f"Param: `{param}` should be a boolean. Current value: `{value}`."
        )
