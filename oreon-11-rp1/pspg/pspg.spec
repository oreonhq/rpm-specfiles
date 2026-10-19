%global source0_hash 3dcfb810cc6675cac6e3ea53775a6f819e0e12e0d2bde8122e3136b740f38ae5
Summary:        A unix pager optimized for psql
Name:		pspg
Version:	5.8.16
Release:        1%{?dist}
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/okbob/%{name}
Source0:        https://github.com/okbob/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  readline-devel
# /oreon:deps
%description
pspg is a unix pager optimized for psql. It can freeze rows, freeze
columns, and lot of color themes are included.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure
%make_build
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
