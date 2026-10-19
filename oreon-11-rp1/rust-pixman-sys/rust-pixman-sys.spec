%global source0_hash a1a0483e89e81d7915defe83c51f23f6800594d64f6f4a21253ce87fd8444ada
%bcond check 1
%global debug_package %{nil}
%global crate pixman-sys
Name:           rust-pixman-sys
Version:        0.1.0
Release:        1%{?dist}
Summary:        Pixman is a low-level software library for pixel manipulation, providing features such as image compositing and trapezoid rasterization
License:        MIT
URL:            https://crates.io/crates/pixman-sys
Source0:        https://static.crates.io/crates/pixman-sys/pixman-sys-%{version}.crate
Source2:        LICENSE
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(pixman-1) >= 0.44
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        Pixman is a low-level software library for pixel manipulation, providing features such as image compositing and trapezoid rasterization
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{crate}-%{version} -p1
cp -pav %{SOURCE2} .
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
%files -n rust-pixman-sys-devel -f %{oreon_filedir}/rust-pixman-sys-devel.list

%changelog

%autochangelog
