%global source0_hash f904df226785644ce174f65c7235d0d5a7ead5861880f7b174dd92566522a14c
Name:           dftd4
Version:        4.3.0
Release:        1%{?dist}
Summary:        Generally Applicable Atomic-Charge Dependent London Dispersion Correction
License:        LGPL-3.0-or-later
URL:            https://dftd4.readthedocs.io/
Source0:        https://github.com/dftd4/dftd4/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel
BuildRequires:  meson
BuildRequires:  mstore-devel
BuildRequires:  multicharge-devel
BuildRequires:  python3-cffi
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
Generally Applicable Atomic-Charge Dependent London Dispersion Correction.

%package devel
Summary:        Development headers for dftd4
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development headers for dftd4

%package -n python3-dftd4
Summary:        Python 3 interface for dftd4
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n python3-dftd4
This package contains the Python 3 interface for dftd4.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%ifarch %{ix86}
%meson -Dlapack=custom -Dcustom_libraries=flexiblas -Dilp64=false -Dpython=true
%else
%meson -Dlapack=custom -Dcustom_libraries=flexiblas64 -Dilp64=true -Dpython=true
%endif
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/dftd4/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
\rm %{buildroot}%{_libdir}/libdftd4.a
%oreon_autofiles python3-dftd4 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

MESON_TESTTHREADS=2 %meson_test --timeout-multiplier 4
%files -f %{oreon_filedir}/main.list
%files -n dftd4-devel -f %{oreon_filedir}/dftd4-devel.list
%files -n python3-dftd4 -f %{oreon_filedir}/python3-dftd4.list

%changelog

%autochangelog
