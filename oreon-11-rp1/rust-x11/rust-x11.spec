%global source0_hash 502da5464ccd04011667b11c435cb992822c2c0dbde1770c988480d312a0db2e
%bcond check 0
%global debug_package %{nil}
%global crate x11
Name:           rust-x11
Version:        2.21.0
Release:        1%{?dist}
Summary:        X11 library bindings for Rust
License:        MIT
URL:            https://crates.io/crates/x11
Source0:        https://static.crates.io/crates/x11/x11-%{version}.crate
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
Summary:        X11 library bindings for Rust
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
%description -n %{name}+all-devel

This package contains library source intended for building other packages which
use the "all" feature of the "%{crate}" crate.

%package     -n %{name}+dox-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
%description -n %{name}+dox-devel

This package contains library source intended for building other packages which
use the "dox" feature of the "%{crate}" crate.

%package     -n %{name}+dpms-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xext) >= 1.3
%description -n %{name}+dpms-devel

This package contains library source intended for building other packages which
use the "dpms" feature of the "%{crate}" crate.

%package     -n %{name}+glx-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(gl) >= 1
%description -n %{name}+glx-devel

This package contains library source intended for building other packages which
use the "glx" feature of the "%{crate}" crate.

%package     -n %{name}+xcursor-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xcursor) >= 1.1
%description -n %{name}+xcursor-devel

This package contains library source intended for building other packages which
use the "xcursor" feature of the "%{crate}" crate.

%package     -n %{name}+xf86vmode-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xxf86vm) >= 1.1
%description -n %{name}+xf86vmode-devel

This package contains library source intended for building other packages which
use the "xf86vmode" feature of the "%{crate}" crate.

%package     -n %{name}+xfixes-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xfixes) >= 3.1
%description -n %{name}+xfixes-devel

This package contains library source intended for building other packages which
use the "xfixes" feature of the "%{crate}" crate.

%package     -n %{name}+xft-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xft) >= 2.1
%description -n %{name}+xft-devel

This package contains library source intended for building other packages which
use the "xft" feature of the "%{crate}" crate.

%package     -n %{name}+xinerama-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xinerama) >= 1.1
%description -n %{name}+xinerama-devel

This package contains library source intended for building other packages which
use the "xinerama" feature of the "%{crate}" crate.

%package     -n %{name}+xinput-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xi) >= 1.7
%description -n %{name}+xinput-devel

This package contains library source intended for building other packages which
use the "xinput" feature of the "%{crate}" crate.

%package     -n %{name}+xlib-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(x11) >= 1.4.99.1
%description -n %{name}+xlib-devel

This package contains library source intended for building other packages which
use the "xlib" feature of the "%{crate}" crate.

%package     -n %{name}+xlib_xcb-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(x11-xcb) >= 1.6
%description -n %{name}+xlib_xcb-devel

This package contains library source intended for building other packages which
use the "xlib_xcb" feature of the "%{crate}" crate.

%package     -n %{name}+xmu-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xmu) >= 1.1
%description -n %{name}+xmu-devel

This package contains library source intended for building other packages which
use the "xmu" feature of the "%{crate}" crate.

%package     -n %{name}+xrandr-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xrandr) >= 1.5
%description -n %{name}+xrandr-devel

This package contains library source intended for building other packages which
use the "xrandr" feature of the "%{crate}" crate.

%package     -n %{name}+xrecord-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
%description -n %{name}+xrecord-devel

This package contains library source intended for building other packages which
use the "xrecord" feature of the "%{crate}" crate.

%package     -n %{name}+xrender-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xrender) >= 0.9.6
%description -n %{name}+xrender-devel

This package contains library source intended for building other packages which
use the "xrender" feature of the "%{crate}" crate.

%package     -n %{name}+xss-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xscrnsaver) >= 1.2
%description -n %{name}+xss-devel

This package contains library source intended for building other packages which
use the "xss" feature of the "%{crate}" crate.

%package     -n %{name}+xt-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xt) >= 1.1
%description -n %{name}+xt-devel

This package contains library source intended for building other packages which
use the "xt" feature of the "%{crate}" crate.

%package     -n %{name}+xtest-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
%description -n %{name}+xtest-devel

This package contains library source intended for building other packages which
use the "xtest" feature of the "%{crate}" crate.

%package     -n %{name}+xtst-devel
Summary:        X11 library bindings for Rust
BuildArch:      noarch
Requires:       pkgconfig(xtst) >= 1.2
%description -n %{name}+xtst-devel

This package contains library source intended for building other packages which
use the "xtst" feature of the "%{crate}" crate.

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
%files -n rust-x11-devel -f %{oreon_filedir}/rust-x11-devel.list

%changelog

%autochangelog
