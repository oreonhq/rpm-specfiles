%global source0_hash 281ec5a92b067942ad29749d7d31dcac972136a223421ca8a1c82d8f50485c1e

%global commit 96d9e0b6e81330c61c954c6bc73a2302276fcda1
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global date 20251004
%global _hardened_build 1

Name: odhcp6c
Version: 0
Release: 0.30.%{date}git%{shortcommit}%{?dist}
Summary: Embedded DHCPv6 and RA client
# License is GPLv2 except:
# ./src/md5.c: ISC
# ./src/md5.h: ISC
# Automatically converted from old format: GPLv2 and ISC - review is highly recommended.
License: GPL-2.0-only AND ISC
URL: https://git.openwrt.org/?p=project/odhcp6c.git
# Source fetched from git:
# git clone https://git.openwrt.org/project/odhcp6c.git
# cd odhcp6c
# git archive --format=tar.gz --prefix=odhcp6c-%%{commit}/ %%{commit} > ../odhcp6c-%%{commit}.tar.gz
Source0: %{name}-%{commit}.tar.gz
Source1: odhcp6c@.service
BuildRequires: cmake
BuildRequires: gcc
%if 0%{?rhel}
BuildRequires: systemd
%else
BuildRequires: systemd-rpm-macros
%endif

%description
odhcp6c is a minimal DHCPv6 and Router Advertisement client for use in embedded
Linux systems, especially routers. It compiles to only about 35 KB.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}

%build
%{cmake}
%{cmake_build}

%install
%{cmake_install}
install -D -p -m 0755 odhcp6c-example-script.sh %{buildroot}%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
install -D -p -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/odhcp6c@.service

%files
%doc README
%license COPYING
%{_bindir}/odhcp6c
%dir %{_sysconfdir}/odhcp6c
%{_sysconfdir}/odhcp6c/odhcp6c-example-script.sh
%{_unitdir}/odhcp6c@.service

%changelog
%autochangelog
