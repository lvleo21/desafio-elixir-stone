from random import choice, randrange
import string

class Item:
    """
    Item é uma classe que possui os atributos nome, preço/valor (em centavo) e quantidade.
    """
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price #! Em centavos
        self.quantity = quantity
    
    def get_calculated_item(self):
        """
        Este método é utilizado para retornar a multiplicação entre o preço e a quantidade.
        """
        return self.price * self.quantity

    def __str__(self):
        return self.name

class Generate(object):

    """ 
    Generate é uma classe com doius métodos estáticos, as quais
    são utilizadas para gerar de forma aleátoria listas de items ou 
    emails.
    
    """
    
    @staticmethod
    def items(quantity_items):
        """
        Este método é utilizado para gerar uma lista de items de forma
        aleatória (nome, quantidade e valor), e recebe como parâmetro a 
        quantidade de items que se deseja ter na lista.

        Ex.: name = adasda, price = 1000 e quantity = 20

        """
        items = []
        letters = string.ascii_lowercase

        for _ in range(quantity_items):

            number_of_characters = randrange(1,10) #! Quantidade de caracteres do item (nome)
            name = ''.join(choice(letters) for _ in range(number_of_characters))  #! Nome do item
            price = randrange(1, 10000) #! Preço do item pode variar entre 1 e 10000 centavos
            quantity = randrange(1,30) #! Quantidade pode variar entre 1 e 30 (pode ser interpretado como unidade, peso, etc, ...)


            item = Item(
                name = name, 
                price = price, 
                quantity = quantity
            )

            items.append(item)

        return items

    @staticmethod
    def emails(quantity_emails):
        """
        Este método é utilizado para gerar uma lista de emails de forma
        aleatória e recebe como parâmetro a quantidade de emails que se deseja 
        ter na lista.

        Ex.: xasdsa@stone.com.br

        """
        letters = string.ascii_lowercase

        emails = []

        for _ in range(quantity_emails):
            number_of_characters = randrange(1,6) #! Quantidade de caracteres do email

            email = ''.join(choice(letters) for _ in range(number_of_characters)) + '@stone.com.br'
            emails.append(email)

        return emails