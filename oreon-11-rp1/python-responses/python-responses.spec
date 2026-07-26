%global source0_hash 9374d047a575c8f781b94454db5cab590b6029505f488d12899ddb10a4af1cf4

%global pypi_name responses

Name:           python-%{pypi_name}
Version:        0.25.8
Release:        4%{?dist}
Summary:        Python library to mock out calls with Python requests
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/getsentry/responses
Source:         %{pypi_source}

BuildArch:      noarch
BuildRequires:  python3-devel
# Upstream added various requirements in its "tests" extras which are only
# required tests we don't want to run in Fedora (coverage) and strict version
# requirements (pytest >= 7.0 as of March 2022 - not yet in rawhide).
# Patching setup.py is error prone as the patch file has to be regenerated
# every time upstream bumps a version requirement.
# Therefore just list the build requirements here explicitely.
BuildRequires:  python3-pytest python3-pytest-xdist

%description
A utility library for mocking out the requests Python library.

%package -n python3-%{pypi_name}
Summary:        Python library to mock out calls with Python requests

%description -n python%{python3_pkgversion}-%{pypi_name}
A utility library for mocking out the requests Python library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

# Remove unnecessary dependencies
sed -i '/coverage/d' setup.py
sed -i '/pytest-cov/d' setup.py
sed -i '/flake8/d' setup.py
sed -i '/types-requests/d' setup.py
sed -i '/mypy/d' setup.py

%generate_buildrequires
%pyproject_buildrequires -r -x tests

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}
# we do not ship tests
sed -i -e '/\/tests\//d' %{pyproject_files}

%check
%pytest -n auto --asyncio-mode=auto

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
