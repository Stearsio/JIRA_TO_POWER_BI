#This is the config file for the api connection
#Enter details where asked and this is all that needs doing

from jira import JIRA

#Type project Key Here
proj_key = 'DWPPT'


def connect_to_jira():
    options = {
        'server': 'https://hiscox.atlassian.net'
    }
    #Put your jira account email, and api key in quote marks
    jira = JIRA(options, basic_auth=('sam.stears@hiscox.com', 'ATATT3xFfGF0Q_KWS91lhvpiAY79ocvpcnP4JjTKVRAuCDLWvFS71SArFgwEhtQ19RosPysRa77g2aa6UX8gkOqs8ROP7CdwfVqp3780z9TJ2rRyk1fY3QiwROrT2DxGCxVqMhhZz7j9-NX-xl98AhgDwqabjWWgvrUu6dF-DSn9liHGxyoCabI=0DF99352'))
    return jira