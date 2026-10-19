%global source0_hash cd97c68c4d2f9c723f9bf07e5295bb619b8589542c2727362b1b631fa88d2682
%global debug_package %{nil}
%global moduletype services
%global modulenames qm
%global seccomp_json /usr/share/%{modulenames}/seccomp-no-rt.json
%global setup_tool %{_prefix}/share/%{modulenames}/setup
%global _installscriptdir %{_prefix}/lib/%{modulenames}
%global _format() export %1=""; for x in %{modulenames}; do %1+=%2; %%1+=" "; done;
%if "%{?copr_username}" != "rhcontainerbot"
%bcond_with copr
%else
%bcond_without copr
%endif
%global podman_epoch 2
Name: qm
%if %{with copr}
Epoch: 101
%endif
Version: 1.0
%if %{defined autorelease}
Release:        1%{?dist}
%else
Release:        1%{?dist}
%endif
License: GPL-2.0-only
URL: https://github.com/containers/qm
Summary:        Containerized environment for running Quality Management software
Source0:        https://github.com/containers/%{name}/archive/v%{version}.tar.gz
BuildArch: noarch
Requires: parted
Requires: containers-common
Requires: selinux-policy >= %_selinux_policy_version
Requires(post): selinux-policy-base >= %_selinux_policy_version
Requires(post): selinux-policy-any >= %_selinux_policy_version
Recommends: selinux-policy-targeted >= %_selinux_policy_version
Requires(post): policycoreutils
Requires(post): libselinux-utils
Requires: podman >= %{podman_epoch}:4.5
Requires: jq
# oreon:deps
BuildRequires:  bluechi-selinux
BuildRequires:  container-selinux
BuildRequires:  git-core
BuildRequires:  golang-github-cpuguy83-md2man
BuildRequires:  make
BuildRequires:  pkgconfig(systemd)
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
# /oreon:deps
%description
This package allow users to setup an environment which prevents applications
and container tools from interfering with other all other processes on the
system.

The QM runs its own version of systemd and Podman to isolate not only the
applications and containers launched by systemd and Podman but systemd and
Podman themselves.

Software install into the QM environment under `/usr/lib/qm/rootfs` is
automatically isolated from the host. If developers need to further
isolate there applications from other processes in the QM they should
use container tools like Podman.

###################
### qmctl ###
###################

%package ctl
Summary:	QM service controller command line tool
Requires:	%{name} = %{version}-%{release}
Requires:	python3 >= 3.9
%description ctl
QM is a containerized environment for running Quality Management software.
This package contains the service controller command line tool for managing
and interacting with QM containers and services.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -Sgit -n %{name}-%{version}
sed -i 's/^install: man all/install:/' Makefile

%build

%if %{defined legacy_var_run}
sed -i 's|^/run/|/var/run/|' qm.fc
%endif
%{__make} all
%install
install -d %{buildroot}%{_sysconfdir}/containers/containers.conf.d
%_format MODULES $x.pp.bz2
%{__make} DESTDIR=%{buildroot} DATADIR=%{_datadir} install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%_format MODULES %{_datadir}/selinux/packages/$x.pp.bz2
. %{_sysconfdir}/selinux/config
%selinux_modules_install -s ${SELINUXTYPE} $MODULES
/usr/share/qm/create-seccomp-rules
/usr/share/qm/comment-tz-local # FIX-ME GH-issue: 367
modprobe ip_tables || true
%preun

if [ $1 = 0 ]; then
   systemctl stop qm
   %{setup_tool} --remove-qm-rootfs &> /dev/null
fi
%postun

if [ $1 -eq 0 ]; then
   . %{_sysconfdir}/selinux/config
   %selinux_modules_uninstall -s ${SELINUXTYPE} %{modulenames}
   if [ -f %{seccomp_json} ]; then
     /bin/rm -f %{seccomp_json}
   fi
fi
%{!?_licensedir:%global license %doc}
%files -f %{oreon_filedir}/main.list
%files -n qm-ctl -f %{oreon_filedir}/qm-ctl.list

%changelog

%autochangelog
