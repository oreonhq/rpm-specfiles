%global source0_hash 4bd536557b58c682b217b8fb199afdff47cd3eff260623f19e77074eb073d63a
%bcond check 0
%global debug_package %{nil}
%global crate enumset_derive
Name:           rust-enumset_derive
Version:        0.15.0
Release:        1%{?dist}
Summary:        An internal helper crate for enumset. Not public API.
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/enumset_derive
Source0:        https://static.crates.io/crates/enumset_derive/enumset_derive-%{version}.crate
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

%package     -n %{name}+proc-macro-crate-devel
Summary:        An internal helper crate for enumset. Not public API.
BuildArch:      noarch
%description -n %{name}+proc-macro-crate-devel

This package contains library source intended for building other packages which
use the "proc-macro-crate" feature of the "%{crate}" crate.

%package     -n %{name}+serde2_deprecation_warning-devel
Summary:        An internal helper crate for enumset. Not public API.
BuildArch:      noarch
%description -n %{name}+serde2_deprecation_warning-devel

This package contains library source intended for building other packages which
use the "serde2_deprecation_warning" feature of the "%{crate}" crate.

%package     -n %{name}+std_deprecation_warning-devel
Summary:        An internal helper crate for enumset. Not public API.
BuildArch:      noarch
%description -n %{name}+std_deprecation_warning-devel

This package contains library source intended for building other packages which
use the "std_deprecation_warning" feature of the "%{crate}" crate.

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
%files -n rust-enumset_derive-devel -f %{oreon_filedir}/rust-enumset_derive-devel.list

%changelog

%autochangelog
