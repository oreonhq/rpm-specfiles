%global source0_hash 9a4967fba6f688f5bb757aefc1f7a0e6e0a8544575a13a5ce66beeedcd9fc406

%global pypi_name pyone

Name:           python-%{pypi_name}
Version:        6.0.2
Release:        16%{?dist}
Summary:        Python Bindings for OpenNebula XML-RPC API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://opennebula.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://github.com/OpenNebula/addon-pyone/blob/master/LICENSE
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-aenum
BuildRequires:  python3-check-manifest
BuildRequires:  python3-coverage
BuildRequires:  python3-dicttoxml
BuildRequires:  python3-lxml
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
BuildRequires:  python3-six
BuildRequires:  python3-tblib
BuildRequires:  python3-xmltodict
%description
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3-aenum
Requires:       python3-coverage
Requires:       python3-dicttoxml
Requires:       python3-lxml
Requires:       python3-requests
Requires:       python3-six
Requires:       python3-tblib
Requires:       python3-xmltodict

%description -n python3-%{pypi_name}
OpenNebula Python Bindings Description --PyOne is an implementation of Open
Nebula XML-RPC bindings in Python. It has been integrated into upstream
OpenNebula release cycles from here <

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
install -pm 0644 %{SOURCE1} LICENSE
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%license LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%changelog
%autochangelog
