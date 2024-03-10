from flask import jsonify


class HistoricoView:
    @staticmethod
    def listar_historico(historico):
        return jsonify(historico)

    @staticmethod
    def adicionar_historico(registro):
        return jsonify(registro), 201

    @staticmethod
    def atualizar_historico(registro):
        if registro:
            return jsonify(registro)
        else:
            return jsonify({'message': 'Registro no histórico não encontrado'}), 404

    @staticmethod
    def remover_historico(registro):
        if registro:
            return jsonify(registro)
        else:
            return jsonify({'message': 'Registro no histórico não encontrado'}), 404

    @staticmethod
    def calcular_media_por_disciplina(media_por_disciplina):
        return jsonify(media_por_disciplina)

    @staticmethod
    def contar_reprovacoes_aluno(num_reprovacoes):
        return jsonify({'num_reprovacoes': num_reprovacoes})

    @staticmethod
    def contar_reprovacoes_disciplina(num_reprovacoes):
        return jsonify({'num_reprovacoes': num_reprovacoes})

    @staticmethod
    def contar_disciplinas_cursadas(disciplinas_cursadas):
        return jsonify({'disciplinas_cursadas': disciplinas_cursadas})

    @staticmethod
    def contar_disciplinas_nao_cursadas(disciplinas_nao_cursadas):
        return jsonify({'disciplinas_nao_cursadas': disciplinas_nao_cursadas})

    @staticmethod
    def contar_disciplinas_que_mais_reprovam(disciplinas_que_mais_reprovam):
        return jsonify({'disciplinas_que_mais_reprovam': disciplinas_que_mais_reprovam})

    @staticmethod
    def contar_medias_por_aluno(medias_por_aluno):
        response_data = {'medias_por_aluno': medias_por_aluno}
        return jsonify(response_data)

    @staticmethod
    def media_geral(media_geral):
        response_data = {'media_geral_disciplinas': media_geral}
        return jsonify(response_data)

    @staticmethod
    def contar_medias_por_aluno(medias_por_aluno):
        response_data = {'medias_por_aluno': medias_por_aluno}
        return jsonify(response_data)

    @staticmethod
    def reprovacoes_por_disciplina(reprovacoes_por_disciplina):
        response_data = {'reprovacoes_por_disciplina': reprovacoes_por_disciplina}
        return jsonify(response_data)

    @staticmethod
    def reprovacoes_total(reprovacoes_total):
        response_data = {'reprovacoes_total': reprovacoes_total}
        return jsonify(response_data)
