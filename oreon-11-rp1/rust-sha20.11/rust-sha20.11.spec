%global source0_hash 446ba717509524cb3f22f17ecc096f10f4822d76ab5c0b9822c5f9c284e825f4
%bcond check 0
%global debug_package %{nil}
%global crate sha2
Name:           rust-sha20.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        Pure Rust implementation of the SHA-2 hash function family
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/sha2
Source0:        https://static.crates.io/crates/sha2/sha2-%{version}.crate
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
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+oid-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
BuildArch:      noarch
%description -n %{name}+oid-devel

This package contains library source intended for building other packages which
use the "oid" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of the SHA-2 hash function family
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
%files -n rust-sha20.11-devel -f %{oreon_filedir}/rust-sha20.11-devel.list

%changelog

%autochangelog
