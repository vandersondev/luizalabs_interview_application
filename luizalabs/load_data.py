#!/usr/bin/env python3


from neo4j.v1 import GraphDatabase
from settings import DATABASES

user = DATABASES['user']
passwd = DATABASES['passwd']

uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=(user, passwd))


def load_data():

    query = '''
            CREATE (arthur:Person {name:"Arthur"}),
              (mari:Person {name:"Mari"}),
              (eduardo:Person {name:"Eduardo"}),
              (gabriel:Person {name:"Gabriel"}),

              (arthur)-[:KNOWS]->(mari),
              (arthur)-[:KNOWS]->(eduardo),

              (mari)-[:KNOWS]->(arthur),
              (mari)-[:KNOWS]->(eduardo),
              (mari)-[:KNOWS]->(gabriel),

              (eduardo)-[:KNOWS]->(arthur),
              (eduardo)-[:KNOWS]->(mari),
              (eduardo)-[:KNOWS]->(gabriel),

              (gabriel)-[:KNOWS]->(mari),
              (gabriel)-[:KNOWS]->(eduardo)
            '''

    with driver.session() as session:
        with session.begin_transaction() as t:
            t.run(query)
    return


if __name__ == "__main__":
    load_data()
