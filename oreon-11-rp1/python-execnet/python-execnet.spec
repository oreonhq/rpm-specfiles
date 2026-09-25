%global source0_hash 63d83bfdd9a23e35b9c6a3261412324f964c2ec8dcd8d3c6916ee9373e0befcd

%global srcname execnet

# Some of the BuildRequires are used in tests only when installed.
# To speedup bootstrap of the next Python version in Fedora
# we allow disabling them.
%bcond optional_test_deps %{undefined rhel}

Name:           python-%{srcname}
Version:        2.1.2
Release:        4%{?dist}
Summary:        Distributed Python deployment and communication
License:        MIT
URL:            https://github.com/pytest-dev/execnet
Source0:        %pypi_source

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  /usr/bin/ps

%global _description %{expand:
execnet provides a share-nothing model with channel-send/receive
communication for distributing execution across many Python
interpreters across version, platform and network barriers. It has a
minimal and fast API targetting the following uses:

 * distribute tasks to (many) local or remote CPUs
 * write and deploy hybrid multi-process applications
 * write scripts to administer multiple environments
}

%description %_description

%package -n python3-%{srcname}
Summary:        Elastic Python Deployment
BuildRequires:  python3-devel
%if %{with optional_test_deps}
#BuildRequires: python3-eventlet -- retired in Fedora 41+
BuildRequires:  python3-gevent
%endif
BuildRequires:  %{_bindir}/sphinx-build-3
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_description


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{srcname}-%{version}
# remove shebangs and fix permissions
find . -type f -a \( -name '*.py' -o -name 'py.*' \) \
   -exec sed -i '1{/^#!/d}' {} \; \
   -exec chmod u=rw,go=r {} \;


%generate_buildrequires
%pyproject_buildrequires -t


%build
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel
make -C doc html PYTHONPATH=$(pwd)/src
# remove hidden file
rm doc/_build/html/.buildinfo


%install
SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_install
%pyproject_save_files -l execnet


%check
PYTEST_SELECT='not test_popen_io[gevent-sys.executable]'
PYTEST_SELECT+=' and not [gevent-socket]'
PYTEST_SELECT+=' and not [eventlet-socket]'
PYTEST_SELECT+=' and not [python2.7]'
PYTHONPATH=$(pwd)/src \
py.test-%{python3_version} -r s \
  -k "$PYTEST_SELECT" \
  testing \
  --timeout=30


%files -n python3-%{srcname} -f %{pyproject_files}
%doc README.rst
%doc doc/_build/html
%license LICENSE

%changelog
%autochangelog
