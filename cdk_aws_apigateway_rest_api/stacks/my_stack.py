from pathlib import Path
from aws_cdk import (
    Stack,
    aws_apigateway as apigw,
)
from aws_cdk.aws_lambda import Code, Function, Runtime
from aws_cdk.aws_apigateway import LambdaIntegration, RestApi
from constructs import Construct


class MyStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        rest_lambda = Function(
            self,
            "RestLambda",
            function_name="rest-lambda",
            code=Code.from_asset(
                str(Path(__file__).parent / ".." / "functions" / "rest")
            ),
            handler="index.handler",
            runtime=Runtime.PYTHON_3_12,
        )

        rest_api = RestApi(
            self,
            "RestApi",
            rest_api_name="rest-api",
        )

        rest_api.root.add_method(
            "GET",
            integration=LambdaIntegration(rest_lambda),
        )
