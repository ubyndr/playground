# Cypher based solution for exercise 2 with Travis CI

### HOW-TO

```sh
git clone https://github.com/ubyndr/playground.git
```
```sh
pip install -r requirements.txt
```
```sh
docker run -d -p:7474:7474 -p 7687:7687 --volume=`pwd`:/import/  --env-file ./src/resources/env.list matentzn/vfb-prod
```
```sh
python3 src/load_db.py file:///src/resources/wine.owl
```
```sh
python3 src/app.py
```

For API documentation you can access swagger page via http://localhost:5001
