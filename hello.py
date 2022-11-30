from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FormField, IntegerField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


# Create a Flask Instance
app = Flask(__name__)

# Secret Key!
app.config['SECRET_KEY'] = "justinelsa"


# Add Databse

# SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

# MySQL DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password123@localhost/animal_shelter'



# Initialize the Database
db = SQLAlchemy(app)



# Create a Contact Form Class
class ContactForm(FlaskForm):
	phone = StringField("Phone Number", validators=[DataRequired()])
	email = StringField("Email", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create an Employee Form Class
class EmployeeForm(FlaskForm):
	first_name = StringField("First Name", validators=[DataRequired()])
	last_name = StringField("Last Name", validators=[DataRequired()])
	address = StringField("Address", validators=[DataRequired()])
	dob = DateField("Date of Birth", validators=[DataRequired()])
	ssn = StringField("SSN", validators=[DataRequired()])
	start_date = DateField("Start Date", validators=[DataRequired()])
	salary = IntegerField("Salary", validators=[DataRequired()])
	position = StringField("Position", validators=[DataRequired()])
	info_id = IntegerField("Contact Information ID#", validators=[DataRequired()])
	submit = SubmitField("Submit")



# Create a Form Class
class NamerForm(FlaskForm):
	name = StringField("What's your name", validators=[DataRequired()])
	submit = SubmitField("Submit")



@app.route('/user/add', methods=['GET', 'POST'])

def add_user():
	return render_template("add_user.html")
#	name = None
#
#	form = UserForm()
#		# Validate Form
#	if form.validate_on_submit():
#		user = Users.query.filter_by(email=form.email.data).first()
#		if user is None:
#			user = Users(name=form.name.data, email=form.email.data)
#			db.session.add(user)
#			db.session.commit()
#		name = form.name.data
#		form.name.data = ''
#		form.email.data= ''
#		flash("User Added Successfully!")
#	our_users = Users.query.order_by(Users.date_added)
#	return render_template("add_user.html", form=form, name =name, our_users = our_users)

@app.route('/contact/add', methods=['GET', 'POST'])
def add_contact():
	form = ContactForm()
		# Validate Form
	if form.validate_on_submit():
		contact = Contact_Information.query.filter_by(email=form.email.data).first()
		if contact is None:
			contact = Contact_Information(email=form.email.data, phone=form.phone.data)
			db.session.add(contact)
			db.session.commit()
		form.email.data = ''
		form.phone.data= ''
		flash("Contact Added Successfully!")
	our_contacts = Contact_Information.query.order_by(Contact_Information.id)
	return render_template("add_contact.html", form = form, our_contacts = our_contacts)

@app.route('/employee/add', methods=['GET', 'POST'])
def add_employee():
	form = EmployeeForm()
		# Validate Form
	if form.validate_on_submit():
		employee = Employee.query.filter_by(ssn=form.ssn.data).first()
		if employee is None:
			employee = Employee(first_name=form.first_name.data, last_name=form.last_name.data, address=form.address.data, dob=form.dob.data, ssn=form.ssn.data, 
				start_date = form.start_date.data, salary = form.salary.data, position = form.position.data, info_id=form.info_id.data)
			db.session.add(employee)
			db.session.commit()
		form.first_name.data = ''
		form.last_name.data = ''
		form.address.data = ''
		form.dob.data = ''
		form.ssn.data = ''
		form.start_date.data = ''
		form.salary.data = ''
		form.position.data = ''
		form.info_id.data = ''
		flash("Employee Added Successfully!")
	our_employees = Employee.query.order_by(Employee.id)
	return render_template("add_employee.html", form = form, our_employees = our_employees)



@app.route('/animal/add', methods=['GET', 'POST'])
def add_animal():
	return render_template("add_animal.html")


@app.route('/donation/add', methods=['GET', 'POST'])
def add_donation():
	return render_template("add_donation.html")

@app.route('/payment/add', methods=['GET', 'POST'])
def add_payment():
	return render_template("add_payment.html")

@app.route('/diagnoses/add', methods=['GET', 'POST'])
def add_diagnoses():
	return render_template("add_diagnoses.html")

@app.route('/treatments/add', methods=['GET', 'POST'])
def add_treatments():
	return render_template("add_treatments.html")


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
    email = db.Column(db.String(150), unique = True)
    phone = db.Column(db.Integer, unique = True)



class Employee(db.Model):
#    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable = False)
    dob = db.Column(db.Date, nullable=False)
    ssn = db.Column(db.Integer, nullable=False, unique = True)
    start_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(150),nullable = False)
    info_id = db.Column(db.Integer, nullable = False, unique = True) #
    #info_id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), nullable = False, unique = True)



class Donation(db.Model):
#    __tablename__ = 'Donation'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=True)
    organization = db.Column(db.String(150), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(150), nullable=True)
    repeat_option = db.Column(db.String(150), nullable=True)
    date = db.Column(db.Date, nullable=False)
    info_id = db.Column(db.Integer, nullable = True) #
    #info_id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), nullable = True)



