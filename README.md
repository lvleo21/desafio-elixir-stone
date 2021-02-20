
<center>

# Desafio Elixir Stone

</center>

## Sumário
- A Solução
- Como executar o programa ?


## A Solução

Bom, tudo começa nessa bloco (onde controlo o escopo da execução do aquivo). Aqui, eu uso uma classe chamada *Generate* que possui os métodos estaticos *items* (serve para gerar items de forma aleatória) e *emails* (serve para gerar emails de forma aleatória).

Depois dos emails e itens serem gerados, eles serão passados para a função calculate, o qual, retorna um dicionário com *key* igual ao email e *value* é o que ele tem que pagar. Por fim, é apenas um for que exibirá no terminal/console a *key* e o *value* (em real).

```python
if __name__ == "__main__":

    # Lista de Items (A classe Item e Generate encontra-se em 
    # models.py)
    items = Generate.items(373) #! Inserir a quantidade de items
    
    # Lista de emails (email é uma string)
    emails = Generate.emails(179) #! inserir a quantidade de emails

    result = calculate(items, emails)
    show_result(result) # Exibir/imprimir result

```

As funções desenvolvidas para esta solução, estão devidamentes explicadas em seus respectivos blocos. Porém, queria abri espaço para o ponto chave dessa solução, a função generate_dictionary. A mesma, é utilizada para gerar um dicionário (email/valor a ser pago) como é solicitado na descrição do desafio. A lógica que utilizei foi verificar se a divisão entre todos os emails possui resto. A segunda parte, é verificar se o contador do meu loop for (variável x) é maior ou igual a quantidade de emails menos o resto. 

"Mas Leonardo, porque essa verificação ?"

Bom, podemos inserir quantidade items e emails de diversas formas e isto vai permitir uma gama enorme de resultados que muitas vezes não serão exatos, por exemplo uma compra onde o valor total seja de R$ 1,00 e a quantidade de emails
1000, o resultado da divisão inteira seria 0 e o resto dessa divisão seria de 100. Com isso, 900 pessoas pagariam 0 centavos e as outras 100, 1 centavo.
Então, para isso eu resolvi dividir este bloco de emails que receberam os centavos e para isso eu utilizo como referência o índice da lista e o resto, que basicamente vai me dizer que X quantidade de pessoas receberão um centavo a mais. 


```python
def generate_dictionary(value_by_email, emails):
    result = {}
    rest = dict2['rest']
    emails_size = len(emails)
   
    for x, email in enumerate(emails): 
        value = 0

        if rest > 0 and x >= (emails_size - rest): 
            value = dict2['division_value'] + 1
        else: 
            value = dict2['division_value']
        
        result[f'{email}'] = value / 100 #! Convertendo o valor de centavo para real
    
    return result
```



# Como rodei o programa ?

Na minha máquina, utilizo o sistema operacional *Linux Mint 19.3 Cinnamon* e para executar o programa utilizei o comando (no terminal):

```
python3 challenge.py 
```

Outra opção seria rodar pela "shell" do Python, para isso siga os seguinte passos:

- Abra a "shell"

```
python3
```
- Importe a classe Generate

```
from models import Generate
```
   
- Impote o método calculate

```
from challenge import calculate, show_result
```

- Agora, baste gerar a quantidade de emails e items que deseja

```python
items = Generate.items(13) # informando a quantidade de items 
emails = Generate.emails(10) # informando a quantidade de emails
```

- E por fim, passe *items* e *emails* como parâmetro para a função calculate

```python
result = calculate(items, emails)
show_result(result) # imprimir result

```