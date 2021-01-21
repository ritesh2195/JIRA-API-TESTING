import configparser

config = configparser.RawConfigParser(allow_no_value=True)

config.read('D:\PYTHON\REST_API_BEHAVE\config\APIDetails.ini')


class configReader:

    @staticmethod
    def getURL():
        return config.get('common', 'url')

    @staticmethod
    def getIssueKey():
        return config.get('common', 'issue_key')

    @staticmethod
    def getIssueId():
        return config.get('common', 'issue_id')

    @staticmethod
    def getDBUser():

        return config.get('SQL', 'user')

    @staticmethod
    def getDBPassword():

        return config.get('SQL', 'password')

    @staticmethod
    def getDBHost():

        return config.get('SQL', 'host')

    @staticmethod
    def getDBName():

        return config.get('SQL', 'database')
