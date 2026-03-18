#!/usr/bin/env python3
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   lldpd-test.py integration test
#   Description: Test for lldpd: implementation of IEEE 802.1ab (LLDP)
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
#~~~

import errno
import os
import sys
import time
import unittest
import subprocess
import signal
import shutil
import re
import socket

LLDPD_TCP_DUMP_FILE='/tmp/lldpd-tcp-dump.pcap'
LLDPD_PID_FILE='/var/run/lldpd.pid'

SERVICE_UNITDIR = '/run/systemd/system'
NETWORK_UNITDIR = '/run/systemd/network'

def setUpModule():
    """Initialize the environment, and perform sanity checks on it."""

    if shutil.which('lldpd') is None:
        raise OSError(errno.ENOENT, 'lldpd not found')

    # Ensure the unit directory exists so tests can dump files into it.
    os.makedirs(NETWORK_UNITDIR, exist_ok=True)

class lldpdUtilities():
    """Provide a set of utility functions start stop lldpd ."""

    def Startlldpd(self):
        """Start lldpd interface lldpd-peer """
        subprocess.check_output(['/usr/sbin/lldpd', '-cfse', '-D', '-C', 'lldpd-peer', '-I', 'lldpd-peer', '-S', 'lldpd-system-name','-m', '192.168.50.6'])

    def Stoplldpd(self):
        try:
            with open(LLDPD_PID_FILE, 'r') as f:
                pid = f.read().rstrip(' \t\r\n\0')
                os.kill(int(pid), signal.SIGTERM)
                os.remove(LLDPD_PID_FILE)
        except IOError:
            pass

    def StartCaptureLLDPPackets(self):
        """Start tcpdump to capture packets"""
        self.WriteServiceFile('tcpdump.service', '''\
[Unit]
Description=TCPDumpd
After=multi-user.target network.target

[Service]
Type=simple

ExecStart=/usr/sbin/tcpdump -pnnli lldpd ether proto 0x88cc -vvv -w "/tmp/lldpd-tcp-dump.pcap"
[Install]
WantedBy=multi-user.target
''')
        subprocess.check_output(['systemctl','daemon-reload'])
        subprocess.check_output(['systemctl','restart', 'tcpdump.service'])

    def StopCapturingPackets(self):
        subprocess.check_output(['systemctl', 'stop', 'tcpdump.service'])
        time.sleep(3);

    def SetupVethInterface(self):
        """Setup veth interface"""
        subprocess.check_output(['ip', 'link', 'add', 'lldpd', 'type', 'veth', 'peer', 'name', 'lldpd-peer'])
        subprocess.check_output(['ip', 'link', 'set', 'lldpd', 'address', '02:01:02:03:04:08'])
        subprocess.check_output(['ip', 'link', 'set', 'lldpd-peer', 'address', '02:01:02:03:04:09'])
        subprocess.check_output(['ip', 'link', 'set', 'lldpd', 'up'])
        subprocess.check_output(['ip', 'link', 'set', 'lldpd-peer', 'up'])

        time.sleep(3);

        self.addCleanup(subprocess.call, ['ip', 'link', 'del', 'dev', 'lldpd'])

    def WriteServiceFile(self, unit_name, contents):
        """Write a tcpdump unit file, and queue it to be removed."""
        unit_path = os.path.join(SERVICE_UNITDIR, unit_name)

        with open(unit_path, 'w') as unit:
            unit.write(contents)
            self.addCleanup(os.remove, unit_path)

    def WriteNetworkFile(self, unit_name, contents):
        """Write a networkd unit file, and queue it to be removed."""
        unit_path = os.path.join(NETWORK_UNITDIR, unit_name)

        with open(unit_path, 'w') as unit:
            unit.write(contents)
            self.addCleanup(os.remove, unit_path)

    def FindProtocolFieldsinTCPDump(self, **kwargs):
        """Look attributes in lldpd logs."""

        contents = subprocess.check_output(['tcpdump', '-v', '-r', LLDPD_TCP_DUMP_FILE]).rstrip().decode('utf-8')
        if kwargs is not None:
                for key in kwargs:
                    self.assertRegex(contents, kwargs[key])

