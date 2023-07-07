#los numeros armónicos se definen como: .... donde Hn es el n-simo número armónico, la entrada consiste en un número n, salida: imprime el n.simo número armonico, con 4 decimales de presicion
n = int(input())

h_n = 0
for i in range(1, n + 1):
    # h_n = h_n + 1/i
    h_n += 1/i

print("{:.4f}".format(h_n))

