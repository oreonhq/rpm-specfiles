%global source0_hash e68164ec523d8544208f0e80d5348a5f81a974c83c417aad2b2343a30404658d

%global pypi_name apypie

Name:           python-%{pypi_name}
Version:        0.7.1
Release:        7%{?dist}
Summary:        Apipie bindings for Python

License:        MIT
URL:            https://github.com/Apipie/apypie
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel

%description
Python bindings for the Apipie - Ruby on Rails API documentation tool.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Apipie bindings for Python

%description -n python%{python3_pkgversion}-%{pypi_name}
Apipie bindings for Python3

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

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
