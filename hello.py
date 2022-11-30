from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


# Create a Flask Instance
app = Flask(__name__)

# Secret Key!
app.config['SECRET_KEY'] = "justinelsa"


# Add Databse

# MySQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/animal_shelter'



# Initialize the Database
db = SQLAlchemy(app)



# Create a Form Class
class UserForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")



# Create a Form Class
class NamerForm(FlaskForm):
	name = StringField("What's your name", validators=[DataRequired()])
	submit = SubmitField("Submit")



@app.route('/user/add', methods=['GET', 'POST'])

def add_user():
	name = None

	form = UserForm()
		# Validate Form
	if form.validate_on_submit():
		user = Users.query.filter_by(email=form.email.data).first()
		if user is None:
			user = Users(name=form.name.data, email=form.email.data)
			db.session.add(user)
			db.session.commit()
		name = form.name.data
		form.name.data = ''
		form.email.data= ''
		flash("User Added Successfully!")
	our_users = Users.query.order_by(Users.date_added)
	return render_template("add_user.html", form=form, name =name, our_users = our_users)


# Create a route decorator
@app.route('/')

def index():

	return render_template("index.html")

#localhost:5000/user/john
@app.route('/user/<name>')

def user(name):
	return render_template("user.html", name=name)

# Create Name Page
@app.route('/name', methods =['GET', 'POST'])
def name():
	name = None
	form = NamerForm()

	# Validate Form
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ''
		flash("Form Submitted Successfully")
	return render_template("name.html", 
		name = name,
		form = form)


# Create Model
class Contact_Information(db.Model): 
#    __tablename__ = 'Contact_Information'
    id = db.Column(db.Integer, primary_key = True)
    phone = db.Column(db.Integer, unique = True)
    email = db.Column(db.String(150), unique = True)


class Employee(db.Model):
#    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key = True)
    ssn = db.Column(db.Integer, nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable = False)
    dob = db.Column(db.DateTime, nullable=False)
    start_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(150),nullable = False)
    info_id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), nullable = False)



class Donation(db.Model):
#    __tablename__ = 'Donation'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=True)
    organization = db.Column(db.String(150), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(150), nullable=True)
    repeat_option = db.Column(db.String(150), nullable=True)
    date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    info_id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), nullable = True)



class Payment(db.Model):
#    __tablename__ = 'Payment'
    id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), primary_key = True)
    credit_card = db.Column(db.Integer)
    name_on_card = db.Column(db.String(150))
    billing_address = db.Column(db.String(150))


class Animal(db.Model):
#    __tablename__ = 'Animal'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    dob = db.Column(db.DateTime, nullable=False)
    sex = db.Column(db.Integer, nullable=False) # 1 for Male, 2 for Female
    species = db.Column(db.String(150), nullable=False)
    breed = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    admission_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
    admission_reason = db.Column(db.String(150), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
    adoption_status = db.Column(db.String(150), nullable=False)
    foster_status = db.Column(db.String(150), nullable=False)

class Diagnoses(db.Model):
#    __tablename__ = 'Diagnoses'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable=False)
	vet_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	date = db.Column(db.DateTime, nullable=False)
	diagnosis = db.Column(db.String(150), nullable=False)

class Treatments(db.Model):
#    __tablename__ = 'Treatments'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	diagnosis_id = db.Column(db.Integer, db.ForeignKey('Diagnoses.id'), nullable = False)
	treatment = db.Column(db.String(150), nullable=False); 
	start_date = db.Column(db.DateTime, nullable=True)
	end_date = db.Column(db.DateTime, nullable=True)
	dosage = db.Column(db.String(150), nullable=True); 


class Surgeries(db.Model):
#    __tablename__ = 'Surgeries'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	diagnosis_id = db.Column(db.Integer, db.ForeignKey('Diagnoses.id'), nullable = False)
	operation_type = db.Column(db.String(150), nullable = False)
	vet_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	date = db.Column(db.DateTime, nullable=False)
	success_or_fail = db.Column(db.String(150), nullable = False)

class Vaccinations(db.Model):
#    __tablename__ = 'Vaccinations'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'))
	vaccine_type = db.Column(db.String(150), primary_key = True)
	vet_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	date = db.Column(db.DateTime, nullable=False)
	notes = db.Column(db.String(150))

class Allergies(db.Model):
	#    __tablename__ = 'Allergies'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	allergy = db.Column(db.String(150), nullable = False)



class Application(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	address = db.Column(db.String(150), nullable = False)
	dob = db.Column(db.DateTime, nullable=False)
	ssn = db.Column(db.Integer, nullable=False)
	candidate_id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), nullable = False)
	application_type = db.Column(db.Integer, nullable = False) # 1 for Adoption, 2 for Fostering
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable =False)
	date = db.Column(db.DateTime, default=datetime.now(), nullable=False)
	employee_supervisor = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable = True)
	application_status = db.Column(db.String(150), nullable=True)


class Background_Check(db.Model):
#    __tablename__ = 'Background_Check'
	id = db.Column(db.Integer, primary_key = True)
	application_id = db.Column(db.Integer, db.ForeignKey('Application.id'), nullable = False)
	income = db.Column(db.Integer, nullable = False)
	ciminal_record = db.Column(db.String(150), nullable = False)
	credit_score = db.Column(db.Integer, nullable = False)
	interview_status = db.Column(db.String(150), nullable = False)
	employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	background_check_status = db.Column(db.String(150), nullable = False)


class Adoptions(db.Model):
#    __tablename__ = 'Adopters'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	app_id = db.Column(db.Integer, db.ForeignKey('Application.id'), nullable = False)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	adoption_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)


class Fosters(db.Model):
#    __tablename__ = 'Foster_Parents'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	app_id = db.Column(db.Integer, db.ForeignKey('Application.id'), nullable = False)
	animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	foster_date = db.Column(db.DateTime, default=datetime.now(), nullable=False)