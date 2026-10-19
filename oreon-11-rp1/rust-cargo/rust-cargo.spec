%global source0_hash 0c30a0d29369c04a80056b22089ad95f28c3df596821f1f8672d44ef64b7e26a
%bcond check 0
%global debug_package %{nil}
%global rustflags_debuginfo 0
%global cargo_install_bin 0
%global crate cargo
Name:           rust-cargo
Version:        0.99.0
Release:        1%{?dist}
Summary:        Package manager for Rust
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/cargo
Source0:        https://static.crates.io/crates/cargo/cargo-%{version}.crate
Patch:          cargo-fix-metadata-auto.diff
Patch:          cargo-fix-metadata.diff
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
Summary:        Package manager for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+http-transport-curl-devel
Summary:        Package manager for Rust
BuildArch:      noarch
%description -n %{name}+http-transport-curl-devel

This package contains library source intended for building other packages which
use the "http-transport-curl" feature of the "%{crate}" crate.

%package     -n %{name}+http-transport-reqwest-devel
Summary:        Package manager for Rust
BuildArch:      noarch
%description -n %{name}+http-transport-reqwest-devel

This package contains library source intended for building other packages which
use the "http-transport-reqwest" feature of the "%{crate}" crate.

%package     -n %{name}+openssl-devel
Summary:        Package manager for Rust
BuildArch:      noarch
%description -n %{name}+openssl-devel

This package contains library source intended for building other packages which
use the "openssl" feature of the "%{crate}" crate.

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
%files -n rust-cargo-devel -f %{oreon_filedir}/rust-cargo-devel.list

%changelog

%autochangelog
