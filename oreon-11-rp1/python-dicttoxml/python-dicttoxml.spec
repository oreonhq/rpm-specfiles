%global source0_hash ea44cc4ec6c0f85098c57a431a1ee891b3549347b07b7414c8a24611ecf37e45

%global pypi_name dicttoxml

Name:           python-%{pypi_name}
Version:        1.7.4
Release:        23%{?dist}
Summary:        Converts a Python dictionary or other native data type into a valid XML string

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            https://github.com/quandyfactory/dicttoxml
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Converts a Python dictionary or other native data type into a valid XML string.
Details Supports item (int, float, long, decimal.Decimal, bool, str, unicode,
datetime, none and other number-like objects) and collection (list, set, tuple
and dict, as well as iterable and dict-like objects) data types, with arbitrary
nesting for the collections.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Converts a Python dictionary or other native data type into a valid XML string.
Details Supports item (int, float, long, decimal.Decimal, bool, str, unicode,
datetime, none and other number-like objects) and collection (list, set, tuple
and dict, as well as iterable and dict-like objects) data types, with arbitrary
nesting for the collections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.markdown
%license LICENCE.txt
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
