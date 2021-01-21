from behave import given, when, then
from Utilities.ConfigReader import configReader
from Utilities.jsonDataProvider import jsonPayLoad


@given(u'user has resource url and issueId')
def step_impl(context):
    uri = configReader.getURL()

    context.issueKey = configReader.getIssueKey()

    context.url = uri + context.issueKey


@given(u'user has resource uri and json payload')
def step_impl(context):
    context.url = configReader.getURL()

    context.jsonBody = jsonPayLoad()


@when(u'user hit "{request}" request to resource server')
def step_impl(context, request):
    if request == 'GET':

        context.response = context.sc.get(context.url)

    elif request == 'POST':

        context.response = context.sc.post(context.url, json=context.jsonBody)


@then(u'user should get response body with status code "{statusCode}"')
def step_impl(context, statusCode):
    assert str(context.response.status_code) == statusCode


@then(u'response body should contain "{key}" and "{Id}"')
def step_impl(context, key, Id):
    response_text = context.response.text

    json_response = context.response.json()

    context.response_key = json_response['key']

    context.response_id = json_response['id']

    assert key in response_text


@then(u'response key and id should match with request key and id')
def step_impl(context):

    assert context.response_key == context.issueKey

    assert configReader.getIssueId() == context.response_id
