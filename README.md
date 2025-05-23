# Collapsible Sidebar Using Bootstrap for Django

*Collapsible Sidebar Using Bootstrap* is a base template with a bootstrap simple
customization in self-hosted mode (non-CDN).

Features:

- Bootstrap 5.3
- Django 4
- Included demo at [example folder](example)
- Templates included:
  - bootstrap_base.html
  - snippets/show_err.html
  - snippets/show_messages.html
- Templates overridden:
  - registration/login.html
  - registration/password_change_form.html
  - 403.html
  - 404.html
  - 500.html
- Bootstrap customization available at bootstrap-theme directory.
- Custom font from google-fonts in local static files.

Bootstrap theme and fonts are customizable using scripts included. See details
[bellow](#customize-bootstrap-theme).

## Testing templates with example/demo

An example is included in the [example folder](example) with a Makefile to
initialize the project and preview the templates. More details in 
[example/README](example/README.md)

## Template preview

![Frontpage preview](doc/front-page.png)

![Secondary page preview](doc/secondary-page.png)


## Installation

The preferred way to install is via pip

    pip3 install django-bootstrap-sidebar

but you can install in develop mode cloning this repo but static files are not
included in the repo. See *Customize bootstrap theme section* for details.

After installing your Django instance in `settings.py`, add `bootstrapsidebar`
before `django.contrib.auth` since some auth templates are overridden.

```python
INSTALLED_APPS = [
    'bootstrapsidebar'
    'django.contrib.auth',
    ...
]
```

## Blocks available in page layout

The base template (`bootstrap_base.html`) includes the following hierarchical
blocks:

- *block custom-css*
- *block head*
- *block page-wrapper*: to override full page, included sidebar.
  - *block sidebar*
  - *block navbar*: to override top navbar
    - *navbar-links*: only to add links in default template navbar.
  - *block messages*: by default this block uses `snippets/show_messages.html`
  - *block content*
  - *block footer*
- *block after-bootstrap-js*: used to run extra javascript like to enable
   Bootstrap Popovers. [See below details](#enable-bootstrap-popovers)

The `registration/login.html` is an example of page using base-template without
sidebar.

## Customize bootstrap theme

Install the package in dev mode is recommended if you want to customize the
Bootstrap Theme. First clone this repo and install in dev mode:

    pip install -e ./django-bootstrap-sidebar

Bootstrap static files and fonts are not included in the repo. They are
generated/downloaded with the commands of makefile but the *node* environment
and `npm` are required.

Bootstrap can be customized at file `bootstrap-theme/custom.scss`. An easy way
to create a new customization is some online theme builder
like <https://bootstrap.build/> and download the *custom.scss*.

To generate/upgrade static files makefile automates the process, run make:

    make

## Enable Bootstrap Popovers

Due performance reasons popovers are not default enabled. One way is to enable
popovers everywhere, which requires an extra javascript after the Bootstrap
javascript. The last solution is not optimal, but it is a simple way, a detailed
instructions are available at [Bootstrap
Popovers](https://getbootstrap.com/docs/5.2/components/popovers/)

The block `after-bootstrap-js` is intended  to enable popovers and
the following code snippet from Bootstrap can be used:

```html
{% block after-bootstrap-js %}
<script>
const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]')
const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl))
</script>
{% endblock %}
```

A full example is included in the example folder in page  
[popovers.html](example/app/templates/popovers.html)

## License

The project is licensed under the Apache 2.0 license.

## Author

Developed and maintained by Paulino Ruiz de Clavijo Vázquez <pruiz@us.es>