from flask import Flask, request, jsonify

from elastic_query import ElasticsearchSearcher

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    """
    API endpoint to search for relevant documents in Elasticsearch.
    """
    # Get parameters from the request
    query = request.args.get('query')
    index_name = request.args.get('index_name', 'wiki')
    hostname = request.args.get('hostname', 'localhost')
    port = int(request.args.get('port', 9200))
    size = int(request.args.get('size', 10))

    if not query:
        return jsonify({"error": "Query parameter is required"}), 400

    # Initialize the searcher
    searcher = ElasticsearchSearcher(hostname=hostname, port=port)

    try:
        # Perform the search
        results = searcher.search(query=query, index_name=index_name, size=size)

        if not results:
            return jsonify({"message": "No relevant documents found."}), 404

        # Return results as JSON
        return jsonify({"results": results}), 200

    except ConnectionError as ce:
        return jsonify({"error": f"Connection Error: {ce}"}), 500
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {e}"}), 500
    finally:
        # Ensure the Elasticsearch connection is closed
        searcher.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(debug=True, host='0.0.0.0', port=5000)