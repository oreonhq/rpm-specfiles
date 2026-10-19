%global source0_hash 2b4a54dfedecb1dc004776a597db0c858cf6c31579296734511309291b8399ce
%bcond check 1
%global debug_package %{nil}
%global crate endian-num
Name:           rust-endian-num
Version:        0.2.0
Release:        1%{?dist}
Summary:        Byte-order-aware numeric types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/endian-num
Source0:        https://static.crates.io/crates/endian-num/endian-num-%{version}.crate
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
Summary:        Byte-order-aware numeric types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+bitflags-devel
Summary:        Byte-order-aware numeric types
BuildArch:      noarch
%description -n %{name}+bitflags-devel

This package contains library source intended for building other packages which
use the "bitflags" feature of the "%{crate}" crate.

%package     -n %{name}+bytemuck-devel
Summary:        Byte-order-aware numeric types
BuildArch:      noarch
%description -n %{name}+bytemuck-devel

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%package     -n %{name}+linux-types-devel
Summary:        Byte-order-aware numeric types
BuildArch:      noarch
%description -n %{name}+linux-types-devel

This package contains library source intended for building other packages which
use the "linux-types" feature of the "%{crate}" crate.

%package     -n %{name}+zerocopy-devel
Summary:        Byte-order-aware numeric types
BuildArch:      noarch
%description -n %{name}+zerocopy-devel

This package contains library source intended for building other packages which
use the "zerocopy" feature of the "%{crate}" crate.

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
%files -n rust-endian-num-devel -f %{oreon_filedir}/rust-endian-num-devel.list

%changelog

%autochangelog
