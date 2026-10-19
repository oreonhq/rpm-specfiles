%global source0_hash 5a49302d1b1c51dd61f0ae7bc3f3700ab812250866716013eb1b0921ba089476
%bcond check 1
%global debug_package %{nil}
%global crate libblkid-rs-sys
Name:           rust-libblkid-rs-sys
Version:        0.3.3
Release:        1%{?dist}
Summary:        Low level bindings for libblkid
License:        MPL-2.0
URL:            https://crates.io/crates/libblkid-rs-sys
Source0:        https://static.crates.io/crates/libblkid-rs-sys/libblkid-rs-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(blkid)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(blkid)
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Low level bindings for libblkid
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+static-devel
Summary:        Low level bindings for libblkid
BuildArch:      noarch
%description -n %{name}+static-devel

This package contains library source intended for building other packages which
use the "static" feature of the "%{crate}" crate.

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
%files -n rust-libblkid-rs-sys-devel -f %{oreon_filedir}/rust-libblkid-rs-sys-devel.list

%changelog

%autochangelog
