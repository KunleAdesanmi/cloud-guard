"""Command-line entry point for cloudguard."""

import sys

import boto3
from botocore.exceptions import (
    NoCredentialsError,
    ProfileNotFound,
    SSOTokenLoadError,
    TokenRetrievalError,
    UnauthorizedSSOTokenError,
)

from cloudguard.identity import get_identity

PROFILE = "cg-sandbox"


LOGIN_ERRORS = (
    NoCredentialsError,
    ProfileNotFound,
    SSOTokenLoadError,
    TokenRetrievalError,
    UnauthorizedSSOTokenError,
)


def main() -> None:
    try:
        session = boto3.Session(profile_name=PROFILE)
        identity = get_identity(session)
    except LOGIN_ERRORS as error:
        print(f"Cannot authenticate to AWS: {error}", file=sys.stderr)
        print(
            f"Fix: aws sso login --use-device-code --profile {PROFILE}", file=sys.stderr
        )
        sys.exit(1)

    print(f"Account: {identity['account']}")

    print(f"ARN:     {identity['arn']}")
