from distutils.core import setup

setup(name='DJ-web-app',
      version='1.0',
      description='Web platform',
      author='mauridb',
      author_email='mauriziocontatto@gmail.com',
      url='https://github.com/mauridb/DJ-web-app.git',
      packages=['django', 'djangorestframework', 'psycopg2', 'django-filter'],
     )