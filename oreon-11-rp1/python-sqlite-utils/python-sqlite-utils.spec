%global source0_hash 76114b6a5414714e6c70e5fa5c4781b301b590f6951b5da39c8cc60c21382ba1
Name:           python-sqlite-utils
Version:        4.2.1
Release:        1%{?dist}
Summary:        CLI tool and Python library for manipulating SQLite databases
License:        Apache-2.0
URL:            https://github.com/simonw/sqlite-utils
Source0:        https://files.pythonhosted.org/packages/source/s/sqlite_utils/sqlite_utils-%{version}.tar.gz
BuildArch:      noarch
Patch:          python-sqlite-utils-3.38-click.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-sqlite-utils = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-sqlite-utils
Summary:        CLI tool and Python library for manipulating SQLite databases
# oreon:reqs
Requires:       python3dist(click) >= 8.3.1
Requires:       python3dist(click-default-group) >= 1.2.3
# /oreon:reqs
%description -n python3-sqlite-utils

%prep
%global oreon_srcdir sqlite_utils-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlite-utils usr/lib/python3*/site-packages/sqlite_utils* usr/lib64/python3*/site-packages/sqlite_utils* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlite_utils* usr/lib64/python3*/site-packages/sqlite_utils* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-sqlite-utils -f %{oreon_filedir}/python3-sqlite-utils.list

%changelog

%autochangelog
