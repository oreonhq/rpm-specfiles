%global source0_hash c68645cecef4a45840cd67c19a18a3a21ecae6b331e9864c2b745c31aee5fc85
%bcond_without tests
%global   dunst_confdir %{_sysconfdir}/xdg
Name:     dunst
Version:  1.13.2
Release:        1%{?dist}
Summary:        Lightweight and customizable notification-daemon
License:  BSD-3-Clause
URL:      https://dunst-project.org
Source0:        https://github.com/dunst-project/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Requires: dbus
Requires: /usr/bin/dbus-send
Recommends: /usr/bin/xdg-open
Recommends: jq
%if %{with tests}
%endif
Provides: desktop-notification-daemon
# oreon:deps
BuildRequires:  /usr/bin/pod2man
BuildRequires:  dbus-daemon
BuildRequires:  gcc
BuildRequires:  librsvg2
BuildRequires:  make
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(pangocairo)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
Dunst is a lightweight replacement for the notification daemons provided by
most desktop environments. It’s very customizable, isn’t dependent on any
toolkits, and therefore fits into those window manager centric setups we all
love to customize to perfection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%global make_options %{shrink:
    PREFIX=%{_prefix}
    SYSCONFDIR=%{dunst_confdir}
    SYSTEMD=1
    VERSION=%{version}
}
%set_build_flags
%make_build %{make_options} wayland-protocols
%make_build %{make_options}
%install
%make_install %{make_options}
install -d -m 0755 -pv %{buildroot}%{dunst_confdir}/%{name}/dunstrc.d
%oreon_autofiles main
%if %{with tests}
%check

%make_build test %{make_options}
%endif
%post

%systemd_user_post %{name}.service
%preun

%systemd_user_preun %{name}.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
