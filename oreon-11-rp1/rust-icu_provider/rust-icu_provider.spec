%global source0_hash d27bbb9d3abbefac45d55f647c9de1d44aafcd1186eb91879afef17c396c3e73
%bcond check 0
%global debug_package %{nil}
%global crate icu_provider
Name:           rust-icu_provider
Version:        2.3.1
Release:        1%{?dist}
Summary:        Trait and struct definitions for the ICU data provider
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_provider
Source0:        https://static.crates.io/crates/icu_provider/icu_provider-%{version}.crate
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
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+baked-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+baked-devel

This package contains library source intended for building other packages which
use the "baked" feature of the "%{crate}" crate.

%package     -n %{name}+deserialize_bincode_1-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+deserialize_bincode_1-devel

This package contains library source intended for building other packages which
use the "deserialize_bincode_1" feature of the "%{crate}" crate.

%package     -n %{name}+deserialize_json-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+deserialize_json-devel

This package contains library source intended for building other packages which
use the "deserialize_json" feature of the "%{crate}" crate.

%package     -n %{name}+deserialize_postcard_1-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+deserialize_postcard_1-devel

This package contains library source intended for building other packages which
use the "deserialize_postcard_1" feature of the "%{crate}" crate.

%package     -n %{name}+export-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+export-devel

This package contains library source intended for building other packages which
use the "export" feature of the "%{crate}" crate.

%package     -n %{name}+logging-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+logging-devel

This package contains library source intended for building other packages which
use the "logging" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+zerotrie-devel
Summary:        Trait and struct definitions for the ICU data provider
BuildArch:      noarch
%description -n %{name}+zerotrie-devel

This package contains library source intended for building other packages which
use the "zerotrie" feature of the "%{crate}" crate.

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
%files -n rust-icu_provider-devel -f %{oreon_filedir}/rust-icu_provider-devel.list

%changelog

%autochangelog
