%global source0_hash aaa23e7042477e741f24279b468b9d20af4ec195ee43b3d312cdaaf84d98c321
%bcond_with compiz_session
Name:           gnome-flashback
Version:        3.58.0
Release:        1%{?dist}
Summary:        GNOME Flashback session
License:        GPL-3.0-or-later
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        https://download.gnome.org/sources/%{name}/3.58/%{name}-%{version}.tar.xz
%ifnarch s390x
%endif
%if %{with compiz_session}
%endif
Requires:       gnome-applets%{?_isa}
Requires:       gnome-keyring%{?_isa}
Requires:       gnome-panel%{?_isa}
Requires:       gnome-session%{?_isa}
Requires:       gnome-settings-daemon%{?_isa}
Requires:       metacity%{?_isa}
Requires:       tecla%{?_isa}
Recommends:     alacarte
Recommends:     geoclue2%{?_isa}
Recommends:     nautilus%{?_isa}
Recommends:     network-manager-applet%{?_isa}
Recommends:     gnome-power-manager
%if %{with compiz_session}
Suggests:       compiz%{?_isa}
%endif
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-bluetooth-3.0)
BuildRequires:  pkgconfig(gnome-desktop-3.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libgnome-panel)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-agent-1)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
GNOME Flashback is a session for GNOME 3 which was initially called "GNOME
Fallback", and shipped as a stand-alone session in Debian and Ubuntu. It
provides a similar user experience to the GNOME 2.x series sessions. The
differences to the MATE project is that GNOME Flashback uses GTK+ 3 and tries to
follow the current GNOME development by integrating recent changes of the GNOME
libraries. The development currently lags behind a little but a lot of progress
has been made and most importantly many open bugs have been fixed.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
NOCONFIGURE=1 gnome-autogen.sh

%build

%if %{with compiz_session}
%configure --with-compiz-session
%else
%configure
%endif
%make_build
%install
%make_install
%find_lang %{name}
install -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/pam.d/%{name}
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
