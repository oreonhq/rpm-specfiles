%global source11_hash 378f5840b258e2779c39418f3f2d7b2ba96f1c7917dd6be0713f88305dbda397
%global source10_hash a60eea817514531668d7e00765731449fe14d059d3249e0bc93b36de45f759f2
%global source0_hash db0fd3421ec63f68efc971ed1242ca54f4a1750aedd68909ed3ac0ecc3274fe8
%bcond check 1
%global crate rustc-demangle-capi
Name:           rust-rustc-demangle-capi
%global so_version 0.1
Version:        0.1.0
Release:        1%{?dist}
Summary:        C API for the rustc-demangle crate
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rustc-demangle-capi
Source0:        https://static.crates.io/crates/rustc-demangle-capi/rustc-demangle-capi-%{version}.crate
Source10:       https://github.com/rust-lang/rustc-demangle/raw/refs/tags/0.1.24/LICENSE-APACHE
Source11:       https://github.com/rust-lang/rustc-demangle/raw/refs/tags/0.1.24/LICENSE-MIT
Patch:          rustc-demangle-capi-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-c
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n librustc_demangle
Summary:        C API for the rustc-demangle crate
License:        MIT OR Apache-2.0
%description -n librustc_demangle

This package contains the shared library providing the C API for
rustc-demangle.

%package     -n librustc_demangle-devel
Summary:        C API for the rustc-demangle crate
Requires:       librustc_demangle%{?_isa} = %{version}-%{release}
%description -n librustc_demangle-devel

This package contains headers and other files needed to develop and build
programs that use the C API for rustc-demangle.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p '%{SOURCE10}' '%{SOURCE11}' .
%oreon_vendor_cargo
%build

%cargo_build -a
%{cargo_license_summary -a}
%{cargo_license -a} > LICENSE.dependencies
%cargo_cbuild -a
%install
%cargo_cinstall -a
rm '%{buildroot}%{_libdir}/librustc_demangle.a'
%oreon_autofiles librustc_demangle usr/*/lib*.so.*
%oreon_autofiles librustc_demangle-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n librustc_demangle -f %{oreon_filedir}/librustc_demangle.list
%files -n librustc_demangle-devel -f %{oreon_filedir}/librustc_demangle-devel.list

%changelog

%autochangelog
