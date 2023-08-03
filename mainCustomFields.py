import jira_connection_config
import pandas as pd
import get_custom_fields


def customIssues():
    jira = jira_connection_config.connect_to_jira()

    #Get project key from 'jira_connection'
    project_key = jira_connection_config.proj_key

    #pagination
    start_at = 0
    page_size = 50
    

    columns = ['Key']

    issue_data = []

    custom_field_names = set()


    #get all issues in project
    while True:
        issues = jira.search_issues(f'project={project_key}', startAt=start_at, maxResults=page_size)

        if not issues:
            break

        for issue in issues:
            
            issue_dict = {
                "Key": issue.key,
            }

            custom_fields = issue.raw['fields']
            for field_name, field_value in custom_fields.items():
                if field_name not in issue_dict:
                    issue_dict[field_name] = field_value
                    custom_field_names.add(field_name)


            issue_data.append(issue_dict)
        
        start_at += page_size
        #print(f"Issues recieved so far: {len(issue_data)}")
        

    df_issues = pd.DataFrame(issue_data)

    custom_field_columns = list(custom_field_names)
    ordered_columns = columns + custom_field_columns
    df_issues = df_issues.reindex(columns=ordered_columns)


    customFields = get_custom_fields.all_custom_fields()

    field_id_to_name = customFields.set_index('field_id')['field_name']
    df_issues.columns = df_issues.columns.map(field_id_to_name)

   
    return df_issues

