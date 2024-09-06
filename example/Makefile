
.PHONY: run init clean
PYBIN = venv/bin/python

run:
	# Insecure is required to serve static files and view error pages in the demo
	$(PYBIN) manage.py runserver --insecure

init:
	[ -d 'venv' ] ||  python3 -m venv venv
	$(PYBIN) -m pip install -r requirements.txt
	$(PYBIN) manage.py migrate
	$(PYBIN) manage.py create1234superuser
	@printf "\nYou can now run 'make run' to start the server and login with user 'admin' and password '1234'\n"

# Util to generate about.html from README.md
app/templates/about.html: README.md
	@echo "{% extends 'demo_base.html' %}\n{% block content %}\n" > $@
	pandoc -f markdown -t html $< >> $@
	@echo "\n{% endblock %}" >> $@

clean:
	rm -rf venv db.sqlite3
