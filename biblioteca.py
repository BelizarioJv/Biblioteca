
#Você foi contratado para desenvolver um sistema simples de cadastro de livros para uma biblioteca.
#O programa deve permitir que o usuário registre informações sobre vários livros, realizando validações e armazenando dados importantes.
totalLivros = 0
livrosUsados = 0
livrosNovos = 0
idadeMaisAntigo = 0
maisAntigo = ''
while True:
  nomeLivro = input('Digite o nome do livro').strip()
  anoLançamento_str = input('Digite o ano de lançamento do livro')
  if anoLançamento_str.isdigit():
    anoLançamento = int(anoLançamento_str)
  else:
    print('Digito invalido')
  
  totalLivros += 1

  estadoLivro = input('Qual o estado do livro:NOVO ou USADO: ').upper().strip()
  if estadoLivro == 'NOVO':
    livrosNovos += 1
  elif estadoLivro == 'USADO':
      livrosUsados += 1
  else:
    print('Digito invalido')

  if anoLançamento > idadeMaisAntigo :
    maisAntigo += nomeLivro
    idadeMaisAntigo += anoLançamento
  
  continuar = input('Deseja cadastrar outro veiculo?(S/N): ').strip().upper()
  if continuar == 'S':
    continue
  elif continuar == 'N':
   print('****************DADOS CADASTRADOS********************')
   print('-                                                       -')
   print(f'O total de livros cadastrados é:{totalLivros}, sendo eles {livrosNovos} livros novos e {livrosUsados} livros usados.\n ')
   print(f'O livro mais antigo e o {maisAntigo} que foi publicado em {idadeMaisAntigo}\n')
  else:
    print('Digito incorreto')
    break
  

   
