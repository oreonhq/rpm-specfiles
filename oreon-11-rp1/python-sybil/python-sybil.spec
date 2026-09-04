%global source0_hash a64b2bf2925bb995dc94acb6a82c51e916acb90e21c0f0cab48282f86378dbd1

%global pypi_name sybil

Name:           python-%{pypi_name}
Version:        9.1.0
Release:        6%{?dist}
Summary:        Automated testing for the examples in your documentation

License:        MIT
URL:            https://sybil.readthedocs.io/
Source0:        https://github.com/simplistix/sybil/archive/refs/tags/%{version}.tar.gz
# seedir is not available in Fedora yet
Patch:          drop-dependency-on-seedir.patch
BuildArch:      noarch

%description
This library provides a way to test examples in your documentation by parsing
them from the documentation source and evaluating the parsed examples as part
of your normal test run. Integration is provided for the three main Python
test runners.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  make
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-testfixtures
BuildRequires:  python3-pyyaml

%description -n python3-%{pypi_name}
This library provides a way to test examples in your documentation by parsing
them from the documentation source and evaluating the parsed examples as part
of your normal test run. Integration is provided for the three main Python
test runners.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
sed -i "/seeddir/d" setup.py

%build
%py3_build

%install
%py3_install

%check
%{pytest} tests

%files -n python3-%{pypi_name}
%doc README.rst
%license docs/license.rst
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{pypi_name}/

%changelog
%autochangelog
