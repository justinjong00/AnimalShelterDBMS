from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FormField, IntegerField, SelectField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date


# Create a Flask Instance
app = Flask(__name__)

# Secret Key!
app.config['SECRET_KEY'] = "justinelsa"


# Add Databse

# SQLite
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

#MySQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:General0667@localhost/animal_shelter1'

# Initialize the Database
db = SQLAlchemy(app)

# Create a route decorator
@app.route('/')

def index():
	return render_template("index.html")



####################################################################################################################################################
##                                                            FORMS                                                                             ####
##                                                                                                                                              ####
####################################################################################################################################################



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

# Create an Animal Form Class
class AnimalForm(FlaskForm):
	SEX = (
		 (1, 'Male'),
		 (2, 'Female')
	)

	ADOPTION_STATUS = (
		(1, 'Adopted'),
		(2, 'Available for Adoption'),
		(3, 'Application Pending')
	)

	FOSTER_STATUS = (
		(1, 'In Foster Home'),
		(2, 'Available for Foster'),
		(3, 'Foster Pending')
	)
	name = StringField("Name", validators=[DataRequired()])
	age = IntegerField("Age", validators=[DataRequired()])
	dob = DateField("Date of Birth", validators=[DataRequired()])
	sex = SelectField("Sex", choices=SEX,  validators=[DataRequired()])
	species = StringField("Species", validators=[DataRequired()])
	breed = StringField("Breed", validators=[DataRequired()])
	weight = IntegerField("Weight", validators=[DataRequired()])
	admission_date = DateField("Admission Date", validators=[DataRequired()])
	admission_reason = StringField("Admission Reason", validators=[DataRequired()])
	employee_id = IntegerField("Employee In Charge ID#", validators=[DataRequired()])
	adoption_status = SelectField("Adoption Status", choices=ADOPTION_STATUS,  validators=[DataRequired()])
	foster_status = SelectField("Foster Status", choices=FOSTER_STATUS,  validators=[DataRequired()])

# Create a Form Class
class NamerForm(FlaskForm):
	name = StringField("What's your name", validators=[DataRequired()])
	submit = SubmitField("Submit")

