%global source0_hash 6cbdf310d77fd3aaee6ea2093db7011dc2d35d2eb3481e5607f1f8d942ed99df
%bcond check 1
%global debug_package %{nil}
%global crate ashpd
Name:           rust-ashpd0.11
Version:        0.11.0
Release:        1%{?dist}
Summary:        XDG portals wrapper in Rust using zbus
License:        MIT
URL:            https://crates.io/crates/ashpd
Source0:        https://static.crates.io/crates/ashpd/ashpd-%{version}.crate
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
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+default-devel

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%package     -n %{name}+async-std-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+async-std-devel

This package contains library source intended for building other packages which
use the "async-std" feature of the "%{crate}" crate.

%package     -n %{name}+async-trait-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+async-trait-devel

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%package     -n %{name}+backend-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+backend-devel

This package contains library source intended for building other packages which
use the "backend" feature of the "%{crate}" crate.

%package     -n %{name}+gdk4wayland-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+gdk4wayland-devel

This package contains library source intended for building other packages which
use the "gdk4wayland" feature of the "%{crate}" crate.

%package     -n %{name}+gdk4x11-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+gdk4x11-devel

This package contains library source intended for building other packages which
use the "gdk4x11" feature of the "%{crate}" crate.

%package     -n %{name}+glib-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+glib-devel

This package contains library source intended for building other packages which
use the "glib" feature of the "%{crate}" crate.

%package     -n %{name}+gtk4-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+gtk4-devel

This package contains library source intended for building other packages which
use the "gtk4" feature of the "%{crate}" crate.

%package     -n %{name}+gtk4_wayland-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+gtk4_wayland-devel

This package contains library source intended for building other packages which
use the "gtk4_wayland" feature of the "%{crate}" crate.

%package     -n %{name}+gtk4_x11-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+gtk4_x11-devel

This package contains library source intended for building other packages which
use the "gtk4_x11" feature of the "%{crate}" crate.

%package     -n %{name}+pipewire-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+pipewire-devel

This package contains library source intended for building other packages which
use the "pipewire" feature of the "%{crate}" crate.

%package     -n %{name}+raw-window-handle-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+raw-window-handle-devel

This package contains library source intended for building other packages which
use the "raw-window-handle" feature of the "%{crate}" crate.

%package     -n %{name}+raw_handle-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+raw_handle-devel

This package contains library source intended for building other packages which
use the "raw_handle" feature of the "%{crate}" crate.

%package     -n %{name}+tokio-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+tokio-devel

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%package     -n %{name}+tracing-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+tracing-devel

This package contains library source intended for building other packages which
use the "tracing" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+wayland-devel

This package contains library source intended for building other packages which
use the "wayland" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-backend-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+wayland-backend-devel

This package contains library source intended for building other packages which
use the "wayland-backend" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-client-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+wayland-client-devel

This package contains library source intended for building other packages which
use the "wayland-client" feature of the "%{crate}" crate.

%package     -n %{name}+wayland-protocols-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+wayland-protocols-devel

This package contains library source intended for building other packages which
use the "wayland-protocols" feature of the "%{crate}" crate.

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
%files -n rust-ashpd0.11-devel -f %{oreon_filedir}/rust-ashpd0.11-devel.list

%changelog

%autochangelog
