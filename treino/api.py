from ninja import Router

treino_router = Router()

@treino_router.get('teste/')
def criar_aluno(request):
    return{'Ola mundo':'Ola mundo'}