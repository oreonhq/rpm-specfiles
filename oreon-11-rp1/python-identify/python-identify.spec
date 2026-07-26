%global source0_hash 1b4d68f5f7267f2b9c4637379742fb6764abae63b5c053ac30c1ded252a2525b

%bcond check 0
%global pypi_name identify

Name:           python-%{pypi_name}
Version:        2.6.18
Release:        1%{?dist}
Summary:        File identification library for Python

License:        MIT
URL:            https://github.com/chriskuehl/identify
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(ukkonen)
%if %{with check}
BuildRequires:  python3-pytest
%endif

%description
Given a file (or some information about a file), return a set of standardized
tags identifying what the file is.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
%{summary}.

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

%if %{with check}
%check
%pyproject_check_import

%{python3} -m pytest -v
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.md
%{_bindir}/%{pypi_name}-cli

%changelog
%autochangelog
