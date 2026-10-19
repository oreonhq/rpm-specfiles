%global source0_hash 2ce7db7dc38b957f0e31de9bf554fdc8bedaf59e41a53dec548c17530ec7f639
Name:           python-admesh
Version:        0.98.9
Release:        1%{?dist}
Summary:        Python bindings for ADMesh, STL manipulation library
License:        GPL-2.0-or-later
URL:            https://github.com/admesh/python-admesh
Source0:        https://files.pythonhosted.org/packages/source/a/admesh/admesh-%{version}.tar.gz
Source1:        %{url}/raw/v%{version}/test/utils.py
Patch:          %{url}/pull/17.patch
%if 0%{?fedora} >= 42 || 0%{?rhel} >= 11 || 0%{?oreon} >= 11
ExcludeArch:    %{ix86}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-admesh = %{version}-%{release}
# /oreon:deps
%description
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.

%package -n     python3-admesh
Summary:        Python 3 bindings for ADMesh, STL manipulation library
%description -n python3-admesh
This module provides bindings for the ADMesh library.
It lets you manipulate 3D models in binary or ASCII STL
format and partially repair them if necessary.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n admesh-%{version} -p1
cp %{SOURCE1} test/

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-admesh usr/lib/python3*/site-packages/admesh* usr/lib64/python3*/site-packages/admesh* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/admesh* usr/lib64/python3*/site-packages/admesh* usr/bin/*

%check

%pyproject_check_import
%pytest -v
%files
%files -n python3-admesh -f %{oreon_filedir}/python3-admesh.list

%changelog

%autochangelog
