%global source0_hash 7151afed925ad9962cd49134e445c8df40deab06fc56aff2e6ae166c7037a5bc
%global commit      8654bc94ddbfaeec33e3403c6424e2dec8e86c30
%global shortcommit %{sub %{commit} 1 7}
Name:           doh
Version:        0.1^1.%{shortcommit}
Release:        1%{?dist}
Summary:        Application for DNS-over-HTTPS name resolves and lookups
License:        MIT
URL:            https://github.com/curl/doh
Source0:        https://github.com/curl/%{name}/archive/%{commit}/%{name}-8654bc9.tar.gz
Patch:          0001-Makefile-install-manpage-to-DESTDIR.patch
Patch:          0002-Makefile-install-manpage-without-execute-permission.patch
Patch:          0003-Makefile-create-manpage-directory-structure.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libcurl-devel
BuildRequires:  make
# /oreon:deps
%description
A libcurl-using application that resolves a host name using DNS-over-HTTPS
(DoH).  This code uses POST requests unconditionally for this.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n doh-%{commit}

%build

%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
