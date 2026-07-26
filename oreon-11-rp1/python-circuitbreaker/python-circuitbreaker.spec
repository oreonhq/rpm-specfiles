%global source0_hash 0a89578d626a04e39e58c9ac28f181076ac8a88d71a4eca37b0f7a1bf7bf6755

%bcond_without  tests

%global         srcname     circuitbreaker

Name:           python-%{srcname}
Version:        2.1.3
Release:        %autorelease
Summary:        Python "Circuit Breaker" implementation

License:        BSD-3-Clause
URL:            https://github.com/fabfuel/circuitbreaker
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel

%if %{with tests}
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-mock)
%endif

%global _description %{expand:
This is a Python implementation of the "Circuit Breaker" Pattern.}

%description %{_description}

%package -n python3-%{srcname}
Summary:        %{summary}

%description -n python3-%{srcname} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%pyproject_check_import

%if %{with tests}
%pytest
%endif

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE.rst
%doc README.rst

%changelog
%autochangelog
