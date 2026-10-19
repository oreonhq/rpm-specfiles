%global source0_hash f05391a505666bdf2b5d2626f41b7f0f49052b1e33cceac960eaa818008141da
%bcond check 0
%global debug_package %{nil}
%global crate ed25519-compact
Name:           rust-ed25519-compact
Version:        2.4.2
Release:        1%{?dist}
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
License:        MIT
URL:            https://crates.io/crates/ed25519-compact
Source0:        https://static.crates.io/crates/ed25519-compact/ed25519-compact-%{version}.crate
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
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+blind-keys-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+blind-keys-devel

This package contains library source intended for building other packages which
use the "blind-keys" feature of the "%{crate}" crate.

%package     -n %{name}+ct-codecs-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+ct-codecs-devel

This package contains library source intended for building other packages which
use the "ct-codecs" feature of the "%{crate}" crate.

%package     -n %{name}+disable-signatures-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+disable-signatures-devel

This package contains library source intended for building other packages which
use the "disable-signatures" feature of the "%{crate}" crate.

%package     -n %{name}+ed25519-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+ed25519-devel

This package contains library source intended for building other packages which
use the "ed25519" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+opt_size-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+opt_size-devel

This package contains library source intended for building other packages which
use the "opt_size" feature of the "%{crate}" crate.

%package     -n %{name}+pem-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+pem-devel

This package contains library source intended for building other packages which
use the "pem" feature of the "%{crate}" crate.

%package     -n %{name}+random-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+random-devel

This package contains library source intended for building other packages which
use the "random" feature of the "%{crate}" crate.

%package     -n %{name}+self-verify-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+self-verify-devel

This package contains library source intended for building other packages which
use the "self-verify" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+traits-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+traits-devel

This package contains library source intended for building other packages which
use the "traits" feature of the "%{crate}" crate.

%package     -n %{name}+x25519-devel
Summary:        A small, self-contained, wasm-friendly Ed25519 implementation
BuildArch:      noarch
%description -n %{name}+x25519-devel

This package contains library source intended for building other packages which
use the "x25519" feature of the "%{crate}" crate.

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
%files -n rust-ed25519-compact-devel -f %{oreon_filedir}/rust-ed25519-compact-devel.list

%changelog

%autochangelog
