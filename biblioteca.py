totalLivros = 0
totalNovo = 0
MaisAntigo = ''
MaisAntigo_Ano = 0 
totalUsados = 0


while True:
    nomeLivro = input('Digite o nome do livro').strip()
    anoPublicaçao_str= input('Digite o ano da publicaçao do livro')
    if anoPublicaçao_str.isdigit() and anoPublicaçao_str != 0:
        anoPublicaçao = int(anoPublicaçao_str)
    else:
        print('Digito invalido')
        break
    
    estadoLivro = input('Digite o estado fisico do livro:NOVO ou USADO').strip().upper()
    if estadoLivro == 'NOVO':
        totalNovo += 1
    elif estadoLivro =='USADO':
        MaisAntigo = nomeLivro
        MaisAntigo_Ano = anoPublicaçao
        
    totalLivros +=1
    continuar = input('Deseja cadastrar mais um aluno e as suas notas?(S/N)').strip().upper()
    if continuar != 'S':
     break
    
    
    
print('***********************************************')
print('-                                                  -')
print(f'A biblioteca tem {totalNovo} livros novos')
print(f'O total de livros na biblioteca e de {totalLivros}')
if totalUsados != 0:   
 print(f'O mais antigo e o {MaisAntigo} que foi publicado em {MaisAntigo_Ano}')
print('-                                                  -')
print('***********************************************')