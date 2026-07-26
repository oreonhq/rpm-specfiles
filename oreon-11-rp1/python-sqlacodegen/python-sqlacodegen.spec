%global source0_hash e9ca5ee839421616f1113b728d1c67a2bdb0ecd08b02a1d57819eee819929559

%{?python_enable_dependency_generator}

%global modname sqlacodegen

Name:           python-%{modname}
Version:        2.0.0
Release:        29%{?dist}
Summary:        Automatic model code generator for SQLAlchemy

License:        MIT
URL:            https://github.com/agronholm/sqlacodegen
Source0:        https://files.pythonhosted.org/packages/source/%(n=%{modname}; echo ${n:0:1})/%{modname}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description\
This is a tool that reads the structure of an existing database and generates\
the appropriate SQLAlchemy model code, using the declarative style if possible.\
\
This tool was written as a replacement for sqlautocode, which was suffering\
from several issues (including, but not limited to, incompatibility with\
Python 3 and the latest SQLAlchemy version).\
\
Features:\
* Supports SQLAlchemy 0.8.x - 1.2.x\
* Produces declarative code that almost looks like it was hand written\
* Produces PEP 8 compliant code\
* Accurately determines relationships, including many-to-many, one-to-one\
* Automatically detects joined table inheritance\
* Excellent test coverage

%description %{_description}

%package -n python3-%{modname}
Summary:        Automatic model code generator for SQLAlchemy
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools >= 36.2.7
BuildRequires:  python3-setuptools_scm >= 1.7.0

%description -n python3-%{modname} %{_description}

Python 3 version.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

#check
# Requires multiple DBs to be running

%files -n python3-%{modname}
%license LICENSE
%doc README.rst CHANGES.rst
%{_bindir}/%{modname}
%{python3_sitelib}/%{modname}*

%changelog
%autochangelog