class DonationForm(FlaskForm):
	name = StringField("Name", validators=[DataRequired()])
	organization = StringField("Organization", validators=[DataRequired()])
	amount = IntegerField("Amount", validators=[DataRequired()])
	message = StringField("Message", validators=[DataRequired()])
	repeat_option = StringField("Repeat Option", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	info_id = IntegerField("Contact Information ID#", validators=[DataRequired()])


class PaymentForm(FlaskForm):
	credit_card = IntegerField("Credit Card Number", validators=[DataRequired()])
	name_on_card = StringField("Name on Card", validators=[DataRequired()])
	billing_address = StringField("Billing Address", validators=[DataRequired()])

class DiagnosesForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	vet_id = IntegerField("Vet ID#", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	diagnosis = StringField("Diagnosis", validators=[DataRequired()])

class TreatmentForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	diagnosis_id = IntegerField("Diagnosis ID#", validators=[DataRequired()])
	treatment = StringField("Treatment", validators=[DataRequired()])
	start_date = DateField("Start Date", validators=[DataRequired()])
	end_date = DateField("End Date", validators=[DataRequired()])
	dosage = StringField("Dosage", validators=[DataRequired()])

class SurgeryForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	diagnosis_id = IntegerField("Diagnosis ID#", validators=[DataRequired()])
	vet_id = IntegerField("Vet ID#", validators=[DataRequired()])
	operation_type = StringField("Operation Type", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	success_or_fail = StringField("Success Status", validators=[DataRequired()])

class VaccinationForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	vet_id = IntegerField("Vet ID#", validators=[DataRequired()])
	vaccine_type = StringField("Vaccine Type", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	notes = StringField("Notes", validators=[DataRequired()])


class AllergyForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	allergy = StringField("Allergy", validators=[DataRequired()])

class ApplicationForm(FlaskForm):

	APPLICATION = (
		(1, 'Adoption'),
		(2, 'Foster')
	)
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	first_name = StringField("First Name", validators=[DataRequired()])
	last_name = StringField("Last Name", validators=[DataRequired()])
	address = StringField("Address", validators=[DataRequired()])
	dob = DateField("Date of Birth", validators=[DataRequired()])
	ssn = StringField("SSN", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	candidate_id = IntegerField("Candidate ID#", validators=[DataRequired()])
	application_type = SelectField("Application Type", choices = APPLICATION,  validators=[DataRequired()])
	employee_supervisor = IntegerField("Employee Supervisor ID#", validators=[DataRequired()])
	application_status = StringField("Application Status", validators=[DataRequired()])

class BackgroundCheckForm(FlaskForm):
	application_id = IntegerField("Application ID#", validators=[DataRequired()])
	income = IntegerField("Income", validators=[DataRequired()])
	criminal_record = StringField("Criminal Record", validators=[DataRequired()])
	credit_score = StringField("Credit Score", validators=[DataRequired()])
	interview_status = StringField("Interview Status", validators=[DataRequired()])
	employee_id = IntegerField("Employee Supervisor ID#", validators=[DataRequired()])
	background_check_status = StringField("Background Check Status", validators=[DataRequired()])

class AdoptionForm(FlaskForm):
	first_name = StringField("First Name", validators=[DataRequired()])
	last_name = StringField("Last Name", validators=[DataRequired()])
	application_id = IntegerField("Application ID#", validators=[DataRequired()])
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	adoption_date = DateField("Adoption Date", validators=[DataRequired()])

class FosterForm(FlaskForm):
	first_name = StringField("First Name", validators=[DataRequired()])
	last_name = StringField("Last Name", validators=[DataRequired()])
	application_id = IntegerField("Application ID#", validators=[DataRequired()])
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	foster_date = DateField("Foster Date", validators=[DataRequired()])



####################################################################################################################################################
##                                                           ADD ROUTES                                                                         ####
##                                                                                                                                              ####
####################################################################################################################################################


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
	form = AnimalForm()
	# Validate Form
	if form.validate_on_submit():
		animal = Animal.query.filter_by(name=form.name.data).first()
		if animal is None:
			animal = Animal(name=form.name.data, age=form.age.data,
								sex =form.sex.data, dob=form.dob.data, species=form.species.data,
								breed=form.breed.data, weight=form.weight.data, admission_date=form.admission_date.data,
								admission_reason=form.admission_reason.data, adoption_status=form.adoption_status.data,
								foster_status=form.foster_status.data, employee_id = form.employee_id.data)
			db.session.add(animal)
			db.session.commit()
		form.name.data = ''
		form.age.data = ''
		form.sex.data = ''
		form.dob.data = ''
		form.species.data = ''
		form.breed.data = ''
		form.weight.data = ''
		form.admission_reason.data = ''
		form.admission_date.data = ''
		form.adoption_status.data = ''
		form.foster_status.data = ''
		form.employee_id.data = ''
		flash("Animal Added Successfully!")
	our_animals = Animal.query.order_by(Animal.id)
	return render_template("add_animal.html", form=form, our_animals=our_animals)


@app.route('/donation/add', methods=['GET', 'POST'])
def add_donation():
	form = DonationForm()
	# Validate Form
	if form.validate_on_submit():
		donation = Donation.query.filter_by(name=form.name.data).first()
		if donation is None:
			donation = Donation(name=form.name.data, organization=form.organization.data,
								amount=form.amount.data, message=form.message.data, repeat_option=form.repeat_option.data,
								date=form.date.data, info_id=form.info_id.data)
			db.session.add(donation)
			db.session.commit()
		form.name.data = ''
		form.organization.data = ''
		form.amount.data = ''
		form.message.data = ''
		form.repeat_option.data = ''
		form.date.data = ''
		form.info_id.data = ''
		flash("Donation Added Successfully!")
	our_donations = Donation.query.order_by(Donation.id)
	return render_template("add_donation.html", form=form, our_donations=our_donations)

@app.route('/payment/add', methods=['GET', 'POST'])
def add_payment():
	form = PaymentForm()
	# Validate Form
	if form.validate_on_submit():
		payment = Payment.query.filter_by(name=form.name.data).first()
		if payment is None:
			payment = Payment(credit_card=form.credit_card.data, name_on_card=form.name_on_card.data,
								billing_address=form.billing_address.data)
			db.session.add(payment)
			db.session.commit()
		form.credit_card.data = ''
		form.name_on_card.data = ''
		form.billing_address.data = ''

		flash("Payment Added Successfully!")
	our_payments = Payment.query.order_by(Payment.id)
	return render_template("add_payment.html", form=form, our_payments=our_payments)

@app.route('/diagnoses/add', methods=['GET', 'POST'])
def add_diagnoses():
	form = DiagnosesForm()
	# Validate Form
	if form.validate_on_submit():
		diagnoses = Diagnoses.query.filter_by(animal_id=form.animal_id.data).first()
		if diagnoses is None:
			diagnosis = Diagnoses(aniaml_id=form.animal_id.data, vet_id=form.vet_id.data,
							 date=form.date.data, diagnosis=form.diagnosis.data)
			db.session.add(diagnoses)
			db.session.commit()
		form.animal_id.data = ''
		form.vet_id.data = ''
		form.date.data = ''
		form.diagnosis.data = ''

		flash("Diagnosis Added Successfully!")
	our_diagnoses = Diagnoses.query.order_by(Diagnoses.id)
	return render_template("add_diagnosis.html", form=form, our_diagnoses=our_diagnoses)

@app.route('/treatments/add', methods=['GET', 'POST'])
def add_treatments():
	form = TreatmentForm()
	# Validate Form
	if form.validate_on_submit():
		treatments = Treatments.query.filter_by(animal_id=form.animal_id.data).first()
		if treatments is None:
			treatments = Diagnoses(aniaml_id=form.animal_id.data, diagnosis_id=form.diagnosis.data,
								  start_date=form.start_date.data, end_date=form.end_date.data,
								   treatment=form.treatment.data, dosage = form.dosage.data)
			db.session.add(treatments)
			db.session.commit()
		form.animal_id.data = ''
		form.diagnosis_id.data = ''
		form.start_date.data = ''
		form.end_date.data = ''
		form.treatment.data = ''
		form.dosage.data = ''

		flash("Treatment Added Successfully!")
	our_treatments = Treatments.query.order_by(Treatments.id)
	return render_template("add_treatments.html", form=form, our_treatments=our_treatments)

@app.route('/surgeries/add', methods=['GET', 'POST'])
def add_surgeries():
	form = SurgeryForm()
	# Validate Form
	if form.validate_on_submit():
		surgeries = Surgeries.query.filter_by(animal_id=form.animal_id.data).first()
		if surgeries is None:
			surgeries = Surgeries(aniaml_id=form.animal_id.data, diagnosis_id=form.diagnosis.data,
								  date=form.date.data, operation_type=form.operation_type.data,
								   vet_id=form.vet_id.data, success_or_fail = form.success_or_fail.data)
			db.session.add(surgeries)
			db.session.commit()
		form.animal_id.data = ''
		form.diagnosis_id.data = ''
		form.date.data = ''
		form.operation_type.data = ''
		form.vet_id.data = ''
		form.success_or_fail.data = ''

		flash("Surgery Added Successfully!")
	our_surgeries = Surgeries.query.order_by(Surgeries.id)
	return render_template("add_surgeries.html", form=form, our_surgeries=our_surgeries)

@app.route('/vaccinations/add', methods=['GET', 'POST'])
def add_vaccinations():
	form = VaccinationForm()
	# Validate Form
	if form.validate_on_submit():
		vaccinations = Vaccinations.query.filter_by(animal_id=form.animal_id.data).first()
		if vaccinations is None:
			vaccinations = Vaccinations(aniaml_id=form.animal_id.data, vet_id=form.vet_id.data,
								  date=form.date.data, vaccine_type=form.vaccine_type.data,
								   notes=form.notes.data)
			db.session.add(vaccinations)
			db.session.commit()
		form.animal_id.data = ''
		form.vet_id.data = ''
		form.date.data = ''
		form.vaccine_type.data = ''
		form.notes.data = ''

		flash("Vaccination Added Successfully!")
	our_vaccinations = Vaccinations.query.order_by(Vaccinations.id)
	return render_template("add_vaccinations.html", form=form, our_vaccinations=our_vaccinations)

@app.route('/allergies/add', methods=['GET', 'POST'])
def add_allergies():
	form = AllergyForm()
	# Validate Form
	if form.validate_on_submit():
		allergies = Allergies.query.filter_by(animal_id=form.animal_id.data).first()
		if allergies is None:
			allergies = Allergies(aniaml_id=form.animal_id.data,
								   allergy=form.allergy.data)
			db.session.add(allergies)
			db.session.commit()
		form.animal_id.data = ''
		form.allergy.data = ''
		flash("Allergies Added Successfully!")
	our_allergies = Allergies.query.order_by(Allergies.id)
	return render_template("add_allergies.html", form=form, our_allergies=our_allergies)

@app.route('/application/add', methods=['GET', 'POST'])
def add_application():
	form = ApplicationForm()
	# Validate Form
	if form.validate_on_submit():
		application = Application.query.filter_by(candidate_id=form.candidate_id.data).first()
		if application is None:
			application = Application(first_name=form.first_name.data, last_name=form.last_name.data,
									  address=form.address.data, dob=form.dob.data, ssn=form.ssn.data,
									  candidate_id = form.candidate_id.data, application_type = form.application_type.data,
									  animal_id = form.animal_id.data, date=form.date.data,
									  employee_supervisor = form.employee_supervisor.data,
									  application_status = form.application_status.data)
			db.session.add(application)
			db.session.commit()
		form.first_name.data = ''
		form.last_name.data = ''
		form.address.data = ''
		form.dob.data = ''
		form.ssn.data = ''
		form.candidate_id.data = ''
		form.application_status.data = ''
		form.application_type.data = ''
		form.animal_id.data = ''
		form.date.data = ''
		form.employee_supervisor.data = ''

		flash("Application Added Successfully!")
	our_applications = Application.query.order_by(Application.id)
	return render_template("add_application.html", form=form, our_applications=our_applications)


@app.route('/background_check/add', methods=['GET', 'POST'])
def add_background_check():
	form = BackgroundCheckForm()
	# Validate Form
	if form.validate_on_submit():
		background = Background_Check.query.filter_by(application_id=form.application_id.data).first()
		if background is None:
			background = Background_Check(application_id=form.application_id.data, income=form.income.data,
									  criminal_record=form.criminal_record.data, credit_score=form.credit_score.data, ssn=form.ssn.data,
									  candidate_id = form.candidate_id.data, application_type = form.application_type.data,
									  interview_status = form.interview_status.data, employee_id=form.employee_id.data,
									  background_check_status = form.background_check_status.data)
			db.session.add(background)
			db.session.commit()
		form.application_id.data = ''
		form.income.data = ''
		form.criminal_record.data = ''
		form.credit_score.data = ''
		form.interview_status.data = ''
		form.employee_id.data = ''
		form.background_check_status.data = ''

		flash("Background Check Added Successfully!")
	our_background_checks = Background_Check.query.order_by(Background_Check.id)
	return render_template("add_background_check.html", form=form, our_background_checks=our_background_checks)

@app.route('/adoptions/add', methods=['GET', 'POST'])
def add_adoption():
	form = AdoptionForm()
	# Validate Form
	if form.validate_on_submit():
		adoption = Adoptions.query.filter_by(app_id=form.application_id.data).first()
		if adoption is None:
			adoption = Adoptions(first_name=form.first_name.data, last_name=form.last_name.data,
									  app_id=form.application_id.data, animal_id=form.animal_id.data,
									  adoption_date = form.adoption_date.data)
			db.session.add(adoption)
			db.session.commit()
		form.first_name.data = ''
		form.last_name.data = ''
		form.application_id.data = ''
		form.animal_id.data = ''
		form.adoption_date.data = ''

		flash("Adoption Added Successfully!")
	our_adoptions = Adoptions.query.order_by(Adoptions.id)
	return render_template("add_adoptions.html", form=form, our_adoptions=our_adoptions)

@app.route('/fosters/add', methods=['GET', 'POST'])
def add_foster():
	form = FosterForm()
	# Validate Form
	if form.validate_on_submit():
		foster = Fosters.query.filter_by(app_id=form.application_id.data).first()
		if foster is None:
			foster = Fosters(first_name=form.first_name.data, last_name=form.last_name.data,
									  app_id=form.application_id.data, animal_id=form.animal_id.data,
									  foster_date = form.foster_date.data)
			db.session.add(foster)
			db.session.commit()
		form.first_name.data = ''
		form.last_name.data = ''
		form.application_id.data = ''
		form.animal_id.data = ''
		form.foster_date.data = ''

		flash("Foster Added Successfully!")
	our_fosters = Fosters.query.order_by(Fosters.id)
	return render_template("add_fosters.html", form=form, our_fosters=our_fosters)



####################################################################################################################################################
##                                                          UPDATE ROUTES                                                                       ####
##                                                                                                                                              ####
####################################################################################################################################################



@app.route('/contact/update/<int:id>', methods=['GET','POST'])
def update_contact(id):
	form = ContactForm()
	contact_to_update = Contact_Information.query.get_or_404(id)
	if request.method == "POST":
		contact_to_update.email = request.form['email']
		contact_to_update.phone = request.form['phone']
		try:
			db.session.commit()
			flash("Contact Updated Successfully!")
			return render_template("update_contact.html", form = form, contact_to_update = contact_to_update)
		except:
			flash("Error: Could not Update Contact")
			return render_template("update_contact.html", form = form, contact_to_update = contact_to_update)
	else:
		return render_template("update_contact.html", form = form, contact_to_update = contact_to_update, id = id)


@app.route('/employee/update/<int:id>', methods=['GET','POST'])
def update_employee(id):
	form = EmployeeForm()
	employee_to_update = Employee.query.get_or_404(id)
	if request.method == "POST":
		employee_to_update.first_name  = request.form['first_name']
		employee_to_update.last_name = request.form['last_name']
		employee_to_update.address = request.form['address']
		employee_to_update.dob = request.form['dob']
		employee_to_update.ssn = request.form['ssn']
		employee_to_update.start_date = request.form['start_date']
		employee_to_update.salary = request.form['salary']
		employee_to_update.position = request.form['position']
		employee_to_update.info_id = request.form['info_id']
		try:
			db.session.commit()
			flash("Employee Updated Successfully!")
			return render_template("update_employee.html", form = form, employee_to_update = employee_to_update)
		except:
			flash("Error: Could not Update Employee")
			return render_template("update_employee.html", form = form, employee_to_update = employee_to_update)
	else:
		return render_template("update_employee.html", form = form, employee_to_update = employee_to_update, id= id)



####################################################################################################################################################
##                                                          DELETE ROUTES                                                                       ####
##                                                                                                                                              ####
####################################################################################################################################################


@app.route('/contact/delete/<int:id>', methods=['GET','POST'])
def delete_contact(id):
	form = ContactForm()
	contact_to_delete = Contact_Information.query.get_or_404(id)
	
	try:
		db.session.delete(contact_to_delete)
		db.session.commit()
		flash("User Deleted Successfully!")

		our_contacts = Contact_Information.query.order_by(Contact_Information.id)
		return render_template("add_contact.html", form = form, our_contacts = our_contacts)
	except:
		flash("Error: Could not Delete Contact")
		return render_template("add_contact.html", form = form, our_contacts = our_contacts)


####################################################################################################################################################
##                                                           MODELS                                                                             ####
##                                                                                                                                              ####
####################################################################################################################################################

class Contact_Information(db.Model): 
#    __tablename__ = 'Contact_Information'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    phone = db.Column(db.String(150), unique = True)



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