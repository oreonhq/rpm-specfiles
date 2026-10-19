%global source0_hash d9776093b7ca170454ab1406954f7b7d97a57c51dc6c0642957fb2ef25c2d399
%bcond check 0
%global debug_package %{nil}
%global crate rkyv
Name:           rust-rkyv0.8
Version:        0.8.18
Release:        1%{?dist}
Summary:        Zero-copy deserialization framework for Rust
License:        MIT
URL:            https://crates.io/crates/rkyv
Source0:        https://static.crates.io/crates/rkyv/rkyv-%{version}.crate
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
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aligned-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+aligned-devel

This package contains library source intended for building other packages which
use the "aligned" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-0_7-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+arrayvec-0_7-devel

This package contains library source intended for building other packages which
use the "arrayvec-0_7" feature of the "%{crate}" crate.

%package     -n %{name}+big_endian-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+big_endian-devel

This package contains library source intended for building other packages which
use the "big_endian" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-1-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+bytes-1-devel

This package contains library source intended for building other packages which
use the "bytes-1" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-0_14-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-0_14-devel

This package contains library source intended for building other packages which
use the "hashbrown-0_14" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-0_15-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-0_15-devel

This package contains library source intended for building other packages which
use the "hashbrown-0_15" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-0_16-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-0_16-devel

This package contains library source intended for building other packages which
use the "hashbrown-0_16" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-0_17-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-0_17-devel

This package contains library source intended for building other packages which
use the "hashbrown-0_17" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-2-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+indexmap-2-devel

This package contains library source intended for building other packages which
use the "indexmap-2" feature of the "%{crate}" crate.

%package     -n %{name}+little_endian-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+little_endian-devel

This package contains library source intended for building other packages which
use the "little_endian" feature of the "%{crate}" crate.

%package     -n %{name}+pointer_width_16-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+pointer_width_16-devel

This package contains library source intended for building other packages which
use the "pointer_width_16" feature of the "%{crate}" crate.

%package     -n %{name}+pointer_width_32-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+pointer_width_32-devel

This package contains library source intended for building other packages which
use the "pointer_width_32" feature of the "%{crate}" crate.

%package     -n %{name}+pointer_width_64-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+pointer_width_64-devel

This package contains library source intended for building other packages which
use the "pointer_width_64" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-1-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+smallvec-1-devel

This package contains library source intended for building other packages which
use the "smallvec-1" feature of the "%{crate}" crate.

%package     -n %{name}+smol_str-0_2-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+smol_str-0_2-devel

This package contains library source intended for building other packages which
use the "smol_str-0_2" feature of the "%{crate}" crate.

%package     -n %{name}+smol_str-0_3-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+smol_str-0_3-devel

This package contains library source intended for building other packages which
use the "smol_str-0_3" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+thin-vec-0_2-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+thin-vec-0_2-devel

This package contains library source intended for building other packages which
use the "thin-vec-0_2" feature of the "%{crate}" crate.

%package     -n %{name}+tinyvec-1-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+tinyvec-1-devel

This package contains library source intended for building other packages which
use the "tinyvec-1" feature of the "%{crate}" crate.

%package     -n %{name}+triomphe-0_1-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+triomphe-0_1-devel

This package contains library source intended for building other packages which
use the "triomphe-0_1" feature of the "%{crate}" crate.

%package     -n %{name}+unaligned-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+unaligned-devel

This package contains library source intended for building other packages which
use the "unaligned" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-1-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+uuid-1-devel

This package contains library source intended for building other packages which
use the "uuid-1" feature of the "%{crate}" crate.

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
%files -n rust-rkyv0.8-devel -f %{oreon_filedir}/rust-rkyv0.8-devel.list

%changelog

%autochangelog
