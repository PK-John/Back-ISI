from flask import jsonify


class DisciplinaView:
    @staticmethod
    def listar_disciplinas(disciplinas):
        return jsonify(disciplinas)

    @staticmethod
    def obter_disciplina(disciplina):
        if disciplina:
            return jsonify(disciplina)
        else:
            return jsonify({'message': 'Disciplina não encontrada'}), 404

    @staticmethod
    def adicionar_disciplina(disciplina):
        return jsonify(disciplina), 201

    @staticmethod
    def atualizar_disciplina(disciplina):
        if disciplina:
            return jsonify(disciplina)
        else:
            return jsonify({'message': 'Disciplina não encontrada'}), 404

    @staticmethod
    def remover_disciplina(disciplina):
        if disciplina:
            return jsonify(disciplina)
        else:
            return jsonify({'message': 'Disciplina não encontrada'}), 404

    @staticmethod
    def quantidade_de_alunos_matriculados_por_cadeira(alunos_matriculados):
        return jsonify({'alunos_matriculados': alunos_matriculados})