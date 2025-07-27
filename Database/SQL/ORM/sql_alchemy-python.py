from sqlalchemy import column, Integer, String, ForeignKey, Sequence, create_engine, Column
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

#create the database
engine = create_engine("sqlite:///orm.db")                                                                              #establish connection to the DB

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


#Define the table schema
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(50))
    email = Column(String(50))

    blog_posts = relationship("Blog_Post", back_populates="user")

Base.metadata.create_all(engine)

#create an entry in the table
"""
user1 = User(name="Steve", email= "steve@minecraft.com")
user2 = User(name="Edward", email="edward@gmail.com")
user3 = User(name="Alex", email="alex@minecraft.com")
user4 = User(name="Edward", email="edward@minecraft.com")"""

"""
The class defines the table.
The members of the class are teh columns of the table.

The object defines row in the table.
"""

#add and commit to the database
"""session.add_all([user1, user2, user3, user4])
session.commit()"""


#GET an item from the database
"""#get all the values for the following query
user = session.query(User).filter_by(name="Edward").all()
for i in user:
    print(i.name)

#get only the first instance for the following query
user = session.query(User).filter_by(name="Edward").first()
print(user.name)
"""

#DELETE a user
"""session.delete(user)
session.commit()"""

"""Establish Relationship"""
class Blog_Posts(Base):
    __tablename__ = "blog_posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="blog_posts")

#Create the database if it does not exist
Base.metadata.create_all(engine)
"""
To create a relationship between two tables we use the relationship function.
The element to be accessed should be mentioned as Foreign Key.

variable = relationship("Class of the table to establish relationship with", back_populates="variable declared in the class body of table we want to establish relationship with")
"""

#POST (add entries to the tables)
user1 = User(name="Steve", email="steve@minecraft.com")
user2 = User(name="Edward", email="edward@gmail.com")
blog_post1 = Blog_Posts(title="Steve's first post", content="This is Steve's first post")
blog_post2 = Blog_Posts(title="Edward's first post", content="This is Edward's first post")
blog_post3 = Blog_Posts(title="Steve's second post", content="This is Steve's second post")

session.add_all([user1, user2, blog_post1, blog_post2, blog_post3])
session.commit()

posts_with_users = session.query(Blog_Posts, User).join(User).all()

for i, j in posts_with_users:
    print(f"{i.name}         {j.title}")
