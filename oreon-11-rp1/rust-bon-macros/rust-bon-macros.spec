%global source0_hash 519bd3116aeeb42d5372c29d982d16d0170d3d4a5ed85fc7dd91642ffff3c67c
%bcond check 1
%global debug_package %{nil}
%global crate bon-macros
Name:           rust-bon-macros
Version:        3.9.1
Release:        1%{?dist}
Summary:        Compile-time-checked builder generator
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/bon-macros
Source0:        https://static.crates.io/crates/bon-macros/bon-macros-%{version}.crate
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
Summary:        Compile-time-checked builder generator
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+alloc-devel
Summary:        Compile-time-checked builder generator
BuildArch:      noarch
%description -n %{name}+alloc-devel

This package contains library source intended for building other packages which
use the "alloc" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-generics-setters-devel
Summary:        Compile-time-checked builder generator
BuildArch:      noarch
%description -n %{name}+experimental-generics-setters-devel

This package contains library source intended for building other packages which
use the "experimental-generics-setters" feature of the "%{crate}" crate.

%package     -n %{name}+experimental-overwritable-devel
Summary:        Compile-time-checked builder generator
BuildArch:      noarch
%description -n %{name}+experimental-overwritable-devel

This package contains library source intended for building other packages which
use the "experimental-overwritable" feature of the "%{crate}" crate.

%package     -n %{name}+implied-bounds-devel
Summary:        Compile-time-checked builder generator
BuildArch:      noarch
%description -n %{name}+implied-bounds-devel

This package contains library source intended for building other packages which
use the "implied-bounds" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Compile-time-checked builder generator
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
%files -n rust-bon-macros-devel -f %{oreon_filedir}/rust-bon-macros-devel.list

%changelog

%autochangelog
