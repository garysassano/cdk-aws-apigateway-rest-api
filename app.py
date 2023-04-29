import os
import aws_cdk as cdk
from stacks.apigateway_rest_api_stack import ApiGatewayRestApiStack

app = cdk.App()

ApiGatewayRestApiStack(
    app,
    "dev",
    stack_name="ApiGatewayRestApiStack-dev",
    env=cdk.Environment(
        account=os.environ.get("CDK_DEFAULT_ACCOUNT"),
        region=os.environ.get("CDK_DEFAULT_REGION"),
    ),
)

app.synth()
