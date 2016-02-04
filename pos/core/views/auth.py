import urllib

from django.conf import settings
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    """Log the user out, and carry on the logout chain.
    """
    def _get_redirect(self, data):
        """Find the next link on the logout chain, or the master server.
        """
        master = settings.MASTER_SERVER

        if 'remaining' in data:
            remaining = data.getlist('remaining')
            redirect_to = remaining[0]

            remaining_query = [{'remaining': r} for r in remaining[1:]]

            querystring = '&'.join(
                urllib.urlencode(r) for r in remaining_query)

            if querystring:
                url = u'{}?{}'.format(redirect_to, querystring)
            else:
                url = redirect_to
        else:
            url = master

        return redirect(url)

    def get(self, *args, **kwargs):
        """
        """
        logout(self.request)
        return self._get_redirect(self.request.GET)

    def post(self, *args, **kwargs):
        """
        """
        logout(self.request)
        return self._get_redirect(self.request.POST)
