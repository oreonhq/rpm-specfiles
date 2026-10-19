%global source0_hash 9eb8f655bba2d0c0459e43a5b0e6cd3cd388109898fb3d85d048165e8b0abd08
%bcond check 1
%global debug_package %{nil}
%global crate icu_decimal
Name:           rust-icu_decimal
Version:        2.3.0
Release:        1%{?dist}
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_decimal
Source0:        https://static.crates.io/crates/icu_decimal/icu_decimal-%{version}.crate
Patch:          icu_decimal-fix-metadata.diff
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
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+compiled_data-devel
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
BuildArch:      noarch
%description -n %{name}+compiled_data-devel

This package contains library source intended for building other packages which
use the "compiled_data" feature of the "%{crate}" crate.

%package     -n %{name}+datagen-devel
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
BuildArch:      noarch
%description -n %{name}+datagen-devel

This package contains library source intended for building other packages which
use the "datagen" feature of the "%{crate}" crate.

%package     -n %{name}+ryu-devel
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
BuildArch:      noarch
%description -n %{name}+ryu-devel

This package contains library source intended for building other packages which
use the "ryu" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        API for formatting basic decimal numbers in a locale-sensitive way
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -f datagen
%install
%cargo_install -f datagen
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -f datagen -- --lib
%cargo_test -f datagen -- --tests
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_decimal-devel -f %{oreon_filedir}/rust-icu_decimal-devel.list

%changelog

%autochangelog
