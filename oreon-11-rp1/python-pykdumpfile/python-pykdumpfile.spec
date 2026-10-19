%global source0_hash c92551ab2be318320c3e002bdd92d2bbdf148749e31c8c6449c431d04db2052a
Name:           python-pykdumpfile
Version:        0.5.5.1
Release:        1%{?dist}
Summary:        Python bindings to libkdumpfile
License:        GPL-2.0-or-later
URL:            https://github.com/ptesarik/pykdumpfile
Source0:        https://files.pythonhosted.org/packages/source/p/pykdumpfile/pykdumpfile-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pykdumpfile = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pykdumpfile
Summary:        Python bindings to libkdumpfile
%description -n python3-pykdumpfile

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n pykdumpfile-%{version}
# These are meant for Python 2 and wont' byte-compile
rm {addrxlat,kdumpfile}/defs_py2.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pykdumpfile usr/lib/python3*/site-packages/pykdumpfile* usr/lib64/python3*/site-packages/pykdumpfile* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pykdumpfile* usr/lib64/python3*/site-packages/pykdumpfile* usr/bin/*

%check

%pyproject_check_import
%pytest -v
%files
%files -n python3-pykdumpfile -f %{oreon_filedir}/python3-pykdumpfile.list

%changelog

%autochangelog
