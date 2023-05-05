def eh_vogal(letra):
    
    vogais = 'aeiou'
    return letra.lower() in vogais
    

letra1 = 'a'
letra2 = 'E'
letra3 = 'z'

print(eh_vogal(letra1)) 
print(eh_vogal(letra2)) 
print(eh_vogal(letra3)) 