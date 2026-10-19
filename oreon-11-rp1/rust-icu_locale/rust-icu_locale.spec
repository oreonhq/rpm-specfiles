%global source0_hash 785f595c61ef57169a467eeed7b4b6936a66f6cacbb116a96ee86da983251bf4
%bcond check 1
%global debug_package %{nil}
%global crate icu_locale
Name:           rust-icu_locale
Version:        2.3.1
Release:        1%{?dist}
Summary:        API for Unicode Language and Locale Identifiers canonicalization
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_locale
Source0:        https://static.crates.io/crates/icu_locale/icu_locale-%{version}.crate
Patch:          icu_locale-fix-metadata.diff
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
Summary:        API for Unicode Language and Locale Identifiers canonicalization
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        API for Unicode Language and Locale Identifiers canonicalization
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        API for Unicode Language and Locale Identifiers canonicalization
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for Unicode Language and Locale Identifiers canonicalization
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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
%cargo_test -- --tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_locale-devel -f %{oreon_filedir}/rust-icu_locale-devel.list

%changelog

%autochangelog