class Payment(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	credit_card = db.Column(db.Integer)
	name_on_card = db.Column(db.String(150))
	billing_address = db.Column(db.String(150))
     #id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), primary_key = True)


class Animal(db.Model):
#    __tablename__ = 'Animal'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    dob = db.Column(db.Date, nullable=False)
    sex = db.Column(db.Integer, nullable=False) # 1 for Male, 2 for Female
    species = db.Column(db.String(150), nullable=False)
    breed = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    admission_date = db.Column(db.Date, nullable=False)
    admission_reason = db.Column(db.String(150), nullable=False)
    adoption_status = db.Column(db.String(150), nullable=False)
    foster_status = db.Column(db.String(150), nullable=False)
    employee_id = db.Column(db.Integer, nullable=False)
    #employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)

class Diagnoses(db.Model):
#    __tablename__ = 'Diagnoses'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, nullable=False)
	vet_id = db.Column(db.Integer, nullable=False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable=False)
	#vet_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	date = db.Column(db.Date, nullable=False)
	diagnosis = db.Column(db.String(150), nullable=False)

class Treatments(db.Model):
#    __tablename__ = 'Treatments'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, nullable = False)
	diagnosis_id = db.Column(db.Integer, nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	#diagnosis_id = db.Column(db.Integer, db.ForeignKey('Diagnoses.id'), nullable = False)
	treatment = db.Column(db.String(150), nullable=False); 
	start_date = db.Column(db.Date, nullable=True)
	end_date = db.Column(db.Date, nullable=True)
	dosage = db.Column(db.String(150), nullable=True); 


class Surgeries(db.Model):
#    __tablename__ = 'Surgeries'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, nullable = False)
	diagnosis_id = db.Column(db.Integer, nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	#diagnosis_id = db.Column(db.Integer, db.ForeignKey('Diagnoses.id'), nullable = False)
	operation_type = db.Column(db.String(150), nullable = False)
	vet_id = db.Column(db.Integer,  nullable=False)
	#vet_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	date = db.Column(db.Date, nullable=False)
	success_or_fail = db.Column(db.String(150), nullable = False)

class Vaccinations(db.Model):
#    __tablename__ = 'Vaccinations'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	vaccine_type = db.Column(db.String(150), nullable = False)
	vet_id = db.Column(db.Integer, nullable=False)
	#vet_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	date = db.Column(db.Date, nullable=False)
	notes = db.Column(db.String(150))

class Allergies(db.Model):
	#    __tablename__ = 'Allergies'
	id = db.Column(db.Integer, primary_key = True)
	animal_id = db.Column(db.Integer, nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	allergy = db.Column(db.String(150), nullable = False)



class Application(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	address = db.Column(db.String(150), nullable = False)
	dob = db.Column(db.Date, nullable=False)
	ssn = db.Column(db.Integer, nullable=False)
	candidate_id = db.Column(db.Integer, nullable = False)
	#candidate_id = db.Column(db.Integer, db.ForeignKey('Contact_Information.id'), nullable = False)
	application_type = db.Column(db.Integer, nullable = False) # 1 for Adoption, 2 for Fostering
	animal_id = db.Column(db.Integer, nullable =False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable =False)
	date = db.Column(db.Date, nullable=False)
	employee_supervisor = db.Column(db.Integer, nullable = True)
	#employee_supervisor = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable = True)
	application_status = db.Column(db.String(150), nullable=True)


class Background_Check(db.Model):
#    __tablename__ = 'Background_Check'
	id = db.Column(db.Integer, primary_key = True)
	application_id = db.Column(db.Integer, nullable = False)
	#application_id = db.Column(db.Integer, db.ForeignKey('Application.id'), nullable = False)
	income = db.Column(db.Integer, nullable = False)
	ciminal_record = db.Column(db.String(150), nullable = False)
	credit_score = db.Column(db.Integer, nullable = False)
	interview_status = db.Column(db.String(150), nullable = False)
	employee_id = db.Column(db.Integer,  nullable=False)
	#employee_id = db.Column(db.Integer, db.ForeignKey('Employee.id'), nullable=False)
	background_check_status = db.Column(db.String(150), nullable = False)


class Adoptions(db.Model):
#    __tablename__ = 'Adopters'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	app_id = db.Column(db.Integer, nullable = False)
	animal_id = db.Column(db.Integer, nullable = False)
	#app_id = db.Column(db.Integer, db.ForeignKey('Application.id'), nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	adoption_date = db.Column(db.Date, nullable=False)


class Fosters(db.Model):
#    __tablename__ = 'Foster_Parents'
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	app_id = db.Column(db.Integer, nullable = False)
	animal_id = db.Column(db.Integer, nullable = False)
	#app_id = db.Column(db.Integer, db.ForeignKey('Application.id'), nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	foster_date = db.Column(db.Date, nullable=False)