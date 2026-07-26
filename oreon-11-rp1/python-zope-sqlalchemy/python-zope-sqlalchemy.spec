%global source0_hash 3e6802a02c649477f77e104a16453897ec503f46094ba3b3471e858b67eb15c3

Name:           python-zope-sqlalchemy
Version:        4.1
Release:        2%{?dist}
BuildArch:      noarch

License:        ZPL-2.1
Summary:        Minimal Zope/SQLAlchemy transaction integration
URL:            https://github.com/zopefoundation/zope.sqlalchemy
Source0:        https://github.com/zopefoundation/zope.sqlalchemy/archive/%{version}.tar.gz

BuildRequires:      python3-devel
BuildRequires:      python3-zope-testing

%global _description\
The aim of this package is to unify the plethora of existing packages\
integrating SQLAlchemy with Zope's transaction management. As such it seeks\
only to provide a data manager and makes no attempt to define a zopeish way to\
configure engines.

%description %_description

%package -n python3-zope-sqlalchemy
Summary:   Minimal Zope/SQLAlchemy transaction integration with Python 3 support

Requires:           python3-transaction
Requires:           python3-sqlalchemy >= 0.5.1
Requires:           python3-zope-interface >= 3.6.0

%description -n python3-zope-sqlalchemy
The aim of this package is to unify the plethora of existing packages
integrating SQLAlchemy with Zope's transaction management. As such it seeks
only to provide a data manager and makes no attempt to define a zopeish way to
configure engines.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n zope.sqlalchemy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files zope

%check
%pyproject_check_import

%files -n python3-zope-sqlalchemy -f %{pyproject_files}
%doc src/zope/sqlalchemy/README.rst
%doc CHANGES.rst CREDITS.rst
%license COPYRIGHT.txt LICENSE.txt
%exclude %{python3_sitelib}/zope/sqlalchemy/*.rst

%changelog
%autochangelog
