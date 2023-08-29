# handle all imports needed
import tornado.ioloop
import tornado.web
from sqlalchemy import create_engine, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import warnings

# Create the SQLite database for user registration
engine = create_engine('sqlite:///users.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the User class
class User(Base):
    __tablename__ = "accounts"
    
    accNum = Column("accNum", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    username = Column("username", String)
    password = Column("password", String)

    def __repr__(self):
        return f"({self.accNum}) {self.firstname} {self.lastname} {self.username} {self.password}"

# Create the SQLite database for car models
engine_two = create_engine('sqlite:///models.db', echo=True)
# Create a second base class for declarative class definitions
sec_base = declarative_base()
# Define the models class
class models(sec_base):
    __tablename__ = "models"
    
    ID = Column("id",Integer, primary_key = True)
    manifacture = Column("manifacture",String)
    model = Column("model",String)
    releaseyear = Column("releaseyear",String)
    enginetype = Column("enginetype",String)
    horsepower = Column("horsepower",String)
    transmission = Column("transmission",String)
    exteriorcolor = Column("exteriorcolor",String)
    interiorcolor = Column("interiorcolor",String)
    wheelcolor = Column("wheelcolor",String)
    price = Column("price",String)

    def __repr__(self):
        return f"({self.ID} {self.manifacture} {self.model} {self.releaseyear} {self.enginetype} {self.horsepower} {self.transmission} {self.exteriorcolor} {self.interiorcolor} {self.wheelcolor} {self.price})" 
# Create the table in the database
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()
# registration handler
class RegistrationHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("register.html")
        
    def post(self):
        firstname = self.get_argument("firstname")
        lastname = self.get_argument("lastname")
        username = self.get_argument("username")
        password = self.get_argument("password")

        existing_user = session.query(User).filter_by(username=username).first()

        if existing_user:
            self.write("Username already exists")
        else:
            new_user = User(firstname=firstname, lastname=lastname, username=username, password=password)
            session.add(new_user)
            session.commit()
            self.write("Registration successful")

# Login handling
class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("login.html")
        
    def post(self):
        username = self.get_argument("userrname")
        password = self.get_argument("passsword")

        user = session.query(User).filter_by(username=username, password=password).first()

        if user:
            self.write(f"Welcome {user.username}!")

        else:
            self.write("Invalid username or password")

class CarModelsHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
        
    def __init__(self, file_path):
        self.file_path = file_path
        self.data_array = []

    def read_file(self):
        with open(self.file_path, "r") as file:
            headings = file.readline().strip().split("\t")

            for line in file:
                values = line.strip().split("\t")
                row_dict = dict(zip(headings, values))
                self.data_array.append(row_dict)
                return data_array
    def get_data(self):
        read_file(data_array)
        info = self.data_array
        self.render("index.html", data=info)
    
    def initialize(self, data_array):  # Initialize the handler with the data array
        self.data_array = data_array
        
    def post(self):
        new_model = self.get_argument("new_model")
        new_make = self.get_argument("new_make")
        new_year = self.get_argument("new_year")

        new_model_data = {'Model': new_model, 'Make': new_make, 'Year': new_year}
        self.data_array.append(new_model_data)
        self.write("New model added successfully")
    
    def get(self):
        dbdis_content = "\n".join([f"{item['Model']} - {item['Make']} - {item['Year']}" for item in self.data_array])
        self.render("index.html", dbdis_content=dbdis_content)

    def delete(self):
        model_index = int(self.get_argument("model_index"))

        if 0 <= model_index < len(self.data_array):
            del self.data_array[model_index]
            self.write("Model data deleted successfully")
        else:
            self.write("Invalid model index")
        
    def patch(self):
        model_index = int(self.get_argument("model_index"))
        new_make = self.get_argument("new_make")
        new_year = self.get_argument("new_year")

        if 0 <= model_index < len(self.data_array):
            self.data_array[model_index]['Make'] = new_make
            self.data_array[model_index]['Year'] = new_year
            self.write("Model data updated successfully")
        else:
            self.write("Invalid model index")

        
def make_app():
    return tornado.web.Application([
        (r"/register", RegistrationHandler),
        (r"/login", LoginHandler),
        (r"/index", CarModelsHandler)
    ])


if __name__ == "__main__":
    file_path = "carmodels db.txt" 
    # reader = TabSepFR(file_path)
    # reader.read_file()
    # reader.print_formatted_data() 
    app = make_app()
    app.listen(2040)
    tornado.ioloop.IOLoop.current().start()
