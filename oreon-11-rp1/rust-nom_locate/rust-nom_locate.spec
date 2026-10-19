%global source0_hash 0b577e2d69827c4740cba2b52efaad1c4cc7c73042860b199710b3575c68438d
%bcond check 1
%global debug_package %{nil}
%global crate nom_locate
Name:           rust-nom_locate
Version:        5.0.0
Release:        1%{?dist}
Summary:        Special input type for nom to locate tokens
License:        MIT
URL:            https://crates.io/crates/nom_locate
Source0:        https://static.crates.io/crates/nom_locate/nom_locate-%{version}.crate
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
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+generic-simd-devel
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+generic-simd-devel

This package contains library source intended for building other packages which
use the "generic-simd" feature of the "%{crate}" crate.

%package     -n %{name}+runtime-dispatch-simd-devel
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+runtime-dispatch-simd-devel

This package contains library source intended for building other packages which
use the "runtime-dispatch-simd" feature of the "%{crate}" crate.

%package     -n %{name}+stable-deref-trait-devel
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+stable-deref-trait-devel

This package contains library source intended for building other packages which
use the "stable-deref-trait" feature of the "%{crate}" crate.

%package     -n %{name}+stable_deref_trait-devel
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+stable_deref_trait-devel

This package contains library source intended for building other packages which
use the "stable_deref_trait" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Special input type for nom to locate tokens
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

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
%files -n rust-nom_locate-devel -f %{oreon_filedir}/rust-nom_locate-devel.list

%changelog

%autochangelog
