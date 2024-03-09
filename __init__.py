from flask import Flask
from flask_cors import CORS
from controllers.aluno_controller import AlunoController
from controllers.disciplina_controller import DisciplinaController
from controllers.historico_controller import HistoricoController


def create_app():
    app = Flask(__name__)
    CORS(app)

    # Operação READ - Listar todos os alunos
    @app.route('/alunos', methods=['GET'])
    def listar_alunos():
        return AlunoController.listar_alunos()

    # Operação READ - Obter detalhes de um aluno específico
    @app.route('/alunos/<int:aluno_id>', methods=['GET'])
    def obter_aluno(aluno_id):
        return AlunoController.obter_aluno(aluno_id)

    # Operação CREATE - Adicionar um novo aluno
    @app.route('/alunos', methods=['POST'])
    def adicionar_aluno():
        return AlunoController.adicionar_aluno()

    # Operação UPDATE - Atualizar informações de um aluno
    @app.route('/alunos/<int:aluno_id>', methods=['PUT'])
    def atualizar_aluno(aluno_id):
        return AlunoController.atualizar_aluno(aluno_id)

    # Operação DELETE - Remover um aluno
    @app.route('/alunos/<int:aluno_id>', methods=['DELETE'])
    def remover_aluno(aluno_id):
        return AlunoController.remover_aluno(aluno_id)

    # Operação READ - Listar todas as disciplinas
    @app.route('/disciplinas', methods=['GET'])
    def listar_disciplinas():
        return DisciplinaController.listar_disciplinas()

    # Operação READ - Obter detalhes de uma disciplina específica
    @app.route('/disciplinas/<int:disciplina_id>', methods=['GET'])
    def obter_disciplina(disciplina_id):
        return DisciplinaController.obter_disciplina(disciplina_id)

    # Operação CREATE - Adicionar uma nova disciplina
    @app.route('/disciplinas', methods=['POST'])
    def adicionar_disciplina():
        return DisciplinaController.adicionar_disciplina()

    # Operação UPDATE - Atualizar informações de uma disciplina
    @app.route('/disciplinas/<int:disciplina_id>', methods=['PUT'])
    def atualizar_disciplina(disciplina_id):
        return DisciplinaController.atualizar_disciplina(disciplina_id)

    # Operação DELETE - Remover uma disciplina
    @app.route('/disciplinas/<int:disciplina_id>', methods=['DELETE'])
    def remover_disciplina(disciplina_id):
        return DisciplinaController.remover_disciplina(disciplina_id)

    # Operação READ - Listar histórico de um aluno
    @app.route('/historico/<int:aluno_id>', methods=['GET'])
    def listar_historico(aluno_id):
        return HistoricoController.listar_historico(aluno_id)

    # Operação CREATE - Adicionar um registro ao histórico
    @app.route('/historico', methods=['POST'])
    def adicionar_historico():
        return HistoricoController.adicionar_historico()

    # Operação UPDATE - Atualizar um registro no histórico
    @app.route('/historico/<int:aluno_id>/<int:disciplina_id>/<int:ano>/<int:semestre>', methods=['PUT'])
    def atualizar_historico(aluno_id, disciplina_id, ano, semestre):
        return HistoricoController.atualizar_historico(aluno_id, disciplina_id, ano, semestre)

    # Operação DELETE - Remover um registro do histórico
    @app.route('/historico/<int:aluno_id>/<int:disciplina_id>/<int:ano>/<int:semestre>', methods=['DELETE'])
    def remover_historico(aluno_id, disciplina_id, ano, semestre):
        return HistoricoController.remover_historico(aluno_id, disciplina_id, ano, semestre)

    @app.route('/alunos/matriculados', methods=['GET'])
    def listar_alunos_matriculados():
        return AlunoController.listar_alunos_matriculados()

    @app.route('/historico/media', methods=['GET'])
    def calcular_media_por_disciplina():
        return HistoricoController.calcular_media_por_disciplina()

    # Operação READ - Listar alunos que vão se formar no período certo
    @app.route('/alunos/formacao-periodo-certo', methods=['GET'])
    def listar_alunos_formacao_periodo_certo():
        return AlunoController.listar_alunos_formacao_periodo_certo()

    # Operação READ - Contar reprovações por aluno
    @app.route('/historico/reprovacoes/aluno/<int:aluno_id>', methods=['GET'])
    def contar_reprovacoes_aluno(aluno_id):
        return HistoricoController.contar_reprovacoes_aluno(aluno_id)

    # Operação READ - Contar reprovações por disciplina
    @app.route('/historico/reprovacoes/disciplina/<int:disciplina_id>', methods=['GET'])
    def contar_reprovacoes_disciplina(disciplina_id):
        return HistoricoController.contar_reprovacoes_disciplina(disciplina_id)

    @app.route('/historico/disciplinas-cursadas/<int:aluno_id>', methods=['GET'])
    def contar_disciplinas_cursadas(aluno_id):
        return HistoricoController.contar_disciplinas_cursadas(aluno_id)

    @app.route('/historico/disciplinas-nao-cursadas/<int:aluno_id>', methods=['GET'])
    def contar_disciplinas_nao_cursadas(aluno_id):
        return HistoricoController.contar_disciplinas_nao_cursadas(aluno_id)

    @app.route('/historico/disciplinas-que-mais-reprovam', methods=['GET'])
    def contar_disciplinas_que_mais_reprovam():
        return HistoricoController.contar_disciplinas_que_mais_reprovam()

    return app
