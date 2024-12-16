from neo4j import GraphDatabase
import neo4j_config 

class Neo4jConnector:
    def __init__(self, uri, user, password):
        self.uri = uri
        self.user = user
        self.password = password
        self.driver = GraphDatabase.driver(self.uri, auth=(self.user, self.password))

    def close(self):
        self.driver.close()

    def run_query(self, query):
        with self.driver.session() as session:
            result = session.run(query)
            return result.data()

if __name__ == "__main__":

    connector = Neo4jConnector(neo4j_config.NEO4J_URI, neo4j_config.NEO4J_USER, neo4j_config.NEO4J_PASSWORD)

    query = "MATCH (n) RETURN n LIMIT 5"
    results = connector.run_query(query)
    print(results)

    connector.close()
