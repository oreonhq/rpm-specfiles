%global source0_hash f1c58bc7dfb2ea52bb9adb5f0639c67e0f6636c9f31fc809edeb7f9f83e2629a
%if 0%{!?with_python:1}
%global with_python 1
%endif
%if 0%{?with_coverage}
%global coverage_flags -Dwith_coverage=true
%endif
Name:		bluechi
Version:	1.3.0
Release:        1%{?dist}
Summary:        A systemd service controller for multi-nodes environments
License:	LGPL-2.1-or-later AND CC0-1.0
URL:		https://github.com/eclipse-bluechi/bluechi
Source0:        https://github.com/eclipse-%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
%if 0%{?with_coverage}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bluechi = %{version}-%{release}
# /oreon:deps
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

%post selinux

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

%package coverage
Summary:	Code coverage files for BlueChi
%description coverage
This package contains code coverage files created during the build. Those files
will be used during integration tests when creating code coverage report.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -S git_am

ln -s src/bindings/python/pyproject.toml pyproject.toml
%build

%meson -Dapi_bus=system %{?coverage_flags}
%meson_build
pushd src/bindings/python
%pyproject_wheel
popd
%install
%meson_install
%if 0%{?with_coverage}
mkdir -p %{buildroot}/%{_datadir}/bluechi-coverage/bin
cp tests/scripts/gather-code-coverage.sh %{buildroot}/%{_datadir}/bluechi-coverage/bin
cp tests/scripts/setup-src-dir-for-coverage.sh %{buildroot}/%{_datadir}/bluechi-coverage/bin
mkdir -p %{buildroot}/%{_datadir}/bluechi-coverage/unit-test-results
mkdir -p %{buildroot}/%{_localstatedir}/tmp/bluechi-coverage/
%endif
pushd src/bindings/python
%pyproject_install
popd
%oreon_autofiles bluechi-controller usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluechi-agent usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluechi-selinux usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluechi-ctl usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bluechi-is-online usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles python3-bluechi usr/lib/python3*/site-packages/bluechi* usr/lib64/python3*/site-packages/bluechi* usr/bin/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/lib/python3*/site-packages/bluechi* usr/lib64/python3*/site-packages/bluechi* usr/bin/*

%check

%meson_test
%if 0%{?with_coverage}
build-scripts/generate-unit-tests-code-coverage.sh %{_vpath_builddir} %{buildroot}/%{_datadir}
%endif
%files
%files -n bluechi-controller -f %{oreon_filedir}/bluechi-controller.list
%files -n bluechi-agent -f %{oreon_filedir}/bluechi-agent.list
%files -n bluechi-selinux -f %{oreon_filedir}/bluechi-selinux.list
%files -n bluechi-ctl -f %{oreon_filedir}/bluechi-ctl.list
%files -n bluechi-is-online -f %{oreon_filedir}/bluechi-is-online.list
%files -n python3-bluechi -f %{oreon_filedir}/python3-bluechi.list

%changelog

%autochangelog
