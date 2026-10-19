%global source0_hash 22a1b61fccf9e4da9f925452984e458d85b34323f4399125cd36854f5eb66cc4
%global nm_version 1.2
%global nma_version 1.0
%global glib_required_version 2.64
%global gtk_required_version 4.17
%global geoclue_version 2.6.0
%global gnome_desktop_version 44.0-7
%global tarball_version %(echo %{version} | tr '~' '.')
%bcond_without webkitgtk
Name:           gnome-initial-setup
Version:        51.0
Release:        1%{?dist}
Summary:        Bootstrapping your OS
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Design/OS/InitialSetup
Source0:        https://download.gnome.org/sources/%{name}/51/%{name}-%{version}.tar.xz
%if %{with webkitgtk}
%endif
Requires: gdm
Requires: geoclue2-libs%{?_isa} >= %{geoclue_version}
Requires: glib2%{?_isa} >= %{glib_required_version}
Requires: gnome-desktop4%{?_isa} >= %{gnome_desktop_version}
Requires: polkit-js-engine
Requires: /usr/bin/tecla
Requires(pre): shadow-utils
Provides: user(%name)
ExcludeArch: %{ix86}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(accountsservice)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(geocode-glib-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnome-desktop-4)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gweather4)
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(krb5)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libgeoclue-2.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  pkgconfig(libnma-gtk4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(pango)
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(pwquality)
BuildRequires:  pkgconfig(rest-1.0)
BuildRequires:  pkgconfig(webkitgtk-6.0)
# /oreon:deps
%description
GNOME Initial Setup is an alternative to firstboot, providing
a good setup experience to welcome you to your system, and walks
you through configuring it. It is integrated with gdm.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson \
  -Dparental_controls=disabled \
%if !%{with webkitgtk}
  -Dwebkitgtk=disabled \
%endif
  %{nil}
%meson_build
%install
%meson_install
mkdir -p %{buildroot}%{_datadir}/gnome-initial-setup
%find_lang %{name}
%oreon_autofiles main

%pre

useradd -rM -d /run/gnome-initial-setup/ -s /sbin/nologin %{name} &>/dev/null || :
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 50~rc-1
- Prepare for Oreon 11 (RP1)
