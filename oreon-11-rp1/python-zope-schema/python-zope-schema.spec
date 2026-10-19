%global source0_hash 2d9faa7f91a7bf09fcab2c039d9182fcc9ce7042dc77e18d3df277904aee0948
%global modname zope.schema
Summary:        Zope 3 schemas
Name: python-zope-schema
Version: 8.1
Release:        1%{?dist}
License: ZPL-2.1
BuildArch: noarch
URL: http://pypi.python.org/pypi/zope.schema
Source0:        https://files.pythonhosted.org/packages/source/z/zope_schema/zope_schema-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) == 78.1.1
Requires:       python3-zope-schema = %{version}-%{release}
# /oreon:deps
%description
This package is a zope.interface extension for defining data schemas.

%package -n python3-zope-schema
Summary:        Zope 3 schemas
%{?python_provide:%python_provide python3-zope-schema}
%description -n python3-zope-schema
This package is a zope.interface extension for defining data schemas.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n zope_schema-%{version}
# we don't have specific versions of setuptools available
sed -i -r 's/("| )setuptools == /\1setuptools >= /' pyproject.toml tox.ini

%build

%pyproject_wheel
PYTHONPATH="src" sphinx-build-%{python3_version} -b html docs/ build/sphinx/html
cp -pr build/sphinx/html .
rm -fr html/{.buildinfo,.doctrees}
%install
%pyproject_install
%oreon_autofiles python3-zope-schema usr/lib/python3*/site-packages/zope_schema* usr/lib64/python3*/site-packages/zope_schema* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_schema* usr/lib64/python3*/site-packages/zope_schema* usr/bin/*

%check

PYTHONPATH=%{buildroot}%{python3_sitelib} zope-testrunner --test-path=src
%files
%files -n python3-zope-schema -f %{oreon_filedir}/python3-zope-schema.list

%changelog

%autochangelog
