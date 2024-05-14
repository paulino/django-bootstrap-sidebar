# Example Project for django-bootstrap-sidebar

This example contains a simple Django project with a sidebar menu using the
`django-bootstrap-sidebar` package. The demo includes:

- Several pages with a sidebar menu that tracks the current page
- A login form demo
- A password reset form demo
- Default pages for errors 500, 403, and 404
- Popovers

## Running the Example

The following command automates the setup of the project and creates an `admin`
user with the password `1234`:

    make init

This command creates a Python *virtualenv* in the *venv* directory, installs the
requirements, and sets up Django with an admin user. Upon success, you can to
run the server with:

    make run

The server should be available at http://127.0.0.1:8000/

## Sidebar Menu Tracking

The example also tracks the current page using a context variable in the
template called `sidebar_active`. This variable is used to highlight the current
page using the `active` Bootstrap class.