counties={'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}
counties["Arapahoe"]=422829
counties
{'Arapahoe': 422829}
counties["Denver"]=463353
counties["Jefferson"]=432438
counties
{'Arapahoe': 422829, 'Denver': 463353, 'Jefferson': 432438}

voting_data=[]
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Denver","registered_voters":463353})
voting_data.append({"county":"Jefferson","registered_voters":432438})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]

voting_data.insert(1,{"county":"El Paso","registered_voters":461149})
voting_data
[{'county': 'Arapahoe', 'registered_voters': 422829}, {'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}]
voting_data.remove({"county":"Denver","registered_voters":463353})
voting_data.insert(2,{"county":"Denver","registered_voters":463353})
voting_data.remove({"county":"Arapahoe","registered_voters":422829})
voting_data.append({"county":"Arapahoe","registered_voters":422829})
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Arapahoe', 'registered_voters': 422829}]
voting_data.remove({"county":"Denver","registered_voters":463353})
voting_data.insert(2,{"county":"Denver","registered_voters":463353})
voting_data
[{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]


#For loops
# for county in counties:
#         print(county)

for county, voters in counties.items():
    print("In " [county] "there are "[registered_voters] "registered voters")


# counties=["Arapahoe","Denver","Jefferson"]

# # if counties[1]=="Denver":
# #     print(counties[1])


# # temperature=int(input("What is the temperature outside?"))
# # if temperature>80:
# #     print("Turn on the AC.")
# # else:
# #     print("Open the windows.")

# # score=int(input("What is your test score?"))
# # if score >=90:
# #     print("Your Grade is an A")
# # elif score >=80:
# #     print("Your Grade is a B")
# # elif score >=70:
# #     print("Your Grade is a C")
# # elif score >=60:
# #     print("Your Grade is a D")

# # if "El Paso" in counties:
# #     print("El Paso is in the list of counties")
# # else:
# #     print("El Paso is not in the list of counties")
# # if "Arapahoe" in counties and "El Paso" not in counties:
# #     print("Only Arapahoe is in the list of counties")
# # else:
# #     print("Arapahoe is in the list of counties and El Paso is not in the list of counties")
# count=7
# while count<1:
#     print("Hello")

