import re


class EnvSpecSyntaxError(Exception):
    pass


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
    If input_str=[1,2,], returns empty list(syntax error).
    """
    input_str = input_str.replace("[", "")
    input_str = input_str.replace("]", "")
    new_list = input_str.split(",")

    if "" in new_list:
        return []

    for pos in range(0, len(new_list)):
        new_list[pos] = str(new_list[pos]).strip()

    return new_list


def render_to_html(env_spec_list):
    html_output = ""

    for dict in env_spec_list:
        if dict["choices"] is None:
            if dict["default_value"] is None:
                ret_str = (
                    f'<label for="env_spec_{dict["name"].lower()}">{dict["name"]}</label>\n'
                    f'<input id="env_spec_{dict["name"].lower()}" name="{dict["name"].lower()}" type="{dict["type"]}" />\n'
                )
            elif dict["default_value"] is not None:
                ret_str = (
                    f'<label for="env_spec_{dict["name"].lower()}">{dict["name"]}</label>\n'
                    f'<input id="env_spec_{dict["name"].lower()}" name="{dict["name"].lower()}" type="{dict["type"]}" value="{dict["default_value"]}" />\n'
                )
        elif dict["choices"] is not None:
            ret_str = (
                f'<label for="env_spec_{dict["name"].lower()}">{dict["name"]}</label>\n'
                f'<select id="env_spec_{dict["name"].lower()}" name="{dict["name"].lower()}">\n'
            )

            for x in range(0, len(dict["choices"])):
                if (
                    dict["default_value"] is not None
                    and dict["default_value"] == dict["choices"][x]
                ):
                    ret_str += f'\t<option value="{dict["choices"][x]}"selected>{dict["choices"][x]}</option>\n'
                else:
                    ret_str += f'\t<option value="{dict["choices"][x]}">{dict["choices"][x]}</option>\n'
            ret_str += "</select>\n"
        html_output += ret_str
    return html_output


def parse(env_spec_text):
    env_spec_list = []

    alphanumeric_that_does_not_start_with_digit = r"^[A-Z_][0-9A-Z_]*$"
    name_regex = r"^(.+)\:(.+)$"
    choices_regex = r"^(.+)\]"
    default_values_regex = r"^(.+)\=(.+)$"

    lines = env_spec_text.split("\n")

    for line in lines:
        line_dict = {}

        name_match = re.match(name_regex, line)
        default_value_match = re.match(default_values_regex, line)

        if name_match:
            name = name_match.groups()[0]
            line = name_match.groups()[1]

            ret = re.match(alphanumeric_that_does_not_start_with_digit, name)

            if ret is None:
                try:
                    raise EnvSpecSyntaxError
                except EnvSpecSyntaxError:
                    return []

            line_dict["name"] = name

            choices_match = re.match(choices_regex, line)

            if choices_match:
                choices_str = choices_match.groups()[0]

                choices = create_list(choices_str)
                if not choices:
                    try:
                        raise EnvSpecSyntaxError
                    except EnvSpecSyntaxError:
                        return []
                line_dict["choices"] = choices
            else:
                line_dict["choices"] = None

            if default_value_match:
                default_value = default_value_match.groups()[1]
                default_value = default_value.strip()

                if choices_match:
                    if default_value not in choices or default_value == "":
                        try:
                            raise EnvSpecSyntaxError
                        except EnvSpecSyntaxError:
                            return []
                line_dict["default_value"] = default_value
            else:
                line_dict["default_value"] = None

            if not choices_match:
                if default_value_match:
                    type_t = default_value_match.groups()[0]
                else:
                    type_t = line

                type_t = type_t.strip()

                if type_t not in valid_types_list:
                    try:
                        raise EnvSpecSyntaxError
                    except EnvSpecSyntaxError:
                        return []
                line_dict["type"] = type_t
            else:
                type_t = "text"
                line_dict["type"] = type_t
        else:
            name = line.strip()
            ret = re.match(alphanumeric_that_does_not_start_with_digit, name)

            if ret is None:
                try:
                    raise EnvSpecSyntaxError
                except EnvSpecSyntaxError:
                    return []
            type_t = "text"
            line_dict["name"] = name
            line_dict["type"] = type_t
            line_dict["choices"] = None
            line_dict["default_value"] = None

        env_spec_list.append(line_dict)

    return env_spec_list


def main():
    env_spec_list = parse(spec_str)
    # print(env_spec_list)
    html_output = render_to_html(env_spec_list)
    return html_output


if __name__ == "__main__":
    spec_str = "ADMIN_EMAIL: email\nDEBUG: number\nADMIN_NAME"
    print(main())
