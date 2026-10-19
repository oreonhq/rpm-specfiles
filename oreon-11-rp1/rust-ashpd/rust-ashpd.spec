%global source0_hash 0b09507a218cf6eb4ab0659883e54880cea3984e3dbaa4989b6cda3f8f8a97a5
%bcond check 1
%global debug_package %{nil}
%global crate ashpd
Name:           rust-ashpd
Version:        0.13.5
Release:        1%{?dist}
Summary:        XDG portals wrapper in Rust using zbus
License:        MIT
URL:            https://crates.io/crates/ashpd
Source0:        https://static.crates.io/crates/ashpd/ashpd-%{version}.crate
Patch:          ashpd-fix-metadata.diff
Patch10:        0001-Ignore-one-doctest-that-pulls-in-reis-as-an-addition.patch
Patch11:        0002-Prevent-including-README-as-Rust-documentation.patch
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

%package     -n %{name}+account-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+account-devel

This package contains library source intended for building other packages which
use the "account" feature of the "%{crate}" crate.

%package     -n %{name}+async-io-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+async-io-devel

This package contains library source intended for building other packages which
use the "async-io" feature of the "%{crate}" crate.

%package     -n %{name}+backend-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+backend-devel

This package contains library source intended for building other packages which
use the "backend" feature of the "%{crate}" crate.

%package     -n %{name}+background-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+background-devel

This package contains library source intended for building other packages which
use the "background" feature of the "%{crate}" crate.

%package     -n %{name}+camera-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+camera-devel

This package contains library source intended for building other packages which
use the "camera" feature of the "%{crate}" crate.

%package     -n %{name}+clipboard-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+clipboard-devel

This package contains library source intended for building other packages which
use the "clipboard" feature of the "%{crate}" crate.

%package     -n %{name}+documents-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+documents-devel

This package contains library source intended for building other packages which
use the "documents" feature of the "%{crate}" crate.

%package     -n %{name}+dynamic_launcher-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+dynamic_launcher-devel

This package contains library source intended for building other packages which
use the "dynamic_launcher" feature of the "%{crate}" crate.

%package     -n %{name}+email-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+email-devel

This package contains library source intended for building other packages which
use the "email" feature of the "%{crate}" crate.

%package     -n %{name}+file_chooser-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+file_chooser-devel

This package contains library source intended for building other packages which
use the "file_chooser" feature of the "%{crate}" crate.

%package     -n %{name}+flatpak-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+flatpak-devel

This package contains library source intended for building other packages which
use the "flatpak" feature of the "%{crate}" crate.

%package     -n %{name}+frontend-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+frontend-devel

This package contains library source intended for building other packages which
use the "frontend" feature of the "%{crate}" crate.

%package     -n %{name}+game_mode-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+game_mode-devel

This package contains library source intended for building other packages which
use the "game_mode" feature of the "%{crate}" crate.

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

%package     -n %{name}+global_shortcuts-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+global_shortcuts-devel

This package contains library source intended for building other packages which
use the "global_shortcuts" feature of the "%{crate}" crate.

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

%package     -n %{name}+inhibit-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+inhibit-devel

This package contains library source intended for building other packages which
use the "inhibit" feature of the "%{crate}" crate.

%package     -n %{name}+input_capture-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+input_capture-devel

This package contains library source intended for building other packages which
use the "input_capture" feature of the "%{crate}" crate.

%package     -n %{name}+location-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+location-devel

This package contains library source intended for building other packages which
use the "location" feature of the "%{crate}" crate.

%package     -n %{name}+memory_monitor-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+memory_monitor-devel

This package contains library source intended for building other packages which
use the "memory_monitor" feature of the "%{crate}" crate.

%package     -n %{name}+network_monitor-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+network_monitor-devel

This package contains library source intended for building other packages which
use the "network_monitor" feature of the "%{crate}" crate.

%package     -n %{name}+notification-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+notification-devel

This package contains library source intended for building other packages which
use the "notification" feature of the "%{crate}" crate.

%package     -n %{name}+open_uri-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+open_uri-devel

This package contains library source intended for building other packages which
use the "open_uri" feature of the "%{crate}" crate.

%package     -n %{name}+pipewire-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+pipewire-devel

This package contains library source intended for building other packages which
use the "pipewire" feature of the "%{crate}" crate.

%package     -n %{name}+power_profile_monitor-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+power_profile_monitor-devel

This package contains library source intended for building other packages which
use the "power_profile_monitor" feature of the "%{crate}" crate.

%package     -n %{name}+print-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+print-devel

This package contains library source intended for building other packages which
use the "print" feature of the "%{crate}" crate.

%package     -n %{name}+proxy_resolver-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+proxy_resolver-devel

This package contains library source intended for building other packages which
use the "proxy_resolver" feature of the "%{crate}" crate.

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

%package     -n %{name}+realtime-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+realtime-devel

This package contains library source intended for building other packages which
use the "realtime" feature of the "%{crate}" crate.

%package     -n %{name}+remote_desktop-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+remote_desktop-devel

This package contains library source intended for building other packages which
use the "remote_desktop" feature of the "%{crate}" crate.

%package     -n %{name}+screencast-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+screencast-devel

This package contains library source intended for building other packages which
use the "screencast" feature of the "%{crate}" crate.

%package     -n %{name}+screenshot-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+screenshot-devel

This package contains library source intended for building other packages which
use the "screenshot" feature of the "%{crate}" crate.

%package     -n %{name}+secret-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+secret-devel

This package contains library source intended for building other packages which
use the "secret" feature of the "%{crate}" crate.

%package     -n %{name}+settings-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+settings-devel

This package contains library source intended for building other packages which
use the "settings" feature of the "%{crate}" crate.

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

%package     -n %{name}+trash-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+trash-devel

This package contains library source intended for building other packages which
use the "trash" feature of the "%{crate}" crate.

%package     -n %{name}+usb-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+usb-devel

This package contains library source intended for building other packages which
use the "usb" feature of the "%{crate}" crate.

%package     -n %{name}+wallpaper-devel
Summary:        XDG portals wrapper in Rust using zbus
BuildArch:      noarch
%description -n %{name}+wallpaper-devel

This package contains library source intended for building other packages which
use the "wallpaper" feature of the "%{crate}" crate.

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

%cargo_test -- -- --exact --skip tests::all_interfaces_have_implementations
%endif
%files -f %{oreon_filedir}/main.list
%files -n rust-ashpd-devel -f %{oreon_filedir}/rust-ashpd-devel.list

%changelog

%autochangelog
