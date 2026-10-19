%global source0_hash ef975e30683b2d965054bb0a836f8973857c4ebf6acf274fe46617cd285060d8
%bcond check 1
%global debug_package %{nil}
%global crate fastbloom
Name:           rust-fastbloom
Version:        0.17.0
Release:        1%{?dist}
Summary:        Fastest Bloom filter in Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/fastbloom
Source0:        https://static.crates.io/crates/fastbloom/fastbloom-%{version}.crate
Patch:          fastbloom-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  dos2unix
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
Summary:        Fastest Bloom filter in Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+rand-devel
Summary:        Fastest Bloom filter in Rust
BuildArch:      noarch
%description -n %{name}+rand-devel

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Fastest Bloom filter in Rust
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fastest Bloom filter in Rust
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
dos2unix --keepdate LICENSE-APACHE LICENSE-MIT README.md src/bit_vector.rs src/math.rs
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
%files -n rust-fastbloom-devel -f %{oreon_filedir}/rust-fastbloom-devel.list

%changelog

%autochangelog
