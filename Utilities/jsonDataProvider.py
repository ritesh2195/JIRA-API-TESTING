import json
import requests


class Fields:

    def __init__(self, fields):
        self.fields = fields


class Projects:

    def __init__(self, project, summary, description, issuetype):
        self.project = project

        self.summary = summary

        self.description = description

        self.issuetype = issuetype


class Key:

    def __init__(self, key):
        self.key = key


class Bug:

    def __init__(self, name):
        self.name = name


def jsonPayLoad():

    F = Fields('fields')

    summary = 'REST ye merry gentlemen.'
    description = 'Creating of an issue using project keys and issue type names using the REST API'

    f = F.__dict__

    P = Projects('project', summary, description, 'issuetype')

    p = P.__dict__

    K = Key('BAN')

    k = K.__dict__

    B = Bug('Bug')

    b = B.__dict__

    p['project'] = k

    p['issuetype'] = b

    f['fields'] = p

    json_body = json.dumps(f, indent=4)

    return f


