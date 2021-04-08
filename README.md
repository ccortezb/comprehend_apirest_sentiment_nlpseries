# comprehend-01-nlpseries-ep-3

estos son los 3 archvos que necesitas editar si empieazas desde cero un repo de SAM de Hello World.

- app.py - codigo principal con comprehend
- events/event.json - ejemplo de json para invocar lambda
- template.yaml - plantilla que define SAM

Aqui esta el post completo:

* [Medium Blog](https://ccortez.medium.com)


## Desplegar desde cero este repo


* SAM CLI - [Install the SAM CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
* [Python 3 installed](https://www.python.org/downloads/)
* Docker - [Install Docker community edition](https://hub.docker.com/search/?type=edition&offering=community)

Para construir y desplegar, tener ya configurado tu AWS CLI O un rol que te permita ejecutar Cloud formation y s3:

```bash
sam build --use-container
sam deploy --guided
```


## Puedes probar desplegar localmente con SAM y Docker

Usa  `sam build --use-container` para crear un docker container local con esta demo.

```bash
comprehend-01-nlpseries-ep-3$ sam build --use-container
```


```bash
comprehend-01-nlpseries-ep-3$ sam local invoke "Comprehend01nlpseriesep3Function" -e event.json
```

La SAM CLI tambien puede emular el API de API Gateway localmente. Usa  `sam local start-api` para ejecutar un API por el puerto 3000.

```bash
comprehend-01-nlpseries-ep-3$ sam local start-api
comprehend-01-nlpseries-ep-3$ curl http://localhost:3000/
```

Aqui la definicion en la plantilla que crea el API, revisalo en template.yaml


```yaml
      Events:
        HttpPost:
          Type: Api
          Properties:
            Path: '/sentiment'
            Method: post
```


## Revisa y monitorea los logs del API

Puedes hacer un poco de revision de logs con este comando


```bash
comprehend-01-nlpseries-ep-3$ sam logs -n Comprehend01nlpseriesep3Function --stack-name comprehend-01-nlpseries-ep-3 --tail
```


## Unit tests

lo encuentras en la carpeta `tests` . Usa PIP para instalar [pytest](https://docs.pytest.org/en/latest/) and run unit tests.

```bash
comprehend-01-nlpseries-ep-3$ pip install pytest pytest-mock --user
comprehend-01-nlpseries-ep-3$ python -m pytest tests/ -v
```

## Cleanup

Borrar todo con:

```bash
aws cloudformation delete-stack --stack-name comprehend-01-nlpseries-ep-3
```

## Resources

* [Cortez Cloud](https://cortez.cloud)
* [Al dia con AWS Podcast](https://aldiaconaws.cortez.cloud)
* [Imperio Cloud Podcast](https://imperiocloud.com)


