%global source0_hash 6ebaa1a2bf1290ab3bfe5a7b771d050ebffab2711c19a81691c683a5144a25de
%bcond check 0
%global debug_package %{nil}
%global crate ed25519-dalek
Name:           rust-ed25519-dalek
Version:        3.0.0
Release:        1%{?dist}
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
License:        BSD-3-Clause
URL:            https://crates.io/crates/ed25519-dalek
Source0:        https://static.crates.io/crates/ed25519-dalek/ed25519-dalek-%{version}.crate
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
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+batch-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+batch-devel

This package contains library source intended for building other packages which
use the "batch" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+fast-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+fast-devel

This package contains library source intended for building other packages which
use the "fast" feature of the "%{crate}" crate.

%package     -n %{name}+hazmat-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+legacy_compatibility-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+legacy_compatibility-devel

This package contains library source intended for building other packages which
use the "legacy_compatibility" feature of the "%{crate}" crate.

%package     -n %{name}+merlin-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+merlin-devel

This package contains library source intended for building other packages which
use the "merlin" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+signature-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+signature-devel

This package contains library source intended for building other packages which
use the "signature" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Fast and efficient ed25519 EdDSA key generations, signing, and verifi...
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
%files -n rust-ed25519-dalek-devel -f %{oreon_filedir}/rust-ed25519-dalek-devel.list

%changelog

%autochangelog
