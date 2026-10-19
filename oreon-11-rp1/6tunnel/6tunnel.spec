%global source0_hash f597edda55db4b6e661d7afdaa17c1f0c41aeadc21fc8b5599e678595906552b
Name:           6tunnel
Version:        0.14
Release:        3%{?dist}
Summary:        Tunnelling for application that don't speak IPv6
License:        GPL-2.0-only
URL:            https://github.com/wojtekka/6tunnel
Source0:        https://github.com/wojtekka/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  python3
# /oreon:deps
%description
6tunnel allows you to use services provided by IPv6 hosts with IPv4-only
applications and vice-versa. It can bind to any of your IPv4 (default) or
IPv6 addresses and forward all data to IPv4 or IPv6 (default) host.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vif
%configure
%make_build CFLAGS="%{optflags} -std=gnu17"
%check

%{python3} test.py
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
