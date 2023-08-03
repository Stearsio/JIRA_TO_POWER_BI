import jira_connection_config

import pandas as pd


def all_custom_fields():
    #connect to JIRA
    jira = jira_connection_config.connect_to_jira()

    #Get project key from 'jira_connection'
    project_key = jira_connection_config.proj_key




    custom_fields = []
    start_at = 0
    page_size = 50


    #get custom fields with pagination
    while True:
        fields = jira.fields()

        for field in fields:
            if field['custom']:
                custom_fields.append([field['id'], field['name']])
        
        start_at += page_size

        if start_at >= page_size:
            break

    headers = ["field_id", "field_name"]

    custom_fields_data = pd.DataFrame(custom_fields, columns=headers)

    return custom_fields_data 
    #print(custom_fields_data)

#if __name__ == "__main__":
   # all_custom_fields()