class lldpdTestsViaNetworkd(unittest.TestCase, lldpdUtilities):

    def setUp(self):

        """ Setup veth interface """
        self.WriteNetworkFile('lldpd-veth.netdev', '''\
[NetDev]
Name=lldpd
Kind=veth
MACAddress=12:34:56:78:9a:bc

[Peer]
Name=lldpd-peer
MACAddress=12:34:56:78:9a:bd
''')

        """ Receive LLDP packets via networkd """
        self.WriteNetworkFile('lldp.network', '''\
[Match]
Name=lldpd

[Network]
DHCP=no
IPv6AcceptRA=false
LLDP=yes
EmitLLDP=yes
''')
        """ Receive LLDP packets via networkd """
        self.WriteNetworkFile('lldp-peer.network', '''\
[Match]
Name=lldpd-peer
''')
        subprocess.check_output(['systemctl', 'restart', 'systemd-networkd'])
        time.sleep(5)

    def tearDown(self):
        self.Stoplldpd()
        subprocess.check_output(['ip', 'link', 'del', 'lldpd'])

    def test_lldpd_received_lldp_packets_sent_by_systemd_networkd(self):
        self.Startlldpd()

        time.sleep(10)

        ''' Test whether lldpd receved LLDP packets from networkd '''
        output=subprocess.check_output(['lldpctl']).rstrip().decode('utf-8')
        self.assertRegex(output, "ifname lldpd")
        self.assertRegex(output, socket.gethostname())

    def test_systemd_networkd_received_lldp_packets(self):
        self.Startlldpd()

        time.sleep(10)

        # lldpd 02:01:02:03:04:09 [hostname]  02:01:02:03:04:09 lldpd-peer
        output=subprocess.check_output(['networkctl', 'lldp', '--no-legend', '--no-pager']).rstrip().decode('utf-8')
        self.assertRegex(output, "lldpd")
        self.assertRegex(output, "lldpd-peer")
        self.assertRegex(output, "12:34:56:78:9a:bd")
        self.assertRegex(output, socket.gethostname())

        # Port ID and Chasiss id count should be 2
        self.assertEqual(2, output.count("12:34:56:78:9a:bd"))

class lldpdTests(unittest.TestCase, lldpdUtilities):

    def setUp(self):
        """ Setup """
        self.SetupVethInterface()

    def tearDown(self):
        self.Stoplldpd()
        os.remove(LLDPD_TCP_DUMP_FILE)

    def test_lldpd_trasmitted_lldp_attributes(self):
        """ verify at the other end of veth received LLDP packets that contains attibutes (link address, hostname, TTL, system desc). tcpdump """

        self.StartCaptureLLDPPackets()
        self.Startlldpd()

        """ capture for 10 seconds """
        time.sleep(10)

        self.StopCapturingPackets()

        self.FindProtocolFieldsinTCPDump(Chassis='Subtype MAC address \(4\): 02:01:02:03:04:09',
                                         Port='Subtype MAC address \(3\): 02:01:02:03:04:09',
                                         PortDesc='lldpd-peer',
                                         TTL='TTL.*120s',
                                         HostName=socket.gethostname() ,
                                         System_Description='lldpd-system-name',
                                         ManagementAddress='192.168.50.6')

    def test_lldpd_trasmitted_lldp_packets(self):
        """ verify at the other end of veth ifname lldpd has received LLDP packets. tcpdump """

        self.StartCaptureLLDPPackets()
        self.Startlldpd()

        """ capture for 10 seconds """
        time.sleep(10)

        self.StopCapturingPackets()
        self.FindProtocolFieldsinTCPDump(MAC='02:01:02:03:04:09',
                                         TTL='TTL 120s')


if __name__ == '__main__':
    unittest.main(testRunner=unittest.TextTestRunner(stream=sys.stdout,
                                                     verbosity=2))
