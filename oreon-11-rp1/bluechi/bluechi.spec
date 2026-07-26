%global source0_hash f0ddb8b33c2edc200e73709cd965e43ea830495adebc6d4f6c4398cb4c5ff883

# python bluechi module is enabled by default, it can be disabled passing `--define "with_python 0"` option to rpmbuild
%if 0%{!?with_python:1}
%global with_python 1
%endif

# coverage collection is disabled by default , it can be enabled passing `--define "with_coverage 1"` option to rpmbuild
%if 0%{?with_coverage}
%global coverage_flags -Dwith_coverage=true
%endif

Name:		bluechi
Version:	1.2.2
Release:	1%{?dist}
Summary:	A systemd service controller for multi-nodes environments
License:	LGPL-2.1-or-later AND CC0-1.0
URL:		https://github.com/eclipse-bluechi/bluechi
Source0:	%{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

# Required to apply the patch
BuildRequires:	git-core
BuildRequires:	gcc
# Meson needs to detect C++, because part of inih library (which we don't use) provides C++ functionality
BuildRequires:	gcc-c++
BuildRequires:	meson
BuildRequires:	libselinux-devel
BuildRequires:	systemd-devel
BuildRequires:	systemd-rpm-macros
BuildRequires:	golang-github-cpuguy83-md2man

%if 0%{?with_coverage}
BuildRequires:	lcov
BuildRequires: sed
%endif

%description
BlueChi is a systemd service controller for multi-nodes environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).

##########################
### bluechi-controller ###
##########################

%package	controller
Summary:	BlueChi service controller
Requires:	systemd
Recommends:	bluechi-selinux

%if 0%{?with_coverage}
Requires:	bluechi-coverage = %{version}-%{release}
%endif

Obsoletes:	hirte < 0.6.0
Provides:	hirte = %{version}-%{release}
Obsoletes:	bluechi < 0.7.0
Provides:	bluechi = %{version}-%{release}

%description controller
BlueChi is a systemd service controller for multi-nodes environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).
This package contains the controller service.

%post controller
%systemd_post bluechi-controller.service

%preun controller
%systemd_preun bluechi-controller.service

%postun controller
%systemd_postun_with_restart bluechi-controller.service

%files controller
%ghost %{_sysconfdir}/bluechi/controller.conf
%dir %{_sysconfdir}/bluechi
%dir %{_sysconfdir}/bluechi/controller.conf.d
%doc README.md
%doc README.developer.md
%license LICENSE
%{_libexecdir}/bluechi-controller
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Job.xml
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Controller.xml
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Monitor.xml
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Node.xml
%{_datadir}/dbus-1/system.d/org.eclipse.bluechi.conf
%{_datadir}/bluechi/config/controller.conf
%{_mandir}/man1/bluechi-controller.*
%{_mandir}/man5/bluechi-controller.conf.*
%{_sysconfdir}/bluechi/controller.conf.d/README.md
%{_unitdir}/bluechi-controller.service
%{_unitdir}/bluechi-controller.socket

# Create UDS directory on install and setup tmpfile for reboots
%dir %{_rundir}/bluechi
%attr(700, root, root) %{_rundir}/bluechi
%{_tmpfilesdir}/%{name}.conf

#####################
### bluechi-agent ###
#####################

%package agent
Summary:	BlueChi service controller agent
Requires:	systemd
Recommends:	bluechi-selinux

%if 0%{?with_coverage}
Requires:	bluechi-coverage = %{version}-%{release}
%endif

Obsoletes:	hirte-agent < 0.6.0
Provides:	hirte-agent = %{version}-%{release}

%description agent
BlueChi is a systemd service controller for multi-nodes environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).
This package contains the node agent.

%post agent
%systemd_post bluechi-agent.service

%preun agent
%systemd_preun bluechi-agent.service

%postun agent
%systemd_postun_with_restart bluechi-agent.service

%files agent
%ghost %{_sysconfdir}/bluechi/agent.conf
%dir %{_sysconfdir}/bluechi
%dir %{_sysconfdir}/bluechi/agent.conf.d
%doc README.md
%license LICENSE
%{_libexecdir}/bluechi-agent
%{_libexecdir}/bluechi-proxy
%{_datadir}/dbus-1/system.d/org.eclipse.bluechi.Agent.conf
%{_datadir}/bluechi-agent/config/agent.conf
%{_datadir}/dbus-1/interfaces/org.eclipse.bluechi.Agent.xml
%{_mandir}/man1/bluechi-agent.*
%{_mandir}/man1/bluechi-proxy.*
%{_mandir}/man5/bluechi-agent.conf.*
%{_sysconfdir}/bluechi/agent.conf.d/README.md
%{_unitdir}/bluechi-agent.service
%{_userunitdir}/bluechi-agent.service
%{_unitdir}/bluechi-proxy@.service
%{_userunitdir}/bluechi-proxy@.service
%{_unitdir}/bluechi-dep@.service
%{_userunitdir}/bluechi-dep@.service

#######################
### bluechi-selinux ###
#######################

%package selinux
Summary:	BlueChi SELinux policy
BuildArch:	noarch
BuildRequires:	checkpolicy
BuildRequires:	selinux-policy-devel

%if "%{_selinux_policy_version}" != ""
Requires:	selinux-policy >= %{_selinux_policy_version}
%endif

