from elasticsearch import Elasticsearch

class elasticsearchConnector:
    def __init__(self, host="elastic", port=9200, username=None, password=None):
        self.es = Elasticsearch(
        [host],
        http_auth=(username, password) if username and password else None,
        port=port)

    def create_index(self, index_name, mappings):
        try:
            self.es.indices.create(index=index_name, body=mappings)
            return True
        except Exception as e:
            print(f"Error while creating the index: {str(e)}")
            return False


    def search_query(self, index, query_dto):
        search_query = {
            "query": {
                "multi_match": {
                    "query": query_dto,
                    "fields": ["title", "description", "body"]
                }
            }
        }

        results = self.es.search(index=index, body=search_query)

        return results
    
    def insert_query(self, index, title, description, body, doc_id=None):
        try:
            document = {
                "title": title,
                "description": description,
                "body": body
            }

            if doc_id:
                response = self.es.index(index=index, id=doc_id, body=document)
            else:
                response = self.es.index(index=index, body=document)

            return response
        except Exception as e:
            print(f"Error while inserting document: {str(e)}")
            return None
    
    def update_query(self, index, doc_id, title=None, description=None, body=None):
        try:
            doc = {}
            if title:
                doc["title"] = title
            if description:
                doc["description"] = description
            if body:
                doc["body"] = body

            response = self.es.update(index=index, id=doc_id, body={"doc": doc})

            return response
        except Exception as e:
            print(f"Error while updating document: {str(e)}")
            return None

    def delete_query(self, index, doc_id):
        try:
            response = self.es.delete(index=index, id=doc_id)
            return response["result"] == "deleted"
        except Exception as e:
            print(f"Error while deleting document: {str(e)}")
            return False

    
