from aws_cdk import (
    core,
    aws_dynamodb as ddb,
    aws_s3 as s3,
    aws_s3_deployment as s3_deploy,
    aws_lambda as _lambda,
    aws_ssm as ssm,
    aws_apigateway as apigw,
)
import os

class Bashoutter(core.Stack):

    def __init__(self, scope: core.App, name: str, **kwargs) -> None:
        super().__init__(scope, name, **kwargs)
        
        # dynamoDB table to store pokemon
        table = ddb.Table(
            self, "Bashoutter-Table",
            partition_key=ddb.Attribute(
                name="item_id",
                type=ddb.AttributeType.STRING
            ),
            billing_mode=ddb.BillingMode.PAY_PER_REQUEST,
            removal_policy=core.RemovalPolicy.DESTROY
        )
        common_params = {
            "runtime": _lambda.Runtime.PYTHON_3_7,
            "environment": {
                "TABLE_NAME": table.table_name
            }
        }

        # define Lambda functions
        show_lambda = _lambda.Function(
            self, "ShowPokemon",
            code=_lambda.Code.from_asset("api"),
            handler="api.show_pokemon",
            memory_size=512,
            timeout=core.Duration.seconds(10),
            **common_params,
        )
        get_lambda = _lambda.Function(
            self, "GetPokemon",
            code=_lambda.Code.from_asset("api"),
            handler="api.get_pokemon",
            **common_params,
        )
        levelup_lambda = _lambda.Function(
            self, "LevelUp",
            code=_lambda.Code.from_asset("api"),
            handler="api.level_up",
            **common_params,
        )
        goodbye_lambda = _lambda.Function(
            self, "ByePokemon",
            code=_lambda.Code.from_asset("api"),
            handler="api.bye_pokemon",
            **common_params,
        )

        # grant permissions
        table.grant_read_data(show_lambda)
        table.grant_read_write_data(get_lambda)
        table.grant_read_write_data(levelup_lambda)
        table.grant_read_write_data(goodbye_lambda)

        # define API Gateway
        api = apigw.RestApi(
            self, "BashoutterApi",
            default_cors_preflight_options=apigw.CorsOptions(
                allow_origins=apigw.Cors.ALL_ORIGINS,
                allow_methods=apigw.Cors.ALL_METHODS,
            )
        )

        pokemon = api.root.add_resource("pokemon")
        pokemon.add_method(
            "SHOW",
            apigw.LambdaIntegration(show_lambda)
        )
        pokemon.add_method(
            "GET",
            apigw.LambdaIntegration(get_lambda)
        )

        pokemon_item_id = pokemon.add_resource("{item_id}")
        pokemon_item_id.add_method(
            "LEVELUP",
            apigw.LambdaIntegration(levelup_lambda)
        )
        pokemon_item_id.add_method(
            "BYE",
            apigw.LambdaIntegration(goodbye_lambda)
        )

        # store parameters in SSM
        ssm.StringParameter(
            self, "TABLE_NAME",
            parameter_name="TABLE_NAME",
            string_value=table.table_name
        )
        ssm.StringParameter(
            self, "ENDPOINT_URL",
            parameter_name="ENDPOINT_URL",
            string_value=api.url
        )

app = core.App()
Bashoutter(
    app, "Bashoutter",
    env={
        "region": os.environ["CDK_DEFAULT_REGION"],
        "account": os.environ["CDK_DEFAULT_ACCOUNT"],
    }
)

app.synth()
