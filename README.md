# Multicloud Python Batch

## Install
1. Install docker, docker-compose

## How to build
1. Enter the project root<br>
   ```cd <project directory>```
2. Build docker<br>
   ```docker-compose up -d```
3. Run batch on local<br>
   ```docker exec -it local_batch_python python src/batch.py -o '{"hoge": "fuga"}'```<br>
   Run batch on local AWS<br>
   ```curl -XPOST "http://localhost:8020/2015-03-31/functions/function/invocations" -d '{"hoge": "fuga"}'```<br>
   Run batch on local GCP(Cloud Functions)<br>
   ```curl -XPOST http://localhost:8010/ -H 'Content-Type:application/json; charset=utf-8' -d '{"data": {"hoge": "fuga"}}'```<br>
4. Stop and Delete Docker<br>
   ```docker-compose down --rmi all --volumes --remove-orphans```<br>

## View logs
```docker logs <Container name> -f```

## Test
```docker exec -it local_batch_python pytest tests/```
