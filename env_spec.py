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


def render_env_var_spec(env_var_field, env_var_type):
    """
    Creates html string from env_variables (field, type). Returns the string.
    """
    env_var_field_lower = env_var_field.lower()

    if env_var_type != "":
        ret_str = (
            f'<label for="env_spec_{env_var_field_lower}"> {env_var_field}</label>'
        )
        ret_str += "\n"
        ret_str += f'<input id="env_spec_{env_var_field_lower}" name="{env_var_field_lower}" />'
        ret_str += "\n"
        ret_str += f'<input id="env_spec_{env_var_field_lower}" name="{env_var_field_lower}" type="{env_var_type}" />'
    else:
        ret_str = (
            f'<label for="env_spec_{env_var_field_lower}"> {env_var_field}</label>'
        )

    return ret_str


def render_env_spec_to_html(input_str):
    """
    Takes the whole string and splits it first by \n and then by :, if possible. Returns html output or "".
    """
    html_output = ""
    last_string_flag = False

    while 1:
        try:
            str, rest_str = input_str.split("\n", 1)
            input_str = rest_str

        except:
            str = input_str
            last_string_flag = True
        try:
            input_field, input_type = str.split(": ")

            if check_input(input_field) and check_type(input_type):
                html_output += render_env_var_spec(input_field, input_type)
                html_output += "\n"
            else:
                return ""
        except:
            input_field = str

            if check_input(input_field):
                html_output += render_env_var_spec(input_field, "")
                html_output += "\n"
            else:
                return ""

        if last_string_flag == True:
            return html_output


def main():
    html_output = render_env_spec_to_html(spec_str)
    return html_output


if __name__ == "__main__":
    spec_str = "DATABASE_URL: url\nADMIN_EMAIL: email\nDEBUG: number\nADMIN_NAME"
    print(main())
