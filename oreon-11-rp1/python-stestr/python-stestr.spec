%global source0_hash 5f61c369eece63c292d13599e12aa158af7685990643f24dd6fa7fabfe34e98a

%global pypi_name stestr
# Enable bootstrap
%bcond_without bootstrap
%global with_doc 1

%global common_desc \
stestr is a fork of the testrepository that concentrates on being a \
dedicated test runner for python projects. The generic abstraction layers \
which enabled testr to work with any subunit emitting runner are gone. \
stestr hard codes python-subunit-isms into how it works.

Name:       python-%{pypi_name}
Version:    4.1.0
Release:    12%{?dist}
Summary:    A test runner runner similar to testrepository

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:    Apache-2.0
URL:        https://pypi.python.org/pypi/stestr
Source0:    %pypi_source
BuildArch:  noarch

%description
%{common_desc}

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        A test runner runner similar to testrepository
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

BuildRequires:    python%{python3_pkgversion}-devel
BuildRequires:    git-core

Requires:   python%{python3_pkgversion}-pbr
Requires:   python%{python3_pkgversion}-subunit >= 1.4.0
Requires:   python%{python3_pkgversion}-fixtures >= 3.0.0
Requires:   python%{python3_pkgversion}-testtools >= 2.2.0
Requires:   python%{python3_pkgversion}-PyYAML >= 3.10.0
Requires:   python%{python3_pkgversion}-cliff >= 2.8.0
Requires:   python%{python3_pkgversion}-voluptuous >= 0.8.9

%description -n python%{python3_pkgversion}-%{pypi_name}
%{common_desc}

%if %{without bootstrap}
%package -n     python%{python3_pkgversion}-%{pypi_name}-sql
Summary:        sql plugin for stestr

BuildRequires:  /usr/bin/subunit2sql-db-manage
Requires:       python%{python3_pkgversion}-%{pypi_name} = %{version}-%{release}
Requires:       python%{python3_pkgversion}-subunit2sql

%description    -n python%{python3_pkgversion}-%{pypi_name}-sql
It contains the sql plugin for stestr.
%endif

%if 0%{?with_doc}
%package -n python-%{pypi_name}-doc
Summary:        stestr documentation

%description -n python-%{pypi_name}-doc
%{common_desc}

It contains the documentation for stestr.
%endif

%generate_buildrequires
%pyproject_buildrequires -t %{!?with_bootstrap:-x sql}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -S git
sed -i '/doc8.*/d' test-requirements.txt
sed -i '/hacking.*/d' test-requirements.txt
sed -i '/black.*/d' test-requirements.txt
# Replace removed SafeConfigParser with ConfigParser
# Upstream: https://github.com/mtreinish/stestr/pull/344
sed -i 's/SafeConfigParser/ConfigParser/' stestr/commands/run.py

%build
%pyproject_wheel

%if 0%{?with_doc}
# generate html docs
PYTHONPATH=%{pyproject_build_lib} sphinx-build doc/source doc/build/html
# remove the sphinx-build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
%endif

%install
%pyproject_install
%pyproject_save_files %{pypi_name}
# compat symlinks
ln -s stestr %{buildroot}/%{_bindir}/stestr-3
ln -s stestr-3 %{buildroot}/%{_bindir}/stestr-%{python3_version}

%check
%tox

%files -n python%{python3_pkgversion}-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%{_bindir}/stestr*

%if %{without bootstrap}
%files -n python%{python3_pkgversion}-%{pypi_name}-sql
%{python3_sitelib}/%{pypi_name}/repository/sql.py
%endif

%if 0%{?with_doc}
%files -n python-%{pypi_name}-doc
%license LICENSE
%doc README.rst
%doc doc/build/html
%endif

%changelog
%autochangelog
