%global source2_hash 23f18e03dc49df91622fe2a76176497404e46ced8a715d9d2b67a7446571cca3
%global source1_hash 62c7a1e35f56406896d7aa7ca52d0cc0d272ac022b5d2796e7d6905db8a3636a
%global source0_hash 078ea7b7c29a2b4df841a7f6ac8775ff6074020c6776d48491ce2268e068f972
%bcond check 0
%global debug_package %{nil}
%global crate intl_pluralrules
Name:           rust-intl_pluralrules
Version:        7.0.2
Release:        1%{?dist}
Summary:        Unicode Plural Rules categorizer for numeric input
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/intl_pluralrules
Source0:        https://static.crates.io/crates/intl_pluralrules/intl_pluralrules-%{version}.crate
Source1:        https://github.com/zbraniecki/pluralrules/raw/48089b7/intl_pluralrules/LICENSE-APACHE
Source2:        https://github.com/zbraniecki/pluralrules/raw/48089b7/intl_pluralrules/LICENSE-MIT
Patch:          intl_pluralrules-fix-metadata.diff
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
Summary:        Unicode Plural Rules categorizer for numeric input
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE1} %{SOURCE2} .
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
%files -n rust-intl_pluralrules-devel -f %{oreon_filedir}/rust-intl_pluralrules-devel.list

%changelog

%autochangelog
