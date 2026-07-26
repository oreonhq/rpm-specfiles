%global source0_hash ab9ba6eefa0e8878f737b580dd957e81f21d18dc4a3cb5a25a6abbe82f590f35

%global srcname pyzabbix
#global commit aed72dfe30cd5f8262013af73356a76924cbeb83

Name:           python-pyzabbix
Version:        1.3.1
Release:        8%{?dist}
Summary:        PyZabbix is a Python module for working with the Zabbix API

# license is in README.md
License:        LGPL-2.1-or-later
URL:            https://github.com/lukecyca/pyzabbix
Source0:        https://github.com/lukecyca/pyzabbix/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel

%description
%{summary}.

%package -n python3-%{srcname}
Summary:        PyZabbix is a Python module for working with the Zabbix API

%description -n python3-%{srcname}
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
sed -i 's/"httpretty<0.8.7",/"httpretty",/' setup.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
# There are no runnable tests

%files -n python3-%{srcname} -f %{pyproject_files}
%doc CHANGELOG.md README.md examples/

%changelog
%autochangelog
