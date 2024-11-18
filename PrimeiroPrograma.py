nome = input('Digite o seu nome: ')
idade = int(input('Digite a sua idade: '))
altura = float(input('Digite a sua altura: '))
hobbies = input('Digite os seus hobbies um a um, separando-os por vírgulas: ')
hobbies1 = hobbies.split(',')

# A linha de código hobbies1 = hobbies.split(',') está pegando a variável hobbies, 
# que provavelmente contém uma string de palavras ou frases separadas por vírgulas, 
# e a "quebrando" em uma lista de substrings, utilizando a vírgula como delimitador.
# O método .split(',') divide a string sempre que encontra uma vírgula, gerando elementos separados na lista hobbies1.