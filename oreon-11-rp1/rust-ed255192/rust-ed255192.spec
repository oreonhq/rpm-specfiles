%global source0_hash 115531babc129696a58c64a4fef0a8bf9e9698629fb97e9e40767d235cfbcd53
%bcond check 0
%global debug_package %{nil}
%global crate ed25519
Name:           rust-ed255192
Version:        2.2.3
Release:        1%{?dist}
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ed25519
Source0:        https://static.crates.io/crates/ed25519/ed25519-%{version}.crate
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
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+serde_bytes-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+serde_bytes-devel

This package contains library source intended for building other packages which
use the "serde_bytes" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Edwards Digital Signature Algorithm (EdDSA) over Curve25519 (as speci...
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
%files -n rust-ed255192-devel -f %{oreon_filedir}/rust-ed255192-devel.list

%changelog

%autochangelog
