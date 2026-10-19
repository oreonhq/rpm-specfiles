%global source0_hash 08984ed58ac439ebf3e13d2cf26b0c46a60afcd21721c1d14087c0b240344dda
%bcond check 1
%global debug_package %{nil}
%global crate icu_collator
Name:           rust-icu_collator
Version:        2.3.1
Release:        1%{?dist}
Summary:        API for comparing strings according to language-dependent conventions
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_collator
Source0:        https://static.crates.io/crates/icu_collator/icu_collator-%{version}.crate
Patch:          icu_collator-fix-metadata.diff
Patch10:        icu_collator-2.1.1-no-arraystring-tests.patch
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
Summary:        API for comparing strings according to language-dependent conventions
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        API for comparing strings according to language-dependent conventions
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        API for comparing strings according to language-dependent conventions
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+latin1-devel
Summary:        API for comparing strings according to language-dependent conventions
BuildArch:      noarch
%description -n %{name}+latin1-devel

This package contains library source intended for building other packages which
use the "latin1" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for comparing strings according to language-dependent conventions
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
%files -n rust-icu_collator-devel -f %{oreon_filedir}/rust-icu_collator-devel.list

%changelog

%autochangelog
