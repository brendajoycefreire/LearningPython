# O elif é uma palavra-chave em Python que significa "senão, se" e pode ser considerado 
# uma união do else com um if. Ela é usada em conjunto com a palavra-chave if para formar uma estrutura condicional encadeada.

# if condição1:
    # faça algo
# elif condição2:
    # faça outra coisa
# elif condição3:
    # faça mais alguma coisa
# else:
    # faça algo diferente

media = float(input('Digite a média: '))

if media >= 6.0:
  print('Aprovado(a)')
elif 6.0 > media >= 4.0:
  print('Recuperação')
else:
  print('Reprovado(a)')