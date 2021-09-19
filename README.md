# Cypher based solution for exercise 2 with Travis CI

### HOW-TO

Clone the repository
```sh
git clone https://github.com/ubyndr/playground.git
```
Install requirements
```sh
pip install -r requirements.txt
```
Make sure docker has access to the location where you've checked out this repo.

Launch a local copy of the DB and load the ontology
```sh
docker run -d -p:7474:7474 -p 7687:7687 --volume=`pwd`:/import/  --env-file ./src/resources/env.list matentzn/vfb-prod
```
Import wine ontology into Neo4j
```sh
python3 src/load_db.py file:///src/resources/wine.owl
```
Run the app
```sh
python3 src/app.py
```

For API documentation you can access swagger page via http://localhost:5001
