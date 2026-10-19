%global source0_hash d326ec69fc004be3a5fc048f7ecf2c8eb828b7d8b682f1e7a2ba01a5e72993e1
%define url_ver %(echo %{version}|cut -d. -f1)
%global tarball_version %(echo %{version} | tr '~' '.')
%global __provides_exclude_from ^%{_libdir}/%{name}/.*\\.so.*$
Name:           sushi
Version:        51.1
Release:        1%{?dist}
Summary:        A quick previewer for Nautilus
License:        GPL-2.0-or-later WITH GStreamer-exception-2008 AND CC0-1.0 AND (LGPL-2.0-or-later AND LGPL-2.1-or-later WITH GStreamer-exception-2005)
URL:            https://gitlab.gnome.org/GNOME/sushi
Source0:        https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
Obsoletes:      sushi-devel < 0.5.1
Requires: gtksourceview4
Recommends: webkit2gtk4.1
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gjs-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(evince-document-3.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtksourceview-4)
# /oreon:deps
%description
This is sushi, a quick previewer for Nautilus, the GNOME desktop
file manager.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# check for human errors
if [ `echo "%{version}" | grep -cE "\.alpha|\.beta|\.rc"` = "1" ]; then echo "Error: Use tilde in Version field in front of alpha/beta/rc; checked '%{version}'" 1>&2; exit 1; fi

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
