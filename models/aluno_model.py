from sqlalchemy import create_engine, text
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)


class AlunoModel:
    @staticmethod
    def listar_alunos():
        with engine.connect() as conn:
            query = text('SELECT * FROM aluno;')
            response = conn.execute(query)
            column_names = response.keys()
            alunos = [dict(zip(column_names, row)) for row in response]
        return alunos

    @staticmethod
    def obter_aluno(aluno_id):
        with engine.connect() as conn:
            query = text('SELECT * FROM aluno WHERE id = :aluno_id;')
            response = conn.execute(query, {'aluno_id': aluno_id})
            aluno = response.fetchone()
            if aluno:
                column_names = response.keys()
                aluno_dict = dict(zip(column_names, aluno))
                return aluno_dict
            else:
                return None

    @staticmethod
    def adicionar_aluno(novo_aluno):
        query = text('INSERT INTO aluno (nome, cpf, arg_class, ano_entrada) '
                     'VALUES (:nome, :cpf, :arg_class, :ano_entrada) RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'nome': novo_aluno.get('nome'), 'cpf': novo_aluno.get('cpf'),
                                            'arg_class': novo_aluno.get('arg_class', None),  # Permitir None
                                            'ano_entrada': novo_aluno.get('ano_entrada')})
            novo_aluno_inserido = response.fetchone()
            conn.commit()

        column_names = response.keys()
        aluno_dict = dict(zip(column_names, novo_aluno_inserido))
        return aluno_dict

    @staticmethod
    def atualizar_aluno(aluno_id, aluno_atualizado):
        query = text('UPDATE aluno SET nome = :nome, cpf = :cpf, arg_class = :arg_class, '
                     'ano_entrada = :ano_entrada WHERE id = :aluno_id RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'nome': aluno_atualizado.get('nome'), 'cpf': aluno_atualizado.get('cpf'),
                                            'arg_class': aluno_atualizado.get('arg_class'),
                                            'ano_entrada': aluno_atualizado.get('ano_entrada'),
                                            'aluno_id': aluno_id})
            aluno_atualizado = response.fetchone()
            conn.commit()
        if aluno_atualizado:
            column_names = response.keys()
            aluno_dict = dict(zip(column_names, aluno_atualizado))
            return aluno_dict
        else:
            return None

    @staticmethod
    def remover_aluno(aluno_id):
        query = text('DELETE FROM aluno WHERE id = :aluno_id RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'aluno_id': aluno_id})
            aluno_removido = response.fetchone()
            conn.commit()
        if aluno_removido:
            column_names = response.keys()
            aluno_dict = dict(zip(column_names, aluno_removido))
            return aluno_dict
        else:
            return None

    @staticmethod
    def listar_alunos_matriculados():
        with engine.connect() as conn:
            query = text('SELECT * FROM aluno WHERE id IN (SELECT id_aluno FROM historico);')
            response = conn.execute(query)
            column_names = response.keys()
            alunos_matriculados = [dict(zip(column_names, row)) for row in response]
        return alunos_matriculados

    @staticmethod
    def listar_alunos_formacao_periodo_certo():
        with engine.connect() as conn:
            query = text('SELECT * FROM aluno '
                         'WHERE id IN ('
                         '    SELECT id_aluno FROM historico '
                         '    JOIN aluno ON historico.id_aluno = aluno.id '
                         '    GROUP BY id_aluno, aluno.ano_entrada '
                         '    HAVING COUNT(DISTINCT historico.ano) >= (aluno.ano_entrada + 4)'
                         ');')
            response = conn.execute(query)
            column_names = response.keys()
            alunos_formacao_periodo_certo = [dict(zip(column_names, row)) for row in response]
        return alunos_formacao_periodo_certo
