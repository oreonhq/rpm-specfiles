# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5cddc243c75114ba845f01b1f87aca1572dbf7b6c2d88636ed3e1d2bccd7f1bf

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           python3-numpy
Version:        2.5.5
Release:        1%{?dist}
Summary:        Array processing for numbers, strings, records, and objects
License:        BSD-3-Clause AND 0BSD AND MIT AND Zlib AND CC0-1.0
URL:            https://numpy.org
Source0:        https://files.pythonhosted.org/packages/4e/3a/8770c288c47f0b5c2a786d3c20e79f66fd245f2d42cd232d7cd5e00e83e5/numpy-%{version}.tar.gz
Provides:       python3dist(numpy) = %{version}

BuildRequires:  oreon-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-build
BuildRequires:  python3-installer
BuildRequires:  python3-meson-python
BuildRequires:  python3-cython
BuildRequires:  meson
BuildRequires:  ninja-build
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  flang
BuildRequires:  openblas-devel
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-charset-normalizer
BuildRequires:  python3-tzdata
Requires:       python3

%description
NumPy is the array library for Python. This build links OpenBLAS.

%prep
%oreon_sha256
%autosetup -n numpy-%{version}

%build
FFLAGS=$(printf '%s\n' "$FFLAGS" | sed \
  -e 's/-fplugin=[^ ]*//g' \
  -e 's/-grecord-gcc-switches//g' \
  -e 's/-fexceptions//g' \
  -e 's/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=[0-9]*//g' \
  -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//g' \
  -e 's/-pipe//g' \
  -e 's/-fstack-protector-strong//g' \
  -e 's/-fasynchronous-unwind-tables//g' \
  -e 's/-fstack-clash-protection//g' \
  -e 's/-fcf-protection\(=[^ ]*\)\{0,1\}//g' \
  -e 's/-mtls-dialect=[^ ]*//g' \
  -e 's/-mno-omit-leaf-frame-pointer//g' \
  -e 's/-mbranch-protection=[^ ]*//g' \
  -e 's/-mbackchain//g' \
  -e 's/-mfpmath=[^ ]*//g' \
  -e 's/-mstackrealign//g' \
  -e 's/-msse2//g' \
  -e 's/-I[^ ]*gfortran\/modules//g')
FCFLAGS="$FFLAGS"
LDFLAGS=$(printf '%s\n' "$LDFLAGS" | sed \
  -e 's/--config=[^ ]*oreon-hardened-clang-ld.cfg//g')
export FFLAGS FCFLAGS LDFLAGS FC=flang F77=flang
python3 -m build --wheel --no-isolation \
  -Csetup-args=-Dblas=openblas \
  -Csetup-args=-Dlapack=openblas \
  -Csetup-args=-Dallow-noblas=false

%install
python3 -m installer --destdir %{buildroot} dist/*.whl
%oreon_filelist

%check
FFLAGS=$(printf '%s\n' "$FFLAGS" | sed \
  -e 's/-fplugin=[^ ]*//g' \
  -e 's/-grecord-gcc-switches//g' \
  -e 's/-fexceptions//g' \
  -e 's/-Wp,-U_FORTIFY_SOURCE,-D_FORTIFY_SOURCE=[0-9]*//g' \
  -e 's/-Wp,-D_GLIBCXX_ASSERTIONS//g' \
  -e 's/-pipe//g' \
  -e 's/-fstack-protector-strong//g' \
  -e 's/-fasynchronous-unwind-tables//g' \
  -e 's/-fstack-clash-protection//g' \
  -e 's/-fcf-protection\(=[^ ]*\)\{0,1\}//g' \
  -e 's/-mtls-dialect=[^ ]*//g' \
  -e 's/-mno-omit-leaf-frame-pointer//g' \
  -e 's/-mbranch-protection=[^ ]*//g' \
  -e 's/-mbackchain//g' \
  -e 's/-mfpmath=[^ ]*//g' \
  -e 's/-mstackrealign//g' \
  -e 's/-msse2//g' \
  -e 's/-I[^ ]*gfortran\/modules//g')
FCFLAGS="$FFLAGS"
LDFLAGS=$(printf '%s\n' "$LDFLAGS" | sed \
  -e 's/--config=[^ ]*oreon-hardened-clang-ld.cfg//g')
export FFLAGS FCFLAGS LDFLAGS FC=flang F77=flang
PYTHONPATH=%{buildroot}%{python3_sitearch} python3 -c 'import numpy as np; a = np.eye(4); assert np.allclose(np.linalg.inv(a), a)'
PYTHONPATH=%{buildroot}%{python3_sitearch} python3 -m pytest -q --pyargs numpy -m 'not slow' -p no:cacheprovider

%files -f %{_builddir}/%{name}.files

%changelog
%autochangelog
