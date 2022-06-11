Implementing Full Text Serach with Django and Postgres


## Run Locally
     1. Clone the repository:
            git clone https://github.com/thesaintraphael/django-search.git
     
     2. Up docker:
            docker-compose up -d --build
     
     3. Migrate db: 
            docker-compose exec web python manage.py migrate

     4. Add 10k (chnage amount from the command if you want) quotes to db: 
            docker-compose exec web python manage.py add_quotes


## Used Resources
   1. [Django doc](https://docs.djangoproject.com/en/3.2/topics/db/search/#postgresql-support) 
   2. [DjangoCon US](https://www.youtube.com/watch?v=is3R8d420D4)
   3. [testdriven.io](https://testdriven.io/blog/django-search/)