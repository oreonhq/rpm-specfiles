%global source0_hash 76e3292d6236a026f3f512b34f4bd8b26daf517bcabda58e178ee18567815bef

%global srcname filelock

%if 0%{?fedora}
%bcond_without docs
%else
%bcond_with docs
%endif
%bcond_without tests

Name:           python-%{srcname}
Version:        3.32.5
Release:        %autorelease
Summary:        A platform independent file lock

License:        Unlicense
URL:            https://github.com/tox-dev/filelock
Source0:        https://github.com/tox-dev/filelock/archive/%{version}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
# We cannot install extra dependencies because there are some
# we do not have in Fedora like covdefaults in testing.
# Test dependencies
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-asyncio
BuildRequires:  python3-pytest-mock
BuildRequires:  python3-pytest-timeout
%endif
%if %{with docs}
# Doc dependencies
BuildRequires:  python3-furo
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx-autodoc-typehints
%endif

%description
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%if 0%{?fedora}
Suggests:       %{name}-doc
%endif

%description -n python%{python3_pkgversion}-%{srcname}
This package contains a single module, which implements a platform independent
file locking mechanism for Python.

The lock includes a lock counter and is thread safe. This means, when locking
the same lock object twice, it will not block.

%if %{with docs}
%package doc
Summary:        Documentation for %{srcname}, %{summary}

%description doc
%{summary}
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}

%generate_buildrequires
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_buildrequires -r

%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}; export SETUPTOOLS_SCM_PRETEND_VERSION
%pyproject_wheel

%if %{with docs}
pushd docs
PYTHONPATH=../src sphinx-build ./ html --color -b html -d doctrees
rm html/.buildinfo
popd
%endif

%install
%pyproject_install
%pyproject_save_files -l %{srcname}

%check
%if %{with tests}
%pytest --ignore tests/test_virtualenv.py
%else
%pyproject_check_import
%endif

%if %{with docs}
%files doc
%license LICENSE
%doc docs/html
%endif

%files -n python%{python3_pkgversion}-%{srcname} -f %{pyproject_files}
%doc README.md


%changelog
%autochangelog
