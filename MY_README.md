# Flask NBA Database App - CSPB 3308

## Overview

This Flask application shows how to interact with a PostgreSQL database using Python and the `psycopg2` library. It includes routes for common operations like testing the connection, creating a table, inserting data, selecting data, and dropping the table.

All functionality is tied to a fictional NBA database storing basic player and team information.

---

## Routes and Functionality

### `/`
- Simple test route that returns a "Hello World" message.

### `/db_test`
- Opens and closes a PostgreSQL connection to verify database connectivity.

### `/db_create`
- Creates a `Basketball` table if it does not already exist.
- Columns include: First, Last, City, Team Name, and Jersey Number.

### `/db_insert`
- Populates the `Basketball` table with 4 example NBA players.

### `/db_select`
- Retrieves all data from the `Basketball` table and returns it as an HTML table.

### `/db_drop`
- Drops the `Basketball` table from the database. All data is lost when this is called.

---

## External Dependencies

- **PostgreSQL**: The app uses a remote PostgreSQL database via the `psycopg2` driver.
- **Flask**: A lightweight Python web framework used to define API endpoints.

To install Flask and psycopg2:
```bash
pip install flask psycopg2

