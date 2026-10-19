%global source0_hash 37347a11899c5bfdb5f15fd69766fc5bdfdcb434aa82ae3e9dd10095c3266675
Name: ttyplot
Summary:        Real-time plotting utility for the terminal
License: Apache-2.0
Version: 1.7.6
Release:        1%{?dist}
URL: https://github.com/tenox7/ttyplot/
Source0:        https://github.com/tenox7/%{name}/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncursesw)
# /oreon:deps
%description
%{name} is a realtime plotting utility for text mode consoles and terminals
with data input from stdin / pipe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%make_build
%install
%make_install PREFIX=%{_prefix} MANPREFIX=%{_mandir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
