# GitFlow
A little explanation of the git flow of the project:

|Branch|Description
|-----|------------
|**develop**| is the main branch where developer merge features
|*feature*| is opened by developer for each feature in backlog and takes the name of the feature
|**release**| is the branch for production
|**master** | follow release branch with tag
|*hotfixing*| is the branch where we fix bugs and at the end merge to develop branch and master branch with tag


## Requirements
- Python 2.7+
- PostgreSQL

```
$ virtualenv venv
$ pip install -r requirements/local/local_requirements.txt
```
