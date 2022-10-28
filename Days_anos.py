
number_of_days = int(input("Numero de dias: "))

# Calculando o ano
years = number_of_days // 365

# Calculando os meses
months = (number_of_days - years *365) // 30

# Calculando os dias
days = (number_of_days - years * 365 - months*30)

# Displaying results
print("Anos = ", years)
print("Meses = ", months)
print("Dias = ", days)



