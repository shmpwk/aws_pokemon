# AWS POKEMON

## Description
This repo is for my exercise in building AWS serverless architecture. 

## Requrement
Docker (version?)

## Get Start

### venv を作成し，依存ライブラリのインストールを行う
```
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```
### AWS の認証情報をセットする
#### 自分自身の認証情報に置き換える
```
export AWS_ACCESS_KEY_ID=XXXXXX
export AWS_SECRET_ACCESS_KEY=YYYYYY
export AWS_DEFAULT_REGION=ap-northeast-1
```

#### デプロイを実行
```
$ cdk deploy
```

## Testing API:

```bash
python -m unittest
```
