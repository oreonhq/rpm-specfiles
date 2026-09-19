%global source0_hash 9380117f1811ad1faa1812cb6602479b6290d4a0d8cc442d44427f7f6c0e7a58

%{?mingw_package_header}

Name:           mingw-spice-gtk
Version:        0.42
Release:        10%{?dist}
Summary:        A GTK+ widget for SPICE clients

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://spice-space.org/page/Spice-Gtk
Source0:        http://www.spice-space.org/download/gtk/spice-gtk-%{version}%{?_version_suffix}.tar.xz
#Source1:        http://www.spice-space.org/download/gtk/spice-gtk-%{version}%{?_version_suffix}.tar.xz.sig
#Source2:        victortoso-E37A484F.keyring

Patch0001:     0001-usb-backend-Fix-compiling-with-i686-clang-in-mingw.patch

BuildArch: noarch

BuildRequires: mingw32-filesystem >= 104
BuildRequires: mingw64-filesystem >= 104
BuildRequires: mingw32-gcc
BuildRequires: mingw64-gcc
BuildRequires: mingw32-binutils
BuildRequires: mingw64-binutils
BuildRequires: glib2-devel

BuildRequires: mingw32-gtk3 >= 3.22
BuildRequires: mingw64-gtk3 >= 3.22
BuildRequires: mingw32-pixman
BuildRequires: mingw64-pixman
BuildRequires: mingw32-openssl
BuildRequires: mingw64-openssl
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw32-zlib
BuildRequires: mingw64-zlib
BuildRequires: mingw32-gstreamer1
BuildRequires: mingw64-gstreamer1
BuildRequires: mingw32-gstreamer1-plugins-base
BuildRequires: mingw64-gstreamer1-plugins-base
BuildRequires: mingw32-opus
BuildRequires: mingw64-opus
BuildRequires: mingw32-spice-protocol >= 0.12.15
BuildRequires: mingw64-spice-protocol >= 0.12.15
BuildRequires: mingw32-libusbx >= 1.0.21
BuildRequires: mingw64-libusbx >= 1.0.21
BuildRequires: mingw32-usbredir >= 0.5
BuildRequires: mingw64-usbredir >= 0.5
BuildRequires: mingw32-json-glib
BuildRequires: mingw64-json-glib

BuildRequires: meson
BuildRequires: gcc
BuildRequires: git
BuildRequires: gettext
BuildRequires: python3-six
BuildRequires: python3-pyparsing
BuildRequires: gnupg2
# FIXME: shouldn't be necessary
BuildRequires: gobject-introspection-devel

%description
Client libraries for SPICE desktop servers.

# Mingw32
%package -n mingw32-spice-gtk3
Summary: %{summary}
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
Summary: %{summary}
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

# meson macro has --auto-features=enabled
# gstreamer should be enough, may be deprecated in the future
%global mjpegflag -Dbuiltin-mjpeg=false

%mingw_meson \
  %{mjpegflag} \
  -Dgtk_doc=disabled \
  -Dintrospection=disabled

%mingw_ninja

%install
export DESTDIR=%{buildroot}
%mingw_ninja install

# man pages don't need to be bundled
find $RPM_BUILD_ROOT -name "*.1" -delete

%mingw_find_lang spice-gtk --all-name

# Mingw32
%files -n mingw32-spice-glib -f mingw32-spice-gtk.lang
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{mingw32_bindir}/libspice-client-glib-2.0-8.dll
%{mingw32_bindir}/spicy-screenshot.exe
%{mingw32_bindir}/spicy-stats.exe
%{mingw32_libdir}/libspice-client-glib-2.0.dll.a
%{mingw32_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{mingw32_includedir}/spice-client-glib-2.0

%files -n mingw32-spice-gtk3
%{mingw32_bindir}/libspice-client-gtk-3.0-5.dll
%{mingw32_bindir}/spicy.exe
%{mingw32_libdir}/libspice-client-gtk-3.0.dll.a
%{mingw32_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{mingw32_includedir}/spice-client-gtk-3.0

# Mingw64
%files -n mingw64-spice-glib -f mingw64-spice-gtk.lang
%doc AUTHORS
%doc COPYING
%doc README.md
%doc CHANGELOG.md
%{mingw64_bindir}/libspice-client-glib-2.0-8.dll
%{mingw64_bindir}/spicy-screenshot.exe
%{mingw64_bindir}/spicy-stats.exe
%{mingw64_libdir}/libspice-client-glib-2.0.dll.a
%{mingw64_libdir}/pkgconfig/spice-client-glib-2.0.pc
%{mingw64_includedir}/spice-client-glib-2.0

%files -n mingw64-spice-gtk3
%{mingw64_bindir}/libspice-client-gtk-3.0-5.dll
%{mingw64_bindir}/spicy.exe
%{mingw64_libdir}/libspice-client-gtk-3.0.dll.a
%{mingw64_libdir}/pkgconfig/spice-client-gtk-3.0.pc
%{mingw64_includedir}/spice-client-gtk-3.0

%changelog
%autochangelog
