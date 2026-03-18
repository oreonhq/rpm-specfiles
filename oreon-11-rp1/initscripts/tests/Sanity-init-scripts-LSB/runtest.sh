#!/bin/bash
# vim: dict=/usr/share/rhts-library/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/initscripts/Sanity/init-scripts-LSB
#   Description: Init scripts should meet LSB specifications
#   Author: Jan Scotka <jscotka@redhat.com>,  Yulia Kopkova <ykopkova@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2009 Red Hat, Inc. All rights reserved.
#
#   This copyrighted material is made available to anyone wishing
#   to use, modify, copy, or redistribute it subject to the terms
#   and conditions of the GNU General Public License version 2.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free
#   Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#   Boston, MA 02110-1301, USA.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include rhts environment
. /usr/bin/rhts-environment.sh
. /usr/share/rhts-library/rhtslib.sh

PACKAGE="initscripts"


SRV_NETCONSOLE=netconsole
SRV_NETFS=netfs
TRG_REMOTEFS=remote-fs.target
SRV_NETWORK=network

rlJournalStart
    
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "useradd testuserqa" 0 "Add test user"
        rlFileBackup /etc/sysconfig/netconsole
        if rlIsRHEL '<7'; then #there is no syslog in rhel7 and highier
            rlRun "sed -i -e 's,^# SYSLOGADDR=,SYSLOGADDR=redhat.com,' /etc/sysconfig/netconsole" 0 "Set remote syslog server address /etc/sysconfig/netconsole"
        fi
    rlPhaseEnd


    rlPhaseStartTest "netconsole service LSB compliance test" 
