from random import choice, randrange
import string

def load_emails(file_name):
    data = []

    try:
        file = open(file_name, "r") 
        
        for line in file.readlines():
            columns = line.strip().split(",")
            data.append(columns[0])
        file.close()

    except (IndexError, FileNotFoundError):
        pass

    return data

def load_items(file_name):

    data = []

    try:
        file = open(file_name, "r") 

        for line in file.readlines():
            columns = line.strip().split("/")
            item = {
                'name': columns[0],
                'value': int(columns[1]),
                'quantity': int(columns[2]),
            }
            data.append(item)
        file.close()

    except (IndexError, FileNotFoundError):
        pass

    return data


def generate_emails(quantity_emails):
    letters = string.ascii_letters

    emails = []

    for _ in range(quantity_emails):
        email = ''.join(choice(letters) for _ in range(4)) + '@stone.com.br'
        emails.append(email)

    return emails

def generate_items(quantity_items):
    items = []
    letters = string.ascii_letters

    for _ in range(quantity_items):
        name = ''.join(choice(letters) for _ in range(randrange(1,6)))  #! Nome do produto
        value = randrange(1, 10000)
        quantity = randrange(1,30)

        item = {
            'name': name,
            'value': value,
            'quantity': quantity,
        }

        items.append(item)

    return items