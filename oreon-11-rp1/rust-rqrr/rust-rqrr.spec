%global source0_hash fbee31f6b3a594eca8afb8bf3359bcd52aa8aa4d90b561d201534558cfadae1b
%bcond check 1
%global debug_package %{nil}
%global crate rqrr
Name:           rust-rqrr
Version:        0.10.0
Release:        1%{?dist}
Summary:        Detect and read QR codes from any image source
License:        (MIT OR Apache-2.0) AND ISC
URL:            https://crates.io/crates/rqrr
Source0:        https://static.crates.io/crates/rqrr/rqrr-%{version}.crate
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
Summary:        Detect and read QR codes from any image source
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Detect and read QR codes from any image source
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+img-devel
Summary:        Detect and read QR codes from any image source
BuildArch:      noarch
%description -n %{name}+img-devel

This package contains library source intended for building other packages which
use the "img" feature of the "%{crate}" crate.

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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-rqrr-devel -f %{oreon_filedir}/rust-rqrr-devel.list

%changelog

%autochangelog
