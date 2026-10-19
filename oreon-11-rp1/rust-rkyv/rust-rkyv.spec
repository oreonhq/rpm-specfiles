%global source0_hash 2297bf9c81a3f0dc96bc9521370b88f054168c29826a75e89c55ff196e7ed6a1
%bcond check 0
%global debug_package %{nil}
%global crate rkyv
Name:           rust-rkyv
Version:        0.7.46
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

%package     -n %{name}+alloc-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arbitrary_enum_discriminant-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+arbitrary_enum_discriminant-devel

This package contains library source intended for building other packages which
use the "arbitrary_enum_discriminant" feature of the "%{crate}" crate.

%package     -n %{name}+archive_be-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+archive_be-devel

This package contains library source intended for building other packages which
use the "archive_be" feature of the "%{crate}" crate.

%package     -n %{name}+archive_le-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+archive_le-devel

This package contains library source intended for building other packages which
use the "archive_le" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+bitvec-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+bitvec-devel

This package contains library source intended for building other packages which
use the "bitvec" feature of the "%{crate}" crate.

%package     -n %{name}+bytecheck-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+bytecheck-devel

This package contains library source intended for building other packages which
use the "bytecheck" feature of the "%{crate}" crate.

%package     -n %{name}+bytes-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+copy-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+copy-devel

This package contains library source intended for building other packages which
use the "copy" feature of the "%{crate}" crate.

%package     -n %{name}+copy_unsafe-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+copy_unsafe-devel

This package contains library source intended for building other packages which
use the "copy_unsafe" feature of the "%{crate}" crate.

%package     -n %{name}+hashbrown-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+hashbrown-devel

This package contains library source intended for building other packages which
use the "hashbrown" feature of the "%{crate}" crate.

%package     -n %{name}+indexmap-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+indexmap-devel

This package contains library source intended for building other packages which
use the "indexmap" feature of the "%{crate}" crate.

%package     -n %{name}+rend-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+rend-devel

This package contains library source intended for building other packages which
use the "rend" feature of the "%{crate}" crate.

%package     -n %{name}+size_16-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+size_16-devel

This package contains library source intended for building other packages which
use the "size_16" feature of the "%{crate}" crate.

%package     -n %{name}+size_32-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+size_32-devel

This package contains library source intended for building other packages which
use the "size_32" feature of the "%{crate}" crate.

%package     -n %{name}+size_64-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+size_64-devel

This package contains library source intended for building other packages which
use the "size_64" feature of the "%{crate}" crate.

%package     -n %{name}+smallvec-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+smallvec-devel

This package contains library source intended for building other packages which
use the "smallvec" feature of the "%{crate}" crate.

%package     -n %{name}+smol_str-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+smol_str-devel

This package contains library source intended for building other packages which
use the "smol_str" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+strict-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+strict-devel

This package contains library source intended for building other packages which
use the "strict" feature of the "%{crate}" crate.

%package     -n %{name}+tinyvec-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+tinyvec-devel

This package contains library source intended for building other packages which
use the "tinyvec" feature of the "%{crate}" crate.

%package     -n %{name}+uuid-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+uuid-devel

This package contains library source intended for building other packages which
use the "uuid" feature of the "%{crate}" crate.

%package     -n %{name}+validation-devel
Summary:        Zero-copy deserialization framework for Rust
BuildArch:      noarch
%description -n %{name}+validation-devel

This package contains library source intended for building other packages which
use the "validation" feature of the "%{crate}" crate.

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
%files -n rust-rkyv-devel -f %{oreon_filedir}/rust-rkyv-devel.list

%changelog

%autochangelog
