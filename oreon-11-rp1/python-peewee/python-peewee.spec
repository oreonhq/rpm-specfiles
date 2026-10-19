%global source0_hash 8005cb45c54e1a282a2f24ddd583f0f7a80cd5d9c635d50d63f57c11d88c392a
Name:           python-peewee
Version:        4.5.1
Release:        1%{?dist}
Summary:        a little orm
License:        ...
URL:            https://github.com/coleifer/peewee
Source0:        https://files.pythonhosted.org/packages/source/p/peewee/peewee-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cython) >= 3
Requires:       python3-peewee = %{version}-%{release}
# /oreon:deps
%package -n       python3-peewee+mysql
Summary:        Metapackage for python3-peewee mysql extras
Requires:       python3-peewee = %{version}-%{release}
Provides:       python3dist(peewee[mysql]) = %{version}-%{release}

%description -n python3-peewee+mysql
Metapackage for python3-peewee mysql extras.

%package -n       python3-peewee+postgres
Summary:        Metapackage for python3-peewee postgres extras
Requires:       python3-peewee = %{version}-%{release}
Provides:       python3dist(peewee[postgres]) = %{version}-%{release}

%description -n python3-peewee+postgres
Metapackage for python3-peewee postgres extras.

%package -n       python3-peewee+psycopg3
Summary:        Metapackage for python3-peewee psycopg3 extras
Requires:       python3-peewee = %{version}-%{release}
Provides:       python3dist(peewee[psycopg3]) = %{version}-%{release}

%description -n python3-peewee+psycopg3
Metapackage for python3-peewee psycopg3 extras.

%package -n       python3-peewee+cysqlite
Summary:        Metapackage for python3-peewee cysqlite extras
Requires:       python3-peewee = %{version}-%{release}
Requires:       python3dist(cysqlite) >= 0.3.5
Provides:       python3dist(peewee[cysqlite]) = %{version}-%{release}

%description -n python3-peewee+cysqlite
Metapackage for python3-peewee cysqlite extras.

%package -n       python3-peewee+aiosqlite
Summary:        Metapackage for python3-peewee aiosqlite extras
Requires:       python3-peewee = %{version}-%{release}
Provides:       python3dist(peewee[aiosqlite]) = %{version}-%{release}

%description -n python3-peewee+aiosqlite
Metapackage for python3-peewee aiosqlite extras.

%package -n       python3-peewee+aiomysql
Summary:        Metapackage for python3-peewee aiomysql extras
Requires:       python3-peewee = %{version}-%{release}
Provides:       python3dist(peewee[aiomysql]) = %{version}-%{release}

%description -n python3-peewee+aiomysql
Metapackage for python3-peewee aiomysql extras.

%package -n       python3-peewee+asyncpg
Summary:        Metapackage for python3-peewee asyncpg extras
Requires:       python3-peewee = %{version}-%{release}
Provides:       python3dist(peewee[asyncpg]) = %{version}-%{release}

%description -n python3-peewee+asyncpg
Metapackage for python3-peewee asyncpg extras.

%description

%package -n     python3-peewee
Summary:        a little orm
%description -n python3-peewee

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras

%prep
%global oreon_srcdir peewee-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-peewee usr/lib/python3*/site-packages/peewee* usr/lib64/python3*/site-packages/peewee* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/peewee* usr/lib64/python3*/site-packages/peewee* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-peewee -f %{oreon_filedir}/python3-peewee.list

%changelog

%autochangelog
