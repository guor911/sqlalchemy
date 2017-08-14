from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

BaseDB = declarative_base()


class DBconn():
        def __init__(self, account, pwd, ip, port, dbname):
                self.dbuser = account
                self.dbuserpwd = pwd
                self.dbaddr = ip
                self.dbport = port
                self.dbname = dbname
                # engine = create_engine('mysql+mysqldb://root:123@192.168.151.67:3306/test?charset=utf8')
                self.engine = create_engine('mysql+mysqldb://' + self.dbuser + ':' + self.dbuserpwd + '@' + self.dbaddr + ':' + self.dbport + '/' + self.dbname + '?charset=utf8')

        def mysqlconn(self):
                DBSession = sessionmaker(bind=self.engine)
                self.session = DBSession()
                return self.session

        def initDB(self):
                # create tables
                BaseDB.metadata.create_all(self.engine)

        def dropDB(self):
                # drop tables
                BaseDB.metadata.drop_all(self.engine)

        def insertData(self, table):
                # eg. table = User(id=id, name=name)
                self.mysqlconn()
                newuser = table
                self.session.add(newuser)
                self.session.commit()
                self.session.close()


class User(BaseDB):
        __tablename__ = 'user'
        id = Column(String(20), primary_key=True)
        name = Column(String(20))


class Book(BaseDB):
        __tablename__ = 'book'
        id = Column(String(20), primary_key=True)
        name = Column(String(20))


if __name__ == '__main__':
        DBConnection = DBconn('root','123','192.168.151.67','3306','test')
        session = DBConnection.mysqlconn()
        # insert data
        # DBConnection.insertData(Book(id=1, name='python'))
        # query data
        query = session.query(User.name)
        print(query.all())
        query = session.query(Book.name)
        print(query.all())
