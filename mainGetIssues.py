import jira_connection_config
import pandas as pd


#The following code gets some predefined fields from Jira and then every field follows

def mainIssues():
    #connect to JIRA
    jira = jira_connection_config.connect_to_jira()

    #Get project key from 'jira_connection'
    project_key = jira_connection_config.proj_key

    #pagination
    start_at = 0
    page_size = 50
    issue_data = []

    #total_issues = jira.search_issues(f'project={project_key}', startAt=start_at, maxResults=0).total
    #print(f"Total number of issues:{total_issues}")

    #get all issues in project
    while True:
    
        issues = jira.search_issues(f'project={project_key}', startAt=start_at, maxResults=page_size)

        if not issues:
            break


        for issue in issues:
            
            epic_link = issue.fields.customfield_10008
            epic_name = None

            if epic_link:
                epic = jira.issue(epic_link)
                epic_name = epic.fields.summary
            
            issue_dict = {

                "Key": issue.key,
                "Summary": issue.fields.summary,
                "Assignee": issue.fields.assignee.displayName if issue.fields.assignee else None,
                "Creator": issue.fields.creator.displayName if issue.fields.creator else None,
                "Status": issue.fields.status.name if issue.fields.status else None,
                "Epic Name": epic_name,
                "Epic Link": epic_link,
                "Due Date": issue.fields.duedate if issue.fields.duedate else None,
                "Priority": issue.fields.priority if issue.fields.priority else None,
                "Issue Type":issue.fields.issuetype.name,     
                "Resolution date": issue.fields.resolutiondate if issue.fields.resolutiondate else None, 
                "Resolution": issue.fields.resolution if issue.fields.resolution else None, 
                "Subtasks": [subtask.key for subtask in issue.fields.subtasks],
                "Labels": issue.fields.labels if issue.fields.labels else None
            }

            
            issue_data.append(issue_dict)

        start_at += page_size
        #print(f"Issues recieved so far: {len(issue_data)}")
        

    df_issues = pd.DataFrame(issue_data)
    return df_issues

#df = mainIssues()
#print(df)