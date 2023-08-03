Please read this document prior to working on JIRA API to POWER BI

There are instalations required to work on this please copy and paste individual lines into the terminal and run:

    pip install pandas
    pip install jira
    python -m pip install jupyter


The 2 Jupyter notebooks in this folder enable easy use of the rest of the files, and save the data in casche so you do not need to execute each file if you want to manipulate the data afterwards:


    LoadAndSaveAllData.ipnb:

        This notebook does not need to be executed but contains the code to run all of the python files described below.

    LoadSavedData.ipnb:

        This notebook is the key for execution. It runs LoadAndSaveAllData.ipnb so you work on the data, and then has a few lines to show how to display the data.




There are 4 python files contained in this folder which are required for execution:


    jira_connection_config.py:

        This file is for the config of the API connection, you need to enter 'project key' this is the JIRA project you want to grab the data from

        The server variable should be the same across all Hiscox JIRA projects

        For the AUTHORISATION, enter your email, and API KEY within the highlighted brackets, for example:

            jira = JIRA(options, basic_auth=('EMAIL', 'API KEY'))

        After these have been entered, just save the python file and you can leave it like that unless done incorrectly.


    mainGetIssues.py:

        This python file is the main execution to get the main fields and the data along with it from the JIRA project specified. 

        If the config file has been setup correctly, you should be able to run this, and the data will be grabbed.

        If you would like to see this data, uncomment the last 2 lines of code which involve a print.

    mainCustomFields.py:

        This python fie is also another execution to get all of the custom fields associated with the JIRA project specified.

        I have written a mapping so that the field names are not just the IDS and you can fully understand what the data is.


    get_custom_fields.py:

        This is a support file for the mainCustomFields.py file. Executing this code, returns all of the custom field IDs and the names of those fields.

        This is a crucial file to enable the mapping of custom field IDS to custom field names in the execution of the mainCustomFields.py file