import importlib
from xmlrpc.client import Boolean
# from config import settings
from ..helpers import get_variable_by_pathname, instantiate_class


__search_engine_cache = {}


def get_search_engine_config(alias:str='default'):
    assert alias in settings.SEARCH_ENGINES, f"Não existe um search engine com o nome apelido '{alias}' nas settings"
    return settings.SEARCH_ENGINES[alias]


def dsl_connection(alias:str='default'):
    se_config = get_search_engine_config(alias)

    dsl_connections = get_variable_by_pathname(se_config['dsl_engine'])
    if alias not in dsl_connections._conns:
        dsl_connections.add_connection(alias, search_engine(alias))
    # dsl_connections.create_connection(
    #     alias=alias,
    #     http_auth=(se_config['user'], se_config['password']), 
    #     **{k:v for k,v in se_config.items() if k not in ('user', 'password', 'engine', 'dsl_engine')},
    # )
    return dsl_connections.get_connection(alias)
    
    
def search_engine(alias:str='default'):
    assert alias in settings.SEARCH_ENGINES, f"Não existe um search engine com o nome apelido '{alias}' nas settings"
    se_config = settings.SEARCH_ENGINES[alias]

    if alias not in __search_engine_cache:
        engine = se_config['engine']
        params = {k:v for k,v in se_config.items() if k not in ('username', 'password', 'engine', 'dsl_engine', 'hosts')}
        client = instantiate_class(engine, se_config['hosts'].split(','), http_auth=(se_config['username'], se_config['password']), **params)
        __search_engine_cache[alias] = client
    return __search_engine_cache[alias]


def create_index_if_not_exists(index_name: str) -> bool:
    """ Cria um índice caso não exista. Retorna True se criou e False se não criou.

    Args:
        index_name (str): nome do índice a ser criado

    Raises:
        exception: Erro conforme retornado pelo Search Engine.

    Returns:
        bool: True se criou. False se não criou.
    """
    try:
        search_engine().indices.create(index_name, body={})
        return True
    except Exception as e:
        if hasattr(e, 'error') and e.error == 'resource_already_exists_exception':
            return False
        raise e


def query(index_name: str, query_string: str, fields: list, alias="default") -> tuple:
    response = search_engine(alias).search(
        index = index_name,
        body = {
            'size': 5,
            'query': {
                'multi_match': {
                    'query': query_string,
                    'fields': fields
                }
            }
        }
    )
    return response['hits']['hits'], response['hits']['total']['value']


def search(index_name: str, body: dict, alias="default") -> tuple:
    response = search_engine(alias).search(
        index = index_name,
        body = body
    )
    return response['hits']['hits'], response['hits']['total']['value']


def index(index_name: str, body: str, id=None, params=None, headers=None, alias:str="default") -> tuple:
    response = search_engine(alias).index(
        index = index_name,
        body = body,
        id=id, 
        params=params, 
        headers=headers
    )
    return response['hits']['hits'], response['hits']['total']['value']


def search_engine_healthy(alias:str='default'):
    p = search_engine(alias).ping()
    return p != False
