%global source0_hash e475e6766ef87b1d3c1f97be6363995b0bfaeddbc789671615df598a97ff0593
%bcond check 1
%global debug_package %{nil}
%global crate icu_plurals
Name:           rust-icu_plurals
Version:        2.3.0
Release:        1%{?dist}
Summary:        Unicode Plural Rules categorizer for numeric input
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_plurals
Source0:        https://static.crates.io/crates/icu_plurals/icu_plurals-%{version}.crate
Patch:          icu_plurals-fix-metadata.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  rustc
BuildRequires:  tomcli
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

%package     -n %{name}+compiled_data-devel
Summary:        Unicode Plural Rules categorizer for numeric input
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        Unicode Plural Rules categorizer for numeric input
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-devel
Summary:        Unicode Plural Rules categorizer for numeric input
BuildArch:      noarch
%description -n %{name}+experimental-devel

This package contains library source intended for building other packages which
use the "experimental" feature of the "%{crate}" crate.

%package     -n %{name}+icu_normalizer_data-devel
Summary:        Unicode Plural Rules categorizer for numeric input
BuildArch:      noarch
%description -n %{name}+icu_normalizer_data-devel

This package contains library source intended for building other packages which
use the "icu_normalizer_data" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Unicode Plural Rules categorizer for numeric input
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
tomcli set Cargo.toml str dev-dependencies.icu_locale_core.version '~%{version}'
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a -- --lib
%cargo_test -a -- --test plurals
%cargo_test -a -- --test operands
%cargo_test -a -- --test rules
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_plurals-devel -f %{oreon_filedir}/rust-icu_plurals-devel.list

%changelog

%autochangelog
