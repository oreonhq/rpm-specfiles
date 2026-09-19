%global source0_hash 080a88b940ca844474c239cc7aab0c530187e637a9dc6df111a99e2955bb35db

%{?python_enable_dependency_generator}
%global modname stuf

Name:               python-stuf
Version:            0.9.16
Release:            44%{?dist}
Summary:            Fancy python dictionary types

# Automatically converted from old format: BSD - review is highly recommended.
License:            LicenseRef-Callaway-BSD
URL:                http://pypi.python.org/pypi/stuf
Source0:            https://pypi.python.org/packages/source/s/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:          noarch

%description
A collection of Python dictionary types that support attribute-style
access. Includes *defaultdict*,  *OrderedDict*, restricted, *ChainMap*,
*Counter*, and frozen implementations plus miscellaneous utilities for
writing Python software.

%package -n python3-%{modname}
Summary:            Fancy python dictionary types
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%description -n python3-%{modname}
A collection of Python dictionary types that support attribute-style
access. Includes *defaultdict*,  *OrderedDict*, restricted, *ChainMap*,
*Counter*, and frozen implementations plus miscellaneous utilities for
writing Python software.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

# Remove upstreams egg info
rm -rf *.egg*

%build
%py3_build

%install
%py3_install

# https://bitbucket.org/lcrees/stuf/issues/9/find_packages-should-exclude-tests
rm -rf %{buildroot}%{python3_sitelib}/tests/

%files -n python3-%{modname}
%doc README.rst
%license LICENSE.txt
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}-*

%changelog
%autochangelog
