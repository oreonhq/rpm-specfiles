%global source0_hash e0056ad9064e7923e874e6769015b032580b639e29246f5ab1044f7959c1c7e0

%global pypi_name hvac

Name:           python-%{pypi_name}
Version:        2.4.0
Release:        %autorelease
Summary:        HashiCorp Vault API client for Python

License:        Apache-2.0
URL:            https://github.com/hvac/hvac
Source:         %{pypi_source %{pypi_name}}
BuildArch:      noarch

%global _description %{expand:
This package provides a Python API client for HashiCorp Vault.}

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
BuildRequires:  python3-devel

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove shebangs from non-executable files
find hvac -type f ! -executable -name '*.py' -print -exec sed -r -i -e '1{\@^#!/usr/bin/(env )?python@d}' '{}' +

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L hvac

%check
# All test require the "vault" executable, so this is all that we can do:
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
