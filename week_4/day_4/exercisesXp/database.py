import psycopg2

class DatabaseManager:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            return connection
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to the database:", error)
            return None

    def execute_query(self, query, params=None):
        connection = self.connect()
        if connection:
            try:
                cursor = connection.cursor()
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)

                # Check if the query is an UPDATE/DELETE/INSERT, in which case no results to fetch
                query_type = query.strip().split()[0].upper()
                if query_type in ("UPDATE", "DELETE", "INSERT"):
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return True
                else:
                    rows = cursor.fetchall()
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return rows

            except (Exception, psycopg2.Error) as error:
                print("Error while executing query:", error)
                connection.rollback()
                connection.close()
                return False

        return False


