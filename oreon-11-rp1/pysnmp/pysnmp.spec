%global source0_hash 23189db7ee5a037454ed051c373a217b6d222e78b334fbfc739a491ce91f54c9
Name:           pysnmp
Version:        7.1.29
Release:        1%{?dist}
Summary:        An SNMP engine written in Python
License:        BSD-2-Clause
URL:            https://pysnmp.com/
Source0:        https://github.com/lextudio/pysnmp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       net-snmp
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) >= 3.9.0
Requires:       python3-pysnmp = %{version}-%{release}
# /oreon:deps
%package -n       python3-pysnmp+dev
Summary:        Metapackage for python3-pysnmp dev extras
Requires:       python3-pysnmp = %{version}-%{release}
Requires:       python3dist(codecov) >= 2.1.12
Requires:       python3dist(pytest) >= 7.2.0
Requires:       python3dist(pytest-codecov) >= 0.4.0
Requires:       python3dist(pytest-cov) >= 4.1.0
Requires:       python3dist(pytest-asyncio) >= 0.21.1
Requires:       python3dist(pytest-rerunfailures) >= 12.0
Requires:       python3dist(pytest-rerunfailures) < 13.0
Requires:       python3dist(tomli) >= 2.0.1
Requires:       python3dist(tomli) < 3.0.0
Requires:       python3dist(sphinx) >= 7.0.0
Requires:       python3dist(sphinx) < 8.0.0
Requires:       python3dist(sphinx-copybutton) >= 0.5.2
Requires:       python3dist(sphinx-notfound-page) >= 1.0.0
Requires:       python3dist(sphinx-sitemap-lextudio) >= 2.5.2
Requires:       python3dist(sphinx-polyversion) >= 1.0.0
Requires:       python3dist(furo) >= 2023.1.1
Requires:       python3dist(pre-commit) == 2.21.0
Requires:       python3dist(doc8) >= 1.0.0
Requires:       python3dist(flake8) >= 7.0.0
Requires:       python3dist(pep8-naming) >= 0.14.1
Requires:       python3dist(cryptography) >= 50.0.0
Requires:       python3dist(pysmi) >= 2.0.0
Requires:       python3dist(bump2version) >= 1.0.1
Requires:       python3dist(ruff) >= 0.11.7
Requires:       python3dist(jinja2) >= 3.1.6
Provides:       python3dist(pysnmp[dev]) = %{version}-%{release}

%description -n python3-pysnmp+dev
Metapackage for python3-pysnmp dev extras.

%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

%package -n python3-%{name}
Summary:        An SNMP engine written in Python
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{name}}
%description -n python3-%{name}
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pysnmp* usr/lib64/python3*/site-packages/pysnmp* usr/bin/*

%check

%pyproject_check_import -e '*.smi.mibs.*'
%files
%files -n python3-pysnmp -f %{oreon_filedir}/python3-pysnmp.list

%changelog

%autochangelog
