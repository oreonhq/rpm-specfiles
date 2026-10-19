%global source0_hash 35f0f96ce78e38c3dc6d8948aa8163d06385be74000f3c7a95bf1eef35d3ea32
%bcond check 0
%global debug_package %{nil}
%global crate aes
Name:           rust-aes0.9
Version:        0.9.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of the Advanced Encryption Standard (a.k.a....
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/aes
Source0:        https://static.crates.io/crates/aes/aes-%{version}.crate
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

%package     -n %{name}+hazmat-devel
Summary:        Pure Rust implementation of the Advanced Encryption Standard (a.k.a....
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of the Advanced Encryption Standard (a.k.a....
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
%files -n rust-aes0.9-devel -f %{oreon_filedir}/rust-aes0.9-devel.list

%changelog

%autochangelog
