%global source0_hash c6b78b5bb486b541a5c484c93a22079ad7fab8c142a26793830748586457b3c8
Name:           python-sqlite-migrate
Version:        0.2
Release:        1%{?dist}
Summary:        Compatibility package for sqlite-utils migrations
License:        Apache-2.0
URL:            https://github.com/simonw/sqlite-migrate
Source0:        https://files.pythonhosted.org/packages/source/s/sqlite_migrate/sqlite_migrate-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-sqlite-migrate-0.1b0-toml.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(uv-build) < 0.12.0
BuildRequires:  python3dist(uv-build) >= 0.9.18
Requires:       python3-sqlite-migrate = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sqlite-migrate
Summary:        Compatibility package for sqlite-utils migrations
# oreon:reqs
Requires:       python3dist(sqlite-utils) >= 4
# /oreon:reqs
%description -n python3-sqlite-migrate

%prep
%global oreon_srcdir sqlite_migrate-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlite-migrate usr/lib/python3*/site-packages/sqlite_migrate* usr/lib64/python3*/site-packages/sqlite_migrate* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlite_migrate* usr/lib64/python3*/site-packages/sqlite_migrate* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlite-migrate -f %{oreon_filedir}/python3-sqlite-migrate.list

%changelog

%autochangelog
