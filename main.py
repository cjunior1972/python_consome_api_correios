import requests

def main():
    print('####################')
    print('### Consulta CEP ###')
    print('####################')
    print()

    cep_input = input('Digite o CEP para consultas:')
    if len(cep_input) != 8:
        print('Você precisa digitar 8 dígitos para o CEP!')
        exit()

    print('Resultados')

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))
    address_data = request.json()

    if 'erro' not in address_data:
        print('')
        print('CEP encontrado:')
        print(request.json())
        print('')
        print('CEP: {}'.format(address_data['cep']))
        print('ENDERECO: {}'.format(address_data['logradouro']))
        print('COMPLEMENTO: {}'.format(address_data['complemento']))
        print('BAIRRO: {}'.format(address_data['bairro']))
        print('CIDADE: {}'.format(address_data['localidade']))
        print('ESTADO: {}'.format(address_data['uf']))
    else:
        print('{}: CEP inválido'.format(cep_input))
    print('........................................................................')
    option = int(input('Deseja realizar uma nova consulta ?\nl. Sim\n2. Sair\n3.'))
    if option ==1:
        main()
    else:
        print('Saindo...')




if __name__ == '__main__':
    main()




