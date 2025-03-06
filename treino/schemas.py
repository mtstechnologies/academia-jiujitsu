from ninja import ModelSchema
from .models import Alunos

class AlunosSchema(ModelSchema):
    """
    Schema para representar o modelo Alunos na API. E para serializar e desserializar objetos do modelo Alunos.

    Utiliza ModelSchema para facilitar a conversão entre instâncias do modelo e formatos estruturados como JSON.

    Atributos:
        model (class): Define o modelo associado ao schema.
        fields (list): Lista de campos do modelo Alunos que serão serializados.

     Exemplo de uso:
        >>> aluno = Alunos(nome="João", email="joao@email.com", faixa="Preta", data_nascimento="2000-05-10")
        >>> schema = AlunosSchema.from_orm(aluno)
        >>> print(schema.dict())
        {'nome': 'João', 'email': 'joao@email.com', 'faixa': 'Preta', 'data_nascimento': '2000-05-10'}

    """
    class Meta:
        model = Alunos
        fields = ['nome', 'email', 'faixa', 'data_nascimento',]