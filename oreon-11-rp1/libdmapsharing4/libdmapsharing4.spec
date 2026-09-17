%global source0_hash 3659f63f29e11d6d6ae78b53d7cc6be3f3adeff9c00c67cc50ad19c6af699f7a

Name: libdmapsharing4
Version: 3.9.13
Release: 10%{?dist}
Summary: A DMAP client and server library

License: LGPL-2.1-or-later
URL: https://www.flyn.org/projects/libdmapsharing/
Source0: https://www.flyn.org/projects/libdmapsharing/libdmapsharing-%{version}.tar.gz

BuildRequires: pkgconfig, glib2-devel, libsoup3-devel
BuildRequires: gdk-pixbuf2-devel, gstreamer1-plugins-base-devel
BuildRequires: pkgconfig(avahi-client) pkgconfig(avahi-glib)
BuildRequires: vala libgee-devel
BuildRequires: make

%description 
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.

%package devel
Summary: Libraries/include files for libdmapsharing
Requires: %{name}%{?_isa} = %{version}-%{release}
# -vala subpackage removed in F30
Obsoletes: libdmapsharing4-vala < 3.9.3-3
Provides: libdmapsharing4-vala = %{version}-%{release}

%description devel
libdmapsharing implements the DMAP protocols. This includes support for
DAAP and DPAP.  This package provides the libraries, include files, and
other resources needed for developing applications using libdmapsharing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libdmapsharing-%{version}

%build
%configure --disable-static --disable-tests --disable-check
make %{?_smp_mflags}

%install
%make_install
rm -f $RPM_BUILD_ROOT%{_libdir}/libdmapsharing-4.0.la

%ldconfig_scriptlets

%files
%{_libdir}/libdmapsharing-4.0.so.*
%dir %{_libdir}/girepository-1.0/
%{_libdir}/girepository-1.0/Dmap-4.0.typelib

%doc AUTHORS ChangeLog README
%license COPYING

%files devel
%{_libdir}/pkgconfig/libdmapsharing-4.0.pc
%{_includedir}/libdmapsharing-4.0/
%{_libdir}/libdmapsharing-4.0.so
%{_datadir}/gtk-doc/html/libdmapsharing-4.0
%dir %{_datadir}/gir-1.0/
%{_datadir}/gir-1.0/Dmap-4.0.gir
%dir %{_datadir}/vala/
%dir %{_datadir}/vala/vapi/
%{_datadir}/vala/vapi/libdmapsharing-4.0.vapi

%changelog
%autochangelog
