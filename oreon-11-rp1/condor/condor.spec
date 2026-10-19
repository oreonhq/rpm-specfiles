%global source0_hash 68eb2e0c5dffe757b0d68391af5f2a337138ca4b9fc70121284590315a244581
%global version         25.13.2
%global version_ %(tr . _ <<< %{version})
%global with_vault_credmon 0
Name:           condor
Version:        25.13.2
Release:        1%{?dist}
Summary:        HTCondor: High Throughput Computing
License:        Apache-2.0
URL:            http://htcondor.org
Source0:        https://github.com/htcondor/htcondor/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch: %{ix86}
Patch1: exit_37.sif.patch
Patch2: unified-bin.patch
Patch3: CVE-2025-30093.patch
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$
%global __requires_exclude ^libfmt\\.so.*$
Requires: /usr/sbin/sendmail
Requires: python3
Requires: python3-cryptography
Requires: voms
Requires: krb5-libs
Requires: libcom_err
Requires: munge-libs
Requires: openssl-libs
Requires: scitokens-cpp >= 0.6.2
Requires: systemd-libs
Requires: rsync
Requires: condor-upgrade-checks
Requires: openssh-server
Requires: net-tools
Requires: perl(Date::Manip)
Requires: perl(FindBin)
Requires: python3-condor = %{version}-%{release}
Requires: python3-requests
Recommends: bash-completion
Obsoletes: %{name}-procd < 10.8.0
Provides: %{name}-procd = %{version}-%{release}
Obsoletes: %{name}-openstack-gahp < 10.8.0
Provides: %{name}-openstack-gahp = %{version}-%{release}
Obsoletes: %{name}-classads < 10.8.0
Provides: %{name}-classads = %{version}-%{release}
Obsoletes: %{name}-classads-devel < 10.8.0
Provides: %{name}-classads-devel = %{version}-%{release}
# oreon:deps
BuildRequires:  bind-utils
BuildRequires:  boost-devel
BuildRequires:  boost-python3-devel
BuildRequires:  boost-static
BuildRequires:  cmake
BuildRequires:  expat-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  glibc-static
BuildRequires:  krb5-devel
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libcurl-devel
BuildRequires:  libuuid-devel
BuildRequires:  libvirt-devel
BuildRequires:  libxml2
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  munge-devel
BuildRequires:  nss-devel
BuildRequires:  openldap-devel
BuildRequires:  openssl-devel
BuildRequires:  pam-devel
BuildRequires:  patch
BuildRequires:  pcre2-devel
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(XML::Parser)
BuildRequires:  perl-generators
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  scitokens-cpp-devel
BuildRequires:  sqlite-devel
BuildRequires:  systemd-devel
BuildRequires:  systemd-units
BuildRequires:  voms-devel
# /oreon:deps
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

%post annex-ec2

%preun annex-ec2

if [ $1 == 0 ]; then
    /bin/systemctl disable condor-annex-ec2
fi
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
       -DPACKAGEID:STRING=%{version}-%{release} \
       -DCONDOR_PACKAGE_BUILD:BOOL=TRUE \
       -DCONDOR_RPMBUILD:BOOL=TRUE \
       -DCMAKE_INSTALL_PREFIX:PATH=/
