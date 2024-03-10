from sqlalchemy import create_engine, text
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)


class DisciplinaModel:
    @staticmethod
    def listar_disciplinas():
        with engine.connect() as conn:
            query = text('SELECT * FROM disciplina;')
            response = conn.execute(query)
            column_names = response.keys()
            disciplinas = [dict(zip(column_names, row)) for row in response]
        return disciplinas

    @staticmethod
    def obter_disciplina(disciplina_id):
        with engine.connect() as conn:
            query = text('SELECT * FROM disciplina WHERE id = :disciplina_id;')
            response = conn.execute(query, {'disciplina_id': disciplina_id})
            disciplina = response.fetchone()
            if disciplina:
                column_names = response.keys()
                disciplina_dict = dict(zip(column_names, disciplina))
                return disciplina_dict
            else:
                return None

    @staticmethod
    def adicionar_disciplina(nova_disciplina):
        query = text('INSERT INTO disciplina (tipo, nome, credito, codigo, carga_horaria) '
                     'VALUES (:tipo, :nome, :credito, :codigo, :carga_horaria) RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'tipo': nova_disciplina.get('tipo'), 'nome': nova_disciplina.get('nome'),
                                            'credito': nova_disciplina.get('credito'),
                                            'codigo': nova_disciplina.get('codigo'),
                                            'carga_horaria': nova_disciplina.get('carga_horaria')})
            nova_disciplina_inserida = response.fetchone()
            conn.commit()
        column_names = response.keys()
        disciplina_dict = dict(zip(column_names, nova_disciplina_inserida))
        return disciplina_dict

    @staticmethod
    def atualizar_disciplina(disciplina_id, disciplina_atualizada):
        query = text('UPDATE disciplina SET tipo = :tipo, nome = :nome, credito = :credito, '
                     'carga_horaria = :carga_horaria WHERE id = :disciplina_id RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'tipo': disciplina_atualizada.get('tipo'),
                                            'nome': disciplina_atualizada.get('nome'),
                                            'credito': disciplina_atualizada.get('credito'),
                                            'carga_horaria': disciplina_atualizada.get('carga_horaria'),
                                            'disciplina_id': disciplina_id})
            disciplina_atualizada = response.fetchone()
            conn.commit()
        if disciplina_atualizada:
            column_names = response.keys()
            disciplina_dict = dict(zip(column_names, disciplina_atualizada))
            return disciplina_dict
        else:
            return None

    @staticmethod
    def remover_disciplina(disciplina_id):
        query = text('DELETE FROM disciplina WHERE id = :disciplina_id RETURNING *;')
        with engine.connect() as conn:
            response = conn.execute(query, {'disciplina_id': disciplina_id})
            disciplina_removida = response.fetchone()
            conn.commit()
        if disciplina_removida:
            column_names = response.keys()
            disciplina_dict = dict(zip(column_names, disciplina_removida))
            return disciplina_dict
        else:
            return None

    @staticmethod
    def quantidade_de_alunos_matriculados_por_cadeira(disciplina_id):
        with engine.connect() as conn:
            query = text('''
                            SELECT COUNT(*) AS numero_de_alunos
                            FROM historico
                            WHERE id_disciplina = :disciplina_id
                            AND status = 5;
                            ''')
            response = conn.execute(query, {'disciplina_id': disciplina_id})
            column_names = response.keys()
            alunos_matriculados = [dict(zip(column_names, row)) for row in response]
        return alunos_matriculados
