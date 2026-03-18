#!/bin/bash
# vim: dict=/usr/share/rhts-library/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Sanity/init-script-LSB
#   Description: Init script should meet LSB specifications
#   Author: Jan Scotka <jscotka@redhat.com>, Yulia Kopkova <ykopkova@redhat.com>
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
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="cronie"

SERVICE="crond";
reportAllErrors=no;

function isTrue() {
    local string="$@";
    local oldOpt="shopt -p nocasematch";
    local -i rc=1;
    
    shopt -s nocasematch;
    [[ -z "$string" ]] && return 1;
    
    case $string in
         yes) rc=0;;
        true) rc=0;;
         ano) rc=0;;
           1) rc=0;;
          jo) rc=0;;
        yeah) rc=0;;
           y) rc=0;;
           a) rc=0;;
    esac;
    eval $oldOpt;
    return $rc;
}

isTrue no && echo Yes || echo No;

## Is nice to know when things going wrong
function errorHandler() {
    local code="${?}";
    local lineNO="$1";

    case $code in
        127)
            rlFail "Command not found on line $lineNO"
            ;;
        *)
            isTrue $reportAllErrors && rlFail "Unhandled error $code near line $lineNO";
            ;;
    esac
}

function getUserName() {
    local userName="qa_$(tr -dc "[:lower:]" < /dev/urandom | head -c 5)";
    echo "$userName" >&2;⏎
    if getent passwd $userName &>/dev/null; then
        getUserName;
        return $?
    fi
    if [[ -n "$userName" ]]; then
        echo "$userName";
        return $EXIT_SUCCESS;
    else
        return $EXIT_FAILURE;
    fi
}


rlJournalStart
trap 'errorHandler ${LINENO}' ERR;
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "tmpDir=\$(mktemp -d)" 0 "Creating tmp directory";
        testUser="$(getUserName || rlDie "Cannot get username")"
        rlLog "${testUser}"
        rlRun "useradd -d $tmpDir $testUser";
        pushd $tmpDir;
        rlServiceStop $SERVICE
    rlPhaseEnd

    rlPhaseStartTest "starts the service"
        rlRun "service $SERVICE start" 0 " Service must start without problem"
        rlRun "service $SERVICE status" 0 " Then Status command "
        rlRun "service $SERVICE start" 0 " Already started service "
        rlRun "service $SERVICE status" 0 " Again status command "
    rlPhaseEnd

    rlPhaseStartTest "restart the service"
        firstPid=$(ps h -C $SERVICE -o pid);
        rlRun "service $SERVICE restart" 0 " Restarting of service"
        rlRun "service $SERVICE status" 0 " Status command "
        secondPid=$(ps h -C $SERVICE -o pid);
        rlRun "[[ -n $firstPid ]] && [[ -n $secondPid ]] && [[ $firstPid -ne $secondPid ]]" 0 \
            "Pids are different after restart";
    rlPhaseEnd

    rlPhaseStartTest "stop the service"
        rlRun "service $SERVICE stop" 0 " Stopping service "
        rlRun "service $SERVICE status" 3 " Status of stopped service " || true
        rlRun "service $SERVICE stop" 0 " Stopping service again "
        rlRun "service $SERVICE status" 3 " Status of stopped service " || true
    rlPhaseEnd

    if ! rlIsRHEL ">=7"; then
        rlPhaseStartTest "pid file"
            rlServiceStart $SERVICE
            rlAssertExists "/var/run/$SERVICE.pid" "Pid file /var/run/$SERVICE.pid must exist"
            sleep 1
            rlRun "kill -9 `pidof crond`" 0 "Kill $SERVICE"
            sleep 10
            rlRun "service $SERVICE status" 1 " Existing pid file, but service not started " || true;
            sleep 1
            rlRun "rm -fv /var/run/$SERVICE.pid" 0 "Remove .pid file"
        rlPhaseEnd

        rlPhaseStartTest "lock file"
            rlAssertExists "/var/lock/subsys/$SERVICE" "Lock file /var/lock/subsys/$SERVICE must exist"
            rlRun "service $SERVICE status" 2 " Existing lock file, but service not started " || true;
            rlServiceStop $SERVICE
        rlPhaseEnd
    fi

    rlPhaseStartTest "insufficient rights"
        rlRun "service $SERVICE start " 0 " Starting service for restarting under nonpriv user "
        rlRun "su $testUser -c 'service $SERVICE restart'" \
            $(rpm -q systemd &>/dev/null && echo 1 || echo 4) \
            "Insufficient rights, restarting service under nonprivileged user must fail";
    rlPhaseEnd

    rlPhaseStartTest "operations"
        rlRun "service $SERVICE start" 0 " Service have to implement start function "
        rlRun "service $SERVICE restart" 0 " Service have to implement restart function "
        rlRun "service $SERVICE status" 0 " Service have to implement status function "
        rlRun "service $SERVICE reload" 0 " Service have to implement reload function "
        rlRun "service $SERVICE force-reload" 0 " Service have to implement force-reload function "
        rlRun "service $SERVICE condrestart" 0 " Service have to implement condrestart function "
        if ! rlIsRHEL ">=7"; then
            rlRun "service $SERVICE try-restart" 0 " Service have to implement try-restart function "
        fi
    rlPhaseEnd

    rlPhaseStartTest "nonexisting operations"
        rlRun "service $SERVICE noexistop" 2 " Testing proper return code when nonexisting function";
        rlRun "service $SERVICE stopex" 2 " Testing proper return code when nonexisting function";
        rlRun "service $SERVICE foo" 2 " Testing proper return code when nonexisting function" || true
    rlPhaseEnd

    rlPhaseEnd

    rlPhaseStartCleanup
        rlServiceRestore $SERVICE
        rlRun "getent passwd $testUser";
        popd tmpDir;
        rlRun "userdel -fr $testUser" 0 "Remove test user";
#        rlRun "rm -rf $testDir";
        #avoid systemd failing to start crond due start-limit
        sleep 10
    rlPhaseEnd

rlJournalPrintText
trap - ERR;
rlJournalEnd
