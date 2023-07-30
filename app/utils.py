#los archivos utils generalmente solo contienen funciones
def get_population():
    keys = ['col', 'bol']
    values = [300,400]
    return keys,values

#A = 'a'
def population_by_country(data, country): #recivo informacion y quiero un pais en especifico, data es una lista con dict. por eso filtro ese pais
    '''
    '''
    result = list(filter(lambda item:item['Country'] == country), data) #lambda vamos a ir iterandola y va a haber una key ya que es una lista que tiene un dict, se agregan los indices, y decimos de quien es este pais['Country'], si el pais es igual al que me envian como variable entonces va a ser parte del resultado, se agrega la info que voy a iterar
    return result