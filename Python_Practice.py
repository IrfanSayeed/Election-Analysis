# temperature = int(input("What is the temperature outside? "))

# if temperature > 80:
#     print("Turn on the AC.")
# else:
#     print("Open the windows.")
# #What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# else:
#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')
# # What is the score?
# score = int(input("What is your test score? "))

# # Determine the grade.
# if score >= 90:
#     print('Your grade is an A.')
# elif score >= 80:
#     print('Your grade is a B.')
# elif score >= 70:
#     print('Your grade is a C.')
# elif score >= 60:
    # print('Your grade is a D.')
# else:
#     print('Your grade is an F.')
# counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")
# x = 0
# while x <= 5:
#     print(x)
#     x = x + 1
# count = 7

# while count < 1:

#     print("Hello World")

counties_tuples = ('Arapahoe','Denver','Jefferson')
print(counties_tuples)
for i in range(len(counties_tuples)):

    print(counties_tuples[i])

# for i in range(len(counties_tuples)):       
#     print(counties_tuples[i])

# for i in len(counties_tuples):

#     print(counties_tuples[i])

# for i in len(counties_tuples):       
#     print(counties_tuples[i])

# for county in counties_tuples:

#     print(county)

# for county in counties_tuples:
#     print(county),

# for county in counties_tuples:

#       print(counties)
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in voting_data:
#     print(county_dict)
# for county_dict in voting_data:  
#      print(county_dict.values())
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")
print(message_to_candidate)
    