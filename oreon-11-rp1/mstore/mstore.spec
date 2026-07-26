%global source0_hash 56b3d778629eb74b8a515cd53c727d04609f858a07f8d3555fd5fd392a206dcc

Name:           mstore
Version:        0.3.0
Release:        5%{?dist}
Summary:        Molecular structure store for testing
License:        Apache-2.0
URL:            https://github.com/grimme-lab/mstore
Source0:        https://github.com/grimme-lab/mstore/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel

%description
Molecular structure store for testing

%package devel
Summary:       Development headers for mstore
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers for mstore.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install
# Move Fortran modules to the right place
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/mstore/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
# Remove static library
\rm %{buildroot}%{_libdir}/libmstore.a

%check
%meson_test

%files
%license LICENSE
%doc README.md
%{_libdir}/libmstore.so.*
%{_bindir}/mstore-info

%files devel
%{_libdir}/libmstore.so
%{_libdir}/gfortran/modules/mstore*.mod
%{_libdir}/pkgconfig/mstore.pc

%changelog
%autochangelog
