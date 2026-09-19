%global source0_hash 240b60a8f3d9b371a4fb56cca4e627306b16c6f82a226ee305877bb91dd102ba

%global srcname cvss

Name:           python-%{srcname}
Version:        3.6
Release:        2%{?dist}
Summary:        CVSS2/3 library with interactive calculator

# The entire source code is LGPL-3.0+ except cvss/cvss4.py which is BSD-2-Clause
License:        LGPL-3.0-or-later and BSD-2-Clause
URL:            https://github.com/skontar/cvss
Source0:        %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
This Python package contains CVSS v2 and v3 computation utilities and\
interactive calculator.

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:  python3-devel
%generate_buildrequires
%pyproject_buildrequires

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

# Tests are not ran (have to patch code and use nose/pytest)
#check

%files -n python3-%{srcname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{srcname}-*.dist-info/
%{python3_sitelib}/%{srcname}/
%{_bindir}/cvss_calculator

%changelog
%autochangelog
