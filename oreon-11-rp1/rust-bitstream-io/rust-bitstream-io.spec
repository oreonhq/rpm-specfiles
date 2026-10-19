%global source0_hash 7eff00be299a18769011411c9def0d827e8f2d7bf0c3dbf53633147a8867fd1f
%bcond check 0
%global debug_package %{nil}
%global crate bitstream-io
Name:           rust-bitstream-io
Version:        4.10.0
Release:        1%{?dist}
Summary:        Library for reading/writing un-aligned values from/to streams in big-...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bitstream-io
Source0:        https://static.crates.io/crates/bitstream-io/bitstream-io-%{version}.crate
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
Summary:        Library for reading/writing un-aligned values from/to streams in big-...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Library for reading/writing un-aligned values from/to streams in big-...
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Library for reading/writing un-aligned values from/to streams in big-...
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
%files -n rust-bitstream-io-devel -f %{oreon_filedir}/rust-bitstream-io-devel.list

%changelog

%autochangelog
