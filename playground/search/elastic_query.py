from elasticsearch import Elasticsearch
from elasticsearch.exceptions import NotFoundError

class ElasticsearchSearcher:
    """
    A class to interact with an Elasticsearch index for performing search queries.
    """

    def __init__(self, hostname='localhost', port=9200):
        """
        Initializes the ElasticsearchSearcher with the given configuration.

        Args:
            index_name (str): Name of the Elasticsearch index.
            hostname (str, optional): Elasticsearch hostname. Defaults to 'localhost'.
            port (int, optional): Elasticsearch port. Defaults to 9200.
            size (int, optional): Number of search results to return. Defaults to 10.
        """
        self.es = Elasticsearch([{'host': hostname, 'port': port}])

        # Verify connection
        if not self.es.ping():
            raise ConnectionError(f"Cannot connect to Elasticsearch at {hostname}:{port}")

    def search(self, query, size=10, index_name='wiki'):
        """
        Searches the Elasticsearch index for documents matching the query.

        Args:
            query (str): The search query string.

        Returns:
            list: A list of dictionaries containing search results.
        """
        # Define the search query using multi_match to search in 'title' and 'txt' fields
        search_query = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "txt"]  # Adjust fields based on your index
                }
            }
        }

        try:
            # Execute the search
            response = self.es.search(index=index_name, body=search_query, size=size)
        except NotFoundError:
            print(f"Index '{self.index_name}' not found. Please ensure the index name is correct and has been created.")
            return []
        except Exception as e:
            print(f"An error occurred during the search: {e}")
            return []

        # Parse the search results
        results = []
        for hit in response['hits']['hits']:
            doc = {
                'id': hit['_id'],
                'score': hit['_score'],
                'title': hit['_source'].get('title', ''),
                'content': hit['_source'].get('txt', '')
            }
            results.append(doc)

        return results

    def close(self):
        """
        Closes the Elasticsearch connection.
        """
        self.es.close()

def main():
    """
    Main function to handle command-line arguments and perform searches.
    """
    # Parse command-line arguments
    import argparse
    parser = argparse.ArgumentParser(description='Search for relevant information in an Elasticsearch knowledge base.')
    parser.add_argument('--query', type=str, required=True, help='Search query string')
    parser.add_argument('--index_name', type=str, default='wiki', help='Name of the Elasticsearch index')
    parser.add_argument('--hostname', type=str, default='localhost', help='Elasticsearch hostname (default: localhost)')
    parser.add_argument('--port', type=int, default=9200, help='Elasticsearch port (default: 9200)')
    parser.add_argument('--size', type=int, default=10, help='Number of results to return (default: 10)')

    args = parser.parse_args()

    try:
        # Initialize the searcher
        searcher = ElasticsearchSearcher(
            hostname=args.hostname,
            port=args.port,
        )

        # Perform the search
        results = searcher.search(query=args.query)

        # Display the results
        if not results:
            print("No relevant documents found.")
        else:
            for idx, doc in enumerate(results, start=1):
                print(f"Result {idx}:")
                print(f"ID: {doc['id']}")
                print(f"Score: {doc['score']}")
                print(f"Title: {doc['title']}")
                print(f"Content: {doc['content']}\n")

    except ConnectionError as ce:
        print(f"Connection Error: {ce}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Ensure the Elasticsearch connection is closed
        if 'searcher' in locals():
            searcher.close()

if __name__ == '__main__':
    main()
