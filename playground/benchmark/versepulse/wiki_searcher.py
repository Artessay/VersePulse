import os
from tqdm import tqdm
from diskcache import Cache
from elasticsearch import Elasticsearch

class WikiSearcher:
    """
    A class to interact with an Elasticsearch index for performing search queries.
        - `search(query: str, top_k: int = 10, return_score: bool = False)`
        - `batch_search(query: list, top_k: int = 10, return_score: bool = False)`
    """

    def __init__(self, index_name='wiki_en', url: str = "https://162.105.88.178:9200"):
        """
        Initializes the ElasticsearchSearcher with the given configuration.

        Args:
            index_name (str): Name of the Elasticsearch index.
            hostname (str, optional): Elasticsearch hostname. Defaults to 'localhost'.
            port (int, optional): Elasticsearch port. Defaults to 9200.
            size (int, optional): Number of search results to return. Defaults to 10.
        """

        self.index_name = index_name
        self.es = self.create_es_client(url)

        # Verify connection
        if not self.es.ping():
            raise ConnectionError(f"Cannot connect to Elasticsearch at {url}")
        
        self.cache = Cache('.wiki_search_cache')

    def search(self, query: str, top_k: int = 5):
        """
        Searches the Elasticsearch index for documents matching the query.

        Args:
            query (str): The search query string.

        Returns:
            list: A list of dictionaries containing search results.
        """

        # Check if the query is already in the cache
        if query in self.cache:
            return self.cache[query]
        
        # Define the search query using multi_match to search in 'title' and 'text' fields
        search_body = {
            "query": {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "text"] 
                }
            },
            "size": top_k
        }

        # Execute the search
        response = self.es.search(index=self.index_name, body=search_body)

        hits = response['hits']['hits']
        relevant_docs = [hit['_source'] for hit in hits]

        # Cache the result
        self.cache[query] = relevant_docs

        return relevant_docs

    def batch_search(self, queries: list, top_k: int = 5):
        return [self.search(query, top_k) for query in tqdm(queries, desc="Search")]

    def close(self):
        """
        Closes the Elasticsearch connection.
        """
        self.es.close()

    @staticmethod
    def create_es_client(url: str) -> Elasticsearch:
        """Initialize Elasticsearch client with environment configuration."""
        if not os.environ.get('ELASTIC_SEARCH_PASSWORD'):
            raise ValueError('ELASTIC_SEARCH_PASSWORD environment variable not set')

        return Elasticsearch(
            url,
            basic_auth=("elastic", os.getenv("ELASTIC_SEARCH_PASSWORD")),
            verify_certs=False,
            ssl_show_warn=False,
        )

def main():
    """
    Main function to handle command-line arguments and perform searches.
    """
    # Parse command-line arguments
    query = "Paris 2024 Olympic Games"

    try:
        # Initialize the searcher
        searcher = WikiSearcher()

        # Perform the search
        results = searcher.search(query)

        # Display the results
        if not results:
            print("No relevant documents found.")
        else:
            for idx, doc in enumerate(results, start=1):
                print(f"content #{idx}:")
                print(f"{doc}\n")

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
