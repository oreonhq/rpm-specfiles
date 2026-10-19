%global source0_hash 3e6802a02c649477f77e104a16453897ec503f46094ba3b3471e858b67eb15c3
Name:           python-zope-sqlalchemy
Version:        4.1
Release:        1%{?dist}
BuildArch:      noarch
License:        ZPL-2.1
Summary:        Minimal Zope/SQLAlchemy transaction integration
URL:            https://github.com/zopefoundation/zope.sqlalchemy
Source0:        https://github.com/zopefoundation/zope.sqlalchemy/archive/%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) < 81
BuildRequires:  python3dist(setuptools) >= 78.1.1
Requires:       python3-zope-sqlalchemy = %{version}-%{release}
# /oreon:deps
%description

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

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zope-sqlalchemy usr/lib/python3*/site-packages/zope_sqlalchemy* usr/lib64/python3*/site-packages/zope_sqlalchemy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zope_sqlalchemy* usr/lib64/python3*/site-packages/zope_sqlalchemy* usr/bin/*

%check

%pyproject_check_import
%files
%files -n python3-zope-sqlalchemy -f %{oreon_filedir}/python3-zope-sqlalchemy.list

%changelog

%autochangelog
