#!/usr/bin/env python
#
# slurp Google contacts
#
# adapted from http://blog.nguyenvq.com/tag/google-calendar/
#
########

global MAX_CONTACTS
MAX_CONTACTS = 2000 # XXX what's Google's hard limit?

########

import gdata.contacts.service
from getpass import getpass
from optparse import OptionParser

op = OptionParser()
op.add_option('-u', '--username', dest='username', help='Google username')
op.add_option('-p', '--password', dest='password', help='Google password')
op.add_option('-o', '--output', dest='outputfile', \
        help='Output filename (default stdout)')
(options, args) = op.parse_args()

gd_client = gdata.contacts.service.ContactsService()
gd_client.email = options.username and options.username \
                  or raw_input('Google username: ')
gd_client.password = options.password and options.password \
                     or getpass('Password: ')
gd_client.ProgrammaticLogin()

query = gdata.contacts.service.ContactsQuery()

query.max_results = MAX_CONTACTS
feed = gd_client.GetContactsFeed(query.ToUri())

if options.outputfile:
    outfh = open(options.outputfile, 'w')
    outfh.write(str(feed))
    outfh.close()
else:
    print feed
