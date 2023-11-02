# SQL Query Management

## Overview

In a data or Business Intelligence (BI) team, SQL is an indispensable tool for extracting data from relational databases, and it plays a vital role in our daily work. As our team consistently generates numerous SQL queries, there is a growing need to share these queries with other team members, especially new joiners. The primary objective of this project is to develop a simple application that leverages Elasticsearch as a data store. It facilitates various operations, including searching for, creating, updating, and deleting SQL queries. Each query is stored as a document, featuring three essential fields: 'query title,' 'query description,' and 'query body'.


## Projects files and strcture
This project leverages Elasticsearch for storing SQL query documents and employs FastAPI as the backend framework. The core components of this project are organized in the following manner:

- **app/connector.py**: This file contains Elasticsearch instance initialization and various methods necessary for CRUD (Create, Read, Update, and Delete) operations.

- **app/dto.py**: The Data Transfer Object (DTO) is defined in this file to facilitate structured data handling.

- **app/main.py**: In this file, FastAPI is utilized to manage SQL queries and handle API endpoints.

## Getting Started

This project is containerized for ease of use. To run the project, execute the following command:

```shell
docker-compose up --build
```

## Upcoming Features
In the next phases of development, we plan to implement an interface and user role management system to enhance the project's functionality.