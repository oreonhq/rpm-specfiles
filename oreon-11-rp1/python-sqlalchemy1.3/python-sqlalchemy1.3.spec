%global source0_hash ebbb777cbf9312359b897bf81ba00dae0f5cb69fba2a18265dcc18a6f5ef7519

# pytest7 is not compatible
%if (0%{?fedora} && 0%{?fedora} < 37) || (0%{?rhel} && 0%{?rhel} < 10)
%bcond_without tests
%else
%bcond_with tests
%endif

# when bootstrapping Python, pytest-xdist is not yet available
%bcond_without xdist

%global srcname SQLAlchemy

Name:           python-sqlalchemy1.3
Version:        1.3.24
# cope with pre-release versions containing tildes
%global srcversion %{lua: srcversion, num = rpm.expand("%{version}"):gsub("~", ""); print(srcversion);}
Release:        19%{?dist}
Summary:        Modular and flexible ORM library for python (legacy 1.3.x version)

License:        MIT
URL:            http://www.sqlalchemy.org/
Source0:        https://files.pythonhosted.org/packages/source/S/%{srcname}/%{srcname}-%{srcversion}.tar.gz

BuildRequires:  gcc

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%if %{with tests}
BuildRequires:  python3-mock
BuildRequires:  python3-pytest
%if %{with xdist}
BuildRequires:  python3-pytest-xdist
%endif
%endif

%description
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

%package doc
Summary:        Documentation for SQLAlchemy 1.3.x
BuildArch:      noarch

%description doc
Documentation for SQLAlchemy 1.3.x

%package -n python3-sqlalchemy1.3
Summary:        Modular and flexible ORM library for python (legacy 1.3.x version)
%{?python_provide:%python_provide python%{python3_pkgversion}-sqlalchemy1.3}
# This is a compat package that conflicts with the main one
Conflicts:      python3-sqlalchemy
# This is a compatibility package for software that isn't yet updated to work with sqlalchemy 1.4+
Provides:       deprecated()

%description -n python3-sqlalchemy1.3
SQLAlchemy is an Object Relational Mapper (ORM) that provides a flexible,
high-level interface to SQL databases.  Database and domain concepts are
decoupled, allowing both sides maximum flexibility and power. SQLAlchemy
provides a powerful mapping layer that can work as automatically or as manually
as you choose, determining relationships based on foreign keys or letting you
define the join conditions explicitly, to bridge the gap between database and
domain.

This package includes the python 3 version of the module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{srcname}-%{srcversion}

# Remove flag for pytest-xdist. (python2-pytest-xdist is a removed dependency.)
# (--max-worker-restart=5 would end the test run after 5 crashing tests.)
sed -i -e's/\(addopts = .*\) --max-worker-restart=5/\1/' setup.cfg

%build
%py3_build

%install
%py3_install

# remove unnecessary scripts for building documentation
rm -rf doc/build

%if %{with tests}
%check
PYTHONPATH=. %{__python3} -m pytest test \
%if %{with xdist}
--numprocesses=auto
%endif
%endif

%files doc
%doc doc examples

%files -n python3-sqlalchemy1.3
%license LICENSE
%doc README.rst
%{python3_sitearch}/*

%changelog
%autochangelog
