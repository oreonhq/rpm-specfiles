%global source2_hash 3f3d9e0024b1921b067d6f7f88deb4a60cbe7a78e76c64e3f1d7fc3b779b9d04
%global source0_hash d2c67889c5743b5987961460fbc999dbfa1bb4c7a8e5bfe37eb4d5e678ccb6d1
%bcond check 0
%global debug_package %{nil}
%global crate cryptographic-message-syntax
Name:           rust-cryptographic-message-syntax
Version:        0.28.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of Crypographic Message Syntax (RFC 5652)
License:        MPL-2.0
URL:            https://crates.io/crates/cryptographic-message-syntax
Source0:        https://static.crates.io/crates/cryptographic-message-syntax/cryptographic-message-syntax-%{version}.crate
Source2:        https://github.com/indygreg/cryptography-rs/raw/cfaafe05892ce5c617dcac593a9224613bf88a0e/LICENSE
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
Summary:        Pure Rust implementation of Crypographic Message Syntax (RFC 5652)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -p %SOURCE2 .
%oreon_vendor_cargo
%build

%cargo_build
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -- -- --skip time_stamp_protocol::test::simple_request --skip signing::tests::time_stamp_url
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-cryptographic-message-syntax-devel -f %{oreon_filedir}/rust-cryptographic-message-syntax-devel.list

%changelog

%autochangelog
