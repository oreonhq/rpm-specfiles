%global source0_hash db318d6e5b1c90dd29eb4256666b3eeb5f38caf0a68f12d13d2d0793a50d0c77
%bcond check 0
%global debug_package %{nil}
%global crate freetype
Name:           rust-freetype
Version:        0.8.0
Release:        1%{?dist}
Summary:        Bindings for Freetype used by Servo
License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/freetype
Source0:        https://static.crates.io/crates/freetype/freetype-%{version}.crate
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
Summary:        Bindings for Freetype used by Servo
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+freetype-sys-devel
Summary:        Bindings for Freetype used by Servo
BuildArch:      noarch
%description -n %{name}+freetype-sys-devel

This package contains library source intended for building other packages which
use the "freetype-sys" feature of the "%{crate}" crate.

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

%ifarch %{ix86} %{arm}
%cargo_test || :
%else
%cargo_test
%endif
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-freetype-devel -f %{oreon_filedir}/rust-freetype-devel.list

%changelog

%autochangelog
