from ninja import NinjaAPI

from treino.api import treino_router

'''
1 - a instancia do NinjaApi, será responsavel pelo roteamento da minha API, 
2 - depois será necessario criar um Router(treino_router), 
é a funcao responsavel dentro de cada APP criar nossas URLS(muito semelhante arquivos de views)

'''

api = NinjaAPI()
api.add_router('',treino_router)