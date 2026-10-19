%global source0_hash 2c9d3793400a45f954c52e73d068316d76b6f4e36977e3fcebb13a2721e80237
%bcond check 0
%global debug_package %{nil}
%global crate tiny-keccak
Name:           rust-tiny-keccak
Version:        2.0.2
Release:        1%{?dist}
Summary:        An implementation of Keccak derived functions.
License:        CC0-1.0
URL:            https://crates.io/crates/tiny-keccak
Source0:        https://static.crates.io/crates/tiny-keccak/tiny-keccak-%{version}.crate
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
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+cshake-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+cshake-devel

This package contains library source intended for building other packages which
use the "cshake" feature of the "%{crate}" crate.

%package     -n %{name}+fips202-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+fips202-devel

This package contains library source intended for building other packages which
use the "fips202" feature of the "%{crate}" crate.

%package     -n %{name}+k12-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+k12-devel

This package contains library source intended for building other packages which
use the "k12" feature of the "%{crate}" crate.

%package     -n %{name}+keccak-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+keccak-devel

This package contains library source intended for building other packages which
use the "keccak" feature of the "%{crate}" crate.

%package     -n %{name}+kmac-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+kmac-devel

This package contains library source intended for building other packages which
use the "kmac" feature of the "%{crate}" crate.

%package     -n %{name}+parallel_hash-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+parallel_hash-devel

This package contains library source intended for building other packages which
use the "parallel_hash" feature of the "%{crate}" crate.

%package     -n %{name}+sha3-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+sha3-devel

This package contains library source intended for building other packages which
use the "sha3" feature of the "%{crate}" crate.

%package     -n %{name}+shake-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+shake-devel

This package contains library source intended for building other packages which
use the "shake" feature of the "%{crate}" crate.

%package     -n %{name}+sp800-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+sp800-devel

This package contains library source intended for building other packages which
use the "sp800" feature of the "%{crate}" crate.

%package     -n %{name}+tuple_hash-devel
Summary:        An implementation of Keccak derived functions.
BuildArch:      noarch
%description -n %{name}+tuple_hash-devel

This package contains library source intended for building other packages which
use the "tuple_hash" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f cshake,fips202,k12,keccak,kmac,parallel_hash,sha3,shake,sp800,tuple_hash
%install
%cargo_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f cshake,fips202,k12,keccak,kmac,parallel_hash,sha3,shake,sp800,tuple_hash
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-tiny-keccak-devel -f %{oreon_filedir}/rust-tiny-keccak-devel.list

%changelog

%autochangelog
