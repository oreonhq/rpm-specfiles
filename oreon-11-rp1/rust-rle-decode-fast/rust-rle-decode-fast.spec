%global source0_hash 3582f63211428f83597b51b2ddb88e2a91a9d52d12831f9d08f5e624e8977422
%bcond check 0
%global debug_package %{nil}
%global crate rle-decode-fast
Name:           rust-rle-decode-fast
Version:        1.0.3
Release:        1%{?dist}
Summary:        Deprecated: this is available in stable Rust since 1.53 as Vec::exten...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rle-decode-fast
Source0:        https://static.crates.io/crates/rle-decode-fast/rle-decode-fast-%{version}.crate
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

%package     -n %{name}+bench-devel
Summary:        Deprecated: this is available in stable Rust since 1.53 as Vec::exten...
BuildArch:      noarch
%description -n %{name}+bench-devel

This package contains library source intended for building other packages which
use the "bench" feature of the "%{crate}" crate.

%package     -n %{name}+criterion-devel
Summary:        Deprecated: this is available in stable Rust since 1.53 as Vec::exten...
BuildArch:      noarch
%description -n %{name}+criterion-devel

This package contains library source intended for building other packages which
use the "criterion" feature of the "%{crate}" crate.

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
%files -n rust-rle-decode-fast-devel -f %{oreon_filedir}/rust-rle-decode-fast-devel.list

%changelog

%autochangelog
