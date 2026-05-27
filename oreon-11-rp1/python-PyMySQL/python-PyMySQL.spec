%global source0_hash 4961d3e165614ae65014e361811a724e2044ad3ea3739de9903ae7c21f539f03

Name:           python-PyMySQL
Version:        1.1.2
Release:        3%{?dist}
Summary:        Pure-Python MySQL client library

License:        MIT
URL:            https://pypi.org/project/pymysql/
Source:         %{pypi_source pymysql}

BuildArch:      noarch

%description
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%package -n     python3-PyMySQL
Summary:        %{summary}
BuildRequires:  python3-devel


%description -n python3-PyMySQL
This package contains a pure-Python MySQL client library. The goal of PyMySQL is
to be a drop-in replacement for MySQLdb and work on CPython, PyPy, IronPython
and Jython.


%pyproject_extras_subpkg -n python3-PyMySQL rsa %{!?rhel:ed25519}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n pymysql-%{version}


%generate_buildrequires
%pyproject_buildrequires -x rsa %{!?rhel:-x ed25519}


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files pymysql


%check
# Tests cannot be launch on koji, they require a mysqldb running.
%pyproject_check_import


%files -n python3-PyMySQL -f %{pyproject_files}
%doc README.md


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.2-3
- Prepare for Oreon 11 (RP1)
