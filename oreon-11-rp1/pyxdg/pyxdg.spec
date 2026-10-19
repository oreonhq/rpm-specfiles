%global source0_hash 3267bb3074e934df202af2ee0868575484108581e6f3cb006af1da35395e88b4
Name:           pyxdg
Version:        0.28
Release:        1%{?dist}
Summary:        Python library to access freedesktop.org standards
License:        LGPL-2.0-only
URL:            http://freedesktop.org/Software/pyxdg
Source0:        https://files.pythonhosted.org/packages/source/p/pyxdg/pyxdg-0.28.tar.gz
Patch0:         pyxdg-replace-imp-with-importlib.patch
Patch1:         pyxdg-handle-python-3.14-ast.Str-changes.patch
Patch2:         pyxdg-handle-python-3.15-deprecations.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-pyxdg = %{version}-%{release}
# /oreon:deps
%description
PyXDG is a python library to access freedesktop.org standards.

%package -n python%{python3_pkgversion}-pyxdg
Summary:        Python3 library to access freedesktop.org standards
%{?python_provide:%python_provide python%{python3_pkgversion}-pyxdg}
%description -n python%{python3_pkgversion}-pyxdg
PyXDG is a python library to access freedesktop.org standards. This
package contains a Python 3 version of PyXDG.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q
%patch -P0 -p1 -b .replace-imp-with-importlib
%patch -P1 -p1 -b .handle-python-3.14-ast.Str-changes
%patch -P2 -p1 -b .handle-python-3.15-deprecations

# fix symlink example
rm -rf test/example/png_symlink
pushd test/example
ln -s png_file png_symlink
popd

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/pyxdg* usr/lib64/python3*/site-packages/pyxdg* usr/bin/*

%check

%pyproject_check_import
%pytest test/test_*.py
%files
%files -n python3-pyxdg -f %{oreon_filedir}/python3-pyxdg.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-1
- Prepare for Oreon 11 (RP1)
