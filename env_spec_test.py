import env_spec


def test_invalid_input_non_latin():
    assert env_spec.parse("dαtabase_url") == "[]"


def test_invalid_input_start_with_digit():
    assert env_spec.parse("1DATABASE_URL: url") == "[]"


def test_non_existed_type():
    assert env_spec.parse("DATABASE_URL: testing") == "[]"


def test_valid_input_types():
    assert env_spec.render_to_html(
        "[{'name': 'ADMIN_EMAIL', 'choices': None, 'default_value': None, 'type': 'email'}, {'name': 'DEBUG', 'choices': None, 'default_value': None, 'type': 'number'}, {'name': 'ADMIN_NAME', 'type': 'text', 'choices': None, 'default_value': None}]"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" />\n'
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<input id="env_spec_debug" name="debug" type="number" />\n'
        '<label for="env_spec_admin_name">ADMIN_NAME</label>\n'
        '<input id="env_spec_admin_name" name="admin_name" type="text" />\n'
    )
