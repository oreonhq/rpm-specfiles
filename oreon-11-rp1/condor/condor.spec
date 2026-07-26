%global source0_hash e2ceb59e5137365aa121376c50b305bca6902eee49fa61b49c89197bd4269dfd

%global version         23.9.6
%global version_ %(tr . _ <<< %{version})

%global with_vault_credmon 0

#######################
Name:           condor
Version:        23.9.6
Release:        15%{?dist}
Summary:        HTCondor: High Throughput Computing
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://htcondor.org
##############################################################
# NOTE: If you wish to setup a debug build either add a patch
# or adjust the URL to a private github location
##############################################################
Source0:        https://github.com/htcondor/htcondor/archive/v%{version}/%{name}-%{version}.tar.gz

ExcludeArch: %{ix86}

Patch1: exit_37.sif.patch
Patch2: unified-bin.patch
Patch3: CVE-2025-30093.patch

# This is a stopgap until I can conditionalize the cmake files
# use the system libfmt if suitable version available

# Do not check .so files in condor's library directory
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$

# Do not provide libfmt
%global __requires_exclude ^libfmt\\.so.*$

#######################
BuildRequires: gcc gcc-c++
BuildRequires: cmake >= 3.16
BuildRequires: pcre2-devel
BuildRequires: openssl-devel
BuildRequires: krb5-devel
BuildRequires: libvirt-devel
BuildRequires: bind-utils
BuildRequires: libX11-devel
BuildRequires: libXScrnSaver-devel
BuildRequires: libcurl-devel
BuildRequires: expat-devel
BuildRequires: python3-setuptools
BuildRequires: python3-sphinx
BuildRequires: python3-sphinx_rtd_theme
BuildRequires: boost-devel
BuildRequires: boost-python3-devel
BuildRequires: boost-static
BuildRequires: glibc-static
BuildRequires: libuuid-devel
BuildRequires: sqlite-devel
BuildRequires: patch
# needed for param table generator
BuildRequires: perl-generators
BuildRequires: perl(Archive::Tar)
BuildRequires: perl(Data::Dumper)
BuildRequires: perl(Digest::MD5)
BuildRequires: perl(XML::Parser)

BuildRequires: munge-devel
BuildRequires: voms-devel
BuildRequires: nss-devel
BuildRequires: openldap-devel
BuildRequires: scitokens-cpp-devel

# we now need to request the python libs and includes explicitly:
BuildRequires: python3-devel

# Added by B.DeKnuydt (Jan 2020)
BuildRequires: libxml2 libxml2-devel
BuildRequires: pam-devel
BuildRequires: make

BuildRequires: systemd-devel
BuildRequires: systemd-units

#######################
# Installation requirements.
Requires: /usr/sbin/sendmail
Requires: python3
Requires: python3-cryptography

# Require libraries that we dlopen
# Ganglia is optional as well as nVidia and cuda libraries
Requires: voms
Requires: krb5-libs
Requires: libcom_err
Requires: munge-libs
Requires: openssl-libs
Requires: scitokens-cpp >= 0.6.2
Requires: systemd-libs
Requires: rsync
Requires: condor-upgrade-checks

# openssh-server needed for condor_ssh_to_job
Requires: openssh-server

# net-tools needed to provide netstat for condor_who
Requires: net-tools

# Perl modules required for condor_gather_info
Requires: perl(Date::Manip)
Requires: perl(FindBin)

# Useful tools are using the Python bindings
Requires: python3-condor = %{version}-%{release}
Requires: python3-requests

# Ensure that our bash completions work
Recommends: bash-completion

#From /usr/share/doc/setup/uidgid (RPM: setup-2.12.2-11)
#Provides: user(condor) = 64
#Provides: group(condor) = 64

# procd package discontinued as of 10.8.0
Obsoletes: %{name}-procd < 10.8.0
Provides: %{name}-procd = %{version}-%{release}

# all package discontinued as of 10.8.0
Obsoletes: %{name}-openstack-gahp < 10.8.0
Provides: %{name}-openstack-gahp = %{version}-%{release}

# classads package discontinued as of 10.8.0
Obsoletes: %{name}-classads < 10.8.0
Provides: %{name}-classads = %{version}-%{release}

# classads-devel package discontinued as of 10.8.0
Obsoletes: %{name}-classads-devel < 10.8.0
Provides: %{name}-classads-devel = %{version}-%{release}

%description
HTCondor is a workload management system for high-throughput and
high-performance jobs. Like other full-featured batch systems, HTCondor
provides a job queuing mechanism, scheduling policy, priority scheme,
resource monitoring, and resource management. Users submit their
serial or parallel jobs to HTCondor, HTCondor places them into a queue,
chooses when and where to run the jobs based upon a policy, carefully
monitors their progress, and ultimately informs the user upon
completion.

