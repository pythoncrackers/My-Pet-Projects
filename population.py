currentpopulation = 312032486
no_of_days_year = 365
no_of_years = 1#just in case if we ever need to get collective data for n years. Then only this value needs to be changed

total_no_of_days = no_of_days_year * no_of_years
total_no_of_seconds = total_no_of_days * 24 * 60 * 60

total_birth = total_no_of_seconds // 7
total_death = total_no_of_seconds // 13
total_immigrants = total_no_of_seconds // 45

currentpopulation1 = currentpopulation  + (total_birth - total_death - total_immigrants)
print("The number of the births in 1st year: "+ str(total_birth))
print("The number of the deaths in 1st year: "+ str(total_death))
print("The number of the immigrants in 1st year: "+ str(total_immigrants))
print("The total population: "+ str(currentpopulation1))
print("****************************************************")

currentpopulation2 = currentpopulation1  + (total_birth - total_death - total_immigrants)
print("The number of the births in 2nd year: "+ str(total_birth))
print("The number of the deaths in 2nd year: "+ str(total_death))
print("The number of the immigrants in 2nd year: "+ str(total_immigrants))
print("The total population: "+ str(currentpopulation2))
print("****************************************************")

currentpopulation3 = currentpopulation2  + (total_birth - total_death - total_immigrants)
print("The number of the births in 3rd year: "+ str(total_birth))
print("The number of the deaths in 3rd year: "+ str(total_death))
print("The number of the immigrants in 3rd year: "+ str(total_immigrants))
print("The total population: "+ str(currentpopulation3))
print("****************************************************")

currentpopulation4 = currentpopulation3  + (total_birth - total_death - total_immigrants)
print("The number of the births in 4th year: "+ str(total_birth))
print("The number of the deaths in 4th year: "+ str(total_death))
print("The number of the immigrants in 4th year: "+ str(total_immigrants))
print("The total population: "+ str(currentpopulation4))
print("****************************************************")

currentpopulation5 = currentpopulation4  + (total_birth - total_death - total_immigrants)
print("The number of the births in 5th year: "+ str(total_birth))
print("The number of the deaths in 5th year: "+ str(total_death))
print("The number of the immigrants in 5th year: "+ str(total_immigrants))
print("The total population: "+ str(currentpopulation5))
