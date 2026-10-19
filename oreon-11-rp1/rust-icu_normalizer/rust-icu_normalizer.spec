%global source0_hash 12f9cf5f235641ed274641dd81c3f28d870e276763d0797aeeab72317b1c646f
%bcond check 0
%global debug_package %{nil}
%global crate icu_normalizer
Name:           rust-icu_normalizer
Version:        2.3.0
Release:        1%{?dist}
Summary:        API for normalizing text into Unicode Normalization Forms
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_normalizer
Source0:        https://static.crates.io/crates/icu_normalizer/icu_normalizer-%{version}.crate
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
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+harfbuzz_traits-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+harfbuzz_traits-devel

This package contains library source intended for building other packages which
use the "harfbuzz_traits" feature of the "%{crate}" crate.

%package     -n %{name}+icu_properties-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+icu_properties-devel

This package contains library source intended for building other packages which
use the "icu_properties" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+utf16_iter-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+utf16_iter-devel

This package contains library source intended for building other packages which
use the "utf16_iter" feature of the "%{crate}" crate.

%package     -n %{name}+utf8_iter-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+utf8_iter-devel

This package contains library source intended for building other packages which
use the "utf8_iter" feature of the "%{crate}" crate.

%package     -n %{name}+write16-devel
Summary:        API for normalizing text into Unicode Normalization Forms
BuildArch:      noarch
%description -n %{name}+write16-devel

This package contains library source intended for building other packages which
use the "write16" feature of the "%{crate}" crate.

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
%files -n rust-icu_normalizer-devel -f %{oreon_filedir}/rust-icu_normalizer-devel.list

%changelog

%autochangelog
