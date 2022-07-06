
#declare a list of counties
counties = ["Arapahoe","Denver","Jefferson", "El Paso"]

###Example: Use of input & int() methods to set variable equal to user-entered value
#my_votes = int(input("How many votes did you get in the election? "))
#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total votes in the election? "))

###Example: Calculating percentages
#percentage_votes = (my_votes / total_votes) * 100

###Example: Use of concatenation to print statement that includes numeric values
#print("I received " + str(percentage_votes)+"% of the total votes.")

###Example: Use of F-string to print statement that includes numeric values
#print(f"I received {my_votes / total_votes * 100}% of the total votes.")

###Example: Use of multiline F-string to print set of sentences (message_to_candidate)
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)

###Example: Use of membership (in) operator
###Result: El Paso is not the list of counties.
#if "El Paso" in counties:
#    print("El Paso is in the list of counties.")
#else:
#    print("El Paso is not the list of counties.")
    
###Example: Use of compound membership (in) + Logical (and) Operator
###Result: Arapahoe or El Paso is not in the list of counties.
#if "Arapahoe" in counties and "El Paso" in counties:
#    print("Arapahoe and El Paso are in the list of counties.")
#else:
#    print("Arapahoe or El Paso is not in the list of counties.")
    
#Example: Use of compound membership (in) + Logical (inclusive or) Operator
###Result: Arapahoe or El Paso is in the list of counties.
#if "Arapahoe" in counties or "El Paso" in counties:
#    print("Arapahoe or El Paso is in the list of counties.")
#else:
#    print("Arapahoe and El Paso are not in the list of counties.")
    
###Example: Use of compound membership (in/not in) + Logical (and) Operator
###Result: Arapahoe or El Paso is in the list of counties.
#if "Arapahoe" in counties and "El Paso" not in counties:
#   print("Only Arapahoe is in the list of counties.")
#else:
#   print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")    

###Example: Use for-loop to print elements in list
###Result: Executes for-loop and prints elements in list of counties.
#for county in counties:
#    print(county)    

###Example: Use range() function to print elements in list
###Result: Executes range() function and prints elements in list of counties.
#for i in range(len(counties)):
#    print(counties[i])   

#declare a dictionary (county:voter KEY:VALUE pairs)
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

###Example: Use for-loop to get KEYS of DICT object
###Result: Prints elements of dict
#for county in counties_dict:
#    print(county)    
    
###Example: Use for-loop + keys() method to get KEYS of DICT object
###Result: Prints keys of dict    
#for county in counties_dict.keys():
#    print(county)
    
###Example: Use for-loop + values() method to get VALUES of DICT object
###Result: Prints values of dict    
#for county in counties_dict.values():
#    print(county)    
    
###Example: Use for-loop + dict_name[key] method to get VALUES of DICT object
###Result: Prints values of dict    
#for county in counties_dict:
#    print(counties_dict[county])    
    
###Example: Use for-loop + get()method to get VALUES of DICT object
###Result: Prints values of dict    
#for county in counties_dict:
#    print(counties_dict.get(county))   

###Example: Use for-loop + items()method to get KEY:VALUE pairs of DICT object
###Result: Prints KEY:VALUE pairs of dict    
#for county, voters in counties_dict.items():
#    print(county, voters)      
    
###SKILL DRILL: "Print each county and registered voter from the counties dictionary using concatenation of strings  
#for county, voters in counties_dict.items():
#    print(county, "county has ", voters, " registered voters.") 

###Example: Print each county and registered voter from the counties dictionary using F-string  
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.") 
    
#declare a list of dictionaries
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

###Example: Use for-loop to iterate through list of dict objects
###Result: Prints series of dictionaries (one per line)   
for county, voters in counties_dict.items():
    print(county, voters)   

###Example: use range() function to iterate over the list of dict and print counties in voting_data
###Result: Prints list of counties
#for i in range(len(voting_data)):
#    print(voting_data[i]['county'])

###Example: use nested for-loop to get values from list of dict
###Result: Prints key then value then key then value...
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)

###Example: use for-loop to retrieve the number of registered voters from each dictionary
###Result: Prints all and only the numbers
#for county_dict in voting_data:
#     print(county_dict['registered_voters'])
     
###Example: use for-loop to retrieve the county from each dictionary
###Result: Prints all and only the counties
#for county_dict in voting_data:
#    print(county_dict['county'])