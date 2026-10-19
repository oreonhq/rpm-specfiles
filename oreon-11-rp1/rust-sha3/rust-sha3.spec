%global source0_hash 77fd7028345d415a4034cf8777cd4f8ab1851274233b45f84e3d955502d93874
%bcond check 0
%global debug_package %{nil}
%global crate sha3
Name:           rust-sha3
Version:        0.10.9
Release:        1%{?dist}
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha3
Source0:        https://static.crates.io/crates/sha3/sha3-%{version}.crate
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
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+reset-devel
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
BuildArch:      noarch
%description -n %{name}+reset-devel

This package contains library source intended for building other packages which
use the "reset" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of SHA-3, a family of Keccak-based hash func...
BuildArch:      noarch
%description -n %{name}+zeroize-devel

This package contains library source intended for building other packages which
use the "zeroize" feature of the "%{crate}" crate.

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
%files -n rust-sha3-devel -f %{oreon_filedir}/rust-sha3-devel.list

%changelog

%autochangelog
