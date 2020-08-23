import json, os, uuid, decimal
from datetime import datetime, timezone
import boto3

ddb = boto3.resource("dynamodb")
table = ddb.Table(os.environ["TABLE_NAME"])

HEADERS = {
    "Access-Control-Allow-Origin": "*",
}

# this custom class is to handle decimal.Decimal objects in json.dumps()
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

def show_pokemon(event, context):
    """
    handler for SHOW /pokemon
    """
    try:
        response = table.scan()

        status_code = 200
        resp = response.get("Items")
    except Exception as e:
        status_code = 500
        resp = {"description": f"Internal server error. {str(e)}"}
    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp, cls=DecimalEncoder)
    }

def get_pokemon(event, context):
    """
    handler for GET /pokemon
    """
    try:
        body = event.get("body")
        if not body:
            raise ValueError("Invalid request. The request body is missing!")
        body = json.loads(body)

        for key in ["name", "first_move ", "second_move"]:
            if not body.get(key):
                raise ValueError(f"{key} is empty")

        item = {
            "pokemon_number": uuid.uuid4().hex,
            "name": body["name"],
            "first_move": body["first_move"],
            "second_move": body["second_move"],
            "level": 0,
            "created_at": datetime.now(timezone.utc).isoformat(timespec="seconds")
        }
        response = table.put_item(Item=item)

        status_code = 201
        resp = {"description": "Successfully get pokemon"}
    except ValueError as e:
        status_code = 400
        resp = {"description": f"Bad request. {str(e)}"}
    except Exception as e:
        status_code = 500
        resp = {"description": str(e)}
    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp)
    }

def level_up(event, context):
    """
    handler for LEVELUP /pokemon/{pokemon_number}
    """
    try:
        path_params = event.get("pathParameters", {})
        pokemon_number = path_params.get("pokemon_number", "")
        if not pokemon_number:
            raise ValueError("Invalid request. The path parameter 'pokemon_number' is missing")
        
        response = table.update_item(
            Key={"pokemon_number": pokemon_number},
            UpdateExpression=f"SET level = level + :inc",
            ExpressionAttributeValues={
                ':inc': 1,
            }
        )

        status_code = 200
        resp = {"description": "OK"}
    except ValueError as e:
        status_code = 400
        resp = {"description": f"Bad request. {str(e)}"}
    except Exception as e:
        status_code = 500
        resp = {"description": str(e)}
    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp)
    }

def bye_pokemon(event, context):
    """
    handler for BYE /pokemon/{pokemon_number}
    """
    try:
        path_params = event.get("pathParameters", {})
        pokemon_number = path_params.get("pokemon_number", "")
        if not pokemon_number:
            raise ValueError("Invalid request. The path parameter 'pokemon_number' is missing")
        
        response = table.delete_item(
            Key={"pokemon_number": pokemon_number}
        )

        status_code = 204
        resp = {"description": "Successfully saying good bye."}
    except ValueError as e:
        status_code = 400
        resp = {"description": f"Bad request. {str(e)}"}
    except Exception as e:
        status_code = 500
        resp = {"description": str(e)}
    return {
        "statusCode": status_code,
        "headers": HEADERS,
        "body": json.dumps(resp)
    }
