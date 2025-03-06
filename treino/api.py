from ninja import Router
from ninja.errors import HttpError
from .models import Alunos
from typing import List

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

@treino_router.get('/aluno', response=List[AlunosSchema])
def listar_alunos(request):
    alunos = Alunos.objects.all()
    return alunos

@treino_router.get('/aluno/{id}', response=AlunosSchema)
def obter_aluno(request, id:int):
    try:
        aluno = Alunos.objects.get(id=id)
        return aluno
    except Alunos.DoesNotExist:
        raise HttpError(404, "Aluno não encontrado")
    
@treino_router.put('/aluno/{id}', response=AlunosSchema)
def editar_aluno(request, id: int, aluno_schema: AlunosSchema):
    try:
        aluno = Alunos.objects.get(id=id)
        for attr, value in aluno_schema.dict().items():
            setattr(aluno, attr, value)  # Atualiza cada campo do objeto
        aluno.save()
        return aluno
    except Alunos.DoesNotExist:
        raise HttpError(404, "Aluno não encontrado")

@treino_router.delete('/aluno/{id}', response={204: None})
def excluir_aluno(request, id: int):
    try:
        aluno = Alunos.objects.get(id=id)
        aluno.delete()
        return 204, None  # Retorna status 204 (No Content)
    except Alunos.DoesNotExist:
        raise HttpError(404, "Aluno não encontrado")