if ls /lib*/modules/*/kernel/drivers/net/netconsole.ko*; then
	rlRun "ls /lib*/modules/*/kernel/drivers/net/netconsole.ko*" 0
    if rlIsRHEL '<7'; then

        SERVICE=$SRV_NETCONSOLE
        rlServiceStop $SERVICE
        rlLog ">>>>>>>>> service start"
        rlRun "service $SERVICE start" 0 " Service must start without problem "
        rlRun "service $SERVICE status" 0 " Then Status command "
        rlRun "service $SERVICE start" 0 " Already started service "
        rlRun "service $SERVICE status" 0 " Again status command "

        rlLog ">>>>>>>>> service restart"
        rlRun "service $SERVICE restart" 0 " Restarting of service "
        rlRun "service $SERVICE status" 0 " Status command "

        rlLog ">>>>>>>>> service stop"
        rlRun "service $SERVICE stop" 0 " Stopping service "
        rlRun "service $SERVICE status" 3 " Status of stopped service "
        rlRun "service $SERVICE stop" 0 " Stopping service again "
        rlRun "service $SERVICE status" 3 " Status of stopped service "

        rlLog ">>>>>>>>> insufficient rights"
        rlRun "service $SERVICE start " 0 " Starting service for restarting under nonpriv user "
        rlRun "su testuserqa -c 'service $SERVICE restart'" 1 "Insufficient rights, restarting resrvice under nonprivileged user must fail "

        rlLog ">>>>>>>>> operations"
        rlServiceStop $SERVICE
        rlRun "service $SERVICE start" 0 " Service have to implement start function "
        rlRun "service $SERVICE restart" 0 " Service have to implement restart function "
        rlRun "service $SERVICE status" 0 " Service have to implement status function "
        rlRun "service $SERVICE condrestart" 0 " Service have to implement condrestart function "
        rlRun "service $SERVICE reload" 0 " Service have to implement reload function "
        rlRun "service $SERVICE force-reload" 0 " Service have to implement force-reload function "

        rlLog ">>>>>>>>> nonexist operations"
        rlRun "service $SERVICE noexistop" 2 " Testing proper return code when nonexisting function "

        rlServiceRestore $SERVICE
    fi # rhel 6 or less
else
	rlLog ">>>> no netconsole kernel module appear here"
	rlRun "ls /lib*/modules/*/kernel/drivers/net/netconsole.ko*" 1,2
fi
	rlLog "NIC should support polling, NETPOLL should be compliled in kernel and netconsole module should be loaded"
	rlLog "`cat /usr/src/kernels/$(uname -r)/.config | grep -i poll`"	
	rlLog "netconsole module: `lsmod | grep -i netconsole && echo true || echo false`"
	rlLog "`cat /var/log/messages | grep -i netconsole | tail -n 10`"
    rlPhaseEnd

    # for RHEL6 and lower
    if rlIsRHEL '<7'; then
        rlPhaseStartTest "netfs service LSB compliance test" 
    
            SERVICE=$SRV_NETFS
            rlServiceStop $SERVICE
            rlLog ">>>>>>>>> service start"
            rlRun "service $SERVICE start" 0 " Service must start without problem "
            rlRun "service $SERVICE status" 0 " Then Status command "
            rlRun "service $SERVICE start" 0 " Already started service "
            rlRun "service $SERVICE status" 0 " Again status command "
    
            rlLog ">>>>>>>>> service restart"
            rlRun "service $SERVICE restart" 0 " Restarting of service "
            rlRun "service $SERVICE status" 0 " Status command "
    
            rlLog ">>>>>>>>> service stop"
            rlRun "service $SERVICE stop" 0 " Stopping service "
            rlRun "service $SERVICE status" 3 " Status of stopped service "
            rlRun "service $SERVICE stop" 0 " Stopping service again "
            rlRun "service $SERVICE status" 3 " Status of stopped service "
    
            rlLog ">>>>>>>>> insufficient rights"
            rlRun "service $SERVICE start " 0 " Starting service for restarting under nonpriv user "
            rlRun "su testuserqa -c 'service $SERVICE restart'" 4 "Insufficient rights, restarting resrvice under nonprivileged user must fail "
    
            rlLog ">>>>>>>>> operations"
            rlServiceStop $SERVICE
            rlRun "service $SERVICE start" 0 " Service have to implement start function "
            rlRun "service $SERVICE restart" 0 " Service have to implement restart function "
            rlRun "service $SERVICE status" 0 " Service have to implement status function "
    
            rlLog ">>>>>>>>> nonexist operations"
            rlRun "service $SERVICE noexistop" 2 " Testing proper return code when nonexisting function "
    
            rlServiceRestore $SERVICE
    
        rlPhaseEnd
    else
        rlPhaseStartTest "remote-fs target LSB compliance test"

            TARGET=$TRG_REMOTEFS
            rlServiceStop $TARGET
            rlLog ">>>>>>>>> target start"
            rlRun "service $TARGET start" 0 " Target must start without problem "
            rlRun "service $TARGET status" 0 " Then Status command "
            rlRun "service $TARGET start" 0 " Already started target "
            rlRun "service $TARGET status" 0 " Again status command "

            rlLog ">>>>>>>>> target restart"
            rlRun "service $TARGET restart" 0 " Restarting target "
            rlRun "service $TARGET status" 0 " Status command "

            rlLog ">>>>>>>>> target stop"
            rlRun "service $TARGET stop" 0 " Stopping target "
            rlRun "service $TARGET status" 3 " Status of stopped target "
            rlRun "service $TARGET stop" 0 " Stopping target again "
            rlRun "service $TARGET status" 3 " Status of stopped target "

            rlLog ">>>>>>>>> insufficient rights"
            rlRun "service $TARGET start " 0 " Starting target for restarting under nonpriv user "
            rlRun "su testuserqa -c 'service $TARGET restart'" 1 " Insufficient rights, restarting target under nonprivileged user must fail " # returns 1 instead of 4 because of polkit

            rlLog ">>>>>>>>> operations"
            rlServiceStop $TARGET
            rlRun "service $TARGET start" 0 " Target have to implement start function "
            rlRun "service $TARGET restart" 0 " Target have to implement restart function "
            rlRun "service $TARGET status" 0 " Target have to implement status function "

            rlLog ">>>>>>>>> nonexist operations"
            rlRun "service $TARGET noexistop" 2 " Testing proper return code when nonexisting function "

            rlServiceRestore $TARGET

        rlPhaseEnd
    fi


#    rlPhaseStartTest "$SRV_NETWORK service LSB compliance test" 
#
#        SERVICE=$SRV_NETWORK
#        rlServiceStop $SERVICE
#        rlLog ">>>>>>>>> service start"
#        rlRun "service $SERVICE start" 0 " Service must start without problem "
#        rlRun "service $SERVICE status" 0 " Then Status command "
#        rlRun "service $SERVICE start" 1,0 " Already started service "
#        rlRun "service $SERVICE status" 0 " Again status command "

#        rlLog ">>>>>>>>> service restart"
#        rlRun "service $SERVICE restart" 0 " Restarting of service "
#        rlRun "service $SERVICE status" 0 " Status command "

#        rlLog ">>>>>>>>> service stop"
#        rlRun "service $SERVICE stop" 0 " Stopping service "
#        rlRun "service $SERVICE status" 0 " Status of stopped service "
#        rlRun "service $SERVICE stop" 0 " Stopping service again "
#        rlRun "service $SERVICE status" 0 " Status of stopped service "

#        rlLog ">>>>>>>>> insufficient rights"
#        rlRun "service $SERVICE start " 0 " Starting service for restarting under nonpriv user "
#        rlRun "su testuserqa -c 'service $SERVICE restart'" 4 "Insufficient rights, restarting resrvice under nonprivileged user must fail "

#        rlLog ">>>>>>>>> operations"
#        rlServiceStop $SERVICE
#        rlRun "service $SERVICE start" 0 " Service have to implement start function "
#        rlRun "service $SERVICE restart" 0 " Service have to implement restart function "
#        rlRun "service $SERVICE status" 0 " Service have to implement status function "
#        rlRun "service $SERVICE reload" 0 " Service have to implement reload function "
#        rlRun "service $SERVICE force-reload" 0 " Service have to implement force-reload function "

#        rlLog ">>>>>>>>> nonexist operations"
#        rlRun "service $SERVICE noexistop" 2 " Testing proper return code when nonexisting function "

#        rlServiceRestore $SERVICE
#        service $SERVICE start
    rlPhaseEnd


    rlPhaseStartCleanup
        rlRun "userdel -fr testuserqa" 0 "Remove test user"
        rlFileRestore
    rlPhaseEnd

rlJournalPrintText
rlJournalEnd
