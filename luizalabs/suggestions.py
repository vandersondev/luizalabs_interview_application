#!/usr/bin/env python3


from neo4j.v1 import GraphDatabase
from settings import DATABASES

user = DATABASES['user']
passwd = DATABASES['passwd']

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=(user, passwd))


def makeSuggestions():

    query = '''
            MATCH (p)-[:KNOWS*2..2]-(f)
            WHERE NOT (p)-[:KNOWS]-(f)
            AND NOT p.name = f.name
            CREATE UNIQUE (p)-[:SUGGESTED]->(f)
            CREATE UNIQUE (f)-[:SUGGESTED]->(p)
            '''

    with driver.session() as session:
        with session.begin_transaction() as t:
            t.run(query)
    return


if __name__ == "__main__":
    makeSuggestions()
