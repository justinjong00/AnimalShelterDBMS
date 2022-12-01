from flask import Flask, render_template, flash, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, FormField, IntegerField, SelectField
from wtforms.validators import DataRequired
#from webforms import SearchForm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime, date
from sqlalchemy import create_engine



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
migrate = Migrate(app, db)

engine = create_engine('mysql+pymysql://root:General0667@localhost/animal_shelter1')
connection = engine.raw_connection()
cursor = connection.cursor()

# Create a route decorator
@app.route('/')

def index():
	return render_template("index.html")



####################################################################################################################################################
##                                                            FORMS                                                                             ####
##                                                                                                                                              ####
####################################################################################################################################################

class SearchForm(FlaskForm):
	searched = StringField("Searched", validators=[DataRequired()])
	submit = SubmitField("Submit")


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
		(3, 'Foster Pending'),
		(4, 'N/A')
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
	submit = SubmitField("Submit")

# Create a Donation Form Class
class DonationForm(FlaskForm):
	REPEAT = (
		(1, 'One-Time'), 
		(2, 'Weekly'),
		(3, 'Bi-weekly'), 
		(4, 'Monthly'), 
		(5, 'Yearly')
	)
	name = StringField("Name", validators=[DataRequired()])
	organization = StringField("Organization", validators=[DataRequired()])
	amount = IntegerField("Amount", validators=[DataRequired()])
	message = StringField("Message", validators=[DataRequired()])
	repeat_option = SelectField("Repeat Option", choices=REPEAT, validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	info_id = IntegerField("Contact Information ID#", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a Payment Form Class
class PaymentForm(FlaskForm):
	credit_card = StringField("Credit Card Number", validators=[DataRequired()])
	name_on_card = StringField("Name on Card", validators=[DataRequired()])
	billing_address = StringField("Billing Address", validators=[DataRequired()])
	submit = SubmitField("Submit")

# Create a diagnosis Form Class
class DiagnosisForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	vet_id = IntegerField("Vet ID#", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	diagnosis = StringField("Diagnosis", validators=[DataRequired()])
	submit = SubmitField("Submit")

class TreatmentForm(FlaskForm):
	diagnosis_id = IntegerField("Diagnosis ID#", validators=[DataRequired()])
	treatment = StringField("Treatment", validators=[DataRequired()])
	start_date = DateField("Start Date", validators=[DataRequired()])
	end_date = DateField("End Date", validators=[DataRequired()])
	dosage = StringField("Dosage", validators=[DataRequired()])
	submit = SubmitField("Submit")

class SurgeryForm(FlaskForm):
	diagnosis_id = IntegerField("Diagnosis ID#", validators=[DataRequired()])
	vet_id = IntegerField("Vet ID#", validators=[DataRequired()])
	operation_type = StringField("Operation Type", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	success_or_fail = StringField("Success Status", validators=[DataRequired()])
	submit = SubmitField("Submit")

class VaccinationForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	vet_id = IntegerField("Vet ID#", validators=[DataRequired()])
	vaccine_type = StringField("Vaccine Type", validators=[DataRequired()])
	date = DateField("Date", validators=[DataRequired()])
	notes = StringField("Notes", validators=[DataRequired()])
	submit = SubmitField("Submit")


class AllergyForm(FlaskForm):
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	allergy = StringField("Allergy", validators=[DataRequired()])
	medication = StringField("Medication",validators=[DataRequired()])
	submit = SubmitField("Submit")

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
	submit = SubmitField("Submit")

class BackgroundCheckForm(FlaskForm):
	application_id = IntegerField("Application ID#", validators=[DataRequired()])
	income = IntegerField("Income", validators=[DataRequired()])
	criminal_record = StringField("Criminal Record", validators=[DataRequired()])
	credit_score = StringField("Credit Score", validators=[DataRequired()])
	interview_status = StringField("Interview Status", validators=[DataRequired()])
	employee_id = IntegerField("Employee Supervisor ID#", validators=[DataRequired()])
	background_check_status = StringField("Background Check Status", validators=[DataRequired()])
	submit = SubmitField("Submit")

class AdoptionForm(FlaskForm):
	application_id = IntegerField("Application ID#", validators=[DataRequired()])
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	adoption_date = DateField("Adoption Date", validators=[DataRequired()])
	submit = SubmitField("Submit")

class FosterForm(FlaskForm):
	application_id = IntegerField("Application ID#", validators=[DataRequired()])
	animal_id = IntegerField("Animal ID#", validators=[DataRequired()])
	foster_date = DateField("Foster Date", validators=[DataRequired()])
	submit = SubmitField("Submit")



####################################################################################################################################################
##                                                           ADD ROUTES                                                                         ####
##                                                                                                                                              ####
####################################################################################################################################################



@app.route('/contact/add', methods=['GET', 'POST'])
def add_contact():
	form = ContactForm()
		# Validate Form
	if form.validate_on_submit():
		try:
			contact = Contact.query.filter_by(id= id).first()
			if contact is None:
				contact = Contact(email=form.email.data, phone=form.phone.data)
				db.session.add(contact)
				db.session.commit()
			form.email.data = ''
			form.phone.data= ''
			flash("Contact Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not create new Contact")
	our_contacts = Contact.query.order_by(Contact.id)
	return render_template("add_contact.html", form = form, our_contacts = our_contacts)

@app.route('/employee/add', methods=['GET', 'POST'])
def add_employee():
	form = EmployeeForm()
		# Validate Form
	if form.validate_on_submit():
		try:
			employee = Employee.query.filter_by(id=id).first()
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
		except:
			db.session.rollback()
			flash("Error: Could not create new Employee")
	our_employees = Employee.query.order_by(Employee.id)
	return render_template("add_employee.html", form = form, our_employees = our_employees)



@app.route('/animal/add', methods=['GET', 'POST'])
def add_animal():
	form = AnimalForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			animal = Animal.query.filter_by(id = id).first()
			if animal is None:
				animal = Animal(name=form.name.data, age=form.age.data,
									sex =form.sex.data, dob=form.dob.data, 
									species=form.species.data,
									breed=form.breed.data, weight=form.weight.data, 
									admission_date=form.admission_date.data,
									admission_reason=form.admission_reason.data, 
									adoption_status=form.adoption_status.data,
									foster_status=form.foster_status.data, 
									employee_id = form.employee_id.data)
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
		except:
			db.session.rollback()
			flash("Error: Could not create new Animal")
	our_animals = Animal.query.order_by(Animal.id)
	return render_template("add_animal.html", form=form, our_animals=our_animals)


@app.route('/donation/add', methods=['GET', 'POST'])
def add_donation():
	form = DonationForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			donation = Donation.query.filter_by(id = id).first()
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
		except:
			db.session.rollback()
			flash("Error: Could not create new Donation")
	our_donations = Donation.query.order_by(Donation.id)
	return render_template("add_donation.html", form=form, our_donations=our_donations)

@app.route('/payment/add', methods=['GET', 'POST'])
def add_payment():
	form = PaymentForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			payment = Payment.query.filter_by(id = id).first()
			if payment is None:
				payment = Payment(credit_card=form.credit_card.data, name_on_card=form.name_on_card.data,
									billing_address=form.billing_address.data)
				db.session.add(payment)
				db.session.commit()
			form.credit_card.data = ''
			form.name_on_card.data = ''
			form.billing_address.data = ''

			flash("Payment Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not create new Payment")
	our_payments = Payment.query.order_by(Payment.id)
	return render_template("add_payment.html", form=form, our_payments=our_payments)

@app.route('/diagnosis/add', methods=['GET', 'POST'])
def add_diagnosis():
	form = DiagnosisForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			diagnosis = Diagnosis.query.filter_by(id = id).first()
			if diagnosis is None:
				diagnosis = Diagnosis(animal_id=form.animal_id.data, vet_id=form.vet_id.data,
								 date=form.date.data, diagnosis=form.diagnosis.data)
				db.session.add(diagnosis)
				db.session.commit()
			form.animal_id.data = ''
			form.vet_id.data = ''
			form.date.data = ''
			form.diagnosis.data = ''

			flash("Diagnosis Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not create new Diagnosis")
	our_diagnoses = Diagnosis.query.order_by(Diagnosis.id)
	return render_template("add_diagnosis.html", form=form, our_diagnoses=our_diagnoses)

@app.route('/treatment/add', methods=['GET', 'POST'])
def add_treatment():
	form = TreatmentForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			treatments = Treatment.query.filter_by(id = id).first()
			if treatments is None:
				treatments = Treatment(diagnosis_id=form.diagnosis_id.data,
									  start_date=form.start_date.data, end_date=form.end_date.data,
									   treatment=form.treatment.data, dosage = form.dosage.data)
				db.session.add(treatments)
				db.session.commit()
			form.diagnosis_id.data = ''
			form.start_date.data = ''
			form.end_date.data = ''
			form.treatment.data = ''
			form.dosage.data = ''

			flash("Treatment Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not create new Treatment")
	our_treatments = Treatment.query.order_by(Treatment.id)
	return render_template("add_treatment.html", form=form, our_treatments=our_treatments)

@app.route('/surgery/add', methods=['GET', 'POST'])
def add_surgery():
	form = SurgeryForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			surgery = Surgery.query.filter_by(id = id).first()
			if surgery is None:
				surgery = Surgery(diagnosis_id=form.diagnosis_id.data,
									  date=form.date.data, operation_type=form.operation_type.data,
									   vet_id=form.vet_id.data, success_or_fail = form.success_or_fail.data)
				db.session.add(surgery)
				db.session.commit()
			form.diagnosis_id.data = ''
			form.date.data = ''
			form.operation_type.data = ''
			form.vet_id.data = ''
			form.success_or_fail.data = ''

			flash("Surgery Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not create new Surgery")
	our_surgeries = Surgery.query.order_by(Surgery.id)
	return render_template("add_surgery.html", form=form, our_surgeries=our_surgeries)

@app.route('/vaccination/add', methods=['GET', 'POST'])
def add_vaccination():
	form = VaccinationForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			vaccinations = Vaccination.query.filter_by(id = id).first()
			if vaccinations is None:
				vaccinations = Vaccination(animal_id=form.animal_id.data, vet_id=form.vet_id.data,
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
		except:
			db.session.rollback()
			flash("Error: Could not create new Vaccination")
	our_vaccinations = Vaccination.query.order_by(Vaccination.id)
	return render_template("add_vaccination.html", form=form, our_vaccinations=our_vaccinations)

@app.route('/allergy/add', methods=['GET', 'POST'])
def add_allergy():
	form = AllergyForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			allergy = Allergy.query.filter_by(id = id).first()
			if allergy is None:
				allergy = Allergy(animal_id=form.animal_id.data,
									   allergy=form.allergy.data, medication = form.medication.data)
				db.session.add(allergy)
				db.session.commit()
			form.animal_id.data = ''
			form.allergy.data = ''
			form.medication.data = ''
			flash("Allergy Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not add new Allergy")
	our_allergies = Allergy.query.order_by(Allergy.id)
	return render_template("add_allergy.html", form=form, our_allergies=our_allergies)

@app.route('/application/add', methods=['GET', 'POST'])
def add_application():
	form = ApplicationForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			application = Application.query.filter_by(id = id).first()
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
		except:
			db.session.rollback()
			flash("Error: Could not create add new Application")
	our_applications = Application.query.order_by(Application.id)
	return render_template("add_application.html", form=form, our_applications=our_applications)


@app.route('/background/add', methods=['GET', 'POST'])
def add_background():
	form = BackgroundCheckForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			background = Backgroundcheck.query.filter_by(id = id).first()
			if background is None:
				background = Backgroundcheck(application_id=form.application_id.data, income=form.income.data,
										  criminal_record=form.criminal_record.data, credit_score=form.credit_score.data,
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
		except:
			db.session.rollback()
			flash("Error: Could not create new background check")
	our_background_checks = Backgroundcheck.query.order_by(Backgroundcheck.id)
	return render_template("add_background.html", form=form, our_background_checks=our_background_checks)

@app.route('/adoption/add', methods=['GET', 'POST'])
def add_adoption():
	form = AdoptionForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			adoption = Adoption.query.filter_by(id = id).first()
			if adoption is None:
				adoption = Adoption(app_id=form.application_id.data, animal_id=form.animal_id.data,
										  adoption_date = form.adoption_date.data)
				db.session.add(adoption)
				db.session.commit()
			form.application_id.data = ''
			form.animal_id.data = ''
			form.adoption_date.data = ''

			#comment

			flash("Adoption Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not add adoption")
	our_adoptions = Adoption.query.order_by(Adoption.id)
	return render_template("add_adoption.html", form=form, our_adoptions=our_adoptions)

@app.route('/foster/add', methods=['GET', 'POST'])
def add_foster():
	form = FosterForm()
	# Validate Form
	if form.validate_on_submit():
		try:
			foster = Foster.query.filter_by(id = id).first()
			if foster is None:
				foster = Foster(app_id=form.application_id.data, animal_id=form.animal_id.data,
										  foster_date = form.foster_date.data)
				db.session.add(foster)
				db.session.commit()
			form.application_id.data = ''
			form.animal_id.data = ''
			form.foster_date.data = ''

			flash("Foster Added Successfully!")
		except:
			db.session.rollback()
			flash("Error: Could not add foster")
	our_fosters = Foster.query.order_by(Foster.id)
	return render_template("add_foster.html", form=form, our_fosters=our_fosters)



####################################################################################################################################################
##                                                          UPDATE ROUTES                                                                       ####
##                                                                                                                                              ####
####################################################################################################################################################



@app.route('/contact/update/<int:id>', methods=['GET','POST'])
def update_contact(id):
	form = ContactForm()
	contact_to_update = Contact.query.get_or_404(id)
	if request.method == "POST":
		contact_to_update.email = request.form['email']
		contact_to_update.phone = request.form['phone']
		try:
			db.session.commit()
			flash("Contact Updated Successfully!")
			return render_template("update_contact.html", form = form, contact_to_update = contact_to_update, id=id)
		except:
			flash("Error: Could not Update Contact")
			return render_template("update_contact.html", form = form, contact_to_update = contact_to_update, id=id)
	else:
		return render_template("update_contact.html", form = form, contact_to_update = contact_to_update, id = id)


@app.route('/employee/update/<int:id>', methods=['GET','POST'])
def update_employee(id):
	form = EmployeeForm()
	employee_to_update = Employee.query.get_or_404(id)
	if request.method == "POST":
		employee_to_update.first_name = request.form['first_name']
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
			return render_template("update_employee.html", form = form, employee_to_update = employee_to_update, id=id)
		except:
			flash("Error: Could not Update Employee")
			return render_template("update_employee.html", form = form, employee_to_update = employee_to_update, id=id)
	else:
		return render_template("update_employee.html", form = form, employee_to_update = employee_to_update, id = id)


@app.route('/animal/update/<int:id>', methods=['GET','POST'])
def update_animal(id):
	form = AnimalForm()
	animal_to_update = Animal.query.get_or_404(id)
	if request.method == "POST":
		animal_to_update.name = request.form['name']
		animal_to_update.age = request.form['age']
		animal_to_update.sex = request.form['sex']
		animal_to_update.dob = request.form['dob']
		animal_to_update.species = request.form['species']
		animal_to_update.breed = request.form['breed']
		animal_to_update.admission_date = request.form['admission_date']
		animal_to_update.admission_reason = request.form['admission_reason']
		animal_to_update.adoption_status = request.form['adoption_status']
		animal_to_update.foster_status = request.form['foster_status']
		animal_to_update.employee_id = request.form['employee_id']

		try:
			db.session.commit()
			flash("Animal Updated Successfully!")
			return render_template("update_animal.html", form = form, animal_to_update = animal_to_update, id=id)
		except:
			flash("Error: Could not Update Animal")
			return render_template("update_animal.html", form = form, animal_to_update = animal_to_update, id=id)
	else:
		return render_template("update_animal.html", form = form, animal_to_update = animal_to_update, id = id)


@app.route('/donation/update/<int:id>', methods=['GET','POST'])
def update_donation(id):
	form = DonationForm()
	donation_to_update = Donation.query.get_or_404(id)
	if request.method == "POST":
		donation_to_update.name = request.form['name']
		donation_to_update.organization = request.form['organization']
		donation_to_update.amount = request.form['amount']
		donation_to_update.message = request.form['message']
		donation_to_update.repeat_option = request.form['repeat_option']
		donation_to_update.date = request.form['date']
		donation_to_update.info_id = request.form['info_id']

		try:
			db.session.commit()
			flash("Donation Updated Successfully!")
			return render_template("update_donation.html", form = form, donation_to_update = donation_to_update, id=id)
		except:
			flash("Error: Could not Update Donation")
			return render_template("update_donation.html", form = form, donation_to_update = donation_to_update, id=id)
	else:
		return render_template("update_donation.html", form = form, donation_to_update = donation_to_update, id = id)


@app.route('/payment/update/<int:id>', methods=['GET','POST'])
def update_payment(id):
	form = PaymentForm()
	payment_to_update = Payment.query.get_or_404(id)
	if request.method == "POST":
		payment_to_update.credit_card = request.form['credit_card']
		payment_to_update.name_on_card = request.form['name_on_card']
		payment_to_update.billing_address = request.form['billing_address']

		try:
			db.session.commit()
			flash("Payment Updated Successfully!")
			return render_template("update_payment.html", form = form, 
									payment_to_update = payment_to_update, id=id)
		except:
			flash("Error: Could not Update Donation")
			return render_template("update_payment.html", form = form, 
									payment_to_update = payment_to_update, id=id)
	else:
		return render_template("update_payment.html", form = form, payment_to_update = payment_to_update, id = id)


@app.route('/diagnosis/update/<int:id>', methods=['GET','POST'])
def update_diagnosis(id):
	form = DiagnosisForm()
	diagnosis_to_update = Diagnosis.query.get_or_404(id)
	if request.method == "POST":
		diagnosis_to_update.animal_id = request.form['animal_id']
		diagnosis_to_update.vet_id = request.form['vet_id']
		diagnosis_to_update.date = request.form['date']
		diagnosis_to_update.diagnosis = request.form['diagnosis']

		try:
			db.session.commit()
			flash("Diagnosis Updated Successfully!")
			return render_template("update_diagnosis.html", form = form, diagnosis_to_update = diagnosis_to_update, id=id)
		except:
			flash("Error: Could not Update Diagnosis")
			return render_template("update_diagnosis.html", form = form, diagnosis_to_update = diagnosis_to_update, id=id)
	else:
		return render_template("update_diagnosis.html", form = form, diagnosis_to_update = diagnosis_to_update, id = id)


@app.route('/treatment/update/<int:id>', methods=['GET','POST'])
def update_treatment(id):
	form = TreatmentForm()
	treatment_to_update = Treatment.query.get_or_404(id)
	if request.method == "POST":
		treatment_to_update.diagnosis_id = request.form['diagnosis_id']
		treatment_to_update.start_date = request.form['start_date']
		treatment_to_update.end_date = request.form['end_date']
		treatment_to_update.treatment = request.form['treatment']
		treatment_to_update.dosage = request.form['dosage']
		
		try:
			db.session.commit()
			flash("Treatment Updated Successfully!")
			return render_template("update_treatment.html", form = form, treatment_to_update = treatment_to_update, id=id)
		except:
			flash("Error: Could not Update Treatment")
			return render_template("update_treatment.html", form = form, treatment_to_update = treatment_to_update, id=id)
	else:
		return render_template("update_treatment.html", form = form, treatment_to_update = treatment_to_update, id = id)


@app.route('/surgery/update/<int:id>', methods=['GET','POST'])
def update_surgery(id):
	form = SurgeryForm()
	surgery_to_update = Surgery.query.get_or_404(id)
	if request.method == "POST":
		surgery_to_update.diagnosis_id  = request.form['diagnosis_id']
		surgery_to_update.vet_id  = request.form['vet_id']
		surgery_to_update.date  = request.form['date']
		surgery_to_update.operation_type = request.form['operation_type']
		surgery_to_update.success_or_fail = request.form['success_or_fail']
		
		try:
			db.session.commit()
			flash("Surgery Updated Successfully!")
			return render_template("update_surgery.html", form = form, surgery_to_update = surgery_to_update, id=id)
		except:
			flash("Error: Could not Update Surgery")
			return render_template("update_surgery.html", form = form, surgery_to_update = surgery_to_update, id=id)
	else:
		return render_template("update_surgery.html", form = form, surgery_to_update = surgery_to_update, id = id)


@app.route('/vaccination/update/<int:id>', methods=['GET','POST'])
def update_vaccination(id):
	form = VaccinationForm()
	vaccination_to_update = Vaccination.query.get_or_404(id)
	if request.method == "POST":
		vaccination_to_update.animal_id  = request.form['animal_id']
		vaccination_to_update.vet_id  = request.form['vet_id']
		vaccination_to_update.date  = request.form['date']
		vaccination_to_update.vaccine_type  = request.form['vaccine_type']
		vaccination_to_update.notes = request.form['notes']
		
		try:
			db.session.commit()
			flash("Vaccination Updated Successfully!")
			return render_template("update_vaccination.html", form = form, vaccination_to_update = vaccination_to_update, id=id)
		except:
			flash("Error: Could not Update Vaccination")
			return render_template("update_vaccination.html", form = form, vaccination_to_update = vaccination_to_update, id=id)
	else:
		return render_template("update_vaccination.html", form = form, vaccination_to_update = vaccination_to_update, id = id)



@app.route('/allergy/update/<int:id>', methods=['GET','POST'])
def update_allergy(id):
	form = AllergyForm()
	allergy_to_update = Allergy.query.get_or_404(id)
	if request.method == "POST":
		allergy_to_update.animal_id  = request.form['animal_id']
		allergy_to_update.allergy  = request.form['allergy']
		allergy_to_update.medicaiton = request.form['medication']
		
		try:
			db.session.commit()
			flash("Allergy Updated Successfully!")
			return render_template("update_allergy.html", form = form, allergy_to_update = allergy_to_update, id=id)
		except:
			flash("Error: Could not Update Allergy")
			return render_template("update_allergy.html", form = form, allergy_to_update = allergy_to_update, id=id)
	else:
		return render_template("update_allergy.html", form = form, allergy_to_update = allergy_to_update, id = id)


@app.route('/application/update/<int:id>', methods=['GET','POST'])
def update_application(id):
	form = ApplicationForm()
	application_to_update = Application.query.get_or_404(id)
	if request.method == "POST":
		application_to_update.first_name = request.form['first_name']
		application_to_update.last_name = request.form['last_name']
		application_to_update.address = request.form['address']
		application_to_update.dob = request.form['dob']
		application_to_update.ssn = request.form['ssn']
		application_to_update.candidate_id = request.form['candidate_id']
		application_to_update.application_status = request.form['application_status']
		application_to_update.application_type = request.form['application_type']
		application_to_update.animal_id = request.form['animal_id']
		application_to_update.date = request.form['date']
		application_to_update.employee_supervisor = request.form['employee_supervisor']

		try:
			db.session.commit()
			flash("Application Updated Successfully!")
			return render_template("update_application.html", form = form, application_to_update = application_to_update, id=id)
		except:
			flash("Error: Could not Update Application")
			return render_template("update_application.html", form = form, application_to_update = application_to_update, id=id)
	else:
		return render_template("update_application.html", form = form, application_to_update = application_to_update, id = id)

@app.route('/background/update/<int:id>', methods=['GET','POST'])
def update_background(id):
	form = BackgroundCheckForm()
	background_to_update = Backgroundcheck.query.get_or_404(id)
	if request.method == "POST":
		background_to_update.application_id = request.form['application_id']
		background_to_update.income = request.form['income']
		background_to_update.criminal_record = request.form['criminal_record']
		background_to_update.credit_score = request.form['credit_score']
		background_to_update.interview_status = request.form['interview_status']
		background_to_update.employee_id = request.form['employee_id']
		background_to_update.background_check_status = request.form['background_check_status']

		try:
			db.session.commit()
			flash("Background Check Updated Successfully!")
			return render_template("update_background.html", form = form, background_to_update = background_to_update, id=id)
		except:
			flash("Error: Could not Update Background Check")
			return render_template("update_background.html", form = form, background_to_update = background_to_update, id=id)
	else:
		return render_template("update_background.html", form = form, background_to_update = background_to_update, id = id)

@app.route('/adoption/update/<int:id>', methods=['GET','POST'])
def update_adoption(id):
	form = AdoptionForm()
	adoption_to_update = Adoption.query.get_or_404(id)
	if request.method == "POST":
		# adoption_to_update.first_name = request.form['first_name']
		# adoption_to_update.last_name = request.form['last_name']
		adoption_to_update.application_id = request.form['application_id']
		adoption_to_update.adoption_date = request.form['adoption_date']
		adoption_to_update.animal_id = request.form['animal_id']

		try:
			db.session.commit()
			flash("Adoption Updated Successfully!")
			return render_template("update_adoption.html", form = form, adoption_to_update = adoption_to_update, id=id)
		except:
			flash("Error: Could not Update Adoption")
			return render_template("update_adoption.html", form = form, adoption_to_update = adoption_to_update, id=id)
	else:
		return render_template("update_adoption.html", form = form, adoption_to_update = adoption_to_update, id = id)


@app.route('/foster/update/<int:id>', methods=['GET','POST'])
def update_foster(id):
	form = FosterForm()
	foster_to_update = Foster.query.get_or_404(id)
	if request.method == "POST":
		# foster_to_update.first_name = request.form['first_name']
		# foster_to_update.last_name = request.form['last_name']
		foster_to_update.application_id = request.form['application_id']
		foster_to_update.foster_date = request.form['foster_date']
		foster_to_update.animal_id = request.form['animal_id']

		try:
			db.session.commit()
			flash("Foster Updated Successfully!")
			return render_template("update_foster.html", form = form, foster_to_update = foster_to_update, id=id)
		except:
			flash("Error: Could not Update Foster")
			return render_template("update_foster.html", form = form, foster_to_update = foster_to_update, id=id)
	else:
		return render_template("update_foster.html", form = form, foster_to_update = foster_to_update, id = id)


####################################################################################################################################################
##                                                          DELETE ROUTES                                                                       ####
##                                                                                                                                              ####
####################################################################################################################################################


@app.route('/contact/delete/<int:id>', methods=['GET','POST'])
def delete_contact(id):
	form = ContactForm()
	contact_to_delete = Contact.query.get_or_404(id)
	
	try:
		db.session.delete(contact_to_delete)
		db.session.commit()
		flash("User Deleted Successfully!")

		our_contacts = Contact.query.order_by(Contact.id)
		return render_template("add_contact.html", form = form, our_contacts = our_contacts)
	except:
		return render_template("add_contact.html", form = form, our_contacts = our_contacts)


@app.route('/employee/delete/<int:id>', methods=['GET','POST'])
def delete_employee(id):
	form = EmployeeForm()
	employee_to_delete = Employee.query.get_or_404(id)
	
	try:
		db.session.delete(employee_to_delete)
		db.session.commit()
		flash("Employee Deleted Successfully!")

		our_employees = Employee.query.order_by(Employee.id)
		return render_template("add_employee.html", form = form, our_employees = our_employees)
	except:
		return render_template("add_employee.html", form = form, our_employees = our_employees)

@app.route('/animal/delete/<int:id>', methods=['GET','POST'])
def delete_animal(id):
	form = AnimalForm()
	animal_to_delete = Animal.query.get_or_404(id)
	
	try:
		db.session.delete(animal_to_delete)
		db.session.commit()
		flash("Animal Deleted Successfully!")

		our_animals = Animal.query.order_by(Animal.id)
		return render_template("add_animal.html", form = form, our_animals = our_animals)
	except:
		return render_template("add_animal.html", form = form, our_animals = our_animals)

@app.route('/donation/delete/<int:id>', methods=['GET','POST'])
def delete_donation(id):
	form = DonationForm()
	donation_to_delete = Donation.query.get_or_404(id)
	
	try:
		db.session.delete(donation_to_delete)
		db.session.commit()
		flash("Donation Deleted Successfully!")

		our_donations = Donation.query.order_by(Donation.id)
		return render_template("add_donation.html", form = form, our_donations = our_donations)
	except:
		return render_template("add_donation.html", form = form, our_donations = our_donations)

@app.route('/payment/delete/<int:id>', methods=['GET','POST'])
def delete_payment(id):
	form = PaymentForm()
	payment_to_delete = Payment.query.get_or_404(id)
	
	try:
		db.session.delete(payment_to_delete)
		db.session.commit()
		flash("Payment Deleted Successfully!")

		our_payments = Payment.query.order_by(Payment.id)
		return render_template("add_payment.html", form = form, our_payments = our_payments)
	except:
		return render_template("add_payment.html", form = form, our_payments = our_payments)


@app.route('/diagnosis/delete/<int:id>', methods=['GET','POST'])
def delete_diagnosis(id):
	form = DiagnosisForm()
	diagnosis_to_delete = Diagnosis.query.get_or_404(id)
	
	try:
		db.session.delete(diagnosis_to_delete)
		db.session.commit()
		flash("Diagnosis Deleted Successfully!")

		our_diagnosis = Diagnosis.query.order_by(Diagnosis.id)
		return render_template("add_diagnosis.html", form = form, our_diagnosis = our_diagnosis)
	except:
		return render_template("add_diagnosis.html", form = form, our_diagnosis = our_diagnosis)


@app.route('/treatment/delete/<int:id>', methods=['GET','POST'])
def delete_treatment(id):
	form = TreatmentForm()
	treatment_to_delete = Treatment.query.get_or_404(id)
	
	try:
		db.session.delete(treatment_to_delete)
		db.session.commit()
		flash("Treatment Deleted Successfully!")

		our_treatments = Treatment.query.order_by(Treatment.id)
		return render_template("add_treatment.html", form = form, our_treatments = our_treatments)
	except:
		return render_template("add_treatment.html", form = form, our_treatments = our_treatments)


@app.route('/surgery/delete/<int:id>', methods=['GET','POST'])
def delete_surgery(id):
	form = SurgeryForm()
	surgery_to_delete = Surgery.query.get_or_404(id)
	
	try:
		db.session.delete(surgery_to_delete)
		db.session.commit()
		flash("Diagnosis Deleted Successfully!")

		our_surgeries = Surgery.query.order_by(Surgery.id)
		return render_template("add_surgery.html", form = form, our_surgeries = our_surgeries)
	except:
		return render_template("add_surgery.html", form = form, our_surgeries = our_surgeries)


@app.route('/vaccination/delete/<int:id>', methods=['GET','POST'])
def delete_vaccination(id):
	form = VaccinationForm()
	vaccination_to_delete = Vaccination.query.get_or_404(id)
	
	try:
		db.session.delete(vaccination_to_delete)
		db.session.commit()
		flash("Vaccination Deleted Successfully!")

		our_vaccinations = Vaccination.query.order_by(Vaccination.id)
		return render_template("add_vaccination.html", form = form, our_vaccinations = our_vaccinations)
	except:
		return render_template("add_vaccination.html", form = form, our_vaccinations = our_vaccinations)


@app.route('/allergy/delete/<int:id>', methods=['GET','POST'])
def delete_allergy(id):
	form = AllergyForm()
	allergy_to_delete = Allergy.query.get_or_404(id)
	
	try:
		db.session.delete(allergy_to_delete)
		db.session.commit()
		flash("Allergy Deleted Successfully!")

		our_allergies = Allergy.query.order_by(Allergy.id)
		return render_template("add_allergy.html", form = form, our_allergies = our_allergies)
	except:
		return render_template("add_allergy.html", form = form, our_allergies = our_allergies)


@app.route('/application/delete/<int:id>', methods=['GET','POST'])
def delete_application(id):
	form = ApplicationForm()
	application_to_delete = Application.query.get_or_404(id)
	
	try:
		db.session.delete(application_to_delete)
		db.session.commit()
		flash("Application Deleted Successfully!")

		our_applications = Application.query.order_by(Application.id)
		return render_template("add_application.html", form = form, our_applications = our_applications)
	except:
		return render_template("add_application.html", form = form, our_applications = our_applications)


@app.route('/background/delete/<int:id>', methods=['GET','POST'])
def delete_background(id):
	form = BackgroundCheckForm()
	bc_to_delete = Backgroundcheck.query.get_or_404(id)
	
	try:
		db.session.delete(bc_to_delete)
		db.session.commit()
		flash("Background Check Deleted Successfully!")

		our_background_checks = Backgroundcheck.query.order_by(Backgroundcheck.id)
		return render_template("add_background.html", form = form, our_background_checks = our_background_checks)
	except:
		return render_template("add_background.html", form = form, our_background_checks = our_background_checks)

@app.route('/adoption/delete/<int:id>', methods=['GET','POST'])
def delete_adoption(id):
	form = AdoptionForm()
	adoption_to_delete = Adoption.query.get_or_404(id)
	
	try:
		db.session.delete(adoption_to_delete)
		db.session.commit()
		flash("Adoption Deleted Successfully!")

		our_adoptions = Adoption.query.order_by(Adoption.id)
		return render_template("add_adoption.html", form = form, our_adoptions = our_adoptions)
	except:
		return render_template("add_adoption.html", form = form, our_adoptions = our_adoptions)

@app.route('/foster/delete/<int:id>', methods=['GET','POST'])
def delete_foster(id):
	form = FosterForm()
	foster_to_delete = Foster.query.get_or_404(id)
	
	try:
		db.session.delete(foster_to_delete)
		db.session.commit()
		flash("Foster Deleted Successfully!")

		our_fosters = Foster.query.order_by(Foster.id)
		return render_template("add_foster.html", form = form, our_fosters = our_fosters)
	except:
		return render_template("add_foster.html", form = form, our_fosters = our_fosters)

####################################################################################################################################################
##                                                           SEARCH ROUTE                                                                       ####
##                                                                                                                                              ####
####################################################################################################################################################

@app.route('/search', methods=['GET','POST'])
def search():
	anything = None
	form = SearchForm()
	cursor.execute("SELECT * from Contact")
	rows = cursor.fetchall()
	#searches = Employee.query
	#contacts = Contact.query.filter_by(ContactInformation.id == 9)
	if form.validate_on_submit():
		#contact_dict = dict((col, getattr(contacts, col)) for col in contacts.__table__.columns.keys())
		form.searched.data = ''
		flash("Search was Successful!" )
	return render_template("search.html", form = form, searched = anything, rows = rows)

#@app.route('/dropdown', methods=['GET', 'POST'])
#def get_dropdown_values():
	


####################################################################################################################################################
##                                                           MODELS                                                                             ####
##                                                                                                                                              ####
####################################################################################################################################################


class Contact(db.Model): 
#    __tablename__ = 'ContactInformation'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    phone = db.Column(db.String(150), unique = True)
    employees = db.relationship('Employee', backref = 'employeersc')
    donations = db.relationship('Donation', backref = 'donationrsc')
    payments = db.relationship('Payment', backref = 'paymentrsc')
    applications = db.relationship('Application', backref='applicationrsc')
    #relationship on Employee class, employeers will create a fake column in employee, so if you wanted to get email, call employeers.email


class Employee(db.Model):
#    __tablename__ = 'Employee'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    address = db.Column(db.String(150), nullable = False)
    dob = db.Column(db.Date, nullable=False)
    ssn = db.Column(db.String(150), nullable=False, unique = True)
    start_date = db.Column(db.Date, nullable=False)
    salary = db.Column(db.Integer, nullable=True)
    position = db.Column(db.String(150),nullable = False)
    #info_id = db.Column(db.Integer, nullable = False, unique = True) #
    info_id = db.Column(db.Integer, db.ForeignKey(Contact.id), nullable = False, unique = True)
    animals= db.relationship('Animal', backref = 'animalrse')
    diagnosiss = db.relationship('Diagnosis', backref = 'diagnosisrse')
    surgerys = db.relationship('Surgery', backref='surgeryrse')
    vaccinations = db.relationship('Vaccination', backref = 'vaccinationrse')
    applications = db.relationship('Application', backref='applicationrse')
    backgrounds = db.relationship('Backgroundcheck', backref='backgroundrse')



class Donation(db.Model):
#    __tablename__ = 'Donation'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=True)
    organization = db.Column(db.String(150), nullable=True)
    amount = db.Column(db.Integer, nullable=False)
    message = db.Column(db.String(150), nullable=True)
    repeat_option = db.Column(db.Integer, nullable=True)
    date = db.Column(db.Date, nullable=False)
    info_id = db.Column(db.Integer, db.ForeignKey(Contact.id), nullable = True)

    #info_id = db.Column(db.Integer, nullable = True) #


class Payment(db.Model):
	id = db.Column(db.Integer, db.ForeignKey(Contact.id), primary_key = True)
	# info_id = db.Column(db.Integer, db.ForeignKey(Contact.id), nullable = True)
	credit_card = db.Column(db.String(150), nullable = False)
	name_on_card = db.Column(db.String(150), nullable = False)
	billing_address = db.Column(db.String(150), nullable = False)
	date = db.Column(db.Date, default = date.today(), nullable =False )


class Animal(db.Model):
#    __tablename__ = 'Animal'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(150), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    dob = db.Column(db.Date, nullable=True)
    sex = db.Column(db.Integer, nullable=False) # 1 for Male, 2 for Female
    species = db.Column(db.String(150), nullable=False)
    breed = db.Column(db.String(150), nullable=False)
    weight = db.Column(db.Integer, nullable=False)
    admission_date = db.Column(db.Date, nullable=False)
    admission_reason = db.Column(db.String(150), nullable=False)
    adoption_status = db.Column(db.Integer, nullable=False)
    foster_status = db.Column(db.Integer, nullable=False)
    #employee_id = db.Column(db.Integer, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey (Employee.id), nullable=False)
    diagnosiss = db.relationship('Diagnosis', backref = 'diagnosisrsa')
    vaccinations = db.relationship('Vaccination', backref = 'vaccinationrsa')
    allergys = db.relationship('Allergy', backref = 'allergyrsa')
    applications = db.relationship('Application', backref='applicationrsa')
    adoptions = db.relationship('Adoption', backref='adoptionrsa')
    fosters = db.relationship('Foster', backref='fosterrsa')

class Diagnosis(db.Model):
#    __tablename__ = 'diagnosis'
	id = db.Column(db.Integer, primary_key = True)
	#animal_id = db.Column(db.Integer, nullable=False)
	#vet_id = db.Column(db.Integer, nullable=False)
	animal_id = db.Column(db.Integer, db.ForeignKey(Animal.id), nullable=False)
	vet_id = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable=False)
	date = db.Column(db.Date, nullable=False)
	diagnosis = db.Column(db.String(150), nullable=False)
	treatments = db.relationship('Treatment', backref='treatmentrsd')
	surgerys = db.relationship('Surgery', backref='surgeryrsd')
	__table_args__ = (db.UniqueConstraint(animal_id, diagnosis),)

class Treatment(db.Model):
#    __tablename__ = 'Treatments'
	id = db.Column(db.Integer, primary_key = True)
	#diagnosis_id = db.Column(db.Integer, nullable = False)
	diagnosis_id = db.Column(db.Integer, db.ForeignKey(Diagnosis.id), nullable = False)
	treatment = db.Column(db.String(150), nullable=False)
	start_date = db.Column(db.Date, nullable=True)
	end_date = db.Column(db.Date, nullable=True)
	dosage = db.Column(db.String(150), nullable=True) 
	__table_args__ = (db.UniqueConstraint(treatment, diagnosis_id),)


class Surgery(db.Model):
#    __tablename__ = 'Surgeries'
	id = db.Column(db.Integer, primary_key = True)
	#diagnosis_id = db.Column(db.Integer, nullable = False)
	#animal_id = db.Column(db.Integer, db.ForeignKey('Animal.id'), nullable = False)
	diagnosis_id = db.Column(db.Integer, db.ForeignKey(Diagnosis.id), nullable = False)
	operation_type = db.Column(db.String(150), nullable = False)
	#vet_id = db.Column(db.Integer,  nullable=False)
	vet_id = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable=False)
	date = db.Column(db.Date, nullable=False)
	success_or_fail = db.Column(db.String(150), nullable = False)
	__table_args__ = (db.UniqueConstraint(diagnosis_id, operation_type, date),)

class Vaccination(db.Model):
#    __tablename__ = 'Vaccinations'
	id = db.Column(db.Integer, primary_key = True)
	#animal_id = db.Column(db.Integer, nullable = False)
	animal_id = db.Column(db.Integer, db.ForeignKey(Animal.id), nullable = False)
	vaccine_type = db.Column(db.String(150), nullable = False)
	#vet_id = db.Column(db.Integer, nullable=False)
	vet_id = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable=False)
	date = db.Column(db.Date, nullable=False)
	notes = db.Column(db.String(150), nullable = True)
	__table_args__ = (db.UniqueConstraint(animal_id, vaccine_type, date),)

class Allergy(db.Model):
	#    __tablename__ = 'Allergies'
	id = db.Column(db.Integer, primary_key = True)
	#animal_id = db.Column(db.Integer, nullable = False)
	animal_id = db.Column(db.Integer, db.ForeignKey(Animal.id), nullable = False)
	allergy = db.Column(db.String(150), nullable = False)
	medication = db.Column(db.String(150), nullable = True)
	__table_args__ = (db.UniqueConstraint(animal_id, allergy),)

class Application(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(150), nullable=False)
	last_name = db.Column(db.String(150), nullable=False)
	address = db.Column(db.String(150), nullable = False)
	dob = db.Column(db.Date, nullable=False)
	ssn = db.Column(db.String(150), nullable=False)
	#candidate_id = db.Column(db.Integer, nullable = False)
	candidate_id = db.Column(db.Integer, db.ForeignKey(Contact.id), nullable = False)
	application_type = db.Column(db.Integer, nullable = False) # 1 for Adoption, 2 for Fostering
	#animal_id = db.Column(db.Integer, nullable =False)
	animal_id = db.Column(db.Integer, db.ForeignKey(Animal.id), nullable =False)
	date = db.Column(db.Date, nullable=False)
	#employee_supervisor = db.Column(db.Integer, nullable = False)
	employee_supervisor = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable = True)
	application_status = db.Column(db.String(150), nullable=False)
	backgrounds = db.relationship('Backgroundcheck', backref='backgroundrsap')
	adoptions = db.relationship('Adoption', backref='adoptionrsap')
	fosters = db.relationship('Foster', backref='fosterrsap')
	__table_args__ = (db.UniqueConstraint(candidate_id, date),)



class Backgroundcheck(db.Model):
#    __tablename__ = 'BackgroundCheck'
	id = db.Column(db.Integer, primary_key = True)
	#application_id = db.Column(db.Integer, nullable = False, unique=True)
	application_id = db.Column(db.Integer, db.ForeignKey(Application.id), nullable = False)
	income = db.Column(db.Integer, nullable = False)
	criminal_record = db.Column(db.String(150), nullable = False)
	credit_score = db.Column(db.Integer, nullable = False)
	interview_status = db.Column(db.String(150), nullable = False)
	#employee_id = db.Column(db.Integer,  nullable=False)
	employee_id = db.Column(db.Integer, db.ForeignKey(Employee.id), nullable=False)
	background_check_status = db.Column(db.String(150), nullable = False)
 

class Adoption(db.Model):
#    __tablename__ = 'Adopters'
	id = db.Column(db.Integer, primary_key = True)
	#first_name = db.Column(db.String(150), nullable=False)
	#last_name = db.Column(db.String(150), nullable=False)
	#app_id = db.Column(db.Integer, nullable = False)
	#animal_id = db.Column(db.Integer, nullable = False, unique=True)
	app_id = db.Column(db.Integer, db.ForeignKey(Application.id), nullable = False)
	animal_id = db.Column(db.Integer, db.ForeignKey(Animal.id), nullable = False)
	adoption_date = db.Column(db.Date, nullable=False)


class Foster(db.Model):
#    __tablename__ = 'Foster_Parents'
	id = db.Column(db.Integer, primary_key = True)
	# first_name = db.Column(db.String(150), nullable=False)
	# last_name = db.Column(db.String(150), nullable=False)
	# app_id = db.Column(db.Integer, nullable = False)
	# animal_id = db.Column(db.Integer, nullable = False)
	app_id = db.Column(db.Integer, db.ForeignKey(Application.id), nullable = False)
	animal_id = db.Column(db.Integer, db.ForeignKey(Animal.id), nullable = False)
	foster_date = db.Column(db.Date, nullable=False)
	__table_args__ = (db.UniqueConstraint(animal_id, foster_date),)



