%global source0_hash 831010a0f742e1209b3bcea8fab6a8e149051ba6099432c8cb2cc117dec3ead1
%bcond check 0
%global debug_package %{nil}
%global crate aes-gcm
Name:           rust-aes-gcm
Version:        0.10.3
Release:        1%{?dist}
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/aes-gcm
Source0:        https://static.crates.io/crates/aes-gcm/aes-gcm-%{version}.crate
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
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+aes-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+aes-devel

This package contains library source intended for building other packages which
use the "aes" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+arrayvec-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+arrayvec-devel

This package contains library source intended for building other packages which
use the "arrayvec" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+heapless-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+heapless-devel

This package contains library source intended for building other packages which
use the "heapless" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+stream-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+stream-devel

This package contains library source intended for building other packages which
use the "stream" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
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
%files -n rust-aes-gcm-devel -f %{oreon_filedir}/rust-aes-gcm-devel.list

%changelog

%autochangelog
