from flask import request
from models.aluno_model import AlunoModel
from views.aluno_view import AlunoView


class AlunoController:
    @staticmethod
    def listar_alunos():
        alunos = AlunoModel.listar_alunos()
        return AlunoView.listar_alunos(alunos)

    @staticmethod
    def obter_aluno(aluno_id):
        aluno = AlunoModel.obter_aluno(aluno_id)
        return AlunoView.obter_aluno(aluno)

    @staticmethod
    def adicionar_aluno():
        novo_aluno = request.get_json()
        novo_aluno['arg_class'] = novo_aluno.get('arg_class', 80)
        aluno = AlunoModel.adicionar_aluno(novo_aluno)
        return AlunoView.adicionar_aluno(aluno)

    @staticmethod
    def atualizar_aluno(aluno_id):
        aluno_atualizado = request.get_json()
        aluno = AlunoModel.atualizar_aluno(aluno_id, aluno_atualizado)
        return AlunoView.atualizar_aluno(aluno)

    @staticmethod
    def remover_aluno(aluno_id):
        aluno = AlunoModel.remover_aluno(aluno_id)
        return AlunoView.remover_aluno(aluno)

    @staticmethod
    def listar_alunos_matriculados():
        alunos_matriculados = AlunoModel.listar_alunos_matriculados()
        return AlunoView.listar_alunos(alunos_matriculados)

    @staticmethod
    def listar_alunos_formacao_periodo_certo():
        alunos_formacao_periodo_certo = AlunoModel.listar_alunos_formacao_periodo_certo()
        return AlunoView.listar_alunos(alunos_formacao_periodo_certo)
