lista = []

try:
    lista.append(float(input('Digite o primeiro valor')))
    lista.append(float(input('Digite o segundo valor')))
    soma = lista[0] / lista[1]
except ValueError:
    print('Erro! Valor Invalido')
except ZeroDivisionError:
    print('Erro! Divisão por zero')
except IndexError:
    print('Erro! Índice invalido')                         
except KeyboardInterrupt:
    print('Usuário interrompeu a execução')    
else:
    print(f'A divisão é {soma}')    