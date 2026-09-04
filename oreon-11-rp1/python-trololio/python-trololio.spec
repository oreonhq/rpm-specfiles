%global source0_hash 39309509b585f47ea972b9904c40d1c1bf1050e12f667935779150022195b98f

# Created by pyp2rpm-3.3.2
%global pypi_name trololio
%global mod_name Trololio

%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?fedora} && 0%{?fedora} < 29)
%bcond_without python2
%else
%bcond_with python2
%endif

%global sum Trollius and asyncio compatibility library

%global desc \
Trololio provides a compatibility layer for Trollius and asyncio (aka Tulip). \
It addresses the differences listed in Trollius and Tulip: \
\
* Allows the use of Trollius' syntax with asyncio. \
* Provides missing objects and aliases for the others. \
* Synchronizes debug environnement variables.

Name:           python-%{pypi_name}
Version:        1.0b
Release:        1%{?dist}
Summary:        %{sum}

License:        MIT
URL:            http://github.com/ThinkChaos/Trololio/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{mod_name}-%{version}.zip
# License file from source repository
Source1:        https://raw.githubusercontent.com/ThinkChaos/Trololio/25fe6b9a0d9e2dc69d59f1b5c6e6e56a6615c305/LICENSE#/Trololio-LICENSE
BuildArch:      noarch

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

%description %{desc}

%if %{with python2}
%package -n     python2-%{pypi_name}
Summary:        %{sum} for Python 2
%{?python_provide:%python_provide python2-%{pypi_name}}
%if (0%{?rhel} && 0%{?rhel} < 8) || (0%{?fedora} && 0%{?fedora} < 28)
Requires:       python-trollius
%else
Requires:       python2-trollius
%endif

%description -n python2-%{pypi_name} %{desc}

This package provides the Python 2 module.

%endif

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{sum} for Python 3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name} %{desc}

This package provides the Python 3 module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{mod_name}-%{version}
# Remove bundled egg-info
rm -rf *.egg-info

# Install license into source tree
cp %{SOURCE1} LICENSE

%build
%if %{with python2}
%py2_build
%endif
%py3_build

%install
%if %{with python2}
%py2_install
%endif
%py3_install

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%license LICENSE
%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{mod_name}-%{version}-py?.?.egg-info
%endif

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{mod_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
