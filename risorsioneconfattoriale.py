def function(numero):
    if numero<2:
        return 1
    return numero*function(numero-1)

print(function(int(input("Inserisci un numero: "))))