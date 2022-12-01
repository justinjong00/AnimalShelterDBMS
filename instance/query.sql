SELECT AVG(age) FROM Animal;
SELECT MIN(age) FROM Animal; 
SELECT MAX(age) FROM ANIMAL; 

SELECT animal_id, getdate() as CurrentDate, year(getdate())-year(dob) as age
FROM Application
WHERE age BETWEEN 21 AND 25; 

SELECT Adoptions.app_id
FROM Adoptions
JOIN Application
ON Adoptions.app_id = Application.id
JOIN Contact_Information 
ON Application.candidate_id = Contact_Information.id
JOIN Animal
ON Application.animal_id = Animal.id 
WHERE Animal.species = 'Cat' 
AND Contact_Information.email LIKE '%gmail%'; 

SELECT animal_id 
FROM Adoptions
JOIN Animal ON Adoptions.animal_id = Animal.id 
JOIN Backgroundcheck ON Adoptions.app_id = Background_Check.application_id
WHERE Animal.species = 'Dog'
AND Background_Check.status = 'Fail';


SELECT getdate() as CurrentDate, year(getdate())-year(dob) as age, AVG(age) 
FROM Application
JOIN Fosters ON Fosters.app_id = Application.id; 

SELECT AVG(income) 
FROM Background_Check
JOIN Adopter_Application
ON Adopter_Application.info_id = Background_Check.info_id
WHERE Adopter_Application.application_status = 'Success';
 
SELECT COUNT(animal_id) as count
FROM Allergy 
WHERE count > 1;

SELECT COUNT(vet_id) as freq
FROM Surgeries
JOIN Employee 
ON Employee.id = Surgeries.vet_id
JOIN Animal 
ON Surgeries.animal_id = Animal.id 
WHERE Animal.species = 'Dog'
GROUP BY Employee.id 
ORDER BY freq DESC
LIMIT 1;

SELECT id
FROM Animal
ORDER BY admission_date ASC;

SELECT COUNT(species) as freq
FROM Animal 
JOIN Adoptions
ON Adoptions.animal_id = Animal.id 
JOIN Application ON Application.id = Adoptions.app_id
WHERE Application.application_status = 'Success' 
GROUP BY Animal.species
ORDER BY freq DESC;

SELECT COUNT(breed) as freq
FROM Animal 
JOIN Adopter_Application
ON Adopter_Application.animal_id = Animal.id 
WHERE Adopter_Application.application_status = 'Success' 
GROUP BY Animal.breed
ORDER BY freq DESC;

SELECT COUNT(animal_id) as freq
FROM Application
WHERE freq > 1
GROUP BY animal_id;

SELECT COUNT(operation_type) as freq 
FROM Surgeries
JOIN Animal
ON Surgeries.animal_id = Animal.id 
WHERE Animal.species = 'Cat'
GROUP BY Surgeries.operation_type 
ORDER BY freq DESC 
LIMIT 1; 

SELECT admission_date, Adoptions.adoption_date as adopt_date
FROM Animal
JOIN Adoptions ON Animal.id = Adoptions.animal_id
GROUP BY AVG(adopt_date - admission_date);