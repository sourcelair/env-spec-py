import env_spec


def test_invalid_input_non_latin():
    assert env_spec.render_env_spec_to_html("dαtabase_url") == ""


def test_invalid_input_start_with_digit():
    assert env_spec.render_env_spec_to_html("1DATABASE_URL: url") == ""


def test_non_existed_type():
    assert env_spec.render_env_spec_to_html("DATABASE_URL: testing") == ""


def test_valid_input_types():
    assert env_spec.render_env_spec_to_html(
        "ADMIN_EMAIL: email\nDEBUG: number\nADMIN_NAME"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" />\n'
        '<label for="env_spec_debug">DEBUG</label>\n'
        '<input id="env_spec_debug" name="debug" type="number" />\n'
        '<label for="env_spec_admin_name">ADMIN_NAME</label>\n'
        '<input id="env_spec_admin_name" name="admin_name" type="text" />\n'
    )


def test_restricted_choices():
    assert env_spec.render_env_spec_to_html(
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
    assert (
        env_spec.render_env_spec_to_html(
            "DEBUG: [0,1]=1\nENVIRONMENT: [production,staging,development]=develoent"
        )
        == ""
    )


def test_default_values():
    assert env_spec.render_env_spec_to_html(
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
    assert env_spec.render_env_spec_to_html(
        "ADMIN_EMAIL: email # This email will be notified when exceptions get raised\nDEBUG: [0,1]= 1# Switching debug on emits verbose messages in the terminal\nENVIRONMENT: [production,staging,development]= development"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" />\n'
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


def test_ignore_comments():
    assert env_spec.render_env_spec_to_html(
        "# This line will be ignored\nADMIN_EMAIL: email  # This email will be notified for occurring errors"
    ) == (
        '<label for="env_spec_admin_email">ADMIN_EMAIL</label>\n'
        '<input id="env_spec_admin_email" name="admin_email" type="email" />\n'
        "<small> This email will be notified for occurring errors</small>\n"
    )
