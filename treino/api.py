from ninja import Router
from ninja.errors import HttpError
from .models import Alunos

from .schemas import AlunosSchema

treino_router = Router()

@treino_router.post('', response={201: AlunosSchema})
def criar_aluno(request, aluno_schema: AlunosSchema):
    #recebendo os dados 
    nome = aluno_schema.dict()['nome']
    email = aluno_schema.dict()['email']
    faixa = aluno_schema.dict()['faixa']
    data_nascimento = aluno_schema.dict()['data_nascimento']

    #Recebendo: temos uma opcao mais simplificado de fazer a mesma coisa de descompressao de dados.
    #nome, email, faixa, data_nascimento = **aluno_schema.dict()

    if Alunos.objects.filter(email=email).exists():
        raise HttpError(400, 'E-mail já cadastrado')
    
    #Salvando: os dados na model Alunos de maneira simples: aluno = Alunos(**aluno_schema.dict())
    aluno = Alunos(nome=nome,
                   email=email,
                   faixa=faixa,
                   data_nascimento=data_nascimento)
    aluno.save()


    return aluno