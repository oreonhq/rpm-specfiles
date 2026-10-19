%global source0_hash 76afc826de14238e6e8c374ddcc1fa19e374fd8dd986b0d2af0d02377261d83c
%bcond check 0
%global debug_package %{nil}
%global crate rand_core
Name:           rust-rand_core0.9
Version:        0.9.5
Release:        1%{?dist}
Summary:        Core random number generator traits and tools for implementation
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/rand_core
Source0:        https://static.crates.io/crates/rand_core/rand_core-%{version}.crate
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
Summary:        Core random number generator traits and tools for implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+os_rng-devel
Summary:        Core random number generator traits and tools for implementation
BuildArch:      noarch
%description -n %{name}+os_rng-devel

This package contains library source intended for building other packages which
use the "os_rng" feature of the "%{crate}" crate.

%package     -n %{name}+serde-devel
Summary:        Core random number generator traits and tools for implementation
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Core random number generator traits and tools for implementation
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
%files -n rust-rand_core0.9-devel -f %{oreon_filedir}/rust-rand_core0.9-devel.list

%changelog

%autochangelog
