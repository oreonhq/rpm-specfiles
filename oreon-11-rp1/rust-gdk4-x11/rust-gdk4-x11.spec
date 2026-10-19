%global source0_hash 9d892b4cf5a07e90e1390e93cd792975746c68b59f790a2de9e96ce77211ea9a
%bcond check 1
%global debug_package %{nil}
%global crate gdk4-x11
Name:           rust-gdk4-x11
Version:        0.11.4
Release:        1%{?dist}
Summary:        Rust bindings of the GDK4 X11 library
License:        MIT
URL:            https://crates.io/crates/gdk4-x11
Source0:        https://static.crates.io/crates/gdk4-x11/gdk4-x11-%{version}.crate
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
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+v4_10-devel
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+v4_10-devel

This package contains library source intended for building other packages which
use the "v4_10" feature of the "%{crate}" crate.

%package     -n %{name}+v4_16-devel
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+v4_16-devel

This package contains library source intended for building other packages which
use the "v4_16" feature of the "%{crate}" crate.

%package     -n %{name}+v4_18-devel
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+v4_18-devel

This package contains library source intended for building other packages which
use the "v4_18" feature of the "%{crate}" crate.

%package     -n %{name}+v4_4-devel
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+v4_4-devel

This package contains library source intended for building other packages which
use the "v4_4" feature of the "%{crate}" crate.

%package     -n %{name}+x11-devel
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+x11-devel

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%package     -n %{name}+xlib-devel
Summary:        Rust bindings of the GDK4 X11 library
BuildArch:      noarch
%description -n %{name}+xlib-devel

This package contains library source intended for building other packages which
use the "xlib" feature of the "%{crate}" crate.

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
%files -n rust-gdk4-x11-devel -f %{oreon_filedir}/rust-gdk4-x11-devel.list

%changelog

%autochangelog
