from flask import jsonify


class AlunoView:
    @staticmethod
    def listar_alunos(alunos):
        return jsonify(alunos)

    @staticmethod
    def obter_aluno(aluno):
        if aluno:
            return jsonify(aluno)
        else:
            return jsonify({'message': 'Aluno não encontrado'}), 404

    @staticmethod
    def adicionar_aluno(aluno):
        return jsonify(aluno), 201

    @staticmethod
    def atualizar_aluno(aluno):
        if aluno:
            return jsonify(aluno)
        else:
            return jsonify({'message': 'Aluno não encontrado'}), 404

    @staticmethod
    def remover_aluno(aluno):
        if aluno:
            return jsonify(aluno)
        else:
            return jsonify({'message': 'Aluno não encontrado'}), 404

    @staticmethod
    def listar_alunos_matriculados(alunos):
        return jsonify(alunos)

    @staticmethod
    def listar_alunos_formacao_periodo_certo(alunos):
        return jsonify(alunos)
