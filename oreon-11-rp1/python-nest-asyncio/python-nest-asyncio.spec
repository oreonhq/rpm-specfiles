%global source0_hash 6f172d5449aca15afd6c646851f4e31e02c598d553a667e38cafa997cfec55fe

%global pypi_name nest_asyncio

Name:           python-nest-asyncio
Version:        1.6.0
Release:        %autorelease
Summary:        Patch asyncio to allow nested event loops

License:        BSD-2-Clause
URL:            https://github.com/erdewit/nest_asyncio
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

%description
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".
The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.
This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.

%package -n     python3-nest-asyncio
Summary:        %{summary}

# This package used to be called python3-nest_asyncio
Obsoletes:      python3-nest_asyncio < 1.4.3-100
%py_provides    python3-nest_asyncio

%description -n python3-nest-asyncio
By design asyncio does not allow its event loop to be nested.
This presents a practical problem: When in an environment
where the event loop is already running it's impossible to run tasks
and wait for the result. Trying to do so will give the error
"RuntimeError: This event loop is already running".
The issue pops up in various environments, such as web servers,
GUI applications and in Jupyter notebooks.
This module patches asyncio to allow nested use of asyncio.run
and loop.run_until_complete.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pypi_name}-%{version}
# test_timeout fails due to stricter asyncio
# timeout checks in Python 3.14+.
sed -i '/def test_timeout/i \
    @unittest.skipIf(sys.version_info >= (3, 14), "Fails due to stricter asyncio timeout checks in Python 3.14+")' tests/nest_test.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
PYTHONPATH=%{buildroot}%{python3_sitelib} %python3 tests/nest_test.py

%files -n python3-nest-asyncio -f %{pyproject_files}
%doc README.rst

%changelog
%autochangelog
