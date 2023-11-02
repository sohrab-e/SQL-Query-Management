from pydantic import BaseModel

class QueryDTO(BaseModel):
    query_title: str
    query_description: str
    query_body: str