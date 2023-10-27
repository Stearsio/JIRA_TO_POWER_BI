#This is the config file for the api connection
#Enter details where asked and this is all that needs doing

from jira import JIRA

#Type project Key Here
proj_key = 'project key'


def connect_to_jira():
    options = {
        'server': 'server'
    }
    #Put your jira account email, and api key in quote marks
    jira = JIRA(options, basic_auth=('email', 'api key'))
    return jira
