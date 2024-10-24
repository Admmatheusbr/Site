from faker import Faker

FAKE = Faker('pt_BR')

var_num = 0

def cria_livro():
    global var_num
    var_num += 1

    dados = {
        'nome': [FAKE.word()],
        'sigla': 'Bt' + str(var_num),
        'descricao': FAKE.sentence(nb_words=50),
        'data_lanc': FAKE.date_time(),
        'tags': [FAKE.word() for _ in range(5)],
        'responsavel': {
            'nome': FAKE.first_name(),
            'sobrenome': FAKE.last_name(),
        },
        'foto': {
            'url': 'https://loremflickr.com/320/240/python',
        },
    }

    return dados

