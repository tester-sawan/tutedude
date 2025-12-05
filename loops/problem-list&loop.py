#Count all the countries which are starting with "I" also print all there countries.
Countries = ["India","United State","Australia","Ireland","Sri Lanka","Iceland","Cuba","Iran","Poland"]
count = 0 #Declare the temporary count.
country_start_with_I = [] #Declare an empty list to store filter values.
for country in Countries:
    if country[0]=="I":#Validate the logic
        count+=1# store the count
        country_start_with_I.append(country)#Add the matched value under the list.
        #print(country)
print("No. of Countries which starts from 'I' is: ",count)
print("The list of the available countries having first character 'I' is: ", country_start_with_I)