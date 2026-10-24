%global source0_hash bc9842a18898bfacb0ed1252c4febcc7e78fa139fd27fdc7a3e30d9d9356119b
%global oreon_bootstrap %{nil}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: libffi
Version: 3.4.8
Release: 1%{?dist}
Summary: Portable foreign function interface library
License: MIT
URL: https://sourceware.org/libffi/
Source0: https://github.com/libffi/libffi/releases/download/v%{version}/libffi-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
%if %{without bootstrap} && !0%{?bootstrap}
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make
%endif

%description
libffi is a portable foreign function interface library.

%package devel
Summary: Portable foreign function interface library
Requires: libffi%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libffi)

%description devel
libffi is a portable foreign function interface library.

%prep
%oreon_sha256
%autosetup -p1

%build
%oreon_configure --disable-static --disable-docs
%oreon_make

%install
%oreon_make_install
rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_infodir}

%files
%license LICENSE
%{_libdir}/libffi.so.8
%{_libdir}/libffi.so.8.*

%files devel
%{_includedir}/*.h
%{_libdir}/libffi.so
%{_libdir}/pkgconfig/libffi.pc
%{_mandir}/man3/ffi.3*
%{_mandir}/man3/ffi_call.3*
%{_mandir}/man3/ffi_prep_cif.3*
%{_mandir}/man3/ffi_prep_cif_var.3*
