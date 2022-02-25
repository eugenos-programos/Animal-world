import sqlite3

sql_command_create = """

CREATE TABLE animals(
    id AUTO INTEGER PRIMARY KEY,
    name VARCHAR(30),
    row_index INT,
    column_index INT,
    sex VARCHAR(7)
)

"""
#crsr.execute(sql_command_create)

sql_command_insert = """

INSERT INTO animals (name, row_index, column_index, sex)
VALUES 
('Rabbit',1,1,'male'),
('Rabbit',2,2,'female'),
('Plant',1,1,'none'),
('Plant',2,1,'none'),
('Plant',1,1,'none'),
('Zebra',1,2,'male'),
('Zebra',2,4,'female'),
('Plant',2,6,'none'),
('Plant',2,4,'none'),
('Plant',0,0,'none'),
('Tiger',2,2,'male'),
('Tiger',2,0,'female'),
('Lion',2,0,'female'),
('Lion',2,1,'male'),
('Rabbit',2,6,'male'),
('Rabbit',2,5,'female'),
('Rabbit',2,4,'male'),
('Plant',2,6,'none'),
('Plant',2,5,'none'),
('Plant',0,6,'none'),
('Plant',0,5,'none')

"""

def get_data() -> list[tuple]:
    connection = sqlite3.connect('data.db')
    crsr = connection.cursor()
    crsr.execute("SELECT * FROM animals")
    ans = crsr.fetchall()
    return ans

#crsr.execute(sql_command_insert)
def save_data(inh_types : list, row_indices : list, column_indices : list, sex : list) -> None:
    connection = sqlite3.connect('data.db')
    crsr = connection.cursor()
    crsr.execute("DELETE * FROM animals")
    for index in range(len(inh_types)):
        crsr.execute(f"INSERT INTO animals VALUES ({inh_types[index]}, {row_indices[index], {column_indices[index]}, {sex[index]}})")
    connection.commit()
    connection.close()