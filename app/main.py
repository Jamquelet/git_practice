import utils 

#print(utils.A)
data = [
    {
        'Country': 'Colombia',
        'Population': 500
    },
    {
        'Country': 'Bolivia',
        'Population': 300
    }
]

def run():
    keys, values = utils.get_population()
    print(keys, values)


    country = input('Type Country => ')
    result = utils.population_by_country(data, country)
    print(result)

if __name__ == '__main__': #si es ejecutado desde la terminal se ejecuta el metodo run, si es ejecutado desde otro archivo no se ejecuta este bloque de codigo, se ejecuta como script
    run()