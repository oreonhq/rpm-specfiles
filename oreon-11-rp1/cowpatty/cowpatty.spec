%global source0_hash 8aae67f4823edb76dff036808137888d2479477ec1e52aa86d6cecd26d58aa23
Name:		cowpatty
Version:	4.8
Release:        1%{?dist}
Summary:        WPA password cracker
License:	BSD-3-Clause AND GPL-2.0-only
URL:		https://www.willhackforsushi.com/?page_id=50
Source0:        https://github.com/joswr1ght/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:	0000-incompatible-pointer-types.patch
Patch1:	0001-kali-overflow.patch
Patch2:	0002-fix-makefile.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libpcap-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Cowpatty is designed to audit the pre-shared key (PSK) selection for WPA 
networks based on the TKIP protocol. It can perform both dictionary and 
computed rainbow table attacks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install BINDIR="%{_bindir}"
install -m 755 -d %{buildroot}%{_mandir}/man1
install -m 644 -p %{name}.1 genpmk.1 %{buildroot}%{_mandir}/man1/
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
