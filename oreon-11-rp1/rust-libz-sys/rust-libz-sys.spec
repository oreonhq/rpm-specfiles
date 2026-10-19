%global source0_hash 85bc9657773828b90eeb625adff10eeac83cc21bbfd8e23a03eaa8a33c9e28d9
%bcond check 1
%global debug_package %{nil}
%global crate libz-sys
Name:           rust-libz-sys
Version:        1.1.29
Release:        1%{?dist}
Summary:        Low-level bindings to the system libz library (also known as zlib)
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/libz-sys
Source0:        https://static.crates.io/crates/libz-sys/libz-sys-%{version}.crate
Source10:       build.rs
Patch:          libz-sys-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(zlib)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(zlib)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Low-level bindings to the system libz library (also known as zlib)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Low-level bindings to the system libz library (also known as zlib)
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+stock-zlib-devel
Summary:        Low-level bindings to the system libz library (also known as zlib)
BuildArch:      noarch
%description -n %{name}+stock-zlib-devel

This package contains library source intended for building other packages which
use the "stock-zlib" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
rm -r src/zlib/
rm -r src/zlib-ng/
cp -p '%{SOURCE10}' .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-libz-sys-devel -f %{oreon_filedir}/rust-libz-sys-devel.list

%changelog

%autochangelog
