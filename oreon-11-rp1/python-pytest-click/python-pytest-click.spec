%global source0_hash fdd9f6721f877dda021e7c5dc73e70aecd37e5ed23ec6820f8a7b3fd7b4f8d30

Name:           python-pytest-click
Version:        1.1.0
Release:        14%{?dist}
Summary:        Pytest plugin for Click

License:        MIT
URL:            https://github.com/Stranger6667/pytest-click
Source:         %{pypi_source pytest_click}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(click) >= 6
BuildRequires:  python3dist(pytest) >= 5
BuildRequires:  python3dist(setuptools)

%description
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%package -n     python3-pytest-click
Summary:        %{summary}

%description -n python3-pytest-click
pytest-click comes with some configurable fixtures - cli_runner and
isolated_cli_runner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pytest_click-%{version}

%build
%py3_build

%install
%py3_install

%check
%pytest

%files -n python3-pytest-click
%license LICENSE
%doc README.rst
%{python3_sitelib}/pytest_click/
%{python3_sitelib}/pytest_click-%{version}-py%{python3_version}.egg-info/

%changelog
%autochangelog
