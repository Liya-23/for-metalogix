# handle all imports needed
import tornado.ioloop
import tornado.web
# has data typesy to declare columns with
from sqlalchemy import create_engine, Column, String, Integer, CHAR
#this would be used to create databases 
from sqlalchemy.ext.declarative import declarative_base
#also would be used to create databases 
from sqlalchemy.orm import sessionmaker
# helps capture warnings 
import warnings
# this library will be used to encrypt passwords  
import bcrypt 

# Create the SQLite database for user registration
engine = create_engine('sqlite:///users.db', echo=True)

# Create a base class for declarative class definitions
Base = declarative_base()

# Define the User class
class User(Base):
    # name the table name
    __tablename__ = "accounts"
    # list of columns in the table
    accNum = Column("accNum", Integer, primary_key = True)
    firstname = Column("firstname", String)
    lastname = Column("lastname", String)
    username = Column("username", String)
    password = Column("password", String)

    # Show how will the data be written to the data base
    def __repr__(self):
        return f"({self.accNum}) {self.firstname} {self.lastname} {self.username} {self.password})"

# Create the SQLite database for car models
engine_two = create_engine('sqlite:///models.db', echo=True)

# Create a second base class for declarative class definitions
sec_base = declarative_base()

# Define the models class
class models(sec_base):
    # name the table name
    __tablename__ = "models"
    # list of columns in the table
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

    # Show how will the data be written to the data base
    def __repr__(self):
        return f"({self.ID} {self.manifacture} {self.model} {self.releaseyear} {self.enginetype} {self.horsepower} {self.transmission} {self.exteriorcolor} {self.interiorcolor} {self.wheelcolor} {self.price})" 

# Create the table in the database # Create an Alchemy/ declarativebase
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# registration handler, handles everythin concerning the registration html file such as user's names, surnames, username and passwords 
class RegistrationHandler(tornado.web.RequestHandler):
    # retrieve the register html file needed for this class
    def get(self):
        self.render("register.html")
    # get all inputs from users    
    def post(self):
        firstname = self.get_argument("firstname")
        lastname = self.get_argument("lastname")
        username = self.get_argument("username")
        password = self.get_argument("password")
        password_conf = self.get_argument("password-confirm")

        # create a vrible that will search by usersnames 
        existing_user = session.query(User).filter_by(username=username).first()
        # the variable will be used to verify if the new username provided does not correspond with some usernames already captured/registered
        if existing_user:
            self.write("Username already exists")
        else:
            # for the passwords: the password inputs should correspond with each other so the code below justifies just that
            if password == password_conf:
                hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
                new_user = User(firstname=firstname, lastname=lastname, username=username, password=hashed_password)
                session.add(new_user)
                session.commit()
                self.write("Registration successful")
                self.render("login.html")
            else:
                # else if the passwords arent, the user must re enter the correct one 
                self.write("the password you provided is incorrect")
                self.render("register.html")    

# Login handling
class LoginHandler(tornado.web.RequestHandler):
    # retrieve the register html file needed for this class
    def get(self):
        self.render("login.html")
    
    # get all inputs from users        
    def post(self):
        nameuser = self.get_argument("nameuser")
        wordpass = self.get_argument("wordpass")  # Use the correct variable name here
        
        user = session.query(User).filter_by(username=nameuser).first()
        
        if user and bcrypt.checkpw(wordpass.encode("utf-8"), user.password):
            self.write(f"Welcome {user.username}!")
            self.render("index.html")
        else:
            self.write("Invalid username or password")
            self.render("login.html")
            
# car model handling 
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
        new_ID = self.get_argument("ID")
        new_manifacture = self.get_argument("manifacture")
        new_model = self.get_argument("model")
        new_releaseyear = self.get_argument("releaseyear")
        new_enginetype = self.get_argument("enginetype")
        new_horsepower = self.get_argument("horsepower")
        new_transmission = self.get_argument("transmission")
        new_exteriorcolor = self.get_argument("exteriorcolor")
        new_interiorcolor = self.get_argument("interiorcolor")
        new_wheelcolor = self.get_argument("wheelcolor")
        new_price = self.get_argument("price")

        new_model_data = {'ID': new_ID, 'maifacture':new_manifacture, 'model':new_model, 'releaseyear': new_releaseyear, 'enginetype': new_enginetype, 'horsepower':new_horsepower,'transmission': new_transmission, 'exteriorcolor': new_exteriorcolor, 'interiorcolor': new_interiorcolor, 'wheelcolor': new_wheelcolor, 'price': new_price}
        self.data_array.append(new_model_data)
        self.write("New model added successfully")
        return data_array
    def get(self):
        print(data_array)

    def delete(self):
        model_index = int(self.get_argument("model_index"))

        if 0 <= model_index < len(self.data_array):
            del self.data_array[model_index]
            self.write("Model data deleted successfully")
        else:
            self.write("Invalid model index")
        
    def patch(self):
        model_index = int(self.get_argument("ID"))
        new_make = self.get_argument("new_make")
        new_year = self.get_argument("new_year")

        if 0 <= model_index < len(self.data_array):
            #  get araguments from table contents/ edit button will popo u a modal dialog box used to edit idexes
            # compare if data alredy there is it the same whit new data or not
            # eg if oldcarmodel != newcar mode: ["car model"] = new car model 
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
