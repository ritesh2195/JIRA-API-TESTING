import requests


def before_scenario(context, scenario):
    sc = requests.Session()

    sc.auth = ('riteshranjanmishra938@gmail.com', '5W4ViEe5qcxoviSN5IDY3B09')

    sc.headers.update({'Content-Type': 'application/json'})

    context.sc = sc


def after_scenario(context, scenario):

    if 'post' in scenario.tags:

        context.sc.delete(context.url + context.response_id)
