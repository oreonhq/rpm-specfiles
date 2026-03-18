#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="selinux-policy"
POLICY_OPTIONS=${POLICY_OPTIONS:-"lbc clbsa lbsidca lbscid lbsidc agmndislcb"}
TEST_SCRIPTS="abdilns"
#SEPOLICY_CONFINE="confined-users-policy/sepolicy_confine/sepolicy_confine"
SEPOLICY_CONFINE="udica confined_user"

rlJournalStart
    rlPhaseStartSetup
        rlRun "set -o pipefail"
        rlRun "systemctl start telnet.socket"

        if [ -d /etc/ssh/sshd_config.d ] ; then
            rlRun "echo 'PasswordAuthentication yes' > /etc/ssh/sshd_config.d/001-enable-password.conf"
            rlRun "service sshd restart"
        fi

        rlRun "semodule -i /usr/share/udica/macros/confined_user_macros.cil"
        rlRun "setsebool ssh_sysadm_login on"
        # do not show "With great power comes great responsibility." prompt
        # and don't ask for password when using "sudo"
        echo "%users   ALL=(ALL:ALL) NOPASSWD: ALL" >> /etc/sudoers.d/confined_users_test;
        echo "%wheel   ALL=(ALL)     NOPASSWD: ALL" >> /etc/sudoers.d/confined_users_test;
        echo 'Defaults  lecture="never"' >> /etc/sudoers.d/confined_users_test;
    rlPhaseEnd

    #TODO try different level and range for the generated user policy
    rlPhaseStartTest "real scenario -- confined users"
        USER_NAME_SEED="user${RANDOM}"
        USER_NAME_INDEX=1
        USER_LIST=""
        for OPTIONS in ${POLICY_OPTIONS} ; do
            USER_NAME="${USER_NAME_SEED}$((USER_NAME_INDEX++))"
            USER_LIST+=" ${USER_NAME}"
            USER_SECRET="S3kr3t${RANDOM}"
            SELINUX_USER="confined_${OPTIONS}"
            rlLog "Testing SELinux users: ${SELINUX_USER}"
            rlRun "${SEPOLICY_CONFINE} -${OPTIONS} --level s0 --range s0-s0:c0.c1023 ${SELINUX_USER}"
            rlRun "semodule -i ${SELINUX_USER}.cil"
            rlRun "sed -e 's|user|${SELINUX_USER}|g' /etc/selinux/targeted/contexts/users/user_u > /etc/selinux/targeted/contexts/users/${SELINUX_USER}_u"
            rlRun "useradd -Z ${SELINUX_USER}_u ${USER_NAME}"
            rlRun "cp *.sh /home/${USER_NAME}"
            rlRun "echo ${USER_SECRET} | passwd --stdin ${USER_NAME}"
            rlRun "usermod -G wheel ${USER_NAME}"
            # dummy -- first telnet connection does not show results properly
            rlRun "./telnet.exp ${USER_NAME} ${USER_SECRET} localhost whoami"
            # run all available scripts matching given confined user options
            TO_RUN=${OPTIONS//[^"$TEST_SCRIPTS"]}
            for (( i=0; i<${#TO_RUN}; i++ )) ; do
                rlRun -s "./telnet.exp ${USER_NAME} ${USER_SECRET} localhost /home/${USER_NAME}/${TO_RUN:$i:1}.sh ${USER_SECRET}"
                echo "\n"
                rlRun "grep -e 'Error' $rlRun_LOG" 1
            done
            # run test scripts over SSH if the new user is allowed to use it
            if [[ "$OPTIONS" == *"c"* ]]; then
                for (( i=0; i<${#TO_RUN}; i++ )) ; do
                    rlRun -s "./ssh.exp ${USER_NAME} ${USER_SECRET} localhost /home/${USER_NAME}/${TO_RUN:$i:1}.sh ${USER_SECRET}"
                    rlRun "grep -e 'Error' $rlRun_LOG" 1
                done
            fi
            sleep 10
        done
        # remove all test users
        for USER_NAME in ${USER_LIST} ; do
            rlRun "userdel -rfZ ${USER_NAME}"
        done
        sleep 10
        # remove test SELinux users
        for OPTIONS in ${POLICY_OPTIONS} ; do
            rlRun "rm -rf confined_${OPTIONS}.cil /etc/selinux/targeted/contexts/users/confined_${OPTIONS}_u"
            rlRun "semodule -r confined_${OPTIONS}"
        done
        rlRun "rm -rf $rlRun_LOG"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "semodule -r confined_user_macros"
        rlRun "rm -rf /etc/sudoers.d/confined_users_test"
        rlRun "setsebool ssh_sysadm_login off"

        if [ -d /etc/ssh/sshd_config.d ] ; then
            rlRun "rm -f /etc/ssh/sshd_config.d/001-enable-password.conf"
            rlRun "service sshd restart"
        fi
    rlPhaseEnd
rlJournalEnd
