%global source0_hash 399b2536d88557cd1bb8e3734ad76c014ed74ab785e5d2c2b5ce03e17b420592

%global srcname visvis
Name:             python-%{srcname}
Version:          1.15.0
Release:          2%{?dist}
Summary:          Python library for visualization of 1D to 4D data in an object oriented way
# Automatically converted from old format: BSD - review is highly recommended.
License:          LicenseRef-Callaway-BSD
URL:              https://github.com/almarklein/%{srcname}
Source0:          %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz
BuildArch:        noarch
BuildRequires:    python3-devel
BuildRequires:    sed

%global _description\
Visvis is a pure Python library for visualization of 1D to 4D data in an\
object oriented way. Essentially, visvis is an object oriented layer of\
Python on top of OpenGl, thereby combining the power of OpenGl with the\
usability of Python. A Matlab/Matplotlib-like interface in the form of a\
set of functions allows easy creation of objects (e.g. plot(), imshow(),\
volshow(), surf()).

%description
%{_description}

%package -n python3-%{srcname}
Summary:          %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
BuildRequires:    python3-devel, python3-setuptools
Requires:         python3-numpy, python3-pyopengl
Recommends:       python3-PyQt4, python3-wxpython4
Recommends:       python3-gobject

%description -n python3-%{srcname}
%{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -n %{srcname}-%{version}

# fix shebangs in examples
pushd examples
sed -i "1 s|#!/usr/bin/env python|#!%{python3}|" *.py
popd

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files visvis

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
