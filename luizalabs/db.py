from neo4j.v1 import GraphDatabase


uri = 'bolt://localhost:7687'
driver = GraphDatabase.driver(uri, auth=('neo4j', 'root'))


def test():
    with driver.session() as session:
        with session.begin_transaction() as t:
            for record in t.run('MATCH (p:Person) RETURN p.name, ID(p) AS id'):
                print(record['p.name'], record['id'])

    return


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
                                    MATCH (p)-[:KNOWS*2..2]-(f)
                                    WHERE toLower(p.name) = "{0}"
                                    AND NOT (p)-[:KNOWS]-(f)
                                    AND NOT toLower(f.name) = '{0}'
                                    CREATE UNIQUE (p)-[:SUGGESTED]->(f)
                                    CREATE UNIQUE (f)-[:SUGGESTED]->(p)
                                    RETURN f.name, ID(f) AS id
                                    '''.format(name)):

                suggestions.append({
                                    'id': record['id'],
                                    'name': record['f.name']
                                    })

    seen = set()
    sanitize_suggestions = []

    for d in suggestions:
        t = tuple(d.items())
        if t not in seen:
            seen.add(t)
            sanitize_suggestions.append(d)

    print(sanitize_suggestions)

    return sanitize_suggestions
