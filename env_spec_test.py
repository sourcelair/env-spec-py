import env_spec
import pytest


def test_invalid_input_non_latin():
    with pytest.raises(env_spec.EnvSpecSyntaxError) as excinfo:
        env_spec.parse("dαtabase_url")
    assert "SYNTAX ERROR: Invalid variable name." in str(excinfo.value)


def test_invalid_input_start_with_digit():
    with pytest.raises(env_spec.EnvSpecSyntaxError) as excinfo:
        env_spec.parse("1DATABASE_URL: url")
    assert "SYNTAX ERROR: Invalid variable name." in str(excinfo.value)


def test_non_existed_type():
    with pytest.raises(env_spec.EnvSpecSyntaxError) as excinfo:
        env_spec.parse("DATABASE_URL: testing")
    assert "SYNTAX ERROR: Invalid type." in str(excinfo.value)


def test_valid_input_types():
    assert env_spec.render_env_spec(
        "ADMIN_EMAIL: email\nDEBUG: number\nADMIN_NAME"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" " />\n'
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<input id="env_spec_debug" name="debug" type="number" " />\n'
        '<label for="env_spec_admin_name">ADMIN_NAME</label>\n'
        '<input id="env_spec_admin_name" name="admin_name" type="text" " />\n'
    )


def test_restricted_choices():
    assert env_spec.render_env_spec(
        "DEBUG: [0,1]\nENVIRONMENT: [production,staging,development]"
    ) == (
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<select id="env_spec_debug" name="debug">\n'
        '\t<option value="0">0</option>\n'
        '\t<option value="1">1</option>\n'
        "</select>\n"
        '<label for="env_spec_environment">ENVIRONMENT</label>\n'
        '<select id="env_spec_environment" name="environment">\n'
        '\t<option value="production">production</option>\n'
        '\t<option value="staging">staging</option>\n'
        '\t<option value="development">development</option>\n'
        "</select>\n"
    )


def test_wrong_default_values():
    with pytest.raises(env_spec.EnvSpecSyntaxError) as excinfo:
        env_spec.parse(
            "DEBUG: [0,1]=1\nENVIRONMENT: [production,staging,development]=develoent"
        )
    assert "SYNTAX ERROR: Invalid default value." in str(excinfo.value)


def test_default_values():
    assert env_spec.render_env_spec(
        "DEBUG: [0,1]= 1\nENVIRONMENT: [production,staging,development]= development"
    ) == (
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<select id="env_spec_debug" name="debug">\n'
        '\t<option value="0">0</option>\n'
        '\t<option value="1"selected>1</option>\n'
        "</select>\n"
        '<label for="env_spec_environment">ENVIRONMENT</label>\n'
        '<select id="env_spec_environment" name="environment">\n'
        '\t<option value="production">production</option>\n'
        '\t<option value="staging">staging</option>\n'
        '\t<option value="development"selected>development</option>\n'
        "</select>\n"
    )


def test_comments_syntax():
    assert env_spec.render_env_spec(
        "ADMIN_EMAIL: email # This email will be notified when exceptions get raised\nDEBUG: [0,1]= 1# Switching debug on emits verbose messages in the terminal\nENVIRONMENT: [production,staging,development]= development"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" " />\n'
        "<small> This email will be notified when exceptions get raised</small>\n"
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<select id="env_spec_debug" name="debug">\n'
        '\t<option value="0">0</option>\n'
        '\t<option value="1"selected>1</option>\n'
        "</select>\n"
        "<small> Switching debug on emits verbose messages in the terminal</small>\n"
        '<label for="env_spec_environment">ENVIRONMENT</label>\n'
        '<select id="env_spec_environment" name="environment">\n'
        '\t<option value="production">production</option>\n'
        '\t<option value="staging">staging</option>\n'
        '\t<option value="development"selected>development</option>\n'
        "</select>\n"
    )


def test_ignore_line_comments():
    assert env_spec.render_env_spec(
        "# This line will be ignored\nADMIN_EMAIL: email  # This email will be notified for occurring errors"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" " />\n'
        "<small> This email will be notified for occurring errors</small>\n"
    )
