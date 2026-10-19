%global source0_hash 9380117f1811ad1faa1812cb6602479b6290d4a0d8cc442d44427f7f6c0e7a58
%{?mingw_package_header}
Name:           mingw-spice-gtk
Version:        0.42
Release:        1%{?dist}
Summary:        A GTK+ widget for SPICE clients
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://spice-space.org/page/Spice-Gtk
Source0:        http://www.spice-space.org/download/gtk/spice-gtk-%{version}.tar.xz
Patch0001:     0001-usb-backend-Fix-compiling-with-i686-clang-in-mingw.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  glib2-devel
BuildRequires:  gnupg2
BuildRequires:  gobject-introspection-devel
BuildRequires:  meson
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw32-gstreamer1-plugins-base
BuildRequires:  mingw32-gtk3
BuildRequires:  mingw32-json-glib
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-opus
BuildRequires:  mingw32-pixman
BuildRequires:  mingw32-spice-protocol
BuildRequires:  mingw32-usbredir
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw64-gstreamer1-plugins-base
BuildRequires:  mingw64-gtk3
BuildRequires:  mingw64-json-glib
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-opus
BuildRequires:  mingw64-pixman
BuildRequires:  mingw64-spice-protocol
BuildRequires:  mingw64-usbredir
BuildRequires:  mingw64-zlib
BuildRequires:  python3-pyparsing
BuildRequires:  python3-six
# /oreon:deps
%description
Client libraries for SPICE desktop servers.

# Mingw32
%package -n mingw32-spice-gtk3
Summary:        A GTK+ widget for SPICE clients
Requires: mingw32-spice-glib = %{version}-%{release}
Requires: mingw32-gtk3
Requires: pkgconfig
Obsoletes: mingw32-spice-gtk < 0.32
Obsoletes: mingw32-spice-gtk-static < 0.32-2
%description -n mingw32-spice-gtk3
Gtk+3 client libraries for SPICE desktop servers.

%package -n mingw32-spice-glib
Summary: GLib-based library to connect to SPICE servers
Requires: pkgconfig
Requires: mingw32-glib2
Requires: mingw32-spice-protocol
%description -n mingw32-spice-glib
A SPICE client library using GLib2.

# Mingw64
%package -n mingw64-spice-gtk3
Summary:        GLib-based library to connect to SPICE servers
Requires: mingw64-spice-glib = %{version}-%{release}
Requires: mingw64-gtk3
Requires: pkgconfig
Obsoletes: mingw64-spice-gtk < 0.32
Obsoletes: mingw64-spice-gtk-static < 0.32-2
%description -n mingw64-spice-gtk3
Gtk+3 client libraries for SPICE desktop servers.

%package -n mingw64-spice-glib
Summary: GLib-based library to connect to SPICE servers
Requires: pkgconfig
Requires: mingw64-glib2
Requires: mingw64-spice-protocol
%description -n mingw64-spice-glib
A SPICE client library using GLib2.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

#gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am -n spice-gtk-%{version}%{?_version_suffix}

%build

%global mjpegflag -Dbuiltin-mjpeg=false
%mingw_meson \
  %{mjpegflag} \
  -Dgtk_doc=disabled \
  -Dintrospection=disabled
%mingw_ninja
%install
export DESTDIR=%{buildroot}
%mingw_ninja install
find $RPM_BUILD_ROOT -name "*.1" -delete
%mingw_find_lang spice-gtk --all-name
%oreon_autofiles mingw32-spice-gtk3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-spice-glib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-spice-gtk3 usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-spice-glib usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-spice-gtk3 -f %{oreon_filedir}/mingw32-spice-gtk3.list
%files -n mingw32-spice-glib -f %{oreon_filedir}/mingw32-spice-glib.list
%files -n mingw64-spice-gtk3 -f %{oreon_filedir}/mingw64-spice-gtk3.list
%files -n mingw64-spice-glib -f %{oreon_filedir}/mingw64-spice-glib.list

%changelog

%autochangelog
