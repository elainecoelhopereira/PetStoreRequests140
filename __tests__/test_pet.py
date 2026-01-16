# 1 - bibliotecas
import pytest                    # engine / framwork de teste de unidade
import requests                  # framework de test de API
import json                      # leitor e escritor de arquivos json

# 2 - classe (Opcional no Python, em muitos casos)

# 2.1 - atributos ou variaveis
# consulta e resultado esperado
pet_id = 918286801               # codigo do animal
pet_name = "Snoopy"              # nome do animal
pet_category_id = 1              # codigo da categoria do animal
pet_category_name = "dog"        # titulo da categoria
pet_tag_id = 1                   # codigo do rotulo
pet_tag_name = "vacinado"        # titulo do rotulo

# informações em comum
url = 'https://petstore.swagger.io/v2/pet'          # endereço
headers = { 'Content-Type': 'application/json' }    # formato dos dados trafegados

# 2.2 - funções / método

def test_post_pet():
    # configura
    # dados de entrega estão no arquivo json
    pet=open('./fixtures/json/pet1.json')        # abre o arquivo json
    data=json.loads(pet.read())                  # ler o conteudo e carrega como json em uma variavel data
    # dados de saíde / resultado esperado estão nos atributos acima das funções

    # executa 
    response = requests.post(           # executa o método post c as informaçõe a segui
        url=url,                        # endereço
        headers=headers,                # cabeçalho / informações extras da mensagem
        data=json.dumps(data),          # a mensagem = json
        timeout=5                       # tempo limite da transição, em segundos
    )

    # valida
    response_body = response.json()        # cria uma variavel e carrega a resposta em formato json

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name

def test_get_pet():
    # Configura
    # Dados de Entrada e Saída / Resultado Esperado estão na sessão de atributos antes das funções

    # Executa
    response = requests.get(
        url=f'{url}/{pet_id}',  # chama o endereço do get/consulta passando o codigo do animal
        headers=headers
        # não tem corpo de mensagem / body
    )


    # valida
    response_body = response.json()        

    assert response.status_code == 200
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == 'available'


def test_put_pet():
    # Configura
    # dados de entrada vem de um arquivo json
    pet = open('./fixtures/json/pet2.json')
    data = json.loads(pet.read())
    # dados de saída / resultado esperado vem dos atributos descritos antes das funções

    # Executa
    response = requests.put(
        url=url,  
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

       
    # Valida
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name    
    assert response_body['category']['id'] == pet_category_id
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['status'] == 'sold'

def test_delete_pet():
    # Configura
    # dados de entrada vem de um arquivo json
    
    # Executa
    response = requests.delete(
        url=f'{url}/{pet_id}',  
        headers=headers        
    )
       
    # Valida
    response_body = response.json()

    assert response.status_code == 200   # status code 200 é so p saber se chegou
    assert response_body['code'] == 200   # status code 200 é p saber se chegou certo
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(pet_id)    
   