import re

valid_types_array = [
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


def check_input(field_type_array):
    """
    Checks syntax of input(uppercase latin chars,numeric digits, underscores).
    Returns False for error or True for correct syntax.
    """
    alphanumeric_that_does_not_start_with_digit = r"^[A-Z_][0-9A-Z_]*$"

    for line in field_type_array:
        ret = re.match(alphanumeric_that_does_not_start_with_digit, line[0])

        if ret is None:
            return False

    return True


def check_type(input_array):
    """
    checks if given type is valid and returns True, else returs False
    """
    for type in input_array:
        if type[1] not in valid_types_array:
            return False
    return True


def render_env_var_spec(env_var):
    env_var_name = env_var[0]
    env_var_type = env_var[1]
    env_var_name_lower = env_var_name.lower()

    ret_str = f'<label for="env_spec_{env_var_name_lower}"> {env_var_name}</label>'
    ret_str += "\n"
    ret_str += f'<input id="env_spec_{env_var_name_lower}" name="{env_var_name_lower}" type="{env_var_type}" />'

    return ret_str


def render_env_spec_to_html(field_type_array):
    if check_type(field_type_array) and (check_input(field_type_array)):
        html_output = []

        for line in field_type_array:
            html_output.append(render_env_var_spec(line))  # create html output

        return "\n".join(html_output)
    return ""


def main():
    field_array = spec_str.split("\n")
    field_type_array = []

    for line in field_array:
        field_type_array.append(line.split(": "))

    html_output = render_env_spec_to_html(field_type_array)

    return html_output


if __name__ == "__main__":
    spec_str = "DATABASE_URL: url\nADMIN_EMAIL: email\nDEBUG: number"
    print(main())
