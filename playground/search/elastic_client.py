import requests

def search_query(query):
    # Flask server的URL
    url = 'http://123.57.228.132:8288/search'

    # 请求的参数，只需要传入query
    params = {'query': query}

    try:
        # 发送GET请求到Flask服务器
        response = requests.get(url, params=params)

        # 检查返回的状态码
        if response.status_code == 200:
            # 请求成功，打印返回的JSON结果
            data = response.json()

            results = data['results']
            results_str = "\n".join([
                f"Passage #{i+1}\nTitle: {doc['title']}\nSnippet: {doc['content']}" 
                for i, doc in enumerate(results)
            ])
            return results_str
        else:
            print(f"Error: {response.status_code} - {response.json().get('error', 'Unknown error')}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return "An error occurred"

if __name__ == "__main__":
    # 提供查询内容
    query = "Deep Learning" # input("Enter your search query: ")
    result = search_query(query)
    print(result)
