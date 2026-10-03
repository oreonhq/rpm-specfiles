%global source0_hash none

%{?python_enable_dependency_generator}

Name:           pywbem
Version:        1.7.3
Epoch:          1
Release:        6%{?dist}
Summary:        Python WBEM client interface and related utilities
License:        LGPL-2.1-or-later
URL:            https://github.com/pywbem/pywbem
Source0:        https://github.com/pywbem/pywbem/archive/refs/tags/%{version}.tar.gz#/pywbem-%{version}.tar.gz
Patch1:         0001_test_fixes.patch
Patch2:         0002_correct_test_libraries.patch
BuildRequires:  python3-devel
BuildArch:      noarch

%description
A Python library for making CIM (Common Information Model) operations over HTTP\
using the WBEM CIM-XML protocol. It is based on the idea that a good WBEM\
client should be easy to use and not necessarily require a large amount of\
programming knowledge. It is suitable for a large range of tasks from simply\
poking around to writing web and GUI applications.\
\
WBEM, or Web Based Enterprise Management is a manageability protocol, like\
SNMP, standardized by the Distributed Management Task Force (DMTF) available\
at http://www.dmtf.org/standards/wbem.\
\
It also provides a Python provider interface, and is the fastest and\
easiest way to write providers on the planet.

%package -n python3-pywbem
Summary:        Python3 WBEM Client and Provider Interface
BuildArch:      noarch

%description -n python3-pywbem
A WBEM client allows issuing operations to a WBEM server, using the CIM
operations over HTTP (CIM-XML) protocol defined in the DMTF standards DSP0200
and DSP0201. The CIM/WBEM infrastructure is used for a wide variety of systems
management tasks supported by systems running WBEM servers. See WBEM Standards
for more information about WBEM.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install
env PYTHONPATH=%{buildroot}/%{python3_sitelib} %{__python3} ./build_moftab.py
rm -rf %{buildroot}/usr/bin/*.bat

%pyproject_save_files -l -M

%files -n python3-pywbem -f %{pyproject_files}
%license LICENSE.txt
%{python3_sitelib}/pywbem/
%{python3_sitelib}/pywbem_mock/
%{_bindir}/mof_compiler
%doc README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:1.7.3-6
- Import
