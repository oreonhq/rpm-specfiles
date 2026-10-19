%global source0_hash 2161780656db3a7704ac56ac4333cc961ae7e54d4b4d6ffe3bf29f4eb1a7d358
%global __provides_exclude_from ^%{_libdir}/gala/.*\\.so$
%global commit      4b15f84af7e1973d9e6596bb381810113ddee948
%global shortcommit %{sub %{commit} 1 7}
%global gitdate     20260325
Name:           gala
Version:        8.4.1^%{gitdate}.git%{shortcommit}
Release:        1%{?dist}
Summary:        Gala window manager
License:        GPL-3.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/elementary/gala
Source0:        https://github.com/elementary/%{name}/archive/%{commit}/%{name}-4b15f84.tar.gz
Requires:       dbus
Requires:       elementary-notifications
Provides:       firstboot(windowmanager) = gala
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(atk-bridge-2.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(granite-7)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libcanberra)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(xext)
BuildRequires:  systemd-rpm-macros
BuildRequires:  vala
BuildRequires:  wayland-devel
# /oreon:deps
%description
Gala is Pantheon's Window Manager, part of the elementary project.

%package        x11
Summary:        Gala window manager X11 support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gnome-session
Requires:       xorg-x11-server-Xorg
%description    x11
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the support files for running gala on X11.

%package        wayland
Summary:        Gala window manager Wayland support
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gnome-session
Requires:       xorg-x11-server-Xwayland
%description    wayland
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the support files for running gala on Wayland.

%package        devel
Summary:        Gala window manager development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Gala is Pantheon's Window Manager, part of the elementary project.

This package contains the development headers.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n gala-%{commit} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang gala
sed -i '/icon type="stock"/d' %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml
rm %{buildroot}/%{_sysconfdir}/xdg/io.elementary.desktop.wm.shell
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate \
    %{buildroot}/%{_datadir}/applications/gala*.desktop
appstream-util validate-relax --nonet \
    %{buildroot}/%{_datadir}/metainfo/%{name}.metainfo.xml
%post x11

%systemd_user_post io.elementary.gala@x11.service
%post wayland

%systemd_user_post io.elementary.gala@wayland.service
%preun x11

%systemd_user_preun io.elementary.gala@x11.service
%preun wayland

%systemd_user_preun io.elementary.gala@wayland.service
%postun x11

%systemd_user_postun io.elementary.gala@x11.service
%postun wayland

%systemd_user_postun io.elementary.gala@wayland.service
%files -f %{oreon_filedir}/main.list
%files -n gala-x11 -f %{oreon_filedir}/gala-x11.list
%files -n gala-wayland -f %{oreon_filedir}/gala-wayland.list
%files -n gala-devel -f %{oreon_filedir}/gala-devel.list

%changelog

%autochangelog