#######################
%package devel
Summary: Development files for HTCondor
Group: Applications/System

%description devel
Development files for HTCondor

#######################
%package kbdd
Summary: HTCondor Keyboard Daemon
Requires: %name = %version-%release
Requires: condor = %{version}-%{release}

%description kbdd
The condor_kbdd monitors logged in X users for activity. It is only
useful on systems where no device (e.g. /dev/*) can be used to
determine console idle time.

#######################
%package test
Summary: HTCondor Self Tests
Group: Applications/System
Requires: %name = %version-%release

%description test
A collection of tests to verify that HTCondor is operating properly.

#######################
%package vm-gahp
Summary: HTCondor's VM Gahp
Requires: %name = %version-%release
Requires: libvirt
Requires: condor = %{version}-%{release}

%description vm-gahp
The condor_vm-gahp enables the Virtual Machine Universe feature of
HTCondor. The VM Universe uses libvirt to start and control VMs under
HTCondor's Startd.

#######################
%package -n python3-condor
Summary: Python bindings for HTCondor
Requires: %name = %version-%release
%{?python_provide:%python_provide python3-condor}

%description -n python3-condor
The python bindings allow one to directly invoke the C++ implementations of
the ClassAd library and HTCondor from python

#######################
%package credmon-local
Summary: Local issuer credmon for HTCondor
Group: Applications/System
Requires: %name = %version-%release
Requires: python3-condor = %{version}-%{release}
Requires: python3-six
Requires: python3-cryptography
Requires: python3-scitokens

%description credmon-local
The local issuer credmon allows users to obtain credentials from an
admin-configured private SciToken key on the access point and to use those
credentials securely inside running jobs.

#######################
%package credmon-oauth
Summary: OAuth2 credmon for HTCondor
Group: Applications/System
Requires: %name = %version-%release
Requires: condor-credmon-local = %{version}-%{release}
Requires: python3-requests-oauthlib
Requires: python3-flask
Requires: python3-mod_wsgi
Requires: httpd

%description credmon-oauth
The OAuth2 credmon allows users to obtain credentials from configured
OAuth2 endpoints and to use those credentials securely inside running jobs.

%if 0%{?with_vault_credmon}
#######################
%package credmon-vault
Summary: Vault credmon for HTCondor
Group: Applications/System
Requires: %name = %version-%release
Requires: python3-condor = %{version}-%{release}
Requires: python3-six
Requires: python3-cryptography
# Although htgettoken is only needed on the submit machine and
#  condor-credmon-vault is needed on both the submit and credd machines,
#  htgettoken is small so it doesn't hurt to require it in both places.
Requires: htgettoken >= 1.1
Conflicts: %name-credmon-local

%description credmon-vault
The Vault credmon allows users to obtain credentials from Vault using
htgettoken and to use those credentials securely inside running jobs.

%endif
#######################
%package -n minicondor
Summary: Configuration for a single-node HTCondor
Requires: %name = %version-%release
Requires: python3-condor = %version-%release

%description -n minicondor
This example configuration is good for trying out HTCondor for the first time.
It only configures the IPv4 loopback address, turns on basic security, and
shortens many timers to be more responsive.

#######################
%package ap
Summary: Configuration for an Access Point
Group: Applications/System
Requires: %name = %version-%release
Requires: python3-condor = %version-%release

%description ap
This example configuration is good for installing an Access Point.
After installation, one could join a pool or start an annex.

#######################
%package annex-ec2
Summary: Configuration and scripts to make an EC2 image annex-compatible.
Requires: %name = %version-%release

%description annex-ec2
Configures HTCondor to make an EC2 image annex-compatible.  Do NOT install
on a non-EC2 image.

%files annex-ec2
%_libexecdir/condor/condor-annex-ec2
%{_unitdir}/condor-annex-ec2.service
%config(noreplace) %_sysconfdir/condor/config.d/50ec2.config
%config(noreplace) %_sysconfdir/condor/master_shutdown_script.sh

%post annex-ec2
#/bin/systemctl enable condor-annex-ec2

%preun annex-ec2
if [ $1 == 0 ]; then
    /bin/systemctl disable condor-annex-ec2
fi

#######################
%package upgrade-checks
Summary: Script to check for manual interventions needed to upgrade
Group: Applications/System
Requires: python3-condor
Requires: pcre2-tools

%description upgrade-checks
HTCondor V9 to V10 check for for known breaking changes:
1. IDToken TRUST_DOMAIN default value change
2. Upgrade to PCRE2 breaking map file regex sequences
3. The way to request GPU resources for a job

%files upgrade-checks
%_bindir/condor_upgrade_check

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch 1 -p1
%patch 2 -p1
%patch 3 -p1

# fix errant execute permissions
find src -perm /a+x -type f -name "*.[Cch]" -exec chmod a-x {} \;

# Create a sysusers.d config file.
# uid and gid 64 is reserved:
# https://src.fedoraproject.org/rpms/setup/blob/rawhide/f/uidgid#_75
cat >condor.sysusers.conf <<EOF
u condor 64 'Owner of HTCondor Daemons' %{_sharedstatedir}/%{name} -
EOF

%build
make -C docs man
%cmake -DBUILDID:STRING=RH-%{version}-%{release} \
       -DBUILD_TESTING:BOOL=FALSE \
       -DCMAKE_SKIP_RPATH:BOOL=TRUE \
%if 0%{?rhel} == 8
       -DPython3_EXECUTABLE=%__python3 \
%endif
       -DPACKAGEID:STRING=%{version}-%{release} \
       -DCONDOR_PACKAGE_BUILD:BOOL=TRUE \
       -DCONDOR_RPMBUILD:BOOL=TRUE \
       -DCMAKE_INSTALL_PREFIX:PATH=/

%cmake_build

%install
# installation happens into a temporary location, this function is
# useful in moving files into their final locations
function populate {
  _dest="$1"; shift; _src="$*"
  mkdir -p "%{buildroot}/$_dest"
  mv $_src "%{buildroot}/$_dest"
}

rm -rf %{buildroot}
%cmake_install

# TODO: Fix up cmake and remove this hack
%ifarch s390x
mv %{buildroot}/usr/lib/* %{buildroot}/usr/%{_lib}
%endif

# Drop in a symbolic link for backward compatibility
ln -s ../..%{_libdir}/condor/condor_ssh_to_job_sshd_config_template %{buildroot}/%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template

mv %{buildroot}/usr/share/doc/condor-%{version} %{buildroot}/usr/share/doc/condor
populate /usr/share/doc/condor/examples %{buildroot}/usr/share/doc/condor/etc/examples/*

mkdir -p %{buildroot}/%{_sysconfdir}/condor
# the default condor_config file is not architecture aware and thus
# sets the LIB directory to always be /usr/lib, we want to do better
# than that. this is, so far, the best place to do this
# specialization. we strip the "lib" or "lib64" part from _libdir and
# stick it in the LIB variable in the config.
LIB=$(echo %{?_libdir} | sed -e 's:/usr/\(.*\):\1:')
if [ "$LIB" = "%_libdir" ]; then
  echo "_libdir does not contain /usr, sed expression needs attention"
  exit 1
fi

# Install the basic configuration, a Personal HTCondor config. Allows for
# yum install condor + service condor start and go.
mkdir -p -m0755 %{buildroot}/%{_sysconfdir}/condor/config.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/passwords.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/tokens.d

populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-htcondor-9.0.config
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-minicondor
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-access-point
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-kbdd
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/50ec2.config

# Install a second config.d directory under /usr/share, used for the
# convenience of software built on top of Condor such as GlideinWMS.
mkdir -p -m0755 %{buildroot}/usr/share/condor/config.d

mkdir -p -m0755 %{buildroot}/%{_var}/log/condor
# Note we use %{_var}/lib instead of %{_sharedstatedir} for RHEL5 compatibility
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/spool
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/execute
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/krb_credentials
mkdir -p -m2770 %{buildroot}/%{_var}/lib/condor/oauth_credentials

# not packaging configure/install scripts
rm -f %{buildroot}%{_bindir}/make-ap-from-tarball
rm -f %{buildroot}%{_bindir}/make-personal-from-tarball
rm -f %{buildroot}%{_sbindir}/condor_configure
rm -f %{buildroot}%{_sbindir}/condor_install
rm -f %{buildroot}/%{_mandir}/man1/condor_configure.1
rm -f %{buildroot}/%{_mandir}/man1/condor_install.1

mkdir -p %{buildroot}/%{_var}/www/wsgi-scripts/condor_credmon_oauth
mv %{buildroot}/%{_libexecdir}/condor/condor_credmon_oauth.wsgi %{buildroot}/%{_var}/www/wsgi-scripts/condor_credmon_oauth/condor_credmon_oauth.wsgi

# Move oauth credmon config files out of examples and into config.d
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/config/condor/40-oauth-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-credmon.conf
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/config/condor/40-oauth-tokens.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-tokens.conf
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/README.credentials %{buildroot}/%{_var}/lib/condor/oauth_credentials/README.credentials

%if 0%{?with_vault_credmon}
# Move vault credmon config file out of examples and into config.d
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/config/condor/40-vault-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-vault-credmon.conf
%else
rm -f  %{buildroot}%{_bindir}/condor_vault_storer
rm -f  %{buildroot}%{_sbindir}/condor_credmon_vault
%endif

# install tmpfiles.d/condor.conf
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf

install -Dp -m0755 %{buildroot}/usr/share/doc/condor/examples/condor-annex-ec2 %{buildroot}%{_libexecdir}/condor/condor-annex-ec2

mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor-annex-ec2.service %{buildroot}%{_unitdir}/condor-annex-ec2.service
install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor.service %{buildroot}%{_unitdir}/condor.service
# Disabled until HTCondor security fixed.
# install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor.socket %{buildroot}%{_unitdir}/condor.socket

%if 0%{?rhel} >= 7
mkdir -p %{buildroot}%{_datadir}/condor/
cp %{SOURCE8} %{buildroot}%{_datadir}/condor/
%endif

#Fixups for packaged build, should have been done by cmake

mkdir -p %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/Chirp.jar %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/CondorJava*.class %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/libchirp_client.so %{buildroot}/usr/%{_lib}
mv %{buildroot}/usr/%{_lib}/condor/libcondor_utils_*.so %{buildroot}/usr/%{_lib}
mv %{buildroot}/usr/%{_lib}/condor/libpyclassad3*.so %{buildroot}/usr/%{_lib}

rm -rf %{buildroot}/usr/share/doc/condor/LICENSE
rm -rf %{buildroot}/usr/share/doc/condor/NOTICE.txt
rm -rf %{buildroot}/usr/share/doc/condor/README

# classad3 shouldn't be distributed yet
rm -rf %{buildroot}/usr/lib*/python%{python3_version}/site-packages/classad3

# Move batch system customization files to /etc, with symlinks in the
# original location. Admins will need to edit these.
install -m 0755 -d -p %{buildroot}%{_sysconfdir}/blahp
for batch_system in condor kubernetes lsf nqs pbs sge slurm; do
    mv %{buildroot}%{_libexecdir}/blahp/${batch_system}_local_submit_attributes.sh %{buildroot}%{_sysconfdir}/blahp
    ln -s ../.../../etc/blahp/${batch_system}_local_submit_attributes.sh \
        %{buildroot}%{_libexecdir}/blahp/${batch_system}_local_submit_attributes.sh
done

install -m0644 -D condor.sysusers.conf %{buildroot}%{_sysusersdir}/condor.conf

#################
%files
%defattr(-,root,root,-)
%doc LICENSE NOTICE.txt 
%doc /usr/share/doc/condor/examples
%dir %_sysconfdir/condor/
%config %_sysconfdir/condor/condor_config
%{_tmpfilesdir}/%{name}.conf
%{_unitdir}/condor.service
# Disabled until HTCondor security fixed.
# % {_unitdir}/condor.socket
%dir %_datadir/condor/
%_datadir/condor/Chirp.jar
%_datadir/condor/CondorJavaInfo.class
%_datadir/condor/CondorJavaWrapper.class
%if 0%{?rhel} >= 7
%_datadir/condor/htcondor.pp
%endif
%dir %_sysconfdir/condor/passwords.d/
%dir %_sysconfdir/condor/tokens.d/
%dir %_sysconfdir/condor/config.d/
%config(noreplace) %{_sysconfdir}/condor/config.d/00-htcondor-9.0.config
%dir /usr/share/condor/config.d/
%_libdir/condor/condor_ssh_to_job_sshd_config_template
%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template
%_sysconfdir/bash_completion.d/condor
%_libdir/libchirp_client.so
%_libdir/libcondor_utils_%{version_}.so
%_libdir/condor/libfmt.so
%_libdir/condor/libfmt.so.10
%_libdir/condor/libfmt.so.10.1.0

%_libdir/condor/libgetpwnam.so
%dir %_libexecdir/condor/
%_libexecdir/condor/cleanup_locally_mounted_checkpoint
%_libexecdir/condor/linux_kernel_tuning
%_libexecdir/condor/accountant_log_fixer
%_libexecdir/condor/condor_chirp
%_libexecdir/condor/condor_ssh
%_libexecdir/condor/sshd.sh
%_libexecdir/condor/get_orted_cmd.sh
%_libexecdir/condor/orted_launcher.sh
%_libexecdir/condor/set_batchtok_cmd
%_libexecdir/condor/cred_producer_krb
%_libexecdir/condor/condor_job_router
%_libexecdir/condor/condor_pid_ns_init
%_libexecdir/condor/condor_urlfetch
%_libexecdir/condor/htcondor_docker_test
%ifarch aarch64 ppc64le x86_64
%_libexecdir/condor/exit_37.sif
%endif
%dir %_libexecdir/condor/singularity_test_sandbox/
%dir %_libexecdir/condor/singularity_test_sandbox/dev/
%dir %_libexecdir/condor/singularity_test_sandbox/proc/
%_libexecdir/condor/singularity_test_sandbox/exit_37
%_libexecdir/condor/condor_limits_wrapper.sh
%_libexecdir/condor/condor_rooster
%_libexecdir/condor/condor_schedd.init
%_libexecdir/condor/condor_ssh_to_job_shell_setup
%_libexecdir/condor/condor_ssh_to_job_sshd_setup
%_libexecdir/condor/condor_power_state
%_libexecdir/condor/condor_kflops
%_libexecdir/condor/condor_mips
%_libexecdir/condor/data_plugin
%_libexecdir/condor/box_plugin.py
%_libexecdir/condor/gdrive_plugin.py
%_libexecdir/condor/common-cloud-attributes-google.py
%_libexecdir/condor/common-cloud-attributes-aws.py
%_libexecdir/condor/common-cloud-attributes-aws.sh
%_libexecdir/condor/onedrive_plugin.py
# TODO: get rid of these
# Not sure where these are getting built
%if 0%{?rhel} <= 7 && ! 0%{?fedora}
%_libexecdir/condor/box_plugin.pyc
%_libexecdir/condor/box_plugin.pyo
%_libexecdir/condor/gdrive_plugin.pyc
%_libexecdir/condor/gdrive_plugin.pyo
%_libexecdir/condor/onedrive_plugin.pyc
%_libexecdir/condor/onedrive_plugin.pyo
%_libexecdir/condor/adstash/__init__.pyc
%_libexecdir/condor/adstash/__init__.pyo
%_libexecdir/condor/adstash/ad_sources/__init__.pyc
%_libexecdir/condor/adstash/ad_sources/__init__.pyo
%_libexecdir/condor/adstash/ad_sources/registry.pyc
%_libexecdir/condor/adstash/ad_sources/registry.pyo
%_libexecdir/condor/adstash/interfaces/__init__.pyc
%_libexecdir/condor/adstash/interfaces/__init__.pyo
%_libexecdir/condor/adstash/interfaces/generic.pyc
%_libexecdir/condor/adstash/interfaces/generic.pyo
%_libexecdir/condor/adstash/interfaces/null.pyc
%_libexecdir/condor/adstash/interfaces/null.pyo
%_libexecdir/condor/adstash/interfaces/registry.pyc
%_libexecdir/condor/adstash/interfaces/registry.pyo
%_libexecdir/condor/adstash/interfaces/opensearch.pyc
%_libexecdir/condor/adstash/interfaces/opensearch.pyo
%endif
%_libexecdir/condor/curl_plugin
%_libexecdir/condor/condor_shared_port
%_libexecdir/condor/condor_defrag
%_libexecdir/condor/interactive.sub
%_libexecdir/condor/condor_gangliad
%_libexecdir/condor/ce-audit.so
%_libexecdir/condor/adstash/__init__.py
%_libexecdir/condor/adstash/adstash.py
%_libexecdir/condor/adstash/config.py
%_libexecdir/condor/adstash/convert.py
%_libexecdir/condor/adstash/utils.py
%_libexecdir/condor/adstash/ad_sources/__init__.py
%_libexecdir/condor/adstash/ad_sources/ad_file.py
%_libexecdir/condor/adstash/ad_sources/generic.py
%_libexecdir/condor/adstash/ad_sources/registry.py
%_libexecdir/condor/adstash/ad_sources/schedd_history.py
%_libexecdir/condor/adstash/ad_sources/startd_history.py
%_libexecdir/condor/adstash/ad_sources/schedd_job_epoch_history.py
%_libexecdir/condor/adstash/interfaces/__init__.py
%_libexecdir/condor/adstash/interfaces/elasticsearch.py
%_libexecdir/condor/adstash/interfaces/opensearch.py
%_libexecdir/condor/adstash/interfaces/generic.py
%_libexecdir/condor/adstash/interfaces/json_file.py
%_libexecdir/condor/adstash/interfaces/null.py
%_libexecdir/condor/adstash/interfaces/registry.py
%_libexecdir/condor/annex
%_mandir/man1/condor_advertise.1.gz
%_mandir/man1/condor_annex.1.gz
%_mandir/man1/condor_check_password.1.gz
%_mandir/man1/condor_check_userlogs.1.gz
%_mandir/man1/condor_chirp.1.gz
%_mandir/man1/condor_config_val.1.gz
%_mandir/man1/condor_dagman.1.gz
%_mandir/man1/condor_fetchlog.1.gz
%_mandir/man1/condor_findhost.1.gz
%_mandir/man1/condor_gpu_discovery.1.gz
%_mandir/man1/condor_history.1.gz
%_mandir/man1/condor_hold.1.gz
%_mandir/man1/condor_job_router_info.1.gz
%_mandir/man1/condor_master.1.gz
%_mandir/man1/condor_off.1.gz
%_mandir/man1/condor_on.1.gz
%_mandir/man1/condor_pool_job_report.1.gz
%_mandir/man1/condor_preen.1.gz
%_mandir/man1/condor_prio.1.gz
%_mandir/man1/condor_q.1.gz
%_mandir/man1/condor_qsub.1.gz
%_mandir/man1/condor_qedit.1.gz
%_mandir/man1/condor_reconfig.1.gz
%_mandir/man1/condor_release.1.gz
%_mandir/man1/condor_remote_cluster.1.gz
%_mandir/man1/condor_reschedule.1.gz
%_mandir/man1/condor_restart.1.gz
%_mandir/man1/condor_rm.1.gz
%_mandir/man1/condor_run.1.gz
%_mandir/man1/condor_set_shutdown.1.gz
%_mandir/man1/condor_ssh_start.1.gz
%_mandir/man1/condor_sos.1.gz
%_mandir/man1/condor_ssl_fingerprint.1.gz
%_mandir/man1/condor_stats.1.gz
%_mandir/man1/condor_status.1.gz
%_mandir/man1/condor_store_cred.1.gz
%_mandir/man1/condor_submit.1.gz
%_mandir/man1/condor_submit_dag.1.gz
%_mandir/man1/condor_test_token.1.gz
%_mandir/man1/condor_token_create.1.gz
%_mandir/man1/condor_token_fetch.1.gz
%_mandir/man1/condor_token_list.1.gz
%_mandir/man1/condor_token_request.1.gz
%_mandir/man1/condor_token_request_approve.1.gz
%_mandir/man1/condor_token_request_auto_approve.1.gz
%_mandir/man1/condor_token_request_list.1.gz
%_mandir/man1/condor_top.1.gz
%_mandir/man1/condor_transfer_data.1.gz
%_mandir/man1/condor_transform_ads.1.gz
%_mandir/man1/condor_update_machine_ad.1.gz
%_mandir/man1/condor_updates_stats.1.gz
%_mandir/man1/condor_upgrade_check.1.gz
%_mandir/man1/condor_urlfetch.1.gz
%_mandir/man1/condor_userlog.1.gz
%_mandir/man1/condor_userprio.1.gz
%_mandir/man1/condor_vacate.1.gz
%_mandir/man1/condor_vacate_job.1.gz
%_mandir/man1/condor_version.1.gz
%_mandir/man1/condor_wait.1.gz
%_mandir/man1/condor_router_history.1.gz
%_mandir/man1/condor_continue.1.gz
%_mandir/man1/condor_suspend.1.gz
%_mandir/man1/condor_router_q.1.gz
%_mandir/man1/condor_ssh_to_job.1.gz
%_mandir/man1/condor_power.1.gz
%_mandir/man1/condor_gather_info.1.gz
%_mandir/man1/condor_router_rm.1.gz
%_mandir/man1/condor_drain.1.gz
%_mandir/man1/condor_ping.1.gz
%_mandir/man1/condor_rmdir.1.gz
%_mandir/man1/condor_tail.1.gz
%_mandir/man1/condor_who.1.gz
%_mandir/man1/condor_now.1.gz
%_mandir/man1/classad_eval.1.gz
%_mandir/man1/classads.1.gz
%_mandir/man1/condor_adstash.1.gz
%_mandir/man1/condor_evicted_files.1.gz
%_mandir/man1/condor_watch_q.1.gz
%_mandir/man1/get_htcondor.1.gz
%_mandir/man1/htcondor.1.gz
# bin/condor is a link for checkpoint, reschedule, vacate
%_bindir/condor_submit_dag
%_bindir/condor_who
%_bindir/condor_now
%_bindir/condor_prio
%_bindir/condor_transfer_data
%_bindir/condor_check_userlogs
%_bindir/condor_q
%_libexecdir/condor/condor_transferer
%_bindir/condor_docker_enter
%_bindir/condor_qedit
%_bindir/condor_qusers
%_bindir/condor_userlog
%_bindir/condor_release
%_bindir/condor_userlog_job_counter
%_bindir/condor_config_val
%_bindir/condor_reschedule
%_bindir/condor_userprio
%_bindir/condor_check_password
%_bindir/condor_check_config
%_bindir/condor_dagman
%_bindir/condor_rm
%_bindir/condor_vacate
%_bindir/condor_run
%_bindir/condor_router_history
%_bindir/condor_router_q
%_bindir/condor_router_rm
%_bindir/condor_vacate_job
%_bindir/condor_findhost
%_bindir/condor_stats
%_bindir/condor_version
%_bindir/condor_history
%_bindir/condor_status
%_bindir/condor_wait
%_bindir/condor_hold
%_bindir/condor_submit
%_bindir/condor_ssh_to_job
%_bindir/condor_power
%_bindir/condor_gather_info
%_bindir/condor_continue
%_bindir/condor_ssl_fingerprint
%_bindir/condor_suspend
%_bindir/condor_test_match
%_bindir/condor_token_create
%_bindir/condor_token_fetch
%_bindir/condor_token_request
%_bindir/condor_token_request_approve
%_bindir/condor_token_request_auto_approve
%_bindir/condor_token_request_list
%_bindir/condor_token_list
%_bindir/condor_scitoken_exchange
%_bindir/condor_drain
%_bindir/condor_ping
%_bindir/condor_tail
%_bindir/condor_qsub
%_bindir/condor_pool_job_report
%_bindir/condor_job_router_info
%_bindir/condor_transform_ads
%_bindir/condor_update_machine_ad
%_bindir/condor_annex
%_bindir/condor_nsenter
%_bindir/condor_evicted_files
%_bindir/condor_adstash
%_bindir/condor_remote_cluster
%_bindir/bosco_cluster
%_bindir/condor_ssh_start
%_bindir/condor_test_token
%_bindir/condor_manifest
# sbin/condor is a link for master_off, off, on, reconfig,
# reconfig_schedd, restart
%_sbindir/condor_advertise
%_sbindir/condor_aklog
%_sbindir/condor_credmon_krb
%_sbindir/condor_c-gahp
%_sbindir/condor_c-gahp_worker_thread
%_sbindir/condor_collector
%_sbindir/condor_credd
%_sbindir/condor_fetchlog
%_sbindir/condor_ft-gahp
%_sbindir/condor_had
%_sbindir/condor_master
%_sbindir/condor_negotiator
%_sbindir/condor_off
%_sbindir/condor_on
%_sbindir/condor_preen
%_sbindir/condor_reconfig
%_sbindir/condor_replication
%_sbindir/condor_restart
%_sbindir/condor_schedd
%_sbindir/condor_set_shutdown
%_sbindir/condor_shadow
%_sbindir/condor_sos
%_sbindir/condor_startd
%_sbindir/condor_starter
%_sbindir/condor_store_cred
%_sbindir/condor_testwritelog
%_sbindir/condor_updates_stats
%_sbindir/ec2_gahp
%_sbindir/condor_gridmanager
%_sbindir/remote_gahp
%_sbindir/rvgahp_client
%_sbindir/rvgahp_proxy
%_sbindir/rvgahp_server
%_sbindir/AzureGAHPServer
%_sbindir/gce_gahp
%_sbindir/arc_gahp
%_libexecdir/condor/condor_gpu_discovery
%_libexecdir/condor/condor_gpu_utilization
%config(noreplace) %_sysconfdir/condor/ganglia.d/00_default_metrics
%defattr(-,condor,condor,-)
%dir %_var/lib/condor/
%dir %_var/lib/condor/execute/
%dir %_var/lib/condor/spool/
%dir %_var/log/condor/
%defattr(-,root,condor,-)
%dir %_var/lib/condor/oauth_credentials
%defattr(-,root,root,-)
%dir %_var/lib/condor/krb_credentials

###### blahp files #######
%config %_sysconfdir/blah.config
%config %_sysconfdir/blparser.conf
%dir %_sysconfdir/blahp/
%config %_sysconfdir/blahp/condor_local_submit_attributes.sh
%config %_sysconfdir/blahp/kubernetes_local_submit_attributes.sh
%config %_sysconfdir/blahp/lsf_local_submit_attributes.sh
%config %_sysconfdir/blahp/nqs_local_submit_attributes.sh
%config %_sysconfdir/blahp/pbs_local_submit_attributes.sh
%config %_sysconfdir/blahp/sge_local_submit_attributes.sh
%config %_sysconfdir/blahp/slurm_local_submit_attributes.sh
%_bindir/blahpd
%_sbindir/blah_check_config
%_sbindir/blahpd_daemon
%dir %_libexecdir/blahp
%_libexecdir/blahp/*

####### procd files #######
%_sbindir/condor_procd
%_sbindir/gidd_alloc
%_sbindir/procd_ctl
%_mandir/man1/procd_ctl.1.gz
%_mandir/man1/gidd_alloc.1.gz
%_mandir/man1/condor_procd.1.gz

####### classads files #######
%defattr(-,root,root,-)
%_libdir/libclassad.so.*
%{_sysusersdir}/condor.conf

#################
%files devel
%{_includedir}/condor/chirp_client.h
%{_includedir}/condor/condor_event.h
%{_includedir}/condor/file_lock.h
%{_includedir}/condor/read_user_log.h
%{_libdir}/condor/libchirp_client.a
%{_libdir}/libclassad.a

####### classads-devel files #######
%defattr(-,root,root,-)
%_bindir/classad_functional_tester
%_bindir/classad_version
%_libdir/libclassad.so
%dir %_includedir/classad/
%_includedir/classad/attrrefs.h
%_includedir/classad/cclassad.h
%_includedir/classad/classad_distribution.h
%_includedir/classad/classadErrno.h
%_includedir/classad/classad.h
%_includedir/classad/classadCache.h
%_includedir/classad/classad_containers.h
%_includedir/classad/classad_flat_map.h
%_includedir/classad/collectionBase.h
%_includedir/classad/collection.h
%_includedir/classad/common.h
%_includedir/classad/debug.h
%_includedir/classad/exprList.h
%_includedir/classad/exprTree.h
%_includedir/classad/fnCall.h
%_includedir/classad/indexfile.h
%_includedir/classad/jsonSink.h
%_includedir/classad/jsonSource.h
%_includedir/classad/lexer.h
%_includedir/classad/lexerSource.h
%_includedir/classad/literals.h
%_includedir/classad/matchClassad.h
%_includedir/classad/natural_cmp.h
%_includedir/classad/operators.h
%_includedir/classad/query.h
%_includedir/classad/sink.h
%_includedir/classad/source.h
%_includedir/classad/transaction.h
%_includedir/classad/util.h
%_includedir/classad/value.h
%_includedir/classad/view.h
%_includedir/classad/xmlLexer.h
%_includedir/classad/xmlSink.h
%_includedir/classad/xmlSource.h

#################
%files kbdd
%defattr(-,root,root,-)
%config(noreplace) %_sysconfdir/condor/config.d/00-kbdd
%_sbindir/condor_kbdd

#################
%if ! 0%{?amzn}
%files vm-gahp
%defattr(-,root,root,-)
%_sbindir/condor_vm-gahp
%_libexecdir/condor/libvirt_simple_script.awk
%endif

#################
%files test
%defattr(-,root,root,-)
%_libexecdir/condor/condor_sinful
%_libexecdir/condor/condor_testingd
%_libexecdir/condor/test_user_mapping

#################
%files -n python3-condor
%defattr(-,root,root,-)
%_bindir/condor_top
%_bindir/classad_eval
%_bindir/condor_watch_q
%_bindir/htcondor
%_libdir/libpyclassad3*.so
%_libexecdir/condor/libclassad_python_user.cpython-3*.so
%_libexecdir/condor/libclassad_python3_user.so
/usr/%{_lib}/python%{python3_version}/site-packages/classad/
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor/
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor-*.egg-info/
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor_cli/
/usr/%{_lib}/python%{python3_version}/site-packages/classad2/
/usr/%{_lib}/python%{python3_version}/site-packages/htcondor2/

%files credmon-local
%doc /usr/share/doc/condor/examples/condor_credmon_oauth
%_sbindir/condor_credmon_oauth
%_sbindir/scitokens_credential_producer
%_libexecdir/condor/credmon
%_var/lib/condor/oauth_credentials/README.credentials
%config(noreplace) %_sysconfdir/condor/config.d/40-oauth-credmon.conf
%ghost %_var/lib/condor/oauth_credentials/CREDMON_COMPLETE
%ghost %_var/lib/condor/oauth_credentials/pid

%files credmon-oauth
%_var/www/wsgi-scripts/condor_credmon_oauth
%config(noreplace) %_sysconfdir/condor/config.d/40-oauth-tokens.conf
%ghost %_var/lib/condor/oauth_credentials/wsgi_session_key

%if 0%{?with_vault_credmon}
%files credmon-vault
%doc /usr/share/doc/condor/examples/condor_credmon_oauth
%_sbindir/condor_credmon_vault
%_bindir/condor_vault_storer
%_libexecdir/condor/credmon
%config(noreplace) %_sysconfdir/condor/config.d/40-vault-credmon.conf
%ghost %_var/lib/condor/oauth_credentials/CREDMON_COMPLETE
%ghost %_var/lib/condor/oauth_credentials/pid
%endif

%files -n minicondor
%config(noreplace) %_sysconfdir/condor/config.d/00-minicondor

%files ap
%config(noreplace) %_sysconfdir/condor/config.d/00-access-point

#################
%post
/sbin/ldconfig
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun -n condor
%systemd_postun_with_restart %{name}.service 
/sbin/ldconfig

%changelog
%autochangelog
