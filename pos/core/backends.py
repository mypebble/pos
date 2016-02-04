from django.conf import settings
from django.template import loader, Context

from social.backends.open_id import OpenIdAuth


class PebbleBackend(OpenIdAuth):
    """Identify with Pebble's OAuth backend.
    """
    name = 'pebble'
    URL = settings.OPENID_URL
    USERNAME_KEY = 'email'

    def auth_html(self):
        """Return auth HTML returned by service"""
        openid_request = self.setup_request(self.auth_extra_arguments())
        return_to = self.strategy.absolute_uri(self.redirect_uri)
        form_tag = {'id': 'openid_message'}

        form = openid_request.formMarkup(
            self.trust_root(), return_to, form_tag_attrs=form_tag)

        template = loader.get_template('openid/auth.html')
        context = Context({
            'pre_rendered_form': form,
        })
        return template.render(context)
