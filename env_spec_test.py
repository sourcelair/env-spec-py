import env_spec


def test_invalid_input_non_latin():
    assert env_spec.render_env_spec_to_html("dαtabase_url") == ""


def test_invalid_input_start_with_digit():
    assert env_spec.render_env_spec_to_html("1DATABASE_URL: url") == ""


def test_non_existed_type():
    assert env_spec.render_env_spec_to_html("DATABASE_URL: testing") == ""


def test_valid_input():
    assert env_spec.render_env_spec_to_html("DATABASE_URL: url") == (
        '<label for="env_spec_database_url"> DATABASE_URL</label>\n'
        '<input id="env_spec_database_url" name="database_url" />\n'
        '<input id="env_spec_database_url" name="database_url" type="url" />'
    )
