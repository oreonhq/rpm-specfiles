%global source0_hash 3a8c3a0a472b3a556e269be64dc65a5c013ba85e940d089367eb8c88f3fdfda9
%bcond check 0
%global debug_package %{nil}
%global crate alloc_counter
Name:           rust-alloc_counter
Version:        0.0.4
Release:        1%{?dist}
Summary:        Count allocations, reallocations, deallocations. Allow, deny, or forb...
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/alloc_counter
Source0:        https://static.crates.io/crates/alloc_counter/alloc_counter-%{version}.crate
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
Summary:        Count allocations, reallocations, deallocations. Allow, deny, or forb...
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc_counter_macro-devel
Summary:        Count allocations, reallocations, deallocations. Allow, deny, or forb...
BuildArch:      noarch
%description -n %{name}+alloc_counter_macro-devel

This package contains library source intended for building other packages which
use the "alloc_counter_macro" feature of the "%{crate}" crate.

%package     -n %{name}+macros-devel
Summary:        Count allocations, reallocations, deallocations. Allow, deny, or forb...
BuildArch:      noarch
%description -n %{name}+macros-devel

This package contains library source intended for building other packages which
use the "macros" feature of the "%{crate}" crate.

%package     -n %{name}+rustdoc-devel
Summary:        Count allocations, reallocations, deallocations. Allow, deny, or forb...
BuildArch:      noarch
%description -n %{name}+rustdoc-devel

This package contains library source intended for building other packages which
use the "rustdoc" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Count allocations, reallocations, deallocations. Allow, deny, or forb...
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
%files -n rust-alloc_counter-devel -f %{oreon_filedir}/rust-alloc_counter-devel.list

%changelog

%autochangelog
