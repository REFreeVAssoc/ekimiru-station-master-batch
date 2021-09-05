# Multicloud Python Batch

## Install
1. Install docker, docker-compose
2. Install tmux

## How to build
1. Enter the project root<br>
   ```cd <project directory>```
2. Build docker<br>
   ```make start```
3. Run batch on local<br>
   ```docker exec -it local_batch_python python src/batch.py -o '{"hoge": "fuga"}'```<br>
   Run batch on local AWS<br>
   ```curl -XPOST "http://localhost:8020/2015-03-31/functions/function/invocations" -d '{"hoge": "fuga"}'```<br>
   Run batch on local GCP(Cloud Functions)<br>
   ```curl -XPOST http://localhost:8010/ -H 'Content-Type:application/json; charset=utf-8' -d '{"data": {"hoge": "fuga"}}'```<br>
4. Stop Docker<br>
   ```make stop```<br>
5. Remove Docker<br>
   ```make remove```<br>

## View docker logs
```docker logs <Container name> -f```

## Test
```docker exec -it local_batch_python pytest tests/```

## How to Develop
1. Fork this repository to your github project
2. clone your repository<br>
   ```git clone <your repo>```<br>
3. add this repository to your remote upstream<br>
   ```git remote add upstream git@github.com:titabash/multicloud-python-batch.git```<br>
   You are ready to develop your batch.
## How to merge upstream change
4. fetch the upstream repo<br>
   ```git fetch upstream```<br>
5. merge the upstream change<br>
   ```git merge upstream/main```<br>
