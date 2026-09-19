%global source0_hash a6d06a5428dd8f316a3f8784cac0180067b6530121d9cf3976d5f903db264c86

%global pypi_name pyjokes
%global with_tests 0
%global global_desc One line jokes for programmers (jokes as a service)

Name:           %{pypi_name}
Version:        0.6.0
Release:        5%{?dist}
Summary:        %{global_desc}

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://pyjok.es/
Source0:        https://github.com/%{pypi_name}/%{pypi_name}/archive/v%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%if 0%{?with_tests}
BuildRequires:  python3-pytest
%endif

%description
%{global_desc}.

%package     -n python3-%{pypi_name}
Summary: %{global_desc}. This package includes a commandline interface.

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
%{global_desc}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name} pyjokescli

%check
%if %{with_tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENCE.txt
%doc docs/*
%{_bindir}/pyjoke*

%changelog
%autochangelog
