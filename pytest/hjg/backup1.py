#!/usr/bin/python

import os
import time

source = ['/usr/pyworkspace/source/']

target_dir='/usr/pyworkspace/target/'

target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_command="zip -qr '%s' %s" % (target, ' '.join(source))

if os.system(zip_command) == 0:
	print 'successful backup to', target
else:
	print 'backup failed'
