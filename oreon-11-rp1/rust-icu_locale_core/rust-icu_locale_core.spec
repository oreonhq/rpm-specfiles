%global source0_hash d56e28588da92eee5c3201a6eff33fabdd49b62269c8938d4ff050ce4d900deb
%bcond check 0
%global debug_package %{nil}
%global crate icu_locale_core
Name:           rust-icu_locale_core
Version:        2.3.0
Release:        1%{?dist}
Summary:        API for managing Unicode Language and Locale Identifiers
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_locale_core
Source0:        https://static.crates.io/crates/icu_locale_core/icu_locale_core-%{version}.crate
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

%package     -n %{name}+alloc-devel
Summary:        API for managing Unicode Language and Locale Identifiers
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+databake-devel
Summary:        API for managing Unicode Language and Locale Identifiers
BuildArch:      noarch
%description -n %{name}+databake-devel

This package contains library source intended for building other packages which
use the "databake" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for managing Unicode Language and Locale Identifiers
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+zerovec-devel
Summary:        API for managing Unicode Language and Locale Identifiers
BuildArch:      noarch
%description -n %{name}+zerovec-devel

This package contains library source intended for building other packages which
use the "zerovec" feature of the "%{crate}" crate.

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
%files -n rust-icu_locale_core-devel -f %{oreon_filedir}/rust-icu_locale_core-devel.list

%changelog

%autochangelog
