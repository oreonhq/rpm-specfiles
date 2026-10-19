%global source0_hash c73ffd58c461a88504cca36e5a29981dc68b78f8fdd31d7c546bc204fad7c435
%global ver_maj 1
%global ver_min 4
%global ver_patch 2
Name:		pixiewps	
Version:	%{ver_maj}.%{ver_min}.%{ver_patch}
Release:        21%{?dist}
Summary:        An offline Wi-Fi Protected Setup brute-force utility
License:	GPL-3.0-only
URL:		https://github.com/wiire-a/pixiewps
Source0:        https://github.com/wiire-a/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:		0001-unbundle_tc.patch
Patch1:		0002-unbundle_tfm.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libtomcrypt-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  tomsfastmath-devel
# /oreon:deps
%description
Pixiewps is a tool written in C used to bruteforce offline the WPS PIN
exploiting the low or non-existing entropy of some software implementations,
the so-called "pixie-dust attack" discovered by Dominique Bongard in summer
2014.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
sed -i "s|^\tinstall -|\t\$(INSTALL) -|" Makefile
rm -rf src/crypto/tfm
rm -f src/tc/*.h
rm -f src/tc/aes.c
rm -f src/tc/aes_tab.c
rm -f src/tc/sha256.c

%build

%make_build CFLAGS="%{build_cflags}" OPENSSL=1
%install
%make_install PREFIX="%{_prefix}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
