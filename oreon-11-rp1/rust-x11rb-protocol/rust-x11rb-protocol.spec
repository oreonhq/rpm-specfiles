%global source0_hash acf4d1bc32aa46eec18caa634ec3cf4c05bfa151f12b93b510b15190f69a1ca8
%bcond check 1
%global debug_package %{nil}
%global crate x11rb-protocol
Name:           rust-x11rb-protocol
Version:        0.14.0
Release:        1%{?dist}
Summary:        Rust bindings to X11
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/x11rb-protocol
Source0:        https://static.crates.io/crates/x11rb-protocol/x11rb-protocol-%{version}.crate
Patch:          x11rb-protocol-fix-metadata.diff
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

%package     -n %{name}+composite-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+composite-devel

This package contains library source intended for building other packages which
use the "composite" feature of the "%{crate}" crate.

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

%package     -n %{name}+serde-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+serde-devel

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

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

%package     -n %{name}+std-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+std-devel

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%package     -n %{name}+sync-devel
Summary:        Rust bindings to X11
BuildArch:      noarch
%description -n %{name}+sync-devel

This package contains library source intended for building other packages which
use the "sync" feature of the "%{crate}" crate.

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
%files -n rust-x11rb-protocol-devel -f %{oreon_filedir}/rust-x11rb-protocol-devel.list

%changelog

%autochangelog
