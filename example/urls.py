from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views

from views import home,popovers, raise_403, raise_exception

urlpatterns = [
    path('admin/', admin.site.urls),

    # Example of views
    path('',home,name='home'),
    path('popovers',popovers, name="popovers"),

    # Base template empty
    path('base',name='base',view = TemplateView.as_view(template_name="bootstrap_base.html")),

    # Example of view with extra context to highlight an item in the sidebar
    path('forms',name='forms',
         view = TemplateView.as_view(template_name="forms.html",
             extra_context = {'sidebar_active': {
                'forms' : 'active',
                'examples' : 'true'}})
         ),
    path('errors',name='errors',
         view = TemplateView.as_view(template_name="errors.html",
             extra_context = {'sidebar_active': {
                'errors' : 'active',
                'examples' : 'true'}})
         ),
     path('about',name="about",
         view = TemplateView.as_view(template_name="about.html",
              extra_context = {'sidebar_active': {
                 'about' : 'active'}})
          ),

    # DJango template overrides
    path('login',auth_views.LoginView.as_view(), name="login"),
    path('logout', auth_views.LogoutView.as_view(),name="logout"),
    path('password-change',auth_views.PasswordChangeView.as_view(), name="password_change"),

    # Error pages
    path('exception',raise_exception,name='exception'),
    path('secret',raise_403,name='secret'),

]
