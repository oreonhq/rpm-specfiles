%global source0_hash 9386c0b34ae9dd35e61c254980fd9f4e64c510f38fc97fe939b51625418f89f7

Name:           accel-ppp
Version:        1.14.0
Release:        %autorelease
Summary:        High-performance VPN and broadband protocol server
License:        GPL-2.0-Only OR GPL-2.0-Or-Later OR MIT
URL:            https://accel-ppp.org/
Source:         https://github.com/accel-ppp/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		0001-Add-Fedora-CPack-option.patch
Patch1:		0002-Allow-building-in-source-directory-needed-for-EPEL8.patch
Patch2:		0003-Add-EPEL-10-CPack-option.patch
ExcludeArch:	%{ix86}

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  openssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  systemd-rpm-macros

%description
accel-ppp is a Linux kernel-accelerated implementation of PPPoE, PPTP, L2TP
and other VPN and broadband protocols.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%if 0%{?rhel}
%cmake -DCMAKE_BUILD_TYPE=Release -DCPACK_TYPE=Centos%{rhel}
%endif
%if 0%{?fedora}
%cmake -DCMAKE_BUILD_TYPE=Release -DCPACK_TYPE=Fedora
%endif
%cmake_build

%install
%cmake_install

%post
%systemd_post accel-ppp.service

%preun
%systemd_preun accel-ppp.service

%postun
%systemd_postun accel-ppp.service

%files
%{_bindir}/accel-cmd
%{_bindir}/accel-pppd
%dir %{_datadir}/accel-ppp
%dir %{_datadir}/accel-ppp/l2tp
%{_datadir}/accel-ppp/l2tp/dictionary*
%dir %{_datadir}/accel-ppp/radius
%{_datadir}/accel-ppp/radius/dictionary*
%dir %{_libdir}/accel-ppp
%{_libdir}/accel-ppp/*
%{_mandir}/man1/accel-cmd.1.gz
%{_mandir}/man5/accel-ppp.conf.5.gz
%{_sysconfdir}/accel-ppp.conf.dist
%{_unitdir}/accel-ppp.service
%license COPYING

%changelog
%autochangelog
