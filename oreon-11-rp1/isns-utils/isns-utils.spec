%global source0_hash 47499f3ce87a832840884dcf3eedbec8c039f472fe921a5378e3b206a3fc1a32
Name:           isns-utils
Version:        0.103
Release:        1%{?dist}
Summary:        The iSNS daemon and utility programs
License:        LGPL-2.1-or-later
URL:            https://github.com/open-iscsi/open-isns
Source0:        https://github.com/open-iscsi/open-isns/archive/v%{version}.tar.gz#/open-isns-%{version}.tar.gz
Source1:        isnsd.service
Patch1:         test_as_installed.patch
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  systemd
BuildRequires:  systemd-devel
# /oreon:deps
%description
The iSNS package contains the daemon and tools to setup a iSNS server,
and iSNS client tools. The Internet Storage Name Service (iSNS) protocol
allows automated discovery, management and configuration of iSCSI and
Fibre Channel devices (using iFCP gateways) on a TCP/IP network.

%package libs
Summary: Shared library files for iSNS
%description libs
Shared library files for iSNS

%package devel
Summary: Development files for iSNS
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
Development files for iSNS

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir open-isns-%{version}
%oreon_prep
%build

%meson -Dsecurity=disabled -Dslp=disabled
%meson_build
%install
%meson_install
chmod 755 %{buildroot}%{_sbindir}/isns*
chmod 755 %{buildroot}%{_libdir}/libisns.so.0
chmod 700 %{buildroot}/var/lib/isns
rm %{buildroot}%{_unitdir}/isnsd.service
rm %{buildroot}%{_unitdir}/isnsd.socket
install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/isnsd.service
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%post

%systemd_post isnsd.service
%postun

%systemd_postun isnsd.service
%preun

%systemd_preun isnsd.service
%triggerun -- isns-utils < 0.91-7

/usr/bin/systemd-sysv-convert --save isnsd >/dev/null 2>&1 ||:
/sbin/chkconfig --del isnsd >/dev/null 2>&1 || :
/bin/systemctl try-restart isnsd.service >/dev/null 2>&1 || :
%ldconfig_scriptlets -n %{name}-libs
%files -f %{oreon_filedir}/main.list
%files -n isns-utils-libs -f %{oreon_filedir}/isns-utils-libs.list
%files -n isns-utils-devel -f %{oreon_filedir}/isns-utils-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.103-4
- Prepare for Oreon 11 (RP1)
