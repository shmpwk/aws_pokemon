# AWS POKEMON

## Description
This repo is for my exercise in building AWS serverless architecture. 

## Requrement
Docker (version?)

## Get Start

### venv ���쐬���C�ˑ����C�u�����̃C���X�g�[�����s��
```
$ python3 -m venv .env
$ source .env/bin/activate
$ pip install -r requirements.txt
```
### AWS �̔F�؏����Z�b�g����
#### �������g�̔F�؏��ɒu��������
```
export AWS_ACCESS_KEY_ID=XXXXXX
export AWS_SECRET_ACCESS_KEY=YYYYYY
export AWS_DEFAULT_REGION=ap-northeast-1
```

#### �f�v���C�����s
```
$ cdk deploy
```

## Testing API:

```bash
python -m unittest
```
