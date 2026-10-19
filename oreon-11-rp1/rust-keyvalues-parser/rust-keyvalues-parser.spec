%global source101_hash 932194f0301570094a7a39fc7c7514a3a2281f54a78b2b72985683e04f8acc93
%global source100_hash 153220b405aeeec6239446be8abf89981ea4da996c764c86e9588402c1763ffe
%global source0_hash 7e4c8354918309196302015ac9cae43362f1a13d0d5c5539a33b4c2fd2cd6d25
%bcond check 0
%global debug_package %{nil}
%global crate keyvalues-parser
Name:           rust-keyvalues-parser
Version:        0.2.0
Release:        1%{?dist}
Summary:        Parser/renderer for vdf text
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/keyvalues-parser
Source0:        https://static.crates.io/crates/keyvalues-parser/keyvalues-parser-%{version}.crate
Source100:      https://raw.githubusercontent.com/CosmicHorrorDev/vdf-rs/refs/heads/main/LICENSE-MIT
Source101:      https://raw.githubusercontent.com/CosmicHorrorDev/vdf-rs/refs/heads/main/LICENSE-APACHE
Patch:          keyvalues-parser-fix-metadata.diff
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
Summary:        Parser/renderer for vdf text
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE100} %{SOURCE101} .
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
%files -n rust-keyvalues-parser-devel -f %{oreon_filedir}/rust-keyvalues-parser-devel.list

%changelog

%autochangelog
