print('ola mundo')
caixa='caneta'

print(caixa)

nome='leonardo'
idade=25
altura=1.92
estudante=True

print(f'nome:{nome},idade:{idade}idade,{altura}altura,{estudante}estudante')

mensagem="Toma jack toma"
print(mensagem.strip())
print(mensagem.lower())
print(mensagem.upper())
nome=input("qual é o seu nome?")
print(f'ola{nome},vamos da um role')


from datetime import datetime
nome=input('qual o seu nome?')
agora= datetime.now()
hora_atual=agora.strftime('%H:%M')
print(f'ola,{nome}!agora são{hora_atual}.')