%global source0_hash 444879275cb4fd84958b1a1d5420d15e6fcf7c235fe47f053c9c2a80aceb6001
%bcond check 0
%global debug_package %{nil}
%global crate prost
Name:           rust-prost0.9
Version:        0.9.0
Release:        1%{?dist}
Summary:        A Protocol Buffers implementation for the Rust Language.
License:        Apache-2.0
URL:            https://crates.io/crates/prost
Source0:        https://static.crates.io/crates/prost/prost-%{version}.crate
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
Summary:        A Protocol Buffers implementation for the Rust Language.
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+no-recursion-limit-devel
Summary:        A Protocol Buffers implementation for the Rust Language.
BuildArch:      noarch
%description -n %{name}+no-recursion-limit-devel

This package contains library source intended for building other packages which
use the "no-recursion-limit" feature of the "%{crate}" crate.

%package     -n %{name}+prost-derive-devel
Summary:        A Protocol Buffers implementation for the Rust Language.
BuildArch:      noarch
%description -n %{name}+prost-derive-devel

This package contains library source intended for building other packages which
use the "prost-derive" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        A Protocol Buffers implementation for the Rust Language.
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-prost0.9-devel -f %{oreon_filedir}/rust-prost0.9-devel.list

%changelog

%autochangelog