Requires(post):	policycoreutils
%if "%{_selinux_policy_version}" != ""
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-any >= %_selinux_policy_version
%endif

Obsoletes:	hirte-selinux < 0.6.0
Provides:	hirte-selinux = %{version}-%{release}

%description selinux
SELinux policy associated with the bluechi and bluechi-agent daemons

%files selinux
%{_datadir}/selinux/devel/include/services/bluechi.if
%{_datadir}/selinux/packages/bluechi.pp.bz2
%{_mandir}/man8/bluechi*selinux.*

%post selinux
# Remove hirte policy
if [ $1 -eq 1 ]; then
   semodule -N -X 200 -r hirte 2>/dev/null || true
fi
. %{_sysconfdir}/selinux/config
%selinux_modules_install -s ${SELINUXTYPE} %{_datadir}/selinux/packages/bluechi.pp.bz2
restorecon -R %{_bindir}/bluechi* &> /dev/null || :
restorecon -R %{_rundir}/bluechi/ &> /dev/null || :
restorecon -R %{_localstatedir}/%{_rundir}/bluechi/ &> /dev/null || :

%postun selinux
if [ $1 -eq 0 ]; then
   . %{_sysconfdir}/selinux/config
   %selinux_modules_uninstall -s ${SELINUXTYPE} bluechi
   restorecon -R %{_bindir}/bluechi* &> /dev/null || :
   restorecon -R %{_rundir}/bluechi/ &> /dev/null || :
   restorecon -R %{_localstatedir}/%{_rundir}/bluechi/ &> /dev/null || :
fi

###################
### bluechi-ctl ###
###################

%package ctl
Summary:	BlueChi service controller command line tool
Requires:	%{name} = %{version}-%{release}

%if 0%{?with_coverage}
Requires:	bluechi-coverage = %{version}-%{release}
%endif

Obsoletes:	hirte-ctl < 0.6.0
Provides:	hirte-ctl = %{version}-%{release}

%description ctl
BlueChi is a systemd service controller for multi-nodes environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).
This package contains the service controller command line tool.

%files ctl
%doc README.md
%license LICENSE
%{_bindir}/bluechictl
%{_mandir}/man1/bluechictl.*

#########################
### bluechi-is-online ###
#########################

%package is-online
Summary:	Command line tool to monitor the connection state of BlueChi's components
Recommends:	bluechi-controller = %{version}-%{release}
Recommends:	bluechi-agent = %{version}-%{release}

%if 0%{?with_coverage}
Requires:	bluechi-coverage = %{version}-%{release}
%endif

%description is-online
BlueChi is a systemd service controller for multi-nodes environments with a
predefined number of nodes and with a focus on highly regulated environment
such as those requiring functional safety (for example in cars).
This package contains a command line tool for checking and monitoring the
connection state of BlueChi's core components.

%files is-online
%doc README.md
%license LICENSE
%{_bindir}/bluechi-is-online
%{_mandir}/man1/bluechi-is-online.*

#######################
### python3-bluechi ###
#######################

%if %{with_python}
%package -n python3-bluechi
Summary:	Python bindings for BlueChi
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-wheel
Requires:	python3-dasbus

Obsoletes:	python3-hirte < 0.6.0
Provides:	python3-hirte = %{version}-%{release}

%description -n python3-bluechi
bluechi is a python module to access the public D-Bus API of BlueChi project.
It contains typed python code that is auto-generated from BlueChi's
API description and manually written code to simplify recurring tasks.

%files -n python3-bluechi
%{python3_sitelib}
%endif

########################
### bluechi-coverage ###
########################

%if 0%{?with_coverage}
%package coverage
Summary:	Code coverage files for BlueChi

%description coverage
This package contains code coverage files created during the build. Those files
will be used during integration tests when creating code coverage report.

%files coverage
%license LICENSE
%{_datadir}/bluechi-coverage/bin/*
%{_datadir}/bluechi-coverage/*
%dir %{_localstatedir}/tmp/bluechi-coverage/
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

%if %{with_python}
ln -s src/bindings/python/pyproject.toml pyproject.toml
%generate_buildrequires
%pyproject_buildrequires
%endif

%build
%meson -Dapi_bus=system %{?coverage_flags}
%meson_build

%if %{with_python}
pushd src/bindings/python
%pyproject_wheel
popd
%endif

%install
%meson_install

%if 0%{?with_coverage}
mkdir -p %{buildroot}/%{_datadir}/bluechi-coverage/bin
cp tests/scripts/gather-code-coverage.sh %{buildroot}/%{_datadir}/bluechi-coverage/bin
cp tests/scripts/setup-src-dir-for-coverage.sh %{buildroot}/%{_datadir}/bluechi-coverage/bin

mkdir -p %{buildroot}/%{_datadir}/bluechi-coverage/unit-test-results

mkdir -p %{buildroot}/%{_localstatedir}/tmp/bluechi-coverage/
%endif

%if %{with_python}
pushd src/bindings/python
%pyproject_install
popd
%endif

%check
%meson_test

%if 0%{?with_coverage}
# Generate code coverage report from unit tests execution
build-scripts/generate-unit-tests-code-coverage.sh %{_vpath_builddir} %{buildroot}/%{_datadir}
%endif

%changelog
%autochangelog
