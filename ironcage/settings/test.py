from .base import *  # flake8: noqa

# A custom setting for creating full URLs in links in emails
DOMAIN = 'http://testserver'

# Disable sending Slack messaages in tests
SLACK_BACKEND = 'ironcage.tests.slack_backends.TestBackend'

# Admins for mailing errors to
ADMINS = ['admin@example.com']

# Don't spam logs to the console
LOGGING['loggers']['']['handlers'].remove('console')

# Email address to send mail from
SERVER_EMAIL = 'PyCon UK 2017 <noreply@pyconuk.org>'
