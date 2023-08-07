import matplotlib.pyplot as plt

def generate_bar_chart(labels, values):
    '''func para generar grafica. dos variables figura, ax: coordenadas en las cuales vamos a graficar'''
    #labels = ['a', 'b', 'c']
    #values = [100, 200, 80]

    fig, ax = plt.subplots() 
    ax.bar(labels, values) #grafica de barras
    plt.show() #muestra la grafica

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)#indicarle como son los labels
    ax.axis('equal')#le decimos que organice esta grafica en el centro y que sea en objecto circulo
    plt.show()

    if __name__ == '__main__': #si se ejecuta como archivo
        labels = ['a', 'b', 'c']
        values = [100, 200, 80]

        #generate_bar_chart(labels, values)
        generate_pie_chart(labels, values)