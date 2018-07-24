import env_spec


def test_invalid_input_non_latin():
    assert env_spec.render_env_spec_to_html("dαtabase_url") == ""


def test_invalid_input_start_with_digit():
    assert env_spec.render_env_spec_to_html("1DATABASE_URL: url") == ""


def test_non_existed_type():
    assert env_spec.render_env_spec_to_html("DATABASE_URL: testing") == ""


def test_valid_input():
    assert env_spec.render_env_spec_to_html(
        "ADMIN_EMAIL: email\nDEBUG: number\nADMIN_NAME"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" />\n'
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<input id="env_spec_debug" name="debug" type="number" />\n'
        '<label for="env_spec_admin_name">ADMIN_NAME</label>\n'
        '<input id="env_spec_admin_name" name="admin_name" />\n'
    )
