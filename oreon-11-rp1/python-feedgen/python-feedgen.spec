%global source0_hash 03c44b8624749082c67eee2b92f1b79c3b905ca97834372ea5e150a7e0c581b8

%global pypi_name feedgen

Name:           python-%{pypi_name}
Version:        1.0.0
Release:        %autorelease
Summary:        Feed Generator (ATOM, RSS, Podcasts)

License:        BSD-2-Clause OR LGPL-3.0-or-later
URL:            https://lkiesow.github.io/python-feedgen
Source0:        https://github.com/lkiesow/%{name}/archive/v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
Feedgenerator This module can be used to generate web feeds in both ATOM and
RSS format. It has support for extensions. Included is for example an extension
to produce Podcasts.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-dateutil
Requires:       python3-lxml
%description -n python3-%{pypi_name}
Feedgenerator This module can be used to generate web feeds in both ATOM and
RSS format. It has support for extensions. Included is for example an extension
to produce Podcasts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%{python3} -m unittest discover

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license license.lgpl license.bsd
%doc readme.rst

%changelog
%autochangelog
