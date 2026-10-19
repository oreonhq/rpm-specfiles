%global source0_hash cb1494b4dfae03eb386556821efed0b7f174c71f8b78a424cade1045cddbf98c
Name:		pam-ssh-auth-info
Version:	2.0.20250421
Release:        1%{?dist}
Summary:        PAM SSH Authentication Information Module
License:	GPL-3.0-or-later AND LGPL-3.0-or-later
URL:		https://github.eero.häkkinen.fi/%{name}/
Source0:        https://github.com/eehakkin/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:	pam%{?_isa}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  pam-devel
# /oreon:deps
%description
The pam_ssh_auth_info.so PAM module is designed to succeed or fail
authentication based on SSH authentication information consisting of a
list of successfully completed authentication methods and public
credentials (e.g. keys) used to authenticate the user. One use is to
select whether to load other modules based on this test.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf --install
%configure
%make_build
%check

make check
%install
%make_install
[ ${RPM_BUILD_ROOT} != "/" ] && find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
