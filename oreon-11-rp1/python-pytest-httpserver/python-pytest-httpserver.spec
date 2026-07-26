%global source0_hash d25a765e660f252029738392cff49dd3b2d6e5070ac81c7fb794ae6eac93ef76

%global srcname pytest-httpserver

%global desc %{expand: \
This library is designed to help to test http clients without contacting
the real http server. In other words, it is a fake http server which is
accessible via localhost can be started with the pre-defined expected
http requests and their responses.}

Name:		python-%{srcname}
Version:	1.0.8
Release:	12%{?dist}
Summary:	HTTP server for pytest

License:	MIT
URL:		https://github.com/csernazs/pytest-httpserver
Source0:	%{url}/archive/%{version}/%{srcname}-%{version}.tar.gz

Patch0:		pyproject.patch

# https://fedoraproject.org/wiki/Changes/DeprecatePythonToml
# Use tomllib instead of toml (used only in tests)
# https://github.com/csernazs/pytest-httpserver/pull/377
Patch1:		tomllib.patch

BuildArch:	noarch

BuildRequires:	python3-devel
BuildRequires:	python3-pytest
BuildRequires:	python3-requests
BuildRequires:	pyproject-rpm-macros

%description
%{desc}

%package -n python3-%{srcname}
Summary:	%{summary}

%description -n python3-%{srcname} %desc

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{srcname}-%{version}

# Remove unnecessary dependencies
sed -i '/flake8/d' pyproject.toml
sed -i '/pytest-cov/d' pyproject.toml
sed -i '/coverage/d' pyproject.toml
sed -i '/mypy/d' pyproject.toml
sed -i '/types-requests/d' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -x test

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pytest_httpserver

%check
%pytest

%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.md CHANGES.rst CONTRIBUTION.md

%changelog
%autochangelog
