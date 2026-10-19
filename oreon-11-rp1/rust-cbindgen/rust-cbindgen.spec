%global source0_hash 2ecb53484c9c167ba674026b656d8a27d7657a58e6066aa902bfb1a4aa00ae20
%bcond check 1
%global crate cbindgen
Name:           rust-cbindgen
Version:        0.29.4
Release:        1%{?dist}
Summary:        Tool for generating C bindings to Rust code
License:        MPL-2.0
URL:            https://crates.io/crates/cbindgen
Source0:        https://static.crates.io/crates/cbindgen/cbindgen-%{version}.crate
Patch:          cbindgen-fix-metadata.diff
%if %{with check}
%endif
# oreon:deps
BuildRequires:  /usr/bin/cython
BuildRequires:  /usr/bin/g++
BuildRequires:  /usr/bin/gcc
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package     -n %{crate}
Summary:        Tool for generating C bindings to Rust code
License:        %{shrink:
    MPL-2.0
    AND MIT
    AND Unicode-3.0
    AND (Apache-2.0 OR MIT)
    AND (Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT)
    AND (Unlicense OR MIT)
} 
%description -n %{crate}

Provides:       cbindgen = %{version}-%{release}

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Tool for generating C bindings to Rust code
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+clap-devel
Summary:        Tool for generating C bindings to Rust code
BuildArch:      noarch
%description -n %{name}+clap-devel

This package contains library source intended for building other packages which
use the "clap" feature of the "%{crate}" crate.

%package     -n %{name}+unstable_ir-devel
Summary:        Tool for generating C bindings to Rust code
BuildArch:      noarch
%description -n %{name}+unstable_ir-devel

This package contains library source intended for building other packages which
use the "unstable_ir" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%cargo_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n cbindgen -f %{oreon_filedir}/cbindgen.list
%files -n rust-cbindgen-devel -f %{oreon_filedir}/rust-cbindgen-devel.list

%changelog

%autochangelog
