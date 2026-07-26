%global source0_hash 8aae67f4823edb76dff036808137888d2479477ec1e52aa86d6cecd26d58aa23

Name:		cowpatty
Version:	4.8
Release:	1%{?dist}
Summary:	WPA password cracker

# All the source files are BSD-3-Clause, except md5.c, which is GPL-2.0-only.
License:	BSD-3-Clause AND GPL-2.0-only

URL:		https://www.willhackforsushi.com/?page_id=50
Source0:	https://github.com/joswr1ght/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Patches borrowed from Debian.
# 0: Fixes "incompatible pointer type" compilation error
# 1: Fixes integer overflow bug
Patch0:	0000-incompatible-pointer-types.patch
Patch1:	0001-kali-overflow.patch

# Fix usage of CFLAGS in the Makefile and parallel build issues
Patch2:	0002-fix-makefile.patch

BuildRequires:  gcc
BuildRequires:	libpcap-devel
BuildRequires:	openssl-devel	
BuildRequires: make
		
%description
Cowpatty is designed to audit the pre-shared key (PSK) selection for WPA 
networks based on the TKIP protocol. It can perform both dictionary and 
computed rainbow table attacks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%make_build

%install
%make_install BINDIR="%{_bindir}"

install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p %{name}.1 genpmk.1 %{buildroot}%{_mandir}/man1/

%files
%doc AUTHORS COPYING README FAQ TODO CHANGELOG
%{_bindir}/%{name}
%{_bindir}/genpmk
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/genpmk.1*

%changelog
%autochangelog
