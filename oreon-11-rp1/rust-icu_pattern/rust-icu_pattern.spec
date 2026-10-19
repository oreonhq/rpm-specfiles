%global source0_hash 2b3db611446bd92c246b03e4aa0bafa71ddb194af431ddbb42b9d70e4bfce1a0
%bcond check 1
%global debug_package %{nil}
%global crate icu_pattern
Name:           rust-icu_pattern
Version:        0.5.0
Release:        1%{?dist}
Summary:        ICU pattern utilities
License:        Unicode-3.0
URL:            https://crates.io/crates/icu_pattern
Source0:        https://static.crates.io/crates/icu_pattern/icu_pattern-%{version}.crate
Patch:          icu_pattern-fix-metadata.diff
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
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+databake-devel
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+databake-devel

This package contains library source intended for building other packages which
use the "databake" feature of the "%{crate}" crate.

%package     -n %{name}+litemap-devel
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+litemap-devel

This package contains library source intended for building other packages which
use the "litemap" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+yoke-devel
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+yoke-devel

This package contains library source intended for building other packages which
use the "yoke" feature of the "%{crate}" crate.

%package     -n %{name}+zerovec-devel
Summary:        ICU pattern utilities
BuildArch:      noarch
%description -n %{name}+zerovec-devel

This package contains library source intended for building other packages which
use the "zerovec" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
%oreon_vendor_cargo
%build

%cargo_build -a
%install
%cargo_install -a
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%if %{with check}
%check

%cargo_test -a
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-icu_pattern-devel -f %{oreon_filedir}/rust-icu_pattern-devel.list

%changelog

%autochangelog
