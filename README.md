# GitFlow
A little explanation of the git flow of the project:

|Branch|Description
|-----|------------
|**develop**| is the main branch where developer merge features
|*feature*| _branched from develop_ is opened by developer for each feature in backlog and takes the name of the feature
|**release**| is the branch for production
|**master** | follow release branch with tag
|*hotfixing*| _branched from master_ is the branch where we fix bugs and at the end merge to develop branch and master branch with tag


- PS:'To developer' - please follow fabfile to contribute


## Requirements
- Docker
- docker-compose

### Docker build images and run
```bash
$ docker-compose build
$ docker-compose up
```

### Create database
```bash
$ docker-compose exec web python manage.py makemigrations
$ docker-compose exec web python manage.py migrate
```

### Create superuser
```bash
$ docker-compose exec web python manage.py createsuperuser
```


"Yeah, it's alive visit http://localhost:8000/, enjoy! Feel free to contact me in pvt"