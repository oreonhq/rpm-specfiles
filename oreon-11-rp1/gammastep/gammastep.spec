%global source0_hash e16026b8f21d5e02cfe7cd2f738c80f150c1f06a098e5e47e0fc088244a763bd
Name:           gammastep
Version:        2.0.11
Release:        1%{?dist}
Summary:        Adjusts the color temperature of your screen according to time of day
License:        GPL-3.0-or-later AND HPND-sell-variant
URL:            https://gitlab.com/chinstrap/gammastep
Source0:        https://gitlab.com/chinstrap/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Gammastep adjusts the color temperature of your screen according to your
surroundings. This may help your eyes hurt less if you are working in front
of the screen at night.

The color temperature is set according to the position of the sun. A different
color temperature is set during night and daytime. During twilight and early
morning, the color temperature transitions smoothly from night to daytime
temperature to allow your eyes to slowly adapt.

Gammastep supports wlr-gamma-control-unstable-v1 protocol for wlroots-based
wayland compositors.

%package        indicator
Summary:        GTK indicator applet for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       gtk3
Requires:       libappindicator-gtk3
Requires:       python3dist(pygobject)
Requires:       python3dist(pyxdg)
%description    indicator
This package provides a status icon for %{name} that allows the user
to control color temperature.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-v%{version}
%oreon_prep
%build

./bootstrap
%configure \
    --with-systemduserunitdir=%{_userunitdir}
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%post

%systemd_user_post %{name}.service
%post indicator

%systemd_user_post %{name}-indicator.service
%preun

%systemd_user_preun %{name}.service
%preun indicator

%systemd_user_preun %{name}-indicator.service
%files -f %{oreon_filedir}/main.list
%files -n gammastep-indicator -f %{oreon_filedir}/gammastep-indicator.list

%changelog

%autochangelog
