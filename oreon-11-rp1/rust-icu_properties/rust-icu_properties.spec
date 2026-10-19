%global source0_hash 7e7ca276ad3145661a65914e6daf131ca5120cd3dcee8f8f3214b8875184a148
%bcond check 0
%global debug_package %{nil}
%global crate icu_properties
Name:           rust-icu_properties
Version:        2.3.0
Release:        1%{?dist}
Summary:        Definitions for Unicode properties
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_properties
Source0:        https://static.crates.io/crates/icu_properties/icu_properties-%{version}.crate
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
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+harfbuzz_traits-devel
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+harfbuzz_traits-devel

This package contains library source intended for building other packages which
use the "harfbuzz_traits" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+unicode_bidi-devel
Summary:        Definitions for Unicode properties
BuildArch:      noarch
%description -n %{name}+unicode_bidi-devel

This package contains library source intended for building other packages which
use the "unicode_bidi" feature of the "%{crate}" crate.

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
%files -n rust-icu_properties-devel -f %{oreon_filedir}/rust-icu_properties-devel.list

%changelog

%autochangelog
