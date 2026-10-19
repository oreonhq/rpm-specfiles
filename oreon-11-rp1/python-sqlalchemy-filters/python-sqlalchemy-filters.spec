%global source0_hash 40f2daead93c4db2409cf5e5abf67a420179f9e5c1df5c15fa1b474f6533b105
Name:           python-sqlalchemy-filters
Version:        0.13.0
Release:        1%{?dist}
Summary:        A library to filter SQLAlchemy queries.
License:        ...
URL:            https://github.com/juliotrigo/sqlalchemy-filters
Source0:        https://files.pythonhosted.org/packages/source/s/sqlalchemy-filters/sqlalchemy-filters-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sqlalchemy-filters = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sqlalchemy-filters
Summary:        A library to filter SQLAlchemy queries.
%description -n python3-sqlalchemy-filters

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sqlalchemy-filters-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlalchemy-filters usr/lib/python3*/site-packages/sqlalchemy_filters* usr/lib64/python3*/site-packages/sqlalchemy_filters* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlalchemy_filters* usr/lib64/python3*/site-packages/sqlalchemy_filters* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlalchemy-filters -f %{oreon_filedir}/python3-sqlalchemy-filters.list

%changelog

%autochangelog
