%global source0_hash e7e8131a03190127fb2263afc72b322ecadae46b6ff8c6f399ff5d02f5559af6
%bcond check 0
%global debug_package %{nil}
%global crate x25519-dalek
Name:           rust-x25519-dalek
Version:        3.0.0
Release:        1%{?dist}
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
License:        BSD-3-Clause
URL:            https://crates.io/crates/x25519-dalek
Source0:        https://static.crates.io/crates/x25519-dalek/x25519-dalek-%{version}.crate
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
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+precomputed-tables-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+precomputed-tables-devel

This package contains library source intended for building other packages which
use the "precomputed-tables" feature of the "%{crate}" crate.

%package     -n %{name}+reusable_secrets-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+reusable_secrets-devel

This package contains library source intended for building other packages which
use the "reusable_secrets" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+static_secrets-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
BuildArch:      noarch
%description -n %{name}+static_secrets-devel

This package contains library source intended for building other packages which
use the "static_secrets" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        X25519 elliptic curve Diffie-Hellman key exchange in pure-Rust, using...
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
%files -n rust-x25519-dalek-devel -f %{oreon_filedir}/rust-x25519-dalek-devel.list

%changelog

%autochangelog
