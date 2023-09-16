import sqlite3

class Person:
    
    
    
    def __init__(self,id_number=-1,first='',last='',age=-1) :
        self.id_number=id_number
        self.first=first
        self.last=last
        self.age=age
        self.connection=sqlite3.connect('mydata.db')

        self.cursor=self.connection.cursor()

    def load_person(self,id_number):
        self.cursor.execute(
            '''SELECT * FROM persons WHERE id={}'''.format(id_number))
        
        results=self.cursor.fetchone()
        self.id_number=id_number
        self.first=results[1]
        self.last=results[2]
        self.age=results[3]

    def inset_person(self):
        self.cursor.execute('''
                INSERT INTO persons VALUES 
                            ({}, '{}', '{}', {})            
                '''.format(self.id_number,self.first,self.last,self.age))
        self.connection.commit()

    

# p1=Person()
# p1.load_personn(1)
# print(p1.first)

# print(p1.last)
# print(p1.age)
p2=Person(792,'sathwik','Reddy',20)
p2.inset_person()
p2.load_person(792)
# connection=sqlite3.connect('mydata.db')

# cursor=connection.cursor()



# cursor.execute('''
#     CREATE TABLE persons(
#                id INTEGER PRIMARY kEY,
#                first_name TEXT,
#                last_name TEXT,
#                age INTEGER
#     )
# ''')


# cursor.execute('''
#     INSERT INTO  persons VALUES
#                (1,'paul','smith',24),
#                (2,'paul2','smith2',23),
#                (3,'paul','walker',30)
    
# ''')

# cursor.execute('SELECT * FROM persons WHERE age>20')

# rows=cursor.fetchall()
# print(rows)


# connection.commit()

# connection.close()

