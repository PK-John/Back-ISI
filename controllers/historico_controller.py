from flask import request
from models.historico_model import HistoricoModel
from views.historico_view import HistoricoView


class HistoricoController:
    @staticmethod
    def listar_historico(aluno_id):
        historico = HistoricoModel.listar_historico(aluno_id)
        return HistoricoView.listar_historico(historico)

    @staticmethod
    def adicionar_historico():
        novo_registro = request.get_json()
        registro = HistoricoModel.adicionar_historico(novo_registro)
        return HistoricoView.adicionar_historico(registro)

    @staticmethod
    def atualizar_historico(aluno_id, disciplina_id, ano, semestre):
        registro_atualizado = request.get_json()
        registro = HistoricoModel.atualizar_historico(aluno_id, disciplina_id, ano, semestre, registro_atualizado)
        return HistoricoView.atualizar_historico(registro)

    @staticmethod
    def remover_historico(aluno_id, disciplina_id, ano, semestre):
        registro = HistoricoModel.remover_historico(aluno_id, disciplina_id, ano, semestre)
        return HistoricoView.remover_historico(registro)

    @staticmethod
    def calcular_media_por_disciplina():
        media_por_disciplina = HistoricoModel.calcular_media_por_disciplina()
        return HistoricoView.calcular_media_por_disciplina(media_por_disciplina)

    @staticmethod
    def contar_reprovacoes_aluno(aluno_id):
        reprovacoes_aluno = HistoricoModel.contar_reprovacoes_aluno(aluno_id)
        return HistoricoView.contar_reprovacoes_aluno(reprovacoes_aluno)

    @staticmethod
    def contar_reprovacoes_disciplina(disciplina_id):
        reprovacoes_disciplina = HistoricoModel.contar_reprovacoes_disciplina(disciplina_id)
        return HistoricoView.contar_reprovacoes_disciplina(reprovacoes_disciplina)

    @staticmethod
    def contar_disciplinas_cursadas(aluno_id):
        disciplinas_cursadas = HistoricoModel.contar_disciplinas_cursadas(aluno_id)
        return HistoricoView.contar_disciplinas_cursadas(disciplinas_cursadas)

    @staticmethod
    def contar_disciplinas_nao_cursadas(aluno_id):
        disciplinas_nao_cursadas = HistoricoModel.contar_disciplinas_nao_cursadas(aluno_id)
        return HistoricoView.contar_disciplinas_nao_cursadas(disciplinas_nao_cursadas)


    @staticmethod
    def contar_disciplinas_que_mais_reprovam():
        disciplinas_que_mais_reprovam = HistoricoModel.contar_disciplinas_que_mais_reprovam()
        return HistoricoView.contar_disciplinas_que_mais_reprovam(disciplinas_que_mais_reprovam)

    @staticmethod
    def contar_medias_por_aluno(aluno_id):
        medias_por_aluno = HistoricoModel.contar_medias_por_aluno(aluno_id)
        return HistoricoView.contar_medias_por_aluno(medias_por_aluno)

    @staticmethod
    def media_geral():
        media_geral = HistoricoModel.media_geral()
        return HistoricoView.media_geral(media_geral)

    @staticmethod
    def reprovacoes_por_disciplina():
        reprovacoes_por_disciplina = HistoricoModel.reprovacoes_por_disciplina()
        return HistoricoView.reprovacoes_por_disciplina(reprovacoes_por_disciplina)

    @staticmethod
    def reprovacoes_total():
        reprovacoes_total = HistoricoModel.reprovacoes_total()
        return HistoricoView.reprovacoes_total(reprovacoes_total)
