%global source0_hash 2ff038f9360b934342fb3c0a1d6e82c438a2624b51c3c6e3e6d7cf252b6f3ee3
%bcond check 1
%global debug_package %{nil}
%global crate picky-asn1
Name:           rust-picky-asn1_0.8
Version:        0.10.1
Release:        1%{?dist}
Summary:        Provide ASN.1 simple types
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/picky-asn1
Source0:        https://static.crates.io/crates/picky-asn1/picky-asn1-%{version}.crate
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
Summary:        Provide ASN.1 simple types
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+chrono-devel
Summary:        Provide ASN.1 simple types
BuildArch:      noarch
%description -n %{name}+chrono-devel

This package contains library source intended for building other packages which
use the "chrono" feature of the "%{crate}" crate.

%package     -n %{name}+chrono_conversion-devel
Summary:        Provide ASN.1 simple types
BuildArch:      noarch
%description -n %{name}+chrono_conversion-devel

This package contains library source intended for building other packages which
use the "chrono_conversion" feature of the "%{crate}" crate.

%package     -n %{name}+time-devel
Summary:        Provide ASN.1 simple types
BuildArch:      noarch
%description -n %{name}+time-devel

This package contains library source intended for building other packages which
use the "time" feature of the "%{crate}" crate.

%package     -n %{name}+time_conversion-devel
Summary:        Provide ASN.1 simple types
BuildArch:      noarch
%description -n %{name}+time_conversion-devel

This package contains library source intended for building other packages which
use the "time_conversion" feature of the "%{crate}" crate.

%package     -n %{name}+zeroize-devel
Summary:        Provide ASN.1 simple types
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

%cargo_test -- --lib
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-picky-asn1_0.8-devel -f %{oreon_filedir}/rust-picky-asn1_0.8-devel.list

%changelog

%autochangelog
