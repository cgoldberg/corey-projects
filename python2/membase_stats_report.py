#!/usr/bin/env python
# Corey Goldberg - 2010
# print a stats report from membase key-value database (membase.org)
# requires python-memcached


import memcache


HOST = '127.0.0.1'

mc = memcache.Client(['%s:11211' % HOST])

for node_stats in mc.get_stats():
    server, stats = node_stats
    print server
    print '--------------------------'.ljust(25), '--------------'.rjust(15)
    for stat_name, value in sorted(stats.iteritems()):
        if not stat_name.startswith('ep'):
            if stat_name not in ('libevent', 'version'):
                print stat_name.ljust(25), value.rjust(15)
    print '--------------------------'.ljust(25), '--------------'.rjust(15)
    for stat_name, value in sorted(stats.iteritems()):
        if stat_name.startswith('ep'):
            if stat_name not in ('ep_dbname', 'ep_version'):
                print stat_name.ljust(25), value.rjust(15)
                