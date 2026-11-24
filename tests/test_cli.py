"""Tests for the cloudguard command-line entry point."""

import pytest

from cloudguard import cli


def test_main_exits_1_with_fix_hint_when_profile_missing(
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
) -> None:

    monkeypatch.setattr(cli, "PROFILE", "does-not-exist")

    with pytest.raises(SystemExit) as exit_info:
        cli.main()

    assert exit_info.value.code == 1

    assert "aws sso login" in capsys.readouterr().err
