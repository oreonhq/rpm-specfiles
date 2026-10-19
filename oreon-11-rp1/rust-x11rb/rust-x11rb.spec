%global source0_hash 9993aa5be5a26815fe2c3eacfc1fde061fc1a1f094bf1ad2a18bf9c495dd7414
%bcond check 1
%global debug_package %{nil}
%global crate x11rb
Name:           rust-x11rb
Version:        0.13.2
Release:        1%{?dist}
Summary:        Rust bindings to X11
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/x11rb
Source0:        https://static.crates.io/crates/x11rb/x11rb-%{version}.crate
Patch:          x11rb-fix-metadata.diff
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
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+all-extensions-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+all-extensions-devel

This package contains library source intended for building other packages which
use the "all-extensions" feature of the "%{crate}" crate.

%package     -n %{name}+allow-unsafe-code-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+allow-unsafe-code-devel

This package contains library source intended for building other packages which
use the "allow-unsafe-code" feature of the "%{crate}" crate.

%package     -n %{name}+as-raw-xcb-connection-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+as-raw-xcb-connection-devel

This package contains library source intended for building other packages which
use the "as-raw-xcb-connection" feature of the "%{crate}" crate.

%package     -n %{name}+composite-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+composite-devel

This package contains library source intended for building other packages which
use the "composite" feature of the "%{crate}" crate.

%package     -n %{name}+cursor-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+cursor-devel

This package contains library source intended for building other packages which
use the "cursor" feature of the "%{crate}" crate.

%package     -n %{name}+damage-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+damage-devel

This package contains library source intended for building other packages which
use the "damage" feature of the "%{crate}" crate.

%package     -n %{name}+dbe-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+dbe-devel

This package contains library source intended for building other packages which
use the "dbe" feature of the "%{crate}" crate.

%package     -n %{name}+dl-libxcb-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+dl-libxcb-devel

This package contains library source intended for building other packages which
use the "dl-libxcb" feature of the "%{crate}" crate.

%package     -n %{name}+dpms-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+dpms-devel

This package contains library source intended for building other packages which
use the "dpms" feature of the "%{crate}" crate.

%package     -n %{name}+dri2-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+dri2-devel

This package contains library source intended for building other packages which
use the "dri2" feature of the "%{crate}" crate.

%package     -n %{name}+dri3-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+dri3-devel

This package contains library source intended for building other packages which
use the "dri3" feature of the "%{crate}" crate.

%package     -n %{name}+extra-traits-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+extra-traits-devel

This package contains library source intended for building other packages which
use the "extra-traits" feature of the "%{crate}" crate.

%package     -n %{name}+glx-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+glx-devel

This package contains library source intended for building other packages which
use the "glx" feature of the "%{crate}" crate.

%package     -n %{name}+image-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+image-devel

This package contains library source intended for building other packages which
use the "image" feature of the "%{crate}" crate.

%package     -n %{name}+libc-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+libc-devel

This package contains library source intended for building other packages which
use the "libc" feature of the "%{crate}" crate.

%package     -n %{name}+libloading-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+libloading-devel

This package contains library source intended for building other packages which
use the "libloading" feature of the "%{crate}" crate.

%package     -n %{name}+once_cell-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+once_cell-devel

This package contains library source intended for building other packages which
use the "once_cell" feature of the "%{crate}" crate.

%package     -n %{name}+present-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+present-devel

This package contains library source intended for building other packages which
use the "present" feature of the "%{crate}" crate.

%package     -n %{name}+randr-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+randr-devel

This package contains library source intended for building other packages which
use the "randr" feature of the "%{crate}" crate.

%package     -n %{name}+raw-window-handle-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+raw-window-handle-devel

This package contains library source intended for building other packages which
use the "raw-window-handle" feature of the "%{crate}" crate.

%package     -n %{name}+record-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+record-devel

This package contains library source intended for building other packages which
use the "record" feature of the "%{crate}" crate.

%package     -n %{name}+render-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+render-devel

This package contains library source intended for building other packages which
use the "render" feature of the "%{crate}" crate.

%package     -n %{name}+request-parsing-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+request-parsing-devel

This package contains library source intended for building other packages which
use the "request-parsing" feature of the "%{crate}" crate.

%package     -n %{name}+res-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+res-devel

This package contains library source intended for building other packages which
use the "res" feature of the "%{crate}" crate.

%package     -n %{name}+resource_manager-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+resource_manager-devel

This package contains library source intended for building other packages which
use the "resource_manager" feature of the "%{crate}" crate.

%package     -n %{name}+screensaver-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+screensaver-devel

This package contains library source intended for building other packages which
use the "screensaver" feature of the "%{crate}" crate.

%package     -n %{name}+shape-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+shape-devel

This package contains library source intended for building other packages which
use the "shape" feature of the "%{crate}" crate.

%package     -n %{name}+shm-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+shm-devel

This package contains library source intended for building other packages which
use the "shm" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+xcursor-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xcursor-devel

This package contains library source intended for building other packages which
use the "xcursor" feature of the "%{crate}" crate.

%package     -n %{name}+xevie-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xevie-devel

This package contains library source intended for building other packages which
use the "xevie" feature of the "%{crate}" crate.

%package     -n %{name}+xf86dri-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xf86dri-devel

This package contains library source intended for building other packages which
use the "xf86dri" feature of the "%{crate}" crate.

%package     -n %{name}+xf86vidmode-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xf86vidmode-devel

This package contains library source intended for building other packages which
use the "xf86vidmode" feature of the "%{crate}" crate.

%package     -n %{name}+xfixes-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xfixes-devel

This package contains library source intended for building other packages which
use the "xfixes" feature of the "%{crate}" crate.

%package     -n %{name}+xinerama-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xinerama-devel

This package contains library source intended for building other packages which
use the "xinerama" feature of the "%{crate}" crate.

%package     -n %{name}+xinput-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xinput-devel

This package contains library source intended for building other packages which
use the "xinput" feature of the "%{crate}" crate.

%package     -n %{name}+xkb-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xkb-devel

This package contains library source intended for building other packages which
use the "xkb" feature of the "%{crate}" crate.

%package     -n %{name}+xprint-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xprint-devel

This package contains library source intended for building other packages which
use the "xprint" feature of the "%{crate}" crate.

%package     -n %{name}+xselinux-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xselinux-devel

This package contains library source intended for building other packages which
use the "xselinux" feature of the "%{crate}" crate.

%package     -n %{name}+xtest-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xtest-devel

This package contains library source intended for building other packages which
use the "xtest" feature of the "%{crate}" crate.

%package     -n %{name}+xv-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xv-devel

This package contains library source intended for building other packages which
use the "xv" feature of the "%{crate}" crate.

%package     -n %{name}+xvmc-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+xvmc-devel

This package contains library source intended for building other packages which
use the "xvmc" feature of the "%{crate}" crate.

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
%files -n rust-x11rb-devel -f %{oreon_filedir}/rust-x11rb-devel.list

%changelog

%autochangelog
