#Detector de números primos

num_misterioso = int(input("Insira um número inteiro:"))

for i in range(2, num_misterioso):
    if num_misterioso % i == 0:
        print("O número", num_misterioso, "não é primo.")
        break
else:    print("O número", num_misterioso, "é primo.")
 