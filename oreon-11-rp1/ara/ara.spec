%global source0_hash a58b2104760a55ebd7a7832e3a67c8c310e926b2d2cea26be3b9a2a38be11d8b

# Don't attempt to build -docs, -tests and -server on rhel/centos until
# missing packages are available.
%global with_docs %{undefined rhel}
%global with_tests %{undefined rhel}
%global with_server %{undefined rhel}
# python3-dynaconf doesn't provide the yaml extra
%global _python_no_extras_requires 1

Name:           ara
Version:        1.7.4
Release:        3%{?dist}
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot

License:        GPL-3.0-or-later
URL:            https://codeberg.org/ansible-community/ara
Source0:        %{pypi_source ara}
BuildArch:      noarch

BuildRequires:  git-core
BuildRequires:  python3-devel

%if 0%{?with_tests}
BuildRequires:  python3-factory-boy
BuildRequires:  python3-faker
%endif

%if 0%{?with_docs}
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme
BuildRequires:  python3-sphinxcontrib-programoutput
%endif

%description
%{summary}.

%package -n python3-ara
Summary:        %{summary}
# ara used to be a blank package.
Obsoletes:      ara < 1.6.1-1
Provides:       ara = %{version}-%{release}

%description -n python3-ara
%{summary}.

This package installs the python files and Ansible plugins.

%if 0%{?with_server}
# Ending this with +server tells the Python extras dependency generator
# to add dependencies for the 'server' extra as defined in setup.cfg
#
# We can't use %%pyproject_extras_subpkg, because we need more control over
# included Requires/Provides/Obsoletes and files.
%package -n python3-ara+server
Summary:        %{summary}

# Convenience alias
Provides:       ara-server = %{version}-%{release}
# Obsolete the old name
%py_provides    python3-ara-server
Obsoletes:      python3-ara-server < 1.6.1-1

Requires:       python3-ara = %{version}-%{release}
Requires:       python3-ruamel-yaml
Requires:       tzdata

%description -n python3-ara+server
%{summary}.

This package installs the API server dependencies.

%package -n python3-ara+postgresql
Summary:        %{summary}
Requires:       python3-ara+server = %{version}-%{release}

%description -n python3-ara+postgresql
%{summary}.

This package installs the needed dependencies for the API server to use a
PostgreSQL database.

%package -n python3-ara+mysql
Summary:        %{summary}

%description -n python3-ara+mysql
%{summary}.

This package installs the needed dependencies for the API server to use a
MySQL database.
%endif

%if 0%{?with_tests}
%package -n python3-ara-tests
Summary:        %{summary}

Requires:       python3-ara+server = %{version}-%{release}
Requires:       python3-factory-boy
Requires:       python3-faker

%description -n python3-ara-tests
%{summary}.

This package installs the test dependencies.
%endif

%if 0%{?with_docs}
%package doc
Summary:        %{summary}

%description doc
%{summary}.

This package installs the documentation.
%endif

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ara-%{version} -S git
# Remove tzdata from automatic python requirements, it's a system package added to Requires
# See: https://codeberg.org/ansible-community/ara/commit/d08c5adbd3708e777e65889d4ab7203caf6567a6
sed -i '/tzdata/d' setup.cfg

%generate_buildrequires
%pyproject_buildrequires -x server

%build
%pyproject_wheel

%if 0%{?with_docs}
# XXX: The docs build needs to execute `ara` and 'ara-manage'
%{python3} -m venv dummy_install --system-site-packages
. ./dummy_install/bin/activate
pip install %{_pyproject_wheeldir}/ara-%{version}-*.whl
sphinx-build -b html doc/source doc/build/html
# Remove sphinx build leftovers
rm -rf doc/build/html/.{doctrees,buildinfo}
rm -rf doc/build/html/_{sources,static}
%endif

%install
%pyproject_install

%if 0%{?with_tests}
%check
# Run unit tests
# Set time zone to UTC -- buildsystem's timezone is "local" which isn't valid
ARA_TIME_ZONE=UTC %{__python3} manage.py test ara
%endif

%files -n python3-ara
%doc README.md
%license LICENSE
%{_bindir}/ara
%{python3_sitelib}/ara/
%exclude %{python3_sitelib}/ara/api/tests/
%{python3_sitelib}/ara-*.dist-info/

%if 0%{?with_server}
%files -n python3-ara+server
%{_bindir}/ara-manage
# This is needed for the python extras dependency generator
%ghost %{python3_sitelib}/ara-*.dist-info/

%files -n python3-ara+postgresql
%ghost %{python3_sitelib}/ara-*.dist-info/

%files -n python3-ara+mysql
%ghost %{python3_sitelib}/ara-*.dist-info/
%endif

%if 0%{?with_tests}
%files -n python3-ara-tests
%{python3_sitelib}/ara/api/tests/
%endif

%if 0%{?with_docs}
%files doc
%doc README.md doc/build/html
%license LICENSE
%endif

%changelog
%autochangelog
