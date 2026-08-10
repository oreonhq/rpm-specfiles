%global source0_hash 0ebac894fa7c5f8b7a89141c272133d8c1de6ddc75ea4b1f327f00d1f890df92

# Running the tests requires python3-zope-testrunner, which requires
# python3-zope-interface, which requires this package.  Build in bootstrap
# mode to avoid the circular dependency.
%bcond_with bootstrap
%bcond_with docs

# Install doc subpackage files into the main package doc directory
%global _docdir_fmt %{name}

Name:           python-zope-event
Version:        6.0
Release:        2%{?dist}
Summary:        Zope Event Publication
License:        ZPL-2.1
URL:            https://pypi.python.org/pypi/zope.event/
Source0:        %pypi_source zope_event
BuildArch:      noarch

%description
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

%package -n python3-zope-event
Summary:        Zope Event Publication (Python 3)

BuildRequires:  make
BuildRequires:  python3-devel
%if %{with docs}
BuildRequires:  python3-docs
BuildRequires:  %{py3_dist sphinx}
%endif

%description -n python3-zope-event
The zope.event package provides a simple event system. It provides
an event publishing system and a very simple event-dispatching system
on which more sophisticated event dispatching systems can be built.
(For example, a type-based event dispatching system that builds on
zope.event can be found in zope.component.)

This package contains the version for Python 3.

%package doc
Summary:        Documentation for zope.event

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n zope_event-%{version} -p1
# we don't have specific versions of setuptools available
sed -i -r 's/("| )setuptools == /\1setuptools >= /' pyproject.toml tox.ini

# Update the sphinx theme name
sed -i "s/'default'/'classic'/" docs/conf.py

# Use local objects.inv for intersphinx
sed -i "s|\('https://docs\.python\.org/': \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" docs/conf.py

%generate_buildrequires
%if %{with bootstrap}
%pyproject_buildrequires
%else
%pyproject_buildrequires -t
%endif

%build
%pyproject_wheel

%if %{with docs}
# build the sphinx documents
PYTHONPATH=$PWD/src make -C docs html
rm -f docs/_build/html/.buildinfo
%endif

%install
%pyproject_install
%pyproject_save_files zope

%if %{without bootstrap}
%check
%tox
%endif

%files -n python3-zope-event -f %{pyproject_files}
%doc CHANGES.rst COPYRIGHT.txt README.rst
%license LICENSE.txt
%exclude %{python3_sitelib}/zope/event/tests.py*
%exclude %{python3_sitelib}/zope/event/__pycache__/tests*

%files doc
%if %{with docs}
%doc docs/_build/html/
%endif

%changelog
%autochangelog
