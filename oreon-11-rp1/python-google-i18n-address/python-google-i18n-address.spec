%global source0_hash 8aa28072690e66cd36d7e40878d9daf0e55bc7a0263c31f576e629f8b94ff672

Name:           python-google-i18n-address
%global srcname %(echo %{name} | sed 's/^python-//')
%global pypi_name %(echo %{srcname} | sed 's/-/_/g')

Version:        3.1.0
Release:        12%{?dist}
Summary:        Address validation helpers for Google's i18n address database

# Automatically converted from old format: BSD with advertising - review is highly recommended.
License:        LicenseRef-Callaway-BSD-with-advertising
URL:            https://pypi.python.org/pypi/google-i18n-address/
Source0:        %{pypi_source %{pypi_name}}

BuildArch:      noarch

BuildRequires:  python3-devel

%global _description %{expand:
This package contains a copy of Google’s i18n address metadata
repository that contains great data but comes with no uptime guarantees.

Contents of this package will allow you to programatically build address
forms that adhere to rules of a particular region or country, validate
local addresses and format them to produce a valid address label for
delivery.

The package also contains a Python interface for address validation.}

%description %_description

%package -n python3-%{srcname}
Summary: Address validation helpers for Google's i18n address database
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%check
# warns about obsolete testing, and then downloads files from the internet
#{__python3} setup.py test

%install
%pyproject_install
%pyproject_save_files i18naddress
# names used for test files are sure to cause clashses with other packages :/
rm -rf %{buildroot}/%{python3_sitelib}/tests
# 1. It requires `sudo`, since data files are saved in the code directory: `/usr/lib/python3.11/site-packages/i18naddress/data`
# 2. Even with `sudo` it crashes.
rm -rf %{buildroot}/%{_bindir}/update-validation-files

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
