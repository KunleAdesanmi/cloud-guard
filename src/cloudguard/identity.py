"""Look up which AWS identity the current credentials belong to."""

import boto3


def get_identity(session: boto3.Session) -> dict[str, str]:
    """Return the account ID and ARN for the session's credentials."""
    sts = session.client("sts")
    response = sts.get_caller_identity()

    return {"account": response["Account"], "arn": response["Arn"]}
