%global source0_hash add6b9d92e496f16f4526d68ff29da1483aba4b119baeab8bed3b9e3544a6f3d
%bcond check 0
%global debug_package %{nil}
%global crate ml-dsa
Name:           rust-ml-dsa
Version:        0.1.1
Release:        1%{?dist}
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/ml-dsa
Source0:        https://static.crates.io/crates/ml-dsa/ml-dsa-%{version}.crate
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
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+const-oid-devel
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
BuildArch:      noarch
%description -n %{name}+const-oid-devel

This package contains library source intended for building other packages which
use the "const-oid" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+pkcs8-devel
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
BuildArch:      noarch
%description -n %{name}+pkcs8-devel

This package contains library source intended for building other packages which
use the "pkcs8" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Pure Rust implementation of ML-DSA (formerly known as CRYSTALS-Dilith...
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
%files -n rust-ml-dsa-devel -f %{oreon_filedir}/rust-ml-dsa-devel.list

%changelog

%autochangelog
