from sqlalchemy import create_engine, text
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)


class HistoricoModel:
    @staticmethod
    def listar_historico(aluno_id):
        with engine.connect() as conn:
            query = text('SELECT h.*, d.nome as disciplina_nome '
                         'FROM historico h '
                         'JOIN disciplina d ON h.id_disciplina = d.id '
                         'WHERE h.id_aluno = :aluno_id;')
            response = conn.execute(query, {'aluno_id': aluno_id})

            column_names = response.keys()
            historico = [dict(zip(column_names, row)) for row in response]

        return historico

    @staticmethod
    def adicionar_historico(novo_registro):
        query = text('INSERT INTO historico (id_aluno, id_disciplina, status, ano, semestre, nota) '
                     'VALUES (:id_aluno, :id_disciplina, :status, :ano, :semestre, :nota) RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'id_aluno': novo_registro.get('id_aluno'),
                                            'id_disciplina': novo_registro.get('id_disciplina'),
                                            'status': novo_registro.get('status'),
                                            'ano': novo_registro.get('ano'),
                                            'semestre': novo_registro.get('semestre'),
                                            'nota': novo_registro.get('nota')})
            novo_registro_inserido = response.fetchone()
            conn.commit()

        column_names = response.keys()
        registro_dict = dict(zip(column_names, novo_registro_inserido))
        return registro_dict

    @staticmethod
    def atualizar_historico(aluno_id, disciplina_id, ano, semestre, registro_atualizado):
        query = text('UPDATE historico SET status = :status, nota = :nota '
                     'WHERE id_aluno = :aluno_id AND id_disciplina = :disciplina_id AND ano = :ano '
                     'AND semestre = :semestre RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'status': registro_atualizado.get('status'),
                                            'nota': registro_atualizado.get('nota'),
                                            'aluno_id': aluno_id,
                                            'disciplina_id': disciplina_id,
                                            'ano': ano,
                                            'semestre': semestre})

            registro_atualizado = response.fetchone()
            conn.commit()

        if registro_atualizado:
            column_names = response.keys()
            registro_dict = dict(zip(column_names, registro_atualizado))
            return registro_dict
        else:
            return None

    @staticmethod
    def remover_historico(aluno_id, disciplina_id, ano, semestre):
        query = text('DELETE FROM historico WHERE id_aluno = :aluno_id AND id_disciplina = :disciplina_id '
                     'AND ano = :ano AND semestre = :semestre RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'aluno_id': aluno_id,
                                            'disciplina_id': disciplina_id,
                                            'ano': ano,
                                            'semestre': semestre})

            registro_removido = response.fetchone()
            conn.commit()

        if registro_removido:
            column_names = response.keys()
            registro_dict = dict(zip(column_names, registro_removido))
            return registro_dict
        else:
            return None

    @staticmethod
    def calcular_media_por_disciplina():
        with engine.connect() as conn:
            query = text('SELECT id_disciplina, AVG(nota) AS media FROM historico GROUP BY id_disciplina;')
            response = conn.execute(query)
            column_names = response.keys()
            media_por_disciplina = [dict(zip(column_names, row)) for row in response]
        return media_por_disciplina

    @staticmethod
    def contar_reprovacoes_aluno(aluno_id):
        with engine.connect() as conn:
            query = text('SELECT COUNT(*) AS num_reprovacoes FROM historico '
                         'WHERE id_aluno = :aluno_id AND status = 2;')
            response = conn.execute(query, {'aluno_id': aluno_id})
            num_reprovacoes = response.scalar()
        return num_reprovacoes

    @staticmethod
    def contar_reprovacoes_disciplina(disciplina_id):
        with engine.connect() as conn:
            query = text('SELECT COUNT(*) AS num_reprovacoes FROM historico '
                         'WHERE id_disciplina = :disciplina_id AND status IN(3, 4)')
            response = conn.execute(query, {'disciplina_id': disciplina_id})
            num_reprovacoes = response.scalar()
        return num_reprovacoes

    @staticmethod
    def contar_disciplinas_cursadas(aluno_id):
        with engine.connect() as conn:
            query = text('SELECT h.*, d.nome as disciplina_nome '
                         'FROM historico h '
                         'JOIN disciplina d ON h.id_disciplina = d.id '
                         'WHERE h.id_aluno = :aluno_id AND (status = 1 OR status = 2 OR status = 3 OR status = 4);')
            response = conn.execute(query, {'aluno_id': aluno_id})

            column_names = response.keys()
            disciplinas_cursadas = [dict(zip(column_names, row)) for row in response]
        return disciplinas_cursadas

    @staticmethod
    def contar_disciplinas_nao_cursadas(aluno_id):
        with engine.connect() as conn:
            query = text('SELECT h.*, d.nome AS disciplina_nome '
                         'FROM historico h '
                         'JOIN disciplina d ON h.id_disciplina = d.id '
                         'WHERE h.id_aluno = :aluno_id AND (status = 0 OR status = 5 OR status = 6 OR status = 7);')
            response = conn.execute(query, {'aluno_id': aluno_id})
            column_names = response.keys()
            disciplinas_nao_cursadas = [dict(zip(column_names, row)) for row in response]
        return disciplinas_nao_cursadas

    @staticmethod
    def contar_disciplinas_que_mais_reprovam():
        with engine.connect() as conn:
            query = text('''
                SELECT id_disciplina,
                       COUNT(*) AS num_reprovacoes
                FROM historico h
                WHERE status IN (3, 4)
                GROUP BY id_disciplina
                ORDER BY num_reprovacoes DESC
                LIMIT 10;
            ''')
            response = conn.execute(query)
            column_names = response.keys()
            disciplinas_cursadas = [dict(zip(column_names, row)) for row in response]
        return disciplinas_cursadas

    @staticmethod
    def contar_medias_por_aluno(aluno_id):
        with engine.connect() as conn:
            query = text('''
                        SELECT a.nome AS nome_aluno, h.id_disciplina, AVG(h.nota) AS media_nota
                        FROM historico h
                        INNER JOIN aluno a ON h.id_aluno = a.id
                        GROUP BY a.id, a.nome, h.id_disciplina;
                        ''')
            response = conn.execute(query, {'aluno_id': aluno_id})
            column_names = response.keys()
            medias_por_aluno = [dict(zip(column_names, row)) for row in response]
        return medias_por_aluno

    @staticmethod
    def media_geral():
        with engine.connect() as conn:
            query = text('''
                            SELECT AVG(nota) AS media_geral
                            FROM historico;
                            ''')
            response = conn.execute(query)
            column_names = response.keys()
            media_geral = [dict(zip(column_names, row)) for row in response]
        return media_geral

    @staticmethod
    def reprovacoes_por_disciplina():
        with engine.connect() as conn:
            query = text('''
                            SELECT d.nome AS disciplina,
                            COUNT(*) AS numero_reprovacoes
                            FROM historico h
                            JOIN disciplina d ON h.id_disciplina = d.id
                            WHERE h.status IN (3, 4)
                            GROUP BY d.nome;
                            ''')
            response = conn.execute(query)
            column_names = response.keys()
            reprovacoes_por_disciplina = [dict(zip(column_names, row)) for row in response]
        return reprovacoes_por_disciplina

    @staticmethod
    def reprovacoes_total():
        with engine.connect() as conn:
            query = text('''
                            SELECT COUNT(*) AS total_reprovacoes
                            FROM historico
                            WHERE status IN (3, 4)
                        ''')
            response = conn.execute(query)
            column_names = response.keys()
            reprovacoes_total = [dict(zip(column_names, row)) for row in response]
        return reprovacoes_total
