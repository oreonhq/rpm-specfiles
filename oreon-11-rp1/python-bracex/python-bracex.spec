%global source0_hash 094669fec4cf3cc39bcc476d7f909f6d4b9e998d877a0f1b8a81bc99d656b451

# Created by pyp2rpm-3.3.5
%global pypi_name bracex

Name:           python-%{pypi_name}
Version:        2.5
Release:        7%{?dist}
Summary:        Bash style brace expander

License:        MIT
URL:            https://github.com/facelessuser/bracex
Source0:        https://github.com/facelessuser/bracex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)

%description
Bracex is a brace expanding library (à la Bash) for Python.
Brace expanding is used to generate arbitrary strings.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Bracex is a brace expanding library (à la Bash) for Python.
Brace expanding is used to generate arbitrary strings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pytest -vv

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md docs/src/markdown/about/license.md
%doc README.md

%changelog
%autochangelog