%cmake_build
%install
function populate {
  _dest="$1"; shift; _src="$*"
  mkdir -p "%{buildroot}/$_dest"
  mv $_src "%{buildroot}/$_dest"
}
rm -rf %{buildroot}
%cmake_install
%ifarch s390x
mv %{buildroot}/usr/lib/* %{buildroot}/usr/%{_lib}
%endif
ln -s ../..%{_libdir}/condor/condor_ssh_to_job_sshd_config_template %{buildroot}/%_sysconfdir/condor/condor_ssh_to_job_sshd_config_template
mv %{buildroot}/usr/share/doc/condor-%{version} %{buildroot}/usr/share/doc/condor
populate /usr/share/doc/condor/examples %{buildroot}/usr/share/doc/condor/etc/examples/*
mkdir -p %{buildroot}/%{_sysconfdir}/condor
LIB=$(echo %{?_libdir} | sed -e 's:/usr/\(.*\):\1:')
if [ "$LIB" = "%_libdir" ]; then
  echo "_libdir does not contain /usr, sed expression needs attention"
  exit 1
fi
mkdir -p -m0755 %{buildroot}/%{_sysconfdir}/condor/config.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/passwords.d
mkdir -p -m0700 %{buildroot}/%{_sysconfdir}/condor/tokens.d
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-htcondor-9.0.config
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-minicondor
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-access-point
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/00-kbdd
populate %_sysconfdir/condor/config.d %{buildroot}/usr/share/doc/condor/examples/50ec2.config
mkdir -p -m0755 %{buildroot}/usr/share/condor/config.d
mkdir -p -m0755 %{buildroot}/%{_var}/log/condor
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/spool
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/execute
mkdir -p -m0755 %{buildroot}/%{_var}/lib/condor/krb_credentials
mkdir -p -m2770 %{buildroot}/%{_var}/lib/condor/oauth_credentials
rm -f %{buildroot}%{_bindir}/make-ap-from-tarball
rm -f %{buildroot}%{_bindir}/make-personal-from-tarball
rm -f %{buildroot}%{_sbindir}/condor_configure
rm -f %{buildroot}%{_sbindir}/condor_install
rm -f %{buildroot}/%{_mandir}/man1/condor_configure.1
rm -f %{buildroot}/%{_mandir}/man1/condor_install.1
mkdir -p %{buildroot}/%{_var}/www/wsgi-scripts/condor_credmon_oauth
mv %{buildroot}/%{_libexecdir}/condor/condor_credmon_oauth.wsgi %{buildroot}/%{_var}/www/wsgi-scripts/condor_credmon_oauth/condor_credmon_oauth.wsgi
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/config/condor/40-oauth-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-credmon.conf
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/config/condor/40-oauth-tokens.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-oauth-tokens.conf
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/README.credentials %{buildroot}/%{_var}/lib/condor/oauth_credentials/README.credentials
%if 0%{?with_vault_credmon}
mv %{buildroot}/usr/share/doc/condor/examples/condor_credmon_oauth/config/condor/40-vault-credmon.conf %{buildroot}/%{_sysconfdir}/condor/config.d/40-vault-credmon.conf
%else
rm -f  %{buildroot}%{_bindir}/condor_vault_storer
rm -f  %{buildroot}%{_sbindir}/condor_credmon_vault
%endif
mkdir -p %{buildroot}%{_tmpfilesdir}
install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor-tmpfiles.conf %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dp -m0755 %{buildroot}/usr/share/doc/condor/examples/condor-annex-ec2 %{buildroot}%{_libexecdir}/condor/condor-annex-ec2
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor-annex-ec2.service %{buildroot}%{_unitdir}/condor-annex-ec2.service
install -m 0644 %{buildroot}/usr/share/doc/condor/examples/condor.service %{buildroot}%{_unitdir}/condor.service
mkdir -p %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/Chirp.jar %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/CondorJava*.class %{buildroot}/usr/share/condor
mv %{buildroot}/usr/%{_lib}/condor/libchirp_client.so %{buildroot}/usr/%{_lib}
mv %{buildroot}/usr/%{_lib}/condor/libcondor_utils_*.so %{buildroot}/usr/%{_lib}
mv %{buildroot}/usr/%{_lib}/condor/libpyclassad3*.so %{buildroot}/usr/%{_lib}
rm -rf %{buildroot}/usr/share/doc/condor/LICENSE
rm -rf %{buildroot}/usr/share/doc/condor/NOTICE.txt
rm -rf %{buildroot}/usr/share/doc/condor/README
rm -rf %{buildroot}/usr/lib*/python%{python3_version}/site-packages/classad3
install -m 0755 -d -p %{buildroot}%{_sysconfdir}/blahp
for batch_system in condor kubernetes lsf nqs pbs sge slurm; do
    mv %{buildroot}%{_libexecdir}/blahp/${batch_system}_local_submit_attributes.sh %{buildroot}%{_sysconfdir}/blahp
    ln -s ../.../../etc/blahp/${batch_system}_local_submit_attributes.sh \
        %{buildroot}%{_libexecdir}/blahp/${batch_system}_local_submit_attributes.sh
done
install -m0644 -D condor.sysusers.conf %{buildroot}%{_sysusersdir}/condor.conf
%oreon_autofiles condor-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles condor-kbdd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-test usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-vm-gahp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-condor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-credmon-local usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-credmon-oauth usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles minicondor usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-ap usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-annex-ec2 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles condor-upgrade-checks usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

/sbin/ldconfig
%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun -n condor

%systemd_postun_with_restart %{name}.service 
/sbin/ldconfig
%files -f %{oreon_filedir}/main.list
%files -n condor-devel -f %{oreon_filedir}/condor-devel.list
%files -n condor-kbdd -f %{oreon_filedir}/condor-kbdd.list
%files -n condor-test -f %{oreon_filedir}/condor-test.list
%files -n condor-vm-gahp -f %{oreon_filedir}/condor-vm-gahp.list
%files -n python3-condor -f %{oreon_filedir}/python3-condor.list
%files -n condor-credmon-local -f %{oreon_filedir}/condor-credmon-local.list
%files -n condor-credmon-oauth -f %{oreon_filedir}/condor-credmon-oauth.list
%files -n minicondor -f %{oreon_filedir}/minicondor.list
%files -n condor-ap -f %{oreon_filedir}/condor-ap.list
%files -n condor-annex-ec2 -f %{oreon_filedir}/condor-annex-ec2.list
%files -n condor-upgrade-checks -f %{oreon_filedir}/condor-upgrade-checks.list

%changelog

%autochangelog
