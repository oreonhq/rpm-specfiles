%global source0_hash 527eb256dfa313403405f324471872326e58e4d7d0f36cbca2f2280c0e34f5d7

Name:           pysnmp
Version:        7.1.21
Release:        5%{?dist}

Summary:        An SNMP engine written in Python

License:        BSD-2-Clause
URL:            https://pysnmp.com/
Source0:        https://github.com/lextudio/pysnmp/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       net-snmp

%description
This is a Python implementation of SNMP v.1/v.2c engine. It's
general functionality is to assemble/disassemble SNMP messages
from/into given SNMP Object IDs along with associated values.
PySNMP also provides a few transport methods specific to TCP/IP
networking.

%package -n python3-%{name}
Summary:        %{summary}

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

%autosetup -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pysnmp

%check
%pyproject_check_import -e '*.smi.mibs.*'

%files -n python3-%{name} -f  %{pyproject_files}
%doc CHANGES.rst README.md THANKS.txt TODO.txt examples/ docs/
%license LICENSE.rst

%changelog
%autochangelog
