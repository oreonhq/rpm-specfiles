%global source0_hash 0cb11992c07629bc31cdb54c3a7c3f4c5d2a5096fbb01e06b12f68d35aaf5453

%global rpmname debianbts
%global pypi_name python-debianbts

Name:           %{pypi_name}
Version:        2.8.2
Release:        23%{?dist}
Summary:        Python interface to Debian's Bug Tracking System

License:        MIT
URL:            https://github.com/venthur/python-debianbts
Source0:        %{pypi_source}
Source1:        https://raw.githubusercontent.com/venthur/python-debianbts/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(flake8)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)

%description
Python-debianbts is a Python library that allows for querying
Debian's Bug Tracking System.

%package -n     python3-%{rpmname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{rpmname}}

Requires:       python3dist(mock)
Requires:       python3dist(pysimplesoap)
Requires:       python3dist(setuptools)

%description -n python3-%{rpmname}
python-debianbts is a Python library that allows for querying
Debian's Bug Tracking System.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
for lib in debianbts/*.py; do
 sed -e '1{\@^#! /usr/bin/env python@d}' -e '1{\@^#!/usr/bin/env python@d}' \
     -e '1{\@^#!/usr/bin/python@d}' $lib > $lib.new &&
 touch -r $lib $lib.new &&
 mv $lib.new $lib
done
cp -p %{SOURCE1} .

# Remove bundled egg-info
#rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{rpmname}
%doc README.md
%license LICENSE
%{_bindir}/debianbts
%{python3_sitelib}/debianbts
%{python3_sitelib}/python_debianbts-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
