%global source0_hash 3579c8a80b6ce1b08bdbb557418cf0e12971ba6b8734158f7502b5a2bcd850c0
%global with_docs %{undefined rhel}
%global with_tests %{undefined rhel}
%global with_server %{undefined rhel}
%global _python_no_extras_requires 1
Name:           ara
Version:        1.8.0
Release:        1%{?dist}
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot
License:        GPL-3.0-or-later
URL:            https://codeberg.org/ansible-community/ara
Source0:        https://files.pythonhosted.org/packages/source/a/ara/ara-%{version}.tar.gz
BuildArch:      noarch
%if 0%{?with_tests}
%endif
%if 0%{?with_docs}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ara = %{version}-%{release}
# /oreon:deps
%package -n       python3-ara+server
Summary:        Metapackage for python3-ara server extras
Requires:       python3-ara = %{version}-%{release}
Requires:       python3dist(django) >= 5.2
Requires:       python3dist(django) < 5.3
Requires:       python3dist(djangorestframework) >= 3.9.1
Requires:       python3dist(django-health-check) < 4.0.0
Requires:       python3dist(dynaconf[yaml]) >= 3.0.0
Requires:       python3dist(dynaconf[yaml]) < 4.0.0
Requires:       python3dist(tzlocal) >= 4.0
Provides:       python3dist(ara[server]) = %{version}-%{release}

%description -n python3-ara+server
Metapackage for python3-ara server extras.

%package -n       python3-ara+postgresql
Summary:        Metapackage for python3-ara postgresql extras
Requires:       python3-ara = %{version}-%{release}
Provides:       python3dist(ara[postgresql]) = %{version}-%{release}

%description -n python3-ara+postgresql
Metapackage for python3-ara postgresql extras.

%package -n       python3-ara+mysql
Summary:        Metapackage for python3-ara mysql extras
Requires:       python3-ara = %{version}-%{release}
Provides:       python3dist(ara[mysql]) = %{version}-%{release}

%description -n python3-ara+mysql
Metapackage for python3-ara mysql extras.

%package -n       python3-ara+prometheus
Summary:        Metapackage for python3-ara prometheus extras
Requires:       python3-ara = %{version}-%{release}
Provides:       python3dist(ara[prometheus]) = %{version}-%{release}

%description -n python3-ara+prometheus
Metapackage for python3-ara prometheus extras.

%description
%{summary}.

%package -n python3-ara
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot
Obsoletes:      ara < 1.6.1-1
Provides:       ara = %{version}-%{release}
# oreon:reqs
Requires:       python3dist(requests) >= 2.14.2
# /oreon:reqs
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
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot
Provides:       ara-server = %{version}-%{release}
%py_provides    python3-ara-server
Obsoletes:      python3-ara-server < 1.6.1-1
Requires:       python3-ara = %{version}-%{release}
Requires:       python3-ruamel-yaml
Requires:       tzdata
%description -n python3-ara+server
%{summary}.

This package installs the API server dependencies.

%package -n python3-ara+postgresql
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot
Requires:       python3-ara+server = %{version}-%{release}
%description -n python3-ara+postgresql
%{summary}.

This package installs the needed dependencies for the API server to use a
PostgreSQL database.

%package -n python3-ara+mysql
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot
%description -n python3-ara+mysql
%{summary}.

This package installs the needed dependencies for the API server to use a
MySQL database.
%endif

%if 0%{?with_tests}
%package -n python3-ara-tests
Summary:        Records Ansible playbooks and makes them easier to understand and troubleshoot
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

%build

%pyproject_wheel
%if 0%{?with_docs}
%{python3} -m venv dummy_install --system-site-packages
. ./dummy_install/bin/activate
pip install %{_pyproject_wheeldir}/ara-%{version}-*.whl
sphinx-build -b html doc/source doc/build/html
rm -rf doc/build/html/.{doctrees,buildinfo}
rm -rf doc/build/html/_{sources,static}
%endif
%install
%pyproject_install
%oreon_autofiles python3-ara usr/lib/python3*/site-packages/ara* usr/lib64/python3*/site-packages/ara* usr/bin/*
%oreon_autofiles python3-ara-tests usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/lib/python3*/site-packages/ara* usr/lib64/python3*/site-packages/ara* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if 0%{?with_tests}
%check

ARA_TIME_ZONE=UTC %{__python3} manage.py test ara
%endif
%files
%files -n python3-ara -f %{oreon_filedir}/python3-ara.list
%files -n python3-ara-tests -f %{oreon_filedir}/python3-ara-tests.list
%files -n ara-doc -f %{oreon_filedir}/ara-doc.list

%changelog

%autochangelog
