%global source0_hash d63cfdafde4efd6b1730c600c32c5a8ea6282cf4122924edb5da85014a20275e

%global debug_package %{nil}
%global pypi_name yarl

Name:           python-%{pypi_name}
Version:        1.22.0
Release:        2%{?dist}
Summary:        Python module to handle URLs

License:        Apache-2.0
URL:            https://yarl.readthedocs.io
Source0:        https://github.com/aio-libs/yarl/archive/v%{version}/%{pypi_name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(hypothesis)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)

%description
The module provides handy URL class for URL parsing and changing.

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
The module provides handy URL class for URL parsing and changing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1
# Disable coverage
sed -r -e 's/(-.*cov.*$)/#\1/g' -i pytest.ini

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
# Ignore the benchmark tests which require pytest_codspeed which is not
# packaged in Fedora.
%pytest -v --ignore tests/test_quoting_benchmarks.py --ignore tests/test_url_benchmarks.py tests

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc CHANGES.rst README.rst

%changelog
%autochangelog
