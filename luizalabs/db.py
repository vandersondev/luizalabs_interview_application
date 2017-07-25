from neo4j.v1 import GraphDatabase


uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'root'))


def getAllPersons():

    persons = []

    with driver.session() as session:
        with session.begin_transaction() as t:
            for record in t.run('MATCH (p:Person) RETURN p.name, ID(p) AS id'):
                persons.append({'id': record['id'], 'name': record['p.name']})

    return persons


def getAllFriends(name):

    friends = []

    with driver.session() as session:
        with session.begin_transaction() as t:
            for record in t.run('''
                                    MATCH (p:Person)-[k:KNOWS]->(f:Person)
                                    WHERE  toLower(p.name) = "{}"
                                    RETURN f.name, ID(f) AS id
                                    '''.format(name)):

                friends.append({'id': record['id'], 'name': record['f.name']})

    return friends


def getAllSuggestions(name):

    suggestions = []

    with driver.session() as session:
        with session.begin_transaction() as t:
            for record in t.run('''
                                    MATCH (p:Person)-[k:SUGGESTED]->(f:Person)
                                    WHERE  toLower(p.name) = "{}"
                                    RETURN f.name, ID(f) AS id
                                    '''.format(name)):

                suggestions.append({
                                    'id': record['id'],
                                    'name': record['f.name']
                                    })

    return suggestions
