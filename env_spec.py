import re
import json

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


def create_list(input_str):
    """
    Creates a list from input_str_list.Returns the new list.
    """
    input_str = input_str.replace("[", "")
    input_str = input_str.replace("]", "")
    new_list = input_str.split(",")

    for pos in range(0, len(new_list)):
        new_list[pos] = str(new_list[pos])

    return new_list


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
    if "[" in input_type:
        return True
    elif input_type not in valid_types_list:
        return False
    else:
        return True


def render_env_var_spec(env_var_field, env_var_type):
    """
    Creates html string from env_variables (field, type). If env_var_type is a restricted choice,
    calls create_list to create the list of strs from env_var_type string. Returns the string.
    """
    env_var_field_lower = env_var_field.lower()
    env_var_type = env_var_type or "text"

    if "[" not in env_var_type:
        ret_str = (
            f'<label for="env_spec_{env_var_field_lower}">{env_var_field}</label>\n'
            f'<input id="env_spec_{env_var_field_lower}" name="{env_var_field_lower}" type="{env_var_type}" />\n'
        )
    else:
        ret_str = ""

        env_var_type_list = create_list(env_var_type)

        ret_str += (
            f'<label for="env_spec_{env_var_field_lower}">{env_var_field}</label>\n'
            f'<select id="env_spec_{env_var_field_lower}" name="{env_var_field_lower}">\n'
        )
        for line in env_var_type_list:
            ret_str += f'\t<option value="{line}">{line}</option>\n'

        ret_str += "</select>\n"

    return ret_str


def render_env_spec_to_html(input_str):
    """
    Takes the whole string and splits it first by \n and then by :, if possible. Returns html output or "".
    """
    html_output = ""

    lines = input_str.split("\n")

    for line in lines:
        try:
            input_field, input_type = line.split(": ")

            if check_input(input_field) and check_type(input_type):
                html_output += render_env_var_spec(input_field, input_type)
            else:
                return ""
        except:
            input_field = line

            if check_input(input_field):
                html_output += render_env_var_spec(input_field, "")
            else:
                return ""

    return html_output


def main():
    html_output = render_env_spec_to_html(spec_str)
    return html_output


if __name__ == "__main__":
    spec_str = "DEBUG: [0,1]\nENVIRONMENT: [production,staging,development]"
    print(main())
