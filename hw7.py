#hw7
import my_func
import my_func as mf
from my_func import print_stars
import random 
#1
str1 = "Oz Alkobi Massad"
print(len(str1), str1.upper(), str1.lower(), str1.startswith("Oz"), str1.endswith("Massad"), str1.split(), str1.replace(" ", '*').split('*'),  str1.center(50, '='), str1[3:], str1[:4], str1[1::2], str1.title())

#2
print("  fun-day  ".replace(' ', ''), 'hello'.isalpha(), '777'.isdigit(), '    '.isspace(), ''.join(['N', 'I', 'N', 'J', 'A']), '*'.join(['N', 'I', 'N', 'J', 'A']), 'e' in 'hELLo'.lower())
str1 = input("Enter a string")
lst1: list[str] = [i for i in str1 if i.isalpha()]
print(lst1)

#3
mf.print_stars()
print_stars()
help(print_stars)
#זה לא מדפיס את הדוקומנטציה ולדעתי בגלל שאני מתכנת בטאבלט האימפורט לא עובד כרגיל

#4 bonus game
capital_list: list[str] = [
    'Kabul', 'Tirana', 'Algiers', 'Andorra la Vella', 'Luanda', 'Saint John\'s', 'Buenos Aires', 'Yerevan',
    'Canberra', 'Vienna', 'Baku', 'Nassau', 'Manama', 'Dhaka', 'Bridgetown', 'Minsk', 'Brussels', 'Belmopan',
    'Porto-Novo', 'Thimphu', 'Sucre', 'Sarajevo', 'Gaborone', 'Brasília', 'Bandar Seri Begawan', 'Sofia',
    'Ouagadougou', 'Gitega', 'Praia', 'Phnom Penh', 'Yaoundé', 'Ottawa', 'Bangui', 'N\'Djamena', 'Santiago',
    'Beijing', 'Bogotá', 'Moroni', 'Brazzaville', 'Kinshasa', 'San José', 'Zagreb', 'Havana', 'Nicosia',
    'Prague', 'Copenhagen', 'Djibouti', 'Roseau', 'Santo Domingo', 'Quito', 'Cairo', 'San Salvador', 'Malabo',
    'Asmara', 'Tallinn', 'Mbabane', 'Addis Ababa', 'Palikir', 'Suva', 'Helsinki', 'Paris', 'Libreville',
    'Banjul', 'Tbilisi', 'Berlin', 'Accra', 'Athens', 'Saint George\'s', 'Guatemala City', 'Conakry', 'Bissau',
    'Georgetown', 'Port-au-Prince', 'Tegucigalpa', 'Budapest', 'Reykjavík', 'New Delhi', 'Jakarta',
    'Baghdad', 'Dublin', 'Jerusalem', 'Rome', 'Kingston', 'Tokyo', 'Amman', 'Nur-Sultan', 'Nairobi', 'Tarawa',
    'Pyongyang', 'Seoul', 'Kuwait City', 'Bishkek', 'Vientiane', 'Riga', 'Beirut', 'Maseru', 'Monrovia', 'Tripoli',
    'Vaduz', 'Vilnius', 'Luxembourg', 'Antananarivo', 'Lilongwe', 'Kuala Lumpur', 'Malé', 'Bamako', 'Valletta',
    'Majuro', 'Nouakchott', 'Port Louis', 'Mexico City', 'Palau', 'Chisinau', 'Monaco', 'Ulaanbaatar', 'Podgorica',
    'Rabat', 'Maputo', 'Naypyidaw', 'Windhoek', 'Yaren', 'Kathmandu', 'Amsterdam', 'Wellington', 'Managua',
    'Niamey', 'Abuja', 'Skopje', 'Oslo', 'Muscat', 'Islamabad', 'Ngerulmud', 'Panama City', 'Port Moresby',
    'Asunción', 'Lima', 'Manila', 'Warsaw', 'Lisbon', 'Doha', 'Bucharest', 'Moscow', 'Kigali', 'Basseterre',
    'Castries', 'Kingstown', 'Apia', 'San Marino', 'São Tomé', 'Riyadh', 'Dakar', 'Belgrade', 'Victoria',
    'Freetown', 'Singapore', 'Bratislava', 'Ljubljana', 'Honiara', 'Mogadishu', 'Pretoria', 'Juba', 'Madrid',
    'Colombo', 'Khartoum', 'Paramaribo', 'Stockholm', 'Bern', 'Damascus', 'Taipei', 'Dushanbe', 'Dodoma',
    'Bangkok', 'Lomé', 'Nukuʻalofa', 'Port of Spain', 'Tunis', 'Ankara', 'Ashgabat', 'Funafuti', 'Kampala',
    'Kyiv', 'Abu Dhabi', 'London', 'Washington, D.C.', 'Montevideo', 'Tashkent', 'Port Vila', 'Vatican City',
    'Caracas', 'Hanoi', 'Sanaa', 'Lusaka', 'Harare'
]
strRandom = capital_list[random.randint(1,len(capital_list))]

strTemplate = strRandom
for i in strTemplate:
    if i.isalpha():
        strTemplate = strTemplate.replace(i, '_')
    elif i.isspace():
        strTemplate = strTemplate.replace(i, '-')
listTemplate = list(strTemplate)
print(' '.join(listTemplate)) 
guesses: int = 1
stop = False
while '_' in listTemplate:
    chrGuess: chr = input("Enter a letter ").lower()
    if chrGuess in strRandom.lower():        
        lstPoses: list[int] = []
        x = 0
        while x < len(strRandom):
            if strRandom.lower()[x] == chrGuess:
                lstPoses.append(x)
            x += 1        
        for i in range(len(lstPoses)):
            listTemplate[lstPoses[i]] = chrGuess
        print(' '.join(listTemplate))
    else:
        print("There is no such letter here")
        guesses +=1
print(f"You guessed the word ! with {guesses} guesses")