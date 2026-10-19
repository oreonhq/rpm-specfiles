%global source0_hash d3ab0f53974296a806db3219b9191ba0e6d5cbbd1daa2e0d17208cb9b29d2102
Name:           python-zc-lockfile
Version:        4.0
Release:        1%{?dist}
Summary:        Basic Inter-Process Locks
License:        ZPL-2.1
URL:            https://pypi.io/project/zc.lockfile/
Source0:        https://files.pythonhosted.org/packages/source/z/zc_lockfile/zc_lockfile-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) == 78.1.1
Requires:       python3-zc-lockfile = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-zc-lockfile
Summary:        Basic Inter-Process Locks
%description -n python3-zc-lockfile
The zc.lockfile package provides a basic portable implementation of
interprocess locks using lock files. The purpose if not specifically
to lock files, but to simply provide locks with an implementation based
on file-locking primitives. Of course, these locks could be used to
mediate access to other files. For example, the ZODB file storage
implementation uses file locks to mediate access to file-storage
database files. The database files and lock file files are separate files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n zc_lockfile-%{version}

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-zc-lockfile usr/lib/python3*/site-packages/zc_lockfile* usr/lib64/python3*/site-packages/zc_lockfile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/zc_lockfile* usr/lib64/python3*/site-packages/zc_lockfile* usr/bin/*

%check

%tox
%files
%files -n python3-zc-lockfile -f %{oreon_filedir}/python3-zc-lockfile.list

%changelog

%autochangelog
