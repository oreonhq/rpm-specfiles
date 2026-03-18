Name:           pyxdg
Version:        0.28
Release:        1%{?dist}
Summary:        Python library to access freedesktop.org standards
License:        LGPL-2.0-only
URL:            http://freedesktop.org/Software/pyxdg
Source0:        %pypi_source
# https://cgit.freedesktop.org/xdg/pyxdg/commit/?id=275865e620471c194560824232be632c9cb61600
Patch0:         pyxdg-replace-imp-with-importlib.patch
# https://cgit.freedesktop.org/xdg/pyxdg/commit/?id=9291d419017263c922869d79ac1fe8d423e5f929
Patch1:         pyxdg-handle-python-3.14-ast.Str-changes.patch
# https://cgit.freedesktop.org/xdg/pyxdg/commit/?id=63033ac306aa26d32e1439417e59ae8f8a4c9820
Patch2:         pyxdg-handle-python-3.15-deprecations.patch

BuildArch:      noarch
# These are needed for the tests.
BuildRequires:  python3-pytest
BuildRequires:  hicolor-icon-theme
BuildRequires:  shared-mime-info

%description
PyXDG is a python library to access freedesktop.org standards.

%package -n python%{python3_pkgversion}-pyxdg
Summary:        Python3 library to access freedesktop.org standards
%{?python_provide:%python_provide python%{python3_pkgversion}-pyxdg}

%description -n python%{python3_pkgversion}-pyxdg
PyXDG is a python library to access freedesktop.org standards. This
package contains a Python 3 version of PyXDG.

%prep
%setup -q
%patch -P0 -p1 -b .replace-imp-with-importlib
%patch -P1 -p1 -b .handle-python-3.14-ast.Str-changes
%patch -P2 -p1 -b .handle-python-3.15-deprecations

# fix symlink example
rm -rf test/example/png_symlink
pushd test/example
ln -s png_file png_symlink
popd

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l xdg

%check
%pyproject_check_import
%pytest test/test_*.py

%files -n python%{python3_pkgversion}-pyxdg -f %{pyproject_files}
%license COPYING
%doc AUTHORS ChangeLog README TODO

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.28-1
- Prepare for Oreon 11 (RP1)
