"""Tests for cloudguard.identity, using moto's fake AWS."""

import boto3
import pytest
from moto import mock_aws

from cloudguard.identity import get_identity


@pytest.fixture
def fake_aws_credentials(monkeypatch: pytest.MonkeyPatch) -> None:
    """Point boto3 at dummy credentials so a test can never reach real AWS."""

    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "testing")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "testing")
    monkeypatch.setenv("AWS_DEFAULT_REGION", "eu-west-2")

    monkeypatch.delenv("AWS_PROFILE", raising=False)


def test_get_identity_returns_account_and_arn(fake_aws_credentials: None) -> None:
    with mock_aws():
        session = boto3.Session()
        identity = get_identity(session)

    assert identity["account"] == "123456789012"
    assert identity["arn"].startswith("arn:aws:")

    assert set(identity) == {"account", "arn"}
