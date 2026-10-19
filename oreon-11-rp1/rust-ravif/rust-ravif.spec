%global source0_hash 5825c26fddd16ab9f515930d49028a630efec172e903483c94796cfe31893e6b
%bcond check 0
%global debug_package %{nil}
%global crate ravif
Name:           rust-ravif
Version:        0.11.20
Release:        1%{?dist}
Summary:        rav1e-based pure Rust library for encoding images in AVIF format (pow...
License:        BSD-3-Clause
URL:            https://crates.io/crates/ravif
Source0:        https://static.crates.io/crates/ravif/ravif-%{version}.crate
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
Summary:        rav1e-based pure Rust library for encoding images in AVIF format (pow...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+asm-devel
Summary:        rav1e-based pure Rust library for encoding images in AVIF format (pow...
BuildArch:      noarch
%description -n %{name}+asm-devel

This package contains library source intended for building other packages which
use the "asm" feature of the "%{crate}" crate.

%package     -n %{name}+rayon-devel
Summary:        rav1e-based pure Rust library for encoding images in AVIF format (pow...
BuildArch:      noarch
%description -n %{name}+rayon-devel

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%package     -n %{name}+threading-devel
Summary:        rav1e-based pure Rust library for encoding images in AVIF format (pow...
BuildArch:      noarch
%description -n %{name}+threading-devel

This package contains library source intended for building other packages which
use the "threading" feature of the "%{crate}" crate.

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
%files -n rust-ravif-devel -f %{oreon_filedir}/rust-ravif-devel.list

%changelog

%autochangelog
