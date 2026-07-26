%global source0_hash e47843379ea35c1296c3b6c67a948a1a490ae0584edfcbdea0eaffb5dd29960b

%global srcname pyrfc3339

Name:           python-pyrfc3339
Version:        2.0.1
Release:        7%{?dist}
Summary:        Generate and parse RFC 3339 timestamps

License:        MIT
URL:            https://pypi.python.org/pypi/pyRFC3339
Source0:        %{pypi_source}
# release tarballs do not contain unit tests (pyrfc3339/tests/tests.py)
# https://github.com/kurtraschke/pyRFC3339/blob/master/pyrfc3339/tests/test_all.py
# v2.0.1: git commit 53c2d1587d3a
Source1:        https://raw.githubusercontent.com/kurtraschke/pyRFC3339/53c2d1587d3aac1734ddd4d4006a815df2d80f36/pyrfc3339/tests/test_all.py

BuildArch:      noarch

BuildRequires:  python3-devel
# --- unit tests ---
# Specified manually because upstream release tarballs do not contain unit tests
BuildRequires:  python3-pytest

%description
This package contains a python library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%package     -n python3-pyrfc3339
Summary:        Generate and parse RFC 3339 timestamps
%{?python_provide:%python_provide python3-pyrfc3339}

%description -n python3-pyrfc3339
This package contains a Python 3 library to parse and generate
RFC 3339-compliant timestamps using Python datetime.datetime objects.

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -N
cp -a %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files pyrfc3339

%check
%pytest -v test_all.py

%files -n python3-pyrfc3339 -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
