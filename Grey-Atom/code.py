# --------------
# Code starts here
# Create the lists 
class_1 = ['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio' ]
class_2 = ['Hilary Mason','Carla Gentry','Corinna Cortes']

# Concatenate both the strings
new_class = (class_1 + class_2)
print (new_class)


# Append the list
new_class.append('Peter Warden')

# Print updated list
print(new_class)


# Remove the element from the list
new_class.remove('Carla Gentry')

# Print the list
print(new_class)

# Code ends here


# --------------
# Code starts here

#creating dictionary
courses={'Math':65 , 'English':70, 'History':80 , 'French':70, 'Science':60  }

#seeing marks of each subject
print(courses)

#adding all the marks 
total=courses['Math']+courses['English']+courses['History']+courses['French']+courses['Science']
#printing total
print(total)
#calc percentage
percentage=(total/500)*100
#printing percentage
print(percentage)
# Code ends here


# --------------
# Code starts here





#creating dictionary
mathematics={'Geoffery Hinton':78, 'Andrew Ng':95, 'Geoffery Hinton':78, 'Sebastian Raschka':65, 'Yoshua Benjio':50, 'Hilary Mason':70, 'Corinna Cortes':66, 'Peter Warden':75 }

#calculating the max marks
topper=max(mathematics,key=mathematics.get)

#printing max marks
print(topper)




# Code ends here  


# --------------
# Given string
topper = 'andrew ng'


# Code starts here
#splitting topper
first_name,last_name=topper.split()
print(last_name)

#displaying full name
full_name=last_name+" "+first_name

#converting to upper case
certificate_name=full_name.upper()

#printing certificate name
print(certificate_name)


# Code ends here


