nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))
hobbies = input('Digite os seus hobbies um a um, separando-os por vírgulas: ')
hobbies1 = hobbies.split(',')

# A linha de código hobbies1 = hobbies.split(',') está pegando a variável hobbies, 
# que provavelmente contém uma string de palavras ou frases separadas por vírgulas, 
# e a "quebrando" em uma lista de substrings, utilizando a vírgula como delimitador.
# O método .split(',') divide a string sempre que encontra uma vírgula, gerando elementos separados na lista hobbies1.

endereco_rua = input('Digite o nome da sua rua: ')
endereco_numero = int(input('Digite o número da sua casa: '))
endereco_cidade = input('Digite a sua cidade: ')
endereco = (endereco_rua, endereco_numero, endereco_cidade)