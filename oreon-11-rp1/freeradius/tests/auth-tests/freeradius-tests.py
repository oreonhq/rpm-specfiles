#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   Description: Tests for freeradius
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
# ~~~

import errno
import os
import sys
import time
import unittest
import subprocess
import signal
import shutil
import socket

RADIUSD_PID_FILE='/var/run/radiusd/radiusd.pid'

def setUpModule():
    """Initialize the environment, and perform sanity checks on it."""

    if shutil.which('radiusd') is None:
        raise OSError(errno.ENOENT, 'radiusd not found')

    if shutil.which('radtest') is None:
        raise OSError(errno.ENOENT, 'radtest not found')

    if subprocess.call(['systemctl', 'is-active', '--quiet',
                        'radiusd.service']) == 0:
        raise unittest.SkipTest('radiusd.service is already active')

def tearDownModule():
        pass

class GenericUtilities():
    """Provide a set of utility functions start stop daemons. write config files etc """

    def StartRadiusServer(self):
        """Start radiusd"""
        subprocess.check_output(['systemctl', 'start', 'radiusd'])

    def StopRadiusServer(self):
        """stop radiusd"""
        subprocess.check_output(['systemctl', 'stop', 'radiusd'])

class RadiousTests(unittest.TestCase, GenericUtilities):

    def setUp(self):
        self.StartRadiusServer()

    def tearDown(self):
        self.StopRadiusServer()

    def test_radius_plaintext_auth(self):
        time.sleep(1)
        output=subprocess.check_output(['radtest', 'fedora-ci', 'password', '127.0.0.1',  '100', 'testing123']).rstrip().decode('utf-8')
        print(output)

        self.assertRegex(output, "Received Access-Accept")
        self.assertRegex(output, "Reply-Message = \"Hello, fedora-ci\"")

if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout,
                                                     verbosity=3))
