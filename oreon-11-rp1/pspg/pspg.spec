%global source0_hash 3dcfb810cc6675cac6e3ea53775a6f819e0e12e0d2bde8122e3136b740f38ae5

Summary:	A unix pager optimized for psql
Name:		pspg
Version:	5.8.16
Release:	1%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:	LicenseRef-Callaway-BSD
URL:		https://github.com/okbob/%{name}
Source:		https://github.com/okbob/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires: make
BuildRequires:	ncurses-devel readline-devel
BuildRequires:	gcc

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

%files
%if 0%{?rhel} && 0%{?rhel} <= 6
%doc README.md LICENSE
%else
%license LICENSE
%doc README.md
%endif
%{_bindir}/*

%changelog
%autochangelog
