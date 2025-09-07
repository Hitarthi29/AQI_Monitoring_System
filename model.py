import mysql.connector

class AQIDatabase:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS india_aqi (
                sr_no INT AUTO_INCREMENT PRIMARY KEY,
                city VARCHAR(100),
                PM10 VARCHAR(100),
                `PM2.5` VARCHAR(100),
                NO2 VARCHAR(100),
                SO2 VARCHAR(100),
                CO VARCHAR(100),
                OZONE VARCHAR(100),
                NH3 VARCHAR(100),
                last_updated VARCHAR(100)
            )
        """)

    def insert_aqi_data(self, data):
        sql = """
            INSERT INTO india_aqi (city, PM10, `PM2.5`, NO2, SO2, CO, OZONE, NH3, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.executemany(sql, data)
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
