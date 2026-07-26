%global source0_hash 1829ef96ac1cf1a62772bd855177c4e343336e1d78baccbbbe678f2f262b33bb

%global srcname metar
%global summary Coded METAR and SPECI weather reports parser for Python
%global packagezipfile python-metar-20250512git-d87ebdf.zip

Name: python-%{srcname}
Version: 1.11.0
Release: 20250516git%{?dist}
Summary: %{summary}

# This software uses the BSD-Source-Code license
# (but without the second condition on use of names of contributors)
License: BSD-Source-Code

URL: https://github.com/python-metar/python-metar

# note that development was moved to a new github account
# the old account was: http://github.com/tomp/python-metar
# see also this discussion on the 2 project names:
# https://github.com/python-metar/python-metar/issues/58

# releases are at pypi
# Source: https://files.pythonhosted.org/packages/source/m/%%{srcname}/%%{srcname}-%%{version}.tar.gz

# but the latest release does not contain a pyproject.toml file
# so cannot easily be build with the new pyproject macros.
# Therefore a snapshot from github is used in stead:
Source:  https://github.com/python-%{srcname}/python-%{srcname}/archive/d87ebdf3049cb542fb3a94f470dca37821378e91.zip#/%{packagezipfile}

BuildArch: noarch

BuildRequires: python3-devel python3-pytest

%global _description \
Python-metar is a python package for interpreting METAR and SPECI coded \
weather reports.  METAR (Meteorological Aerodrome Report) and SPECI (Specials) \
are reports containing airport weather information encoded in ASCII \
following standards set by WMO (World Meteorological Organization) \
and ICAO (International Civil Aviation Organization).

%description %_description

%package -n python3-%{srcname}
Summary: %{summary}
%{?python_provide:%python_provide python-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

cd %{_builddir}
unzip %{_sourcedir}/%{packagezipfile}
mv python-metar-main python-%{srcname}-%{version}

%generate_buildrequires

cd %{_builddir}/python-%{srcname}-%{version}
%pyproject_buildrequires

%build

cd %{_builddir}/python-%{srcname}-%{version}
%pyproject_wheel

%install

cd %{_builddir}/python-%{srcname}-%{version}
%pyproject_install

# remove executable permissions from sample.py to
# prevent dependencies being pulled in from this file
chmod 644 sample.py

%check

cd %{_builddir}/python-%{srcname}-%{version}
%{__python3} -m pytest -v

%files -n python3-%{srcname}

%doc python-%{srcname}-%{version}/sample.py
%doc python-%{srcname}-%{version}/README.md
%doc python-%{srcname}-%{version}/CHANGELOG.md
%doc python-%{srcname}-%{version}/LICENSE

%{python3_sitelib}/%{srcname}
%{python3_sitelib}/python_%{srcname}*dist-info

%changelog
%autochangelog
