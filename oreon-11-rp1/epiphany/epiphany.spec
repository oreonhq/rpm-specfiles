%global source0_hash c8f2748d7503ac95e98eb488d0787d23b48a51ae71fe9dd5bd2e86abe6ef02b8
%global glib2_version 2.74.0
%global gtk4_version 4.13.3
%global libadwaita_version 1.8~alpha
%global webkitgtk_version 2.43.4
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           epiphany
Epoch:          1
Version:        51.0
Release:        1%{?dist}
Summary:        Web browser for GNOME
License:        GPL-3.0-or-later AND CC-BY-SA-3.0 AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Web
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Patch0:         epiphany-default-bookmarks.patch
Requires: epiphany-runtime%{?_isa} = %{epoch}:%{version}-%{release}
# oreon:deps
BuildRequires:  /usr/bin/rst2man
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  libappstream-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gcr-4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtk4-unix-print)
BuildRequires:  pkgconfig(hogweed)
BuildRequires:  pkgconfig(iso-codes)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libarchive)
BuildRequires:  pkgconfig(libportal-gtk4)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  pkgconfig(webkitgtk-web-process-extension-6.0)
# /oreon:deps
%description
Epiphany is the web browser for the GNOME desktop. Its goal is to be
simple and easy to use. Epiphany ties together many GNOME components
in order to let you focus on the web content, instead of the browser
application.

%package runtime
Summary: Epiphany runtime suitable for web applications
Requires: gsettings-desktop-schemas
Requires: glib2%{?_isa} >= %{glib2_version}
Requires: gtk4%{?_isa} >= %{gtk4_version}
Requires: iso-codes
Requires: libadwaita%{?_isa} >= %{libadwaita_version}
Requires: webkitgtk6.0%{?_isa} >= %{webkitgtk_version}
Provides: bundled(gvdb)
Provides: bundled(highlightjs)
Provides: bundled(readabilityjs)
%description runtime
This package provides a runtime for web applications without actually
installing the epiphany application itself.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Epiphany.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n epiphany-runtime -f %{oreon_filedir}/epiphany-runtime.list

%changelog

%autochangelog
