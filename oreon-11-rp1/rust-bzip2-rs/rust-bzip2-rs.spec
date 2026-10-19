%global source0_hash beeb59e7e4c811ab37cc73680c798c7a5da77fc9989c62b09138e31ee740f735
%bcond check 0
%global debug_package %{nil}
%global crate bzip2-rs
Name:           rust-bzip2-rs
Version:        0.1.2
Release:        1%{?dist}
Summary:        Pure Rust bzip2 decompressor
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bzip2-rs
Source0:        https://static.crates.io/crates/bzip2-rs/bzip2-rs-%{version}.crate
Patch:          bzip2-rs-fix-metadata.diff
Patch:          0002-Drop-pretty_assertions-removed-upstream.patch
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Pure Rust bzip2 decompressor
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_37-devel
Summary:        Pure Rust bzip2 decompressor
BuildArch:      noarch
%description -n %{name}+rustc_1_37-devel

This package contains library source intended for building other packages which
use the "rustc_1_37" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_40-devel
Summary:        Pure Rust bzip2 decompressor
BuildArch:      noarch
%description -n %{name}+rustc_1_40-devel

This package contains library source intended for building other packages which
use the "rustc_1_40" feature of the "%{crate}" crate.

%package     -n %{name}+rustc_1_51-devel
Summary:        Pure Rust bzip2 decompressor
BuildArch:      noarch
%description -n %{name}+rustc_1_51-devel

This package contains library source intended for building other packages which
use the "rustc_1_51" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
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
%files -n rust-bzip2-rs-devel -f %{oreon_filedir}/rust-bzip2-rs-devel.list

%changelog

%autochangelog
