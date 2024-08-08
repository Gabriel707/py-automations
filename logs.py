import logging

logging.basicConfig(level=logging.DEBUG, filename='app.log',
                    filemode='a', format='%(levelname)s - %(message)s - %(asctime)s')

try:
    email = input('Digite seu e-mail: ')
    senha = int(input('Digite sua senha bancáris: '))
    if senha == 1234:
        print('Login feito com sucesso')
        logging.info(f'{email}, entrou em sua conta bancária')
except ValueError as erro:
    print('digite apenas numeros')
    logging.info(erro)
