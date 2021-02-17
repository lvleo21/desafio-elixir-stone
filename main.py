from data_base import load_emails, load_items

class ShoppingList:
    def __init__(self):
            self.items = []
            self.purchase_price = 0

    def add_item(self, name, quantity, value):
        new_item = {
            'name': name,
            'quantity': quantity,
            'value': value,
        }

        self.items.append(new_item)
        self.calculate_shopping_list_value()

    def calculate_shopping_list_value(self):

        if len(self.items) is not 0:
            amount = 0
            for item in self.items:
                amount += (item['quantity'] * item['value']) 
            self.purchase_price = amount


    def print_list(self):
        for x, item in enumerate(self.items):
            print(f'{x} -> { item["name"] } : R$ {item["value"] / 100}')

def split_list_value(purchase_price, email_list):
    email_list_size = len(email_list)

    has_rest =  (purchase_price%email_list_size) if (purchase_price%email_list_size) > 0 else False

    division_value = purchase_price // email_list_size

    data = {
        "rest" : has_rest,
        "division_value" : division_value,
        "email_list_size" : email_list_size,
    }


    return data  


def calculate_shopping_list_value(items):
    purchase_list_price = 0
    for item in items:
        purchase_list_price += (item['quantity'] * item['value'])
    
    return purchase_list_price

def split_shopping_list_value(purchase_list_price, quantity_emails):

    if quantity_emails >= 0:
        rest = purchase_list_price%quantity_emails
        division_value = purchase_list_price // quantity_emails

        data = {
            'rest' : rest,
            'division_value' : division_value,
        }

        return data

def generate_dictionary(dict2, emails):
    temp = {}
    temp_rest = dict2['rest']
    
    for email in emails:
        if temp_rest > 0 :
            temp[f'{email}'] =  dict2['division_value'] + 1
            temp_rest-=1
        else:
            temp[f'{email}'] =  dict2['division_value']

    return temp
        
def main(items, emails):
    
    #! Calcular a soma dos valores, ou seja, multiplicar o preço de cada item por sua quantidade e somar todos os itens
    purchase_list_price = calculate_shopping_list_value(items)
    
    #! Dividir o valor de forma igual entre a quantidade de e-mails
    dict2 = split_shopping_list_value(purchase_list_price, len(emails))
    
    #! Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto ele deve pagar nessa conta
    dict3 = generate_dictionary(dict2, emails)

    for x, y in dict3.items():
        print(f"{x} - {y}")

if __name__ == "__main__":

    items = load_items('files/items.txt')
    emails = load_emails('files/emails.txt')
   
    main(items, emails)

    

    # shopping_list.add_item('Pão', 10, 15) #! Nome, Quantidade, valor
    # shopping_list.add_item('Café', 8, 425)
    # shopping_list.add_item('Biscoito', 3, 325)
    # shopping_list.add_item('Leite', 4, 450)
    # shopping_list.add_item('Feijão', 2, 800)
    # shopping_list.add_item('Arroz', 2, 400)
    # shopping_list.add_item('Carne', 1, 3800)
    # shopping_list.add_item('Farinha', 1, 200)

    # shopping_list.print_list()

    # print()

    # price = shopping_list.purchase_price
   
    # print(f'PRICE: R$ {price/100}')

    
    # data = split_list_value(price, email_list)

    # print(data)
    # teste = email_list[-data['rest']:]
    # print(teste)
    
    # new_list = []
    # temp_rest = data['rest']
    
    # email_list.reverse()
    
    # if data['rest'] is not 0:
       
    #     for email in email_list:
    #         if temp_rest > 0:
    #             new_dict = {
    #                 f"{email}" : (data['division_value'] + 1) / 100
    #             }
    #             temp_rest-=1
    #         else:

    #             new_dict = {
    #                 f"{email}" : data['division_value'] / 100
    #             }
    #         new_list.insert(0, new_dict)
    # else:
    #     print('Não Tem resto !')
    #     for email in email_list:
    #         print(f'{email} - {data["division_value"]}')

    
    

    # for x, i in enumerate(new_list):
        
    #     print(f"{x+1} -> {i}")

        