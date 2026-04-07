print('Olá, Mundo!')
print('Eulla Paula dos Santos Oliveira')
print('Nome: Ana\nIdade: 15\nCurso: Infoweb')
print('1,2,3,4,5')
print("*****")
print("*   *")
print("*****")
print('Phyton é incrível!', end="")
print(10, 20, sep=" ")
for i in range(1, 6):
    print(2 * i)
print(f"{'Produto':<10} {'Preço'}")
print(f"{'Caneta':<10} {2.50:>.2f}")
print(f"{'Caderno':<10} {12.00:>.2f}")
print(f"{'Borracha':<10} {1.75:>.2f}")
cidade = "Natal,"
estado = "RN"
print('Eu moro em', cidade, estado)
ano_nascimento = "2011"
print('O ano de nascimento é:', ano_nascimento)

a = 5
b = 10
a, b = b, a
print('A =', a)
print('B =', b)

x = 1
y = 2
z = 3
soma = x + y + z
print('A soma dos números de x, y e z é:', soma)

mensagem = 'Aprendendo Phyton'
print(mensagem)

preco = '49,90'
print('O preço do produto é: R$', preco)

ativo = True
print(ativo)

pontos = 100
print(pontos + 50)

nome = 'Eulla'
idade = '15'
nota = '0'
print('Aluno:', nome, '\nIdade:', idade, '\nNota:', nota)

#nome = input("Digite seu nome: ")
#print(f"Olá, {nome}!")

cidade2 = input("Qual a sua cidade?")
print(f'Ótimo, você mora em {cidade2}.')