%global source0_hash c856aabe038880aaab7ffeed79e8d28673d16c71ce540bfec1c1bd4256496193
%{!?_hardened_build:%global _hardened_build 1}
%if %{?_hardened_build}%{!?_hardened_build:0}
%global cflags_harden -fpie
%global ldflags_harden -pie -z relro -z now
%endif
Summary:        An user-space IPIP encapsulation daemon for the ampr network
Name: amprd
Version: 3.0.1
Release:        1%{?dist}
License: GPL-3.0-or-later
URL: http://www.yo2loj.ro/hamprojects/
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
Source0:        http://www.yo2loj.ro/hamprojects/%{name}-%{version}.tgz
Source1: amprd.service
Patch0: amprd-3.0-install-fix.patch
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
An user-space IPIP encapsulation daemon with automatic RIPv2 multicast
processing and multiple tunnel support for the ampr network.
All RIPv2 processing, encapsulation, decapsulation and routing happens
inside the daemon and it offers one or more virtual TUN interfaces to
the system for your 44net traffic.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

dos2unix minGlue.h

%build

make %{?_smp_mflags} CFLAGS="%{optflags} %{?cflags_harden}" LDFLAGS="%{?__global_ldflags} %{?ldflags_harden}"
%install
make %{?_smp_mflags} DESTDIR=%{buildroot} SBINDIR=%{buildroot}%{_sbindir} install
install -Dpm 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
install -Dd %{buildroot}%{_datadir}/%{name}
install -Dpm 644 -t %{buildroot}%{_datadir}/%{name} startup_example.sh interfaces_example
%oreon_autofiles main

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
