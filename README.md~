# AWS POKEMON

## Description
This repo is for my exercise in building AWS serverless architecture. 

## Requrement
Docker (version?)

## Get Start

### Create venv and install dependent libraries
```
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```
### Set your AWS credential
Note that you should change "XXXXXXXX".
```
export AWS_ACCESS_KEY_ID=XXXXXX
export AWS_SECRET_ACCESS_KEY=YYYYYY
export AWS_DEFAULT_REGION=ap-northeast-1
```

### deploy!!!
```
$ cdk deploy
```

## Let's play

### API 
First, set end point.

You can get your end point when deploing.
End point is written like `Bashoutter.BashoutterApiEndpoint = XXXXXXXXX`.
Change XXXXXXXXXX to your end point.
```
$ export ENDPOINT_URL="https:XXXXXXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/prod/"
```

#### SHOW YOUR POKEMON
```
$ http GET "${ENDPOINT_URL}/pokemon"

```

#### GET NEW POKEMON

```
$ http POST "${ENDPOINT_URL}/pokemon" name="XXXXX"  first_move="XXXXXX" second_move="XXXXX"      
```
For example,
```
$ http POST "${ENDPOINT_URL}/pokemon" name="pikachu"  first_move="1000000bolt" second_move="tackle"
```

#### LEVEL UP 
XXXXX is pokemon_number

```
$ http PATCH "${ENDPOINT_URL}/pokemon/XXXXX"
```

#### SAY GOOD BYE TO POKEMON
XXXXX is pokemon_number
```
$ http DELETE "${ENDPOINT_URL}/pokemon/XXXXX"

```

## Testing API:

```bash
python -m unittest
```
