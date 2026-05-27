%global source0_hash none

%bcond docs %{undefined rhel}
%bcond pbr %{undefined rhel}
%bcond tests %{undefined rhel}

%global sname pyghmi
%global common_summary Python General Hardware Management Initiative (IPMI and others)

%global common_desc This is a pure Python implementation of IPMI protocol. \
\
The included pyghmicons and pyghmiutil scripts demonstrate how one may \
incorporate the pyghmi library into a Python application.

%global common_desc_tests Tests for the pyghmi library

Summary: %{common_summary}
Name: python-%{sname}
Version: %{?version:%{version}}%{!?version:1.6.2}
Release: 5%{?dist}
Source0: https://tarballs.opendev.org/x/%{sname}/%{sname}-%{version}.tar.gz
License: Apache-2.0
Prefix: %{_prefix}
BuildArch: noarch
Url: https://opendev.org/x/pyghmi

## RHEL-specific patches
Patch1000:  nopbr.patch
Patch1001:  setup.patch

%description
%{common_desc}

%package -n python3-%{sname}
Summary: %{common_summary}
%{?python_provide:%python_provide python3-%{sname}}

BuildRequires: python3-devel
%if %{with pbr}
BuildRequires: python3-pbr
%endif
BuildRequires: python3-setuptools
%if %{with tests}
BuildRequires: python3-oslotest
BuildRequires: python3-stestr
%endif

BuildRequires: python3-cryptography
BuildRequires: python3-six
BuildRequires: python3-dateutil

Requires: python3-cryptography >= 2.1
Requires: python3-six >= 1.10.0
Requires: python3-dateutil >= 2.8.1

%description -n python3-%{sname}
%{common_desc}

%package -n python3-%{sname}-tests
Summary: %{common_desc_tests}
Requires: python3-%{sname} = %{version}-%{release}

%description -n python3-%{sname}-tests
%{common_desc_tests}

%if %{with docs}
%package -n python-%{sname}-doc
Summary: The pyghmi library documentation

BuildRequires: python3-sphinx
BuildRequires: python3-openstackdocstheme

%description -n python-%{sname}-doc
Documentation for the pyghmi library
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -qn %{sname}-%{version}
%if %{without pbr}
%patch -P1000 -p1
%patch -P1001 -p1
sed -i s/@@REDHATVERSION@@/%{version}/ pyghmi/version.py
sed -e "s/#VERSION#/%{version}/" setup.py.tmpl > setup.py
%endif

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%if %{with docs}
sphinx-build -b html doc/source doc/build/html

# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install

%check
%if %{with tests}
stestr run
%else
%py3_check_import %{sname} %{sname}.cmd %{sname}.ipmi %{sname}.ipmi.oem %{sname}.ipmi.oem.lenovo %{sname}.ipmi.private %{sname}.redfish %{sname}.redfish.oem %{sname}.redfish.oem.dell %{sname}.redfish.oem.lenovo %{sname}.util
%endif

%files -n python3-%{sname}
%license LICENSE
%{_bindir}/pyghmicons
%{_bindir}/pyghmiutil
%{_bindir}/virshbmc
%{_bindir}/fakebmc
%{python3_sitelib}/%{sname}
%{python3_sitelib}/%{sname}-*.dist-info
%exclude %{python3_sitelib}/%{sname}/tests

%files -n python3-%{sname}-tests
%license LICENSE
%{python3_sitelib}/%{sname}/tests

%if %{with docs}
%files -n python-%{sname}-doc
%license LICENSE
%doc doc/build/html README.md
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{?version:%{version}}%{!?version:1.6.2}-5
- Prepare for Oreon 11 (RP1)
