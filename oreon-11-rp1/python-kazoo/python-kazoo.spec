%global source0_hash 57e7e6f69295c8f922511488eeb79680729e14bb8eb382d5cad83aa11345c36c

# Created by pyp2rpm-1.0.1
%global pypi_name kazoo

Name:           python-%{pypi_name}
Version:        2.11.0
Release:        1%{?dist}
Summary:        Higher level Python Zookeeper client

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://kazoo.readthedocs.org
Source0:        https://pypi.python.org/packages/source/k/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%global _description\
Kazoo is a Python library designed to make working with Zookeeper a more\
hassle-free experience that is less prone to errors.

%description %_description

%package -n python3-%{pypi_name}
Summary:        Higher level Python Zookeeper client
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# For building documentation
BuildRequires:  python3-sphinx
Requires:       python3-six

%description -n python3-%{pypi_name}
Kazoo is a Python library designed to make working with Zookeeper a more
hassle-free experience that is less prone to errors.

%package doc
Summary:    Documentation for %{name}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0

%description doc
Kazoo is a Python library designed to make working with Zookeeper a more
hassle-free experience that is less prone to errors.

This package contains documentation in HTML format.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'

# generate html docs
sphinx-build docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%build
%py3_build

%install
%py3_install

#delete tests
rm -fr %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/

%files -n python3-%{pypi_name}
%doc README.md LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files doc
%doc html

%changelog
%autochangelog
