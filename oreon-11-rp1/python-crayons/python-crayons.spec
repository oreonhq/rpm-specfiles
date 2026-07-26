%global source0_hash b4a95433721246b157e057eb6c3119a57746707a9c826ad4692de1d1a2b70f37

%global pypi_name crayons

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        20%{?dist}
Summary:        Python module for writing colored text to terminal

License:        MIT
URL:            https://github.com/MasterOdin/crayons
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
This module provides a simple and elegant wrapper for colorama.

%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-colorama

%description -n python3-%{pypi_name}
This module provides a simple and elegant wrapper for colorama.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
