from flask import request
from models.disciplina_model import DisciplinaModel
from views.disciplina_view import DisciplinaView


class DisciplinaController:
    @staticmethod
    def listar_disciplinas():
        disciplinas = DisciplinaModel.listar_disciplinas()
        return DisciplinaView.listar_disciplinas(disciplinas)

    @staticmethod
    def obter_disciplina(disciplina_id):
        disciplina = DisciplinaModel.obter_disciplina(disciplina_id)
        return DisciplinaView.obter_disciplina(disciplina)

    @staticmethod
    def adicionar_disciplina():
        nova_disciplina = request.get_json()
        disciplina = DisciplinaModel.adicionar_disciplina(nova_disciplina)
        return DisciplinaView.adicionar_disciplina(disciplina)

    @staticmethod
    def atualizar_disciplina(disciplina_id):
        disciplina_atualizada = request.get_json()
        disciplina = DisciplinaModel.atualizar_disciplina(disciplina_id, disciplina_atualizada)
        return DisciplinaView.atualizar_disciplina(disciplina)

    @staticmethod
    def remover_disciplina(disciplina_id):
        disciplina = DisciplinaModel.remover_disciplina(disciplina_id)
        return DisciplinaView.remover_disciplina(disciplina)

    @staticmethod
    def quantidade_de_alunos_matriculados_por_cadeira(aluno_id):
        alunos_matriculados = DisciplinaModel.quantidade_de_alunos_matriculados_por_cadeira(aluno_id)
        return DisciplinaView.quantidade_de_alunos_matriculados_por_cadeira(alunos_matriculados)
