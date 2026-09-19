%global source0_hash cb4c3713b2a2510d0b6387c24a68c88ba5eff27e2c392429653b1bdef50f06c9

%global		module		Sample

Name:		coin-or-%{module}
Summary:	Coin-or Sample data files
Version:	1.2.13
Release:	%autorelease
License:	LicenseRef-Not-Copyrightable
URL:		https://github.com/coin-or-tools/Data-Sample
Source0:	%{url}/archive/releases/%{version}/Data-%{module}-%{version}.tar.gz
Source1:	%{name}-COPYING
BuildArch:	noarch

BuildRequires:	make

%description
Coin-or Sample data files.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Data-%{module}-releases-%{version}
cp -p %{SOURCE1} ./COPYING

%build
%configure
%make_build

%install
%make_install pkgconfiglibdir=%{_datadir}/pkgconfig

%files
%{_datadir}/coin/
%{_datadir}/pkgconfig/*
%license COPYING

%changelog
%autochangelog
