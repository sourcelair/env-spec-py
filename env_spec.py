import re

valid_types_list = [
    "color",
    "date",
    "datetime-local",
    "email",
    "month",
    "number",
    "password",
    "tel",
    "text",
    "time",
    "url",
    "week",
]


def check_input(input_field):
    """
    Checks syntax of input field(uppercase latin chars,numeric digits, underscores).
    Returns False for error or True for correct syntax.
    """
    alphanumeric_that_does_not_start_with_digit = r"^[A-Z_][0-9A-Z_]*$"

    ret = re.match(alphanumeric_that_does_not_start_with_digit, input_field)

    if ret is None:
        return False

    return True


def check_type(input_type):
    """
    Checks if given type is valid and returns True, else returs False
    """
    if input_type not in valid_types_list:
        return False
    return True


def render_env_var_spec(env_var):
    """
    Creates html sting from env_variable (field, type). Returns the string.
    """
    try:
        env_var_field, env_var_type = env_var.split(": ")
        env_var_field_lower = env_var_field.lower()

        ret_str = (
            f'<label for="env_spec_{env_var_field_lower}"> {env_var_field}</label>'
        )
        ret_str += "\n"
        ret_str += f'<input id="env_spec_{env_var_field_lower}" name="{env_var_field_lower}" />'
        ret_str += "\n"
        ret_str += f'<input id="env_spec_{env_var_field_lower}" name="{env_var_field_lower}" type="{env_var_type}" />'
    except:
        env_var_field = env_var
        env_var_field_lower = env_var_field.lower()

        ret_str = (
            f'<label for="env_spec_{env_var_field_lower}"> {env_var_field}</label>'
        )

    return ret_str


def render_env_spec_to_html(input_line):
    try:
        input_field, input_type = input_line.split(": ")

        if check_input(input_field) and check_type(input_type):
            html_output = render_env_var_spec(input_line)

            return html_output
    except:
        input_field = input_line

        if check_input(input_field):
            html_output = render_env_var_spec(input_field)

            return html_output
    return ""


def main():
    field_list = spec_str.split("\n")
    html_output = ""

    for line in field_list:
        html_output += render_env_spec_to_html(line)
        html_output += "\n"

    return html_output


if __name__ == "__main__":
    spec_str = "DATABASE_URL: url\nADMIN_EMAIL: email\nDEBUG: number\nADMIN_NAME"
    print(main())
