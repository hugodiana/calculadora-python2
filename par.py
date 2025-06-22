def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False    
        
num = input("Digite um número:")
num = int(num)
if is_even(num):
        print("O número é par!")
else: 
    print("O número é ímpar!")
