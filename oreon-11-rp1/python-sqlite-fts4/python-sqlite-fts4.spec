%global source0_hash 6d2d227665e609cdb00e78323a4cd8c778143e07e8dc98453b8edd0a2e3c8ad8
Summary:        Custom SQLite functions to rank documents indexed using the FTS4 extension
Name:           python-sqlite-fts4
Version:        1.0.3
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://pypi.python.org/project/sqlite-fts4/
Source0:        https://github.com/simonw/sqlite-fts4/archive/%{version}/sqlite-fts4-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-sqlite-fts4 = %{version}-%{release}
# /oreon:deps
%description

%package     -n python3-sqlite-fts4
Summary:        Custom SQLite functions to rank documents indexed using the FTS4 extension
%description -n python3-sqlite-fts4

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir sqlite-fts4-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-sqlite-fts4 usr/lib/python3*/site-packages/sqlite_fts4* usr/lib64/python3*/site-packages/sqlite_fts4* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/sqlite_fts4* usr/lib64/python3*/site-packages/sqlite_fts4* usr/bin/*

%check

%pyproject_check_import
%pytest
%files
%files -n python3-sqlite-fts4 -f %{oreon_filedir}/python3-sqlite-fts4.list

%changelog

%autochangelog
