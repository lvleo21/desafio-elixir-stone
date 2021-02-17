from data_base import load_emails, load_items, generate_emails, generate_items

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

    print(f"VALOR DA COMPRA : {purchase_list_price/100}")
    
    #! Dividir o valor de forma igual entre a quantidade de e-mails
    dict2 = split_shopping_list_value(purchase_list_price, len(emails))

    print(f'RESTO : {dict2["rest"]}')
    
    #! Retornar um mapa/dicionário onde a chave será o e-mail e o valor será quanto ele deve pagar nessa conta
    dict3 = generate_dictionary(dict2, emails)

    for x, y in dict3.items():
        print(f"{x} - R$ {y/100}")

if __name__ == "__main__":

    #! A partir de arquivo txt
    #items = load_items('files/items.txt')
    #emails = load_emails('files/emails.txt')
    
    #! Gerando aleatoriamente
    emails = generate_emails(200) 
    items = generate_items(175)
    
    #print(emails)
    #print(items)

    main(items, emails)


    