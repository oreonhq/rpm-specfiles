%global source0_hash e7cb0ea774db81bf91844db22de72a40aae8f7b0f9bb9ba0f666d474ef6bf9fc

%global pypi_name sshtunnel

# tests are enabled by default
%bcond_without  tests

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        %autorelease
Summary:        Pure python SSH tunnels

License:        MIT
URL:            https://github.com/pahaz/sshtunnel
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  openssh-clients
BuildRequires:  python3-pytest
%endif

%description
Pure python SSH tunnels

%package -n     python3-%{pypi_name}
Summary:        %{summary}
Obsoletes:      python3-azure-sdk < 5.0.1
%description -n python3-%{pypi_name}
Pure python SSH tunnels

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

# Remove the python shebang from non-executable files.
sed -i '1{\@^#!/usr/bin/env python@d}' sshtunnel.py

# Update tests to import the built-in mock.
sed -i 's/^import mock/from unittest import mock/' tests/*.py

%build
%pyproject_wheel

%generate_buildrequires
%pyproject_buildrequires -r

%install
%pyproject_install
%pyproject_save_files sshtunnel

%if %{with tests}
%check
%pytest
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst
%{_bindir}/sshtunnel

%changelog
%autochangelog
