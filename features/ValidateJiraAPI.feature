Feature: Validating Jira API

  @get
  Scenario: validating GET Jira API

    Given user has resource url and issueId
    When user hit "GET" request to resource server
    Then user should get response body with status code "200"
    And response body should contain "key" and "id"
    And response key and id should match with request key and id

  @post
  Scenario: validating POST Jira request
    Given user has resource uri and json payload
    When user hit "POST" request to resource server
    Then user should get response body with status code "201"
    And response body should contain "key" and "id"
