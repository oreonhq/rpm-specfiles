%global source0_hash d87af57419b594aa23fa95f09f0e06d80d84ba01c26148c43844cad6ff4485f0
%bcond check 0
%global debug_package %{nil}
%global crate scrypt
Name:           rust-scrypt
Version:        0.12.0
Release:        1%{?dist}
Summary:        Scrypt password-based key derivation function
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/scrypt
Source0:        https://static.crates.io/crates/scrypt/scrypt-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+ctutils-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+ctutils-devel

This package contains library source intended for building other packages which
use the "ctutils" feature of the "%{crate}" crate.

%package     -n %{name}+getrandom-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+getrandom-devel

This package contains library source intended for building other packages which
use the "getrandom" feature of the "%{crate}" crate.

%package     -n %{name}+kdf-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+kdf-devel

This package contains library source intended for building other packages which
use the "kdf" feature of the "%{crate}" crate.

%package     -n %{name}+mcf-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+mcf-devel

This package contains library source intended for building other packages which
use the "mcf" feature of the "%{crate}" crate.

%package     -n %{name}+parallel-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+parallel-devel

This package contains library source intended for building other packages which
use the "parallel" feature of the "%{crate}" crate.

%package     -n %{name}+password-hash-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+password-hash-devel

This package contains library source intended for building other packages which
use the "password-hash" feature of the "%{crate}" crate.

%package     -n %{name}+phc-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+phc-devel

This package contains library source intended for building other packages which
use the "phc" feature of the "%{crate}" crate.

%package     -n %{name}+rand_core-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+rand_core-devel

This package contains library source intended for building other packages which
use the "rand_core" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        Scrypt password-based key derivation function
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

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
%files -n rust-scrypt-devel -f %{oreon_filedir}/rust-scrypt-devel.list

%changelog

%autochangelog
