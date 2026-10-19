%global source2_hash 3aaadfd1d5dd8719b3a6a1c2012db43a89d9f89b676d88b581dbdb6b09c6f098
%global source1_hash 4565c5e31c894a21492c10ba8b32e1dcb69e171c9adbd112304e17ebaabfdcb0
%global source0_hash 25e9332da735a3e0c0fe05673d5ce62e35b87780a3e5fa770075bed6bd4d0b1b
%global gvc_commit d2442f455844e5292cb4a74ffc66ecc8d7595a9f
%global libcall_ui_version v0.1.5
Name:     phosh
Version:  0.57.0
Release:        1%{?dist}
Summary:        Graphical shell for mobile devices
License:  GPL-3.0-or-later
URL:      https://gitlab.gnome.org/World/Phosh/phosh
Source0:        https://gitlab.gnome.org/World/Phosh/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:  https://gitlab.gnome.org/GNOME/libgnome-volume-control/-/archive/%{gvc_commit}/libgnome-volume-control-%{gvc_commit}.tar.gz
Source2:  https://gitlab.gnome.org/World/Phosh/libcall-ui/-/archive/%{libcall_ui_version}/libcall-ui-%{libcall_ui_version}.tar.gz
Source3:  phosh
ExcludeArch:  %{ix86}
ExcludeArch:  ppc64le
Requires:  gnome-session >= 49.0
Requires:  gnome-settings-daemon >= 49.0
Requires:  gnome-shell-common >= 49.0
Requires:  hicolor-icon-theme
Requires:  lato-fonts
Requires:  mutter-common
Requires:  phoc >= 0.52.0
Requires:  phosh-osk = 1.0
Requires:  xorg-x11-server-Xwayland
Recommends:  gnome-control-center
Recommends:  phosh-mobile-settings
Suggests:    stevia-phosh-osk-provider
# oreon:deps
BuildRequires:  /usr/bin/xauth
BuildRequires:  /usr/bin/xvfb-run
BuildRequires:  dbus-daemon
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(evince-document-3.0)
BuildRequires:  pkgconfig(evince-view-3.0)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gcr-3)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmobile)
BuildRequires:  pkgconfig(gnome-bluetooth-3.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk+-wayland-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libcallaudio-0.1)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libfeedback-0.0)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(mm-glib)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(qrcodegen)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  systemd-rpm-macros
BuildRequires:  xmlstarlet
# /oreon:deps
%description
Phosh is a simple shell for Wayland compositors speaking the layer-surface
protocol. It currently supports

* a lockscreen
* brightness control and nightlight
* the GCR system-prompter interface
* acting as a polkit auth agent
* enough of org.gnome.Mutter.DisplayConfig to make gnome-settings-daemon happy
* a homebutton that toggles a simple favorites menu
* status icons for battery, wwan and wifi

%package devel
Summary:   Development headers for Phosh
Requires:  %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description devel
Development headers for Phosh.

%package -n libphosh
Summary:    Experimental library of Phosh components and functionality.
Requires:   %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libphosh
Experimental shared library of Phosh components and functionality, allowing
other projects to embed Phosh.

%package -n libphosh-devel
Summary:    Development headers for libphosh.
Requires:   lib%{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
%description -n libphosh-devel
Development headers for libphosh.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -a1 -a2 -q -n %{name}-v%{version_no_tilde _}

mv libgnome-volume-control-%{gvc_commit} subprojects/gvc
mv libcall-ui-%{libcall_ui_version} subprojects/libcall-ui

%build

%meson -Dphoc_tests=disabled -Dbindings-lib=true -Dsearchd=true
%meson_build
%install
install -d %{buildroot}%{_sysconfdir}/pam.d/
cp %{SOURCE3} %{buildroot}%{_sysconfdir}/pam.d/
%meson_install
%find_lang %{name}
%{__install} -Dpm 0644 data/phosh.service %{buildroot}%{_unitdir}/phosh.service
rm %{buildroot}%{_libdir}/libphosh-0.45.a
%oreon_autofiles libphosh usr/*/lib*.so.*
%oreon_autofiles libphosh-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
%{buildroot}%{_datadir}/applications/mobi.phosh.Shell.desktop
%{shrink:LC_ALL=C.UTF-8 xvfb-run %meson_test}
%files -f %{oreon_filedir}/main.list
%files -n phosh-devel -f %{oreon_filedir}/phosh-devel.list
%files -n libphosh -f %{oreon_filedir}/libphosh.list
%files -n libphosh-devel -f %{oreon_filedir}/libphosh-devel.list

%changelog

%autochangelog
