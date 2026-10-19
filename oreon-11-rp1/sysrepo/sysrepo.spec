%global source0_hash c897206797427c79c4646baa1d8abe539bbc70af884ac869e827ff9f09d7fcc8
Name: sysrepo
Version: 3.7.11
Release:        2%{?dist}
Summary:        YANG-based configuration and operational data store
Url: https://github.com/sysrepo/sysrepo
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source2: sysrepo.sysusers
Source3: sysrepo-plugind.sysusers
Source4: sysrepo-plugind.service
License: BSD-3-Clause
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(cmocka)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libyang)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%package devel
Summary:   Development files for sysrepo
Requires:  %{name}%{?_isa} = %{version}-%{release}
Requires:  pkgconfig
%package plugind
Summary:   sysrepo plugin daemon
Requires:  %{name}%{?_isa} = %{version}-%{release}
%package tools
Summary:   sysrepo executable tools
Requires:  %{name}%{?_isa} = %{version}-%{release}
%description
YANG-based configuration and operational data store - runtime Applications can
use sysrepo to store their configuration modeled by provided YANG model
instead of using e.g. flat configuration files. Sysrepo will ensure data
consistency of the data stored in the data store and enforce data constraints
defined by YANG model.

The library is implemented in C and provides an API for other software
to use for accessing sysrepo datastore.

%description devel
Headers of sysrepo library.

%description plugind
Sysrepo plugin daemon and service.

%description tools
Executable tools for sysrepo:

* sysrepoctl - manipulation of YANG modules (schemas)
* sysrepocfg - manipulation of YANG instance data

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake -DCMAKE_BUILD_TYPE=RELWITHDEBINFO -DSYSREPO_UMASK=007 -DSYSREPO_GROUP=sysrepo -DNACM_SRMON_DATA_PERM=660
%cmake_build
%install
%cmake_install
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysusersdir}/sysrepo.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysusersdir}/sysrepo-plugind.conf
install -D -p -m 0644 %{SOURCE4} %{buildroot}%{_unitdir}/sysrepo-plugind.service
mkdir -p -m=770 %{buildroot}%{_sysconfdir}/sysrepo
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre

    getent group sysrepo 1>/dev/null || groupadd -r sysrepo
%postun

rm -rf /dev/shm/sr_*
rm -rf /dev/shm/srsub_*
%pre plugind

    getent passwd sysrepo-plugind 1>/dev/null || useradd -r -M -s /sbin/nologin -c "sysrepo plugind user" -g sysrepo sysrepo-plugind
if [ $1 -gt 1 ] ; then
rm -rf /dev/shm/sr_*
rm -rf /dev/shm/srsub_*
fi
%post plugind

%systemd_post %{name}-plugind.service
%postun plugind

%systemd_postun_with_restart %{name}-plugind.service
%files -f %{oreon_filedir}/main.list
%files -n sysrepo-devel -f %{oreon_filedir}/sysrepo-devel.list
%files -n sysrepo-plugind -f %{oreon_filedir}/sysrepo-plugind.list
%files -n sysrepo-tools -f %{oreon_filedir}/sysrepo-tools.list

%changelog

%autochangelog
