%global source0_hash 06c28280c6b12055b5e39e4554271ae4e6630b27c0da9148c4cf6485fc6d245c
%bcond check 0
%global debug_package %{nil}
%global crate cairo-sys-rs
Name:           rust-cairo-sys-rs0.21
Version:        0.21.5
Release:        1%{?dist}
Summary:        FFI bindings to libcairo
License:        MIT
URL:            https://crates.io/crates/cairo-sys-rs
Source0:        https://static.crates.io/crates/cairo-sys-rs/cairo-sys-rs-%{version}.crate
Patch:          cairo-sys-rs-fix-metadata-auto.diff
# oreon:deps
BuildRequires:  cargo
BuildRequires:  cargo-rpm-macros
BuildRequires:  pkgconfig(cairo)
BuildRequires:  rustc
# /oreon:deps
%description

%package        devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       pkgconfig(cairo) >= 1.14
%description    devel

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%package     -n %{name}+default-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+freetype-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+freetype-devel

This package contains library source intended for building other packages which
use the "freetype" feature of the "%{crate}" crate.

%package     -n %{name}+glib-sys-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+glib-sys-devel

This package contains library source intended for building other packages which
use the "glib-sys" feature of the "%{crate}" crate.

%package     -n %{name}+pdf-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+pdf-devel

This package contains library source intended for building other packages which
use the "pdf" feature of the "%{crate}" crate.

%package     -n %{name}+png-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+png-devel

This package contains library source intended for building other packages which
use the "png" feature of the "%{crate}" crate.

%package     -n %{name}+ps-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+ps-devel

This package contains library source intended for building other packages which
use the "ps" feature of the "%{crate}" crate.

%package     -n %{name}+script-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+script-devel

This package contains library source intended for building other packages which
use the "script" feature of the "%{crate}" crate.

%package     -n %{name}+svg-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+svg-devel

This package contains library source intended for building other packages which
use the "svg" feature of the "%{crate}" crate.

%package     -n %{name}+use_glib-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
Requires:       ((pkgconfig(cairo-gobject) >= 1.16 if crate(cairo-sys-rs/v1_16)) and pkgconfig(cairo-gobject) >= 1.14)
Requires:       ((pkgconfig(cairo-gobject) >= 1.17 if crate(cairo-sys-rs/v1_18)) and pkgconfig(cairo-gobject) >= 1.14)
%description -n %{name}+use_glib-devel

This package contains library source intended for building other packages which
use the "use_glib" feature of the "%{crate}" crate.

%package     -n %{name}+v1_16-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
Requires:       pkgconfig(cairo) >= 1.16
%description -n %{name}+v1_16-devel

This package contains library source intended for building other packages which
use the "v1_16" feature of the "%{crate}" crate.

%package     -n %{name}+v1_18-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
Requires:       pkgconfig(cairo) >= 1.17
%description -n %{name}+v1_18-devel

This package contains library source intended for building other packages which
use the "v1_18" feature of the "%{crate}" crate.

%package     -n %{name}+x11-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+x11-devel

This package contains library source intended for building other packages which
use the "x11" feature of the "%{crate}" crate.

%package     -n %{name}+xcb-devel
Summary:        FFI bindings to libcairo
BuildArch:      noarch
%description -n %{name}+xcb-devel

This package contains library source intended for building other packages which
use the "xcb" feature of the "%{crate}" crate.

%package     -n %{name}+xlib-devel
Summary:        FFI bindings to libcairo
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
%files -n rust-cairo-sys-rs0.21-devel -f %{oreon_filedir}/rust-cairo-sys-rs0.21-devel.list

%changelog

%autochangelog
