from fastapi import FastAPI, Query, HTTPException
from app.connector import elasticsearchConnector as esc
from .dto import QueryDTO


app = FastAPI()
elastic = esc()

@app.get("/")
def home():
    return "This is an application to search SQL queries in Elasticsearch"


@app.post("/create_default_index")
async def create_default_index():
    try:
        index_name = "queries"
        mappings = {
            "mappings": {
                "properties": {
                    "query_title": {"type": "text"},
                    "query_description": {"type": "text"},
                    "query_body": {"type": "text"}
                }
            }
        }

        result = elastic.create_index(index_name, mappings)

        if result:
            return {"message": f"Default index '{index_name}' created successfully."}
        else:
            raise HTTPException(status_code=500, detail="Failed to create the default index.")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while creating the default index.")


@app.post("/insert_query/{index_name}")
async def insert_query(query: QueryDTO, index_name: str):
    title = query.query_title
    description = query.query_description
    body = query.query_body

    try:
        elastic.insert_query(index=index_name, title=title, description=description, body=body)
        return "Query inserted successfully"
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while inserting the query.")


@app.get("/search_query/{index_name}")
async def search_query(index_name: str, query_title: str = Query(None, title="Query Title"),
                 query_description: str = Query(None, title="Query Description"),
                 query_body: str = Query(None, title="Query Body")):
    try:
        query_dto = " ".join(filter(None, [query_title, query_description, query_body]))

        if not query_dto:
            raise HTTPException(status_code=400, detail="Please provide at least one search term.")

        search_results = elastic.search_query(index_name, query_dto)

        if search_results:
            return search_results
        else:
            raise HTTPException(status_code=404, detail="No matching documents found")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to perform search operation")


@app.put("/update_query/{index_name}/{doc_id}")
async def update_query(index_name: str, doc_id: str, query: QueryDTO):
    title = query.query_title
    description = query.query_description
    body = query.query_body

    try:
        response = elastic.update_query(index_name, doc_id, title=title, description=description, body=body)

        if response:
            return {"message": "Query updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="Document not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to update query")


@app.delete("/delete_query/{index_name}/{doc_id}")
async def delete_query(index_name: str, doc_id: str):
    try:
        response = elastic.delete_query(index_name, doc_id)

        if response:
            return {"message": "Query deleted successfully"}
        else:
            raise HTTPException(status_code=404, detail="Document not found")

    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to delete query")