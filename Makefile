migrate:
	python photogram/manage.py makemigrations posts users tags
	python photogram/manage.py migrate

shell:
	python photogram/manage.py shell_plus
