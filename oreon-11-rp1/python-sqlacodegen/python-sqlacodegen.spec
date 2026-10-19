%global source0_hash 403b322b22bf5bab9c89e3eb1999005b91164f29e79f8ef7bb461192e0e68118
Name:           python-sqlacodegen
Version:        4.0.4
Release:        1%{?dist}
Summary:        Automatic model code generator for SQLAlchemy
License:        MIT
URL:            https://github.com/agronholm/sqlacodegen
Source0:        https://files.pythonhosted.org/packages/source/s/sqlacodegen/sqlacodegen-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 64
BuildRequires:  python3dist(setuptools-scm[toml]) >= 6.4
Requires:       python3-sqlacodegen = %{version}-%{release}
# /oreon:deps
%package -n       python3-sqlacodegen+sqlmodel
Summary:        Metapackage for python3-sqlacodegen sqlmodel extras
Requires:       python3-sqlacodegen = %{version}-%{release}
Requires:       python3dist(sqlmodel) >= 0.0.22
Provides:       python3dist(sqlacodegen[sqlmodel]) = %{version}-%{release}

%description -n python3-sqlacodegen+sqlmodel
Metapackage for python3-sqlacodegen sqlmodel extras.

%package -n       python3-sqlacodegen+citext
Summary:        Metapackage for python3-sqlacodegen citext extras
Requires:       python3-sqlacodegen = %{version}-%{release}
Requires:       python3dist(sqlalchemy-citext) >= 1.7.0
Provides:       python3dist(sqlacodegen[citext]) = %{version}-%{release}

%description -n python3-sqlacodegen+citext
Metapackage for python3-sqlacodegen citext extras.

%package -n       python3-sqlacodegen+geoalchemy2
Summary:        Metapackage for python3-sqlacodegen geoalchemy2 extras
Requires:       python3-sqlacodegen = %{version}-%{release}
Requires:       python3dist(geoalchemy2) >= 0.17.0
Provides:       python3dist(sqlacodegen[geoalchemy2]) = %{version}-%{release}

%description -n python3-sqlacodegen+geoalchemy2
Metapackage for python3-sqlacodegen geoalchemy2 extras.

%package -n       python3-sqlacodegen+pgvector
Summary:        Metapackage for python3-sqlacodegen pgvector extras
Requires:       python3-sqlacodegen = %{version}-%{release}
Requires:       python3dist(pgvector) >= 0.2.4
Provides:       python3dist(sqlacodegen[pgvector]) = %{version}-%{release}

%description -n python3-sqlacodegen+pgvector
Metapackage for python3-sqlacodegen pgvector extras.

%description

%package -n     python3-sqlacodegen
Summary:        Automatic model code generator for SQLAlchemy
# oreon:reqs
Requires:       python3dist(inflect) >= 4.0.0
Requires:       python3dist(sqlalchemy) >= 2.0.29
# /oreon:reqs
%description -n python3-sqlacodegen

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir sqlacodegen-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlacodegen usr/lib/python3*/site-packages/sqlacodegen* usr/lib64/python3*/site-packages/sqlacodegen* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlacodegen* usr/lib64/python3*/site-packages/sqlacodegen* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlacodegen -f %{oreon_filedir}/python3-sqlacodegen.list

%changelog

%autochangelog
