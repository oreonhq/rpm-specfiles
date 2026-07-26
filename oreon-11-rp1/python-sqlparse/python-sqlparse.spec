%global source0_hash 09f67787f56a0b16ecdbde1bfc7f5d9c3371ca683cfeaa8e6ff60b4807ec9272

Name:           python-sqlparse
Version:        0.5.3
Release:        %autorelease
Summary:        A non-validating SQL parser
License:        BSD-3-Clause
URL:            https://github.com/andialbrecht/sqlparse
Source:         %{pypi_source sqlparse}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
sqlparse is a non-validating SQL parser for Python. It provides support for
parsing, splitting and formatting SQL statements.}

%description %_description

%package -n     python3-sqlparse
Summary:        %{summary}

%description -n python3-sqlparse %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sqlparse-%{version}

# fix ambiguous python shebang
%py3_shebang_fix sqlparse/cli.py

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l sqlparse

%check
%pytest -v tests

%files -n python3-sqlparse -f %{pyproject_files}
%doc CHANGELOG README.rst
%{_bindir}/sqlformat

%changelog
%autochangelog
