from models import Generate, Item

"""

# Pontos de Melhoria
    - Não passou no teste de email duplicado.
    - Não trata números negativos.

[X] Verificação de emails duplicados.
[] Tratar números negativos.

"""

def calculate_shopping_list_value(items):
    """
    Esta função é utilizada para verificar qual é o valor total
    da lista de items, para isso utilizo uma variável acumuladora
    que a cada interação acumula a multiplicação entre o valor do
    item e a sua respectiva quantidade.


    Retorno -> Um inteiro que representa o valor total (em centavos)
    da lista de compras. 

    """
    purchase_list_price = 0

    for item in items:
        purchase_list_price += item.get_calculated_item()

    return purchase_list_price


def split_shopping_list_value(purchase_list_price: float, quantity_emails: int):
    """
    Esta função é utilizada para dividir o valor da compra de
    acordo com a quantidade e-mails e informar o 'resto' desta divisão (caso exista).
    Este resto, será utilizado para que não falte nenhum centavo.

    Retorno -> Dicionário contendo as chaves rest e division_value com 
    seus da respectivos valores.

    """

    if quantity_emails >= 0:
        rest = purchase_list_price % quantity_emails
        division_value = purchase_list_price // quantity_emails

        data = {
            'rest': rest,
            'division_value': division_value,
        }

        return data


def generate_dictionary(value_by_email, emails):
    """
    Esta função é utilizada para criar um dicionário onde a key será
    o email e o value será o valor que o mesmo deverá pagar (convertido para reais).

    Se houver resto (resto > 0), então alguns emails receberão um valor
    maior que outros (como no exemplo citado na descrição do teste).

    """

    result = {}
    rest = value_by_email['rest']
    emails_size = len(emails)

    for x, email in enumerate(emails):
        value = 0

        if rest > 0 and x >= (emails_size - rest):
            value = value_by_email['division_value'] + 1
        else:
            value = value_by_email['division_value']


        result[f'{email}'] = (value / 100)  # ! Convertendo o valor de centavo para real

    return result


def calculate(items, emails):
    result = None

    #! Eliminando emails repetidos, logo se há emails repetidos poderemos interpretar como se a pessoa tivesse feito duas ou mais compras.
    #! Ou não, talvez fosse apenas um erro.
    emails = list(dict.fromkeys(emails)) #Removendo emails repetidos

    if len(items) > 0 and len(emails) > 0:
        # ! Calcular a soma dos valores, ou seja, multiplicar o preço de cada item por sua quantidade e somar todos os itens
        purchase_list_price = calculate_shopping_list_value(items)

        # ! Dividir o valor de forma igual entre a quantidade de e-mails
        value_by_email = split_shopping_list_value(purchase_list_price, len(emails))



        # ! Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto ele deve pagar nessa conta
        result = generate_dictionary(value_by_email, emails)

    return result


def show_result(result):
    if result is not None:
        for key, value in result.items():
            print(f'{key} - R$ {value}')
    else:
        print("O valor de RESULT é nulo, insira uma quantidade de emails e items maior que 0.")


if __name__ == "__main__":
    items = Generate.items(200)  # ! Inserir a quantidade de items
    emails = Generate.emails(200)  # ! inserir a quantidade de emails

    result = calculate(items, emails)
    show_result(result)
