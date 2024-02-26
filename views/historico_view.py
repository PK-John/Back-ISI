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
