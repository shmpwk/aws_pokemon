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
export ENDPOINT_URL="https:XXXXXXXXXXXXX.execute-api.ap-northeast-1.amazonaws.com/prod/"
```



## Testing API:

```bash
python -m unittest
```
