%global source0_hash bd95ad50b9a3d2551e25dd4f6892aff0b772fe5372d84514e9d0583af60a0ce7
%bcond check 0
%global debug_package %{nil}
%global crate gdk-pixbuf-sys
Name:           rust-gdk-pixbuf-sys0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        FFI bindings to libgdk_pixbuf-2.0
License:        MIT
URL:            https://crates.io/crates/gdk-pixbuf-sys
Source0:        https://static.crates.io/crates/gdk-pixbuf-sys/gdk-pixbuf-sys-%{version}.crate
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.36.8
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libgdk_pixbuf-2.0
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v2_40-devel
Summary:        FFI bindings to libgdk_pixbuf-2.0
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.40
%description -n %{name}+v2_40-devel

This package contains library source intended for building other packages which
use the "v2_40" feature of the "%{crate}" crate.

%package     -n %{name}+v2_42-devel
Summary:        FFI bindings to libgdk_pixbuf-2.0
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.42
%description -n %{name}+v2_42-devel

This package contains library source intended for building other packages which
use the "v2_42" feature of the "%{crate}" crate.

%package     -n %{name}+v2_44-devel
Summary:        FFI bindings to libgdk_pixbuf-2.0
BuildArch:      noarch
Requires:       pkgconfig(gdk-pixbuf-2.0) >= 2.43
%description -n %{name}+v2_44-devel

This package contains library source intended for building other packages which
use the "v2_44" feature of the "%{crate}" crate.

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
%files -n rust-gdk-pixbuf-sys0.21-devel -f %{oreon_filedir}/rust-gdk-pixbuf-sys0.21-devel.list

%changelog

%autochangelog
