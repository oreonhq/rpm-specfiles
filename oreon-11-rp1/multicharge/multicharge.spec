%global source0_hash 6b137db34c89ab73f8cc8f2849db1679b2efa1fdec255cd77fca672d7fc8ea5c
Name:           multicharge
Version:        0.5.0
Release:        1%{?dist}
Summary:        Electronegativity equilibration model for atomic partial charges
License:        Apache-2.0
URL:            https://github.com/grimme-lab/multicharge
Source0:        https://github.com/grimme-lab/multicharge/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  flexiblas-devel
BuildRequires:  gcc-gfortran
BuildRequires:  mctc-lib-devel
BuildRequires:  meson
BuildRequires:  mstore-devel
BuildRequires:  rubygem-asciidoctor
# /oreon:deps
%description
Electronegativity equilibration model for atomic partial charges.

%package devel
Summary:        Development headers for multicharge
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package contains the development headers for multicharge

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%ifarch %{ix86}
%meson -Dlapack=custom -Dcustom_libraries=flexiblas -Dilp64=false
%else
%meson -Dlapack=custom -Dcustom_libraries=flexiblas64 -Dilp64=true
%endif
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_libdir}/gfortran/modules
mv %{buildroot}%{_includedir}/multicharge/gcc-*/*.mod %{buildroot}%{_libdir}/gfortran/modules
\rm %{buildroot}%{_libdir}/libmulticharge.a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n multicharge-devel -f %{oreon_filedir}/multicharge-devel.list

%changelog

%autochangelog
