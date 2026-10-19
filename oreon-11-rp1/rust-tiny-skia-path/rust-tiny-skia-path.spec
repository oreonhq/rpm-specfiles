%global source0_hash edca365c3faccca67d06593c5980fa6c57687de727a03131735bb85f01fdeeb9
%bcond check 0
%global debug_package %{nil}
%global crate tiny-skia-path
Name:           rust-tiny-skia-path
Version:        0.12.0
Release:        1%{?dist}
Summary:        Tiny-skia Bezier path implementation
License:        BSD-3-Clause
URL:            https://crates.io/crates/tiny-skia-path
Source0:        https://static.crates.io/crates/tiny-skia-path/tiny-skia-path-%{version}.crate
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
Summary:        Tiny-skia Bezier path implementation
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+libm-devel
Summary:        Tiny-skia Bezier path implementation
BuildArch:      noarch
%description -n %{name}+libm-devel

This package contains library source intended for building other packages which
use the "libm" feature of the "%{crate}" crate.

%package     -n %{name}+no-std-float-devel
Summary:        Tiny-skia Bezier path implementation
BuildArch:      noarch
%description -n %{name}+no-std-float-devel

This package contains library source intended for building other packages which
use the "no-std-float" feature of the "%{crate}" crate.

%package     -n %{name}+std-devel
Summary:        Tiny-skia Bezier path implementation
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
%files -n rust-tiny-skia-path-devel -f %{oreon_filedir}/rust-tiny-skia-path-devel.list

%changelog

%autochangelog
