from urllib import urlencode

from django import template
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _


register = template.Library()


@register.simple_tag(takes_context=True)
def active_navigation(context, nav_compare, active_class='active',
        inactive_class=''):
    """Returns active_class to the template if the active_navigation context
    variable is equal to nav_compare.
    """
    return (
        active_class if context['active_navigation'] == nav_compare
        else inactive_class)


@register.simple_tag(takes_context=True)
def page_title(context):
    """Sets the title from the context variable page_title.
    """
    return context.get('page_title', _('Arro'))


@register.simple_tag(takes_context=True)
def menu_item(context, menu):
    """Given a menu option, context, and a menu, returns the URL for that menu
    item. This function tries to guess the user's current organisation, so they
    have a good chance of not losing their place when they switch between
    systems.
    The supported keys are:
        * donations
        * finance
        * report
        * clubs
        * events
        * projects
        * name
        * group
        * account
        * bank_account
        * support
        * schools
    """
    try:
        school = context['request'].user.organisations.all()[0]
        school_id = school.external_id
    except IndexError:
        school = None
        school_id = 1

    donations = 'transaction/donation/'
    finance = 'transaction/income/'
    report = 'report/'
    clubs = 'clubs/'
    events = 'events/'
    projects = 'project/'
    name = 'name/'
    group = 'name/group'
    account = 'account/'
    bank_account = 'account/bank/'
    if school is not None:
        sch_base = 'school/{school}/'.format(school=school_id)
        donations = '{}{}'.format(sch_base, donations)
        finance = '{}{}'.format(sch_base, finance)
        report = '{}{}'.format(sch_base, report)
        clubs = '{}{}'.format(sch_base, clubs)
        events = '{}{}'.format(sch_base, events)
        projects = '{}{}'.format(sch_base, projects)
        name = '{}{}'.format(sch_base, donations)
        group = '{}{}'.format(sch_base, donations)
        account = '{}{}'.format(sch_base, donations)
        bank_account = '{}{}'.format(sch_base, donations)

    url_map = {
        'donations': donations,
        'finance': finance,
        'report': report,
        'clubs': clubs,
        'events': events,
        'projects': projects,
        'name': name,
        'group': group,
        'account': account,
        'bank_account': bank_account,
        'support': 'main/support/',
        'schools': 'main/schools/change/',
    }
    url = url_map[menu]

    return u'{master}{url}'.format(
        master=settings.MASTER_SERVER, url=url)


def _get_url(package):
    _base_url = reverse('core-not-subscribed')[1:]  # Strip leading /
    return '?'.join((_base_url, urlencode({'package': package})))


def _display_or_advert(package, show_package, school_id):
    """
    """
    url_bases = {
        'club management': 'school/{school}/clubs/',
        'event management': 'school/{school}/events/',
        'project management': 'school/{school}/projects/',
    }

    if show_package:
        return url_bases[package].format(school=school_id), False
    return _get_url(package), True
