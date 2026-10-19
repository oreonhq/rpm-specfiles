%global source0_hash e4b68bb881802dda1a7d878b2fc84c06d1ee57fb40b874d3dc97dabfa36b8312
Name:           python-flask-sqlalchemy
Version:        3.1.1
Release:        1%{?dist}
Summary:        Add SQLAlchemy support to your Flask application.
License:        ...
URL:            https://github.com/pallets-eco/flask-sqlalchemy/
Source0:        https://files.pythonhosted.org/packages/source/f/flask_sqlalchemy/flask_sqlalchemy-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(flit-core) < 4
Requires:       python3-flask-sqlalchemy = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-flask-sqlalchemy
Summary:        Add SQLAlchemy support to your Flask application.
# oreon:reqs
Requires:       python3dist(flask) >= 2.2.5
Requires:       python3dist(sqlalchemy) >= 2.0.16
# /oreon:reqs
%description -n python3-flask-sqlalchemy

%prep
%global oreon_srcdir flask_sqlalchemy-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-flask-sqlalchemy usr/lib/python3*/site-packages/flask_sqlalchemy* usr/lib64/python3*/site-packages/flask_sqlalchemy* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/flask_sqlalchemy* usr/lib64/python3*/site-packages/flask_sqlalchemy* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-flask-sqlalchemy -f %{oreon_filedir}/python3-flask-sqlalchemy.list

%changelog

%autochangelog
