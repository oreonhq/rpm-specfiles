%global source0_hash 56b3d778629eb74b8a515cd53c727d04609f858a07f8d3555fd5fd392a206dcc
Name:           mstore
Version:        0.3.0
Release:        1%{?dist}
Summary:        Molecular structure store for testing
License:        Apache-2.0
URL:            https://github.com/grimme-lab/mstore
Source0:        https://github.com/grimme-lab/mstore/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel
BuildRequires:  meson
# /oreon:deps
%description
Molecular structure store for testing

%package devel
Summary:       Development headers for mstore
Requires:      %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development headers for mstore.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/mstore/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
\rm %{buildroot}%{_libdir}/libmstore.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n mstore-devel -f %{oreon_filedir}/mstore-devel.list

%changelog

%autochangelog
