%global source0_hash d413165e4bf7f808b9a27cbaba657657a2921f0965db833f488c4d4be96dcd2e
%bcond check 1
%global debug_package %{nil}
%global crate picky-asn1-der
Name:           rust-picky-asn1-der
Version:        0.5.6
Release:        1%{?dist}
Summary:        ASN.1-DER subset for serde
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/picky-asn1-der
Source0:        https://static.crates.io/crates/picky-asn1-der/picky-asn1-der-%{version}.crate
Patch:          picky-asn1-der-fix-metadata.diff
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
Summary:        ASN.1-DER subset for serde
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+debug_log-devel
Summary:        ASN.1-DER subset for serde
BuildArch:      noarch
%description -n %{name}+debug_log-devel

This package contains library source intended for building other packages which
use the "debug_log" feature of the "%{crate}" crate.

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
%files -n rust-picky-asn1-der-devel -f %{oreon_filedir}/rust-picky-asn1-der-devel.list

%changelog

%autochangelog
