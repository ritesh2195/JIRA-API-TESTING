import requests


def before_scenario(context, scenario):
    sc = requests.Session()

    sc.auth = ('user', 'APIKEY')

    sc.headers.update({'Content-Type': 'application/json'})

    context.sc = sc


def after_scenario(context, scenario):

    if 'post' in scenario.tags:

        context.sc.delete(context.url + context.response_id)
