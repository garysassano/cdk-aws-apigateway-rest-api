from aws_cdk import (
    Duration,
    Stack,
    aws_apigateway as apigw,
    aws_lambda as _lambda,
)
from constructs import Construct


class ApiGatewayRestApiStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Create lambda function
        test_lambda = _lambda.Function(
            self,
            "LambdaFunction_test-lambda",
            function_name="test-lambda",
            code=_lambda.Code.from_asset("lambda/functions/test-lambda"),
            handler="lambda_function.lambda_handler",
            runtime=_lambda.Runtime.PYTHON_3_10,
        )

        # Create REST API with CORS
        test_rest_api = apigw.RestApi(
            self,
            "RestApiGateway_test-rest-api",
            rest_api_name="test-rest-api",
            default_cors_preflight_options=apigw.CorsOptions(
                allow_methods=["GET"],
                allow_origins=apigw.Cors.ALL_ORIGINS,
                max_age=Duration.days(10),
            ),
        )

        # Add method to REST API
        test_rest_api.root.add_method(
            "GET",
            integration=apigw.LambdaIntegration(test_lambda),
        )
