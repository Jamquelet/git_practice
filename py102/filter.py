numbers = [1,2,3,4,5,6]
new_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(new_numbers)


matches = [
    {
        'home_team': 'Bolivia',
        'away_team': 'Uruguay',
        'home_team_score': 3,
        'away_team_score': 1,
        'home_team_result': 'Win'
    },
    {
        'home_team': 'Brazil',
        'away_team': 'Mexico',
        'home_team_score': 1,
        'away_team_score': 1,
        'home_team_result': 'Draw'

    },
    {
        'home_team': 'Ecuador',
        'away_team': 'Venezuela',
        'home_team_score': 5,
        'away_team_score': 0,
        'home_team_result': 'Win'

    }
]

print(matches)
print(len(matches))

new_list = list(filter(lambda item: item['home_team_result'] == 'Win', matches))
print(new_list)
print(len(new_list))

def filter_by_length(words):
    result = list(filter(lambda x:len(x)>=4,words))
    return result

words = ['amor','paz','arbol','az']
response = filter_by_length(words)
print(response)

##
datos = [1,3,5,2,7,10]
filter(lambda n: n%2 ==0, datos)

datos = [1,3,5,2,7,4, 10]

for num in filter(lambda n: n%2 ==0, datos):
    print(num)

#como lista
print(list(filter(lambda n: n%2 == 0, datos)))

#ejemplo:generar una lista con los cubos de los pares de otra lista
#declarrativo
datos = [1,3,5,2,7,4,10]
res = map(lambda x: x**2, filter(lambda x: x%2 == 0, datos))
print(list(res)) #[4, 16, 100]
