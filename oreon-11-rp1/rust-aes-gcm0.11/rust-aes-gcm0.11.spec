%global source0_hash fdf011db2e21ce0d575593d749db5554b47fed37aff429e4dc50bc91ac93a028
%bcond check 0
%global debug_package %{nil}
%global crate aes-gcm
Name:           rust-aes-gcm0.11
Version:        0.11.0
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

%package     -n %{name}+bytes-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+bytes-devel

This package contains library source intended for building other packages which
use the "bytes" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+hazmat-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+hazmat-devel

This package contains library source intended for building other packages which
use the "hazmat" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Pure Rust implementation of the AES-GCM (Galois/Counter Mode)
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

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
%files -n rust-aes-gcm0.11-devel -f %{oreon_filedir}/rust-aes-gcm0.11-devel.list

%changelog

%autochangelog
