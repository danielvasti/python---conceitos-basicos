print('----- INICIO -----\n')

correct_user = 'PedrinhoMatador'
correct_password = 'Balls123'

user = input('Digite nome de usuario: ')
password= input('Digite a senha: ') 

if user == correct_user and password == correct_password:
    print('Logado com sucesso')
elif user == correct_user and not password == correct_password:
    print('Senha errada!')
elif not user == correct_user and password == correct_password:
    print('Usuário incorreto')
else:
    print('nome de usuario e senha incorreta')
print('\n----- FIM -----')