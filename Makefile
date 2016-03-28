migrate:
	python photogram/manage.py makemigrations posts users
	python photogram/manage.py migrate

shell:
	python photogram/manage.py shell_plus
