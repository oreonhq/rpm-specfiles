%global source0_hash 03c44b8624749082c67eee2b92f1b79c3b905ca97834372ea5e150a7e0c581b8
%global pypi_name feedgen
Name:           python-%{pypi_name}
Version:        1.0.0
Release:        1%{?dist}
Summary:        Feed Generator (ATOM, RSS, Podcasts)
License:        BSD-2-Clause OR LGPL-3.0-or-later
URL:            https://lkiesow.github.io/python-feedgen
Source0:        https://github.com/lkiesow/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-feedgen = %{version}-%{release}
# /oreon:deps
%description
Feedgenerator This module can be used to generate web feeds in both ATOM and
RSS format. It has support for extensions. Included is for example an extension
to produce Podcasts.

%package -n     python3-%{pypi_name}
Summary:        Feed Generator (ATOM, RSS, Podcasts)
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3-dateutil
Requires:       python3-lxml
%description -n python3-%{pypi_name}
Feedgenerator This module can be used to generate web feeds in both ATOM and
RSS format. It has support for extensions. Included is for example an extension
to produce Podcasts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/feedgen* usr/lib64/python3*/site-packages/feedgen* usr/bin/*

%check

%{python3} -m unittest discover
%files
%files -n python3-feedgen -f %{oreon_filedir}/python3-feedgen.list

%changelog

%autochangelog
