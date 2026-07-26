%global source0_hash 83f732d20781fc88b22cdc6aaf2d4f388db6d3d4ff28d1a8fd45be9fb7743a9e

Summary: Window Navigator Construction Kit
Name: libwnck
Version: 2.31.0
Release: 28%{?dist}
URL: http://download.gnome.org/sources/libwnck/
#VCS: git:git://git.gnome.org/libwnck
Source0: http://download.gnome.org/sources/libwnck/2.31/%{name}-%{version}.tar.xz
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+

Requires: startup-notification

BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires:  pango-devel
BuildRequires:  startup-notification-devel
BuildRequires:  libXt-devel
BuildRequires:  libXres-devel
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  gobject-introspection-devel
BuildRequires: make

%description
libwnck (pronounced "libwink") is used to implement pagers, tasklists,
and other such things. It allows applications to monitor information
about open windows, workspaces, their names/icons, and so forth.

%package devel
Summary: Libraries and headers for libwnck
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static --enable-introspection
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%find_lang %{name}

# This package is merely compat for gtk2 apps, now.
# The binaries are shipped in libwnck3
rm -f $RPM_BUILD_ROOT%{_bindir}/wnckprop
rm -f $RPM_BUILD_ROOT%{_bindir}/wnck-urgency-monitor

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS COPYING README NEWS
%{_libdir}/lib*.so.*
%{_libdir}/girepository-1.0/Wnck-1.0.typelib

%files devel
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gir-1.0/Wnck-1.0.gir
%doc %{_datadir}/gtk-doc

%changelog
%autochangelog
