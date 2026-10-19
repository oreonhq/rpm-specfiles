%global source0_hash b5eed333089e2e1c1ac8c6c0398e5e2497b4c9926ca6d0365ed1e099afa5bc23
%bcond check 0
%global debug_package %{nil}
%global crate curve25519-dalek
Name:           rust-curve25519-dalek
Version:        5.0.0
Release:        1%{?dist}
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
License:        BSD-3-Clause
URL:            https://crates.io/crates/curve25519-dalek
Source0:        https://static.crates.io/crates/curve25519-dalek/curve25519-dalek-%{version}.crate
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
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+digest-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+digest-devel

This package contains library source intended for building other packages which
use the "digest" feature of the "%{crate}" crate.

%package     -n %{name}+ff-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+ff-devel

This package contains library source intended for building other packages which
use the "ff" feature of the "%{crate}" crate.

%package     -n %{name}+group-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+group-devel

This package contains library source intended for building other packages which
use the "group" feature of the "%{crate}" crate.

%package     -n %{name}+group-bits-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+group-bits-devel

This package contains library source intended for building other packages which
use the "group-bits" feature of the "%{crate}" crate.

%package     -n %{name}+legacy_compatibility-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+legacy_compatibility-devel

This package contains library source intended for building other packages which
use the "legacy_compatibility" feature of the "%{crate}" crate.

%package     -n %{name}+precomputed-tables-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+precomputed-tables-devel

This package contains library source intended for building other packages which
use the "precomputed-tables" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        A pure-Rust implementation of group operations on ristretto255 and Cu...
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
%files -n rust-curve25519-dalek-devel -f %{oreon_filedir}/rust-curve25519-dalek-devel.list

%changelog

%autochangelog
