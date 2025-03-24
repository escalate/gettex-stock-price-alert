import pytest
import responses
from click.testing import CliRunner

from cli import cli
from gettex_stock_price_alert.gettex_stock_price_alert import (
    gettex_stock_price_alert,
)


@pytest.fixture(scope="function")
def cli_runner():
    return CliRunner()


@pytest.mark.usefixtures("cli_runner")
def test_cli_with_no_parameter(cli_runner):
    actual = cli_runner.invoke(cli, [])
    assert actual.exit_code == 2
    assert "Usage: cli [OPTIONS]" in actual.output
    assert "Error: Missing option '--url'." in actual.output


@pytest.mark.usefixtures("cli_runner")
def test_cli_with_all_parameters(cli_runner, caplog):
    actual = cli_runner.invoke(cli, ["--url=https://example.com"])
    assert "Response: " in caplog.text
    assert actual.exit_code == 0


@responses.activate
def test_request_call():
    responses.get(
        "https://example.com",
        status=200,
    )
    actual = gettex_stock_price_alert("https://example.com")

    assert actual.request.method == "GET"
    assert actual.status_code == 200
