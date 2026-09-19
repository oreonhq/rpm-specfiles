%global source0_hash 64361e7647839d36ed8336d992fd210d3e8139882269bed47dc4674980165dec

Summary: The libglade library for loading user interfaces
Name: libglade2
Version: 2.6.4
Release: 37%{?dist}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Source: http://download.gnome.org/sources/libglade/2.6/libglade-%{version}.tar.bz2
URL: http://www.gnome.org

Requires: xml-common
BuildRequires: libxml2-devel 
BuildRequires: gtk2-devel 
BuildRequires: fontconfig
BuildRequires: pango-devel
BuildRequires: libtool
BuildRequires: gettext-devel
BuildRequires: make

# http://bugzilla.gnome.org/show_bug.cgi?id=121025
Patch1: libglade-2.0.1-nowarning.patch
# http://bugzilla.gnome.org/show_bug.cgi?id=510736
Patch2: libglade-secondary.patch

%description
Libglade is a small library that allows a program to load its user
interface from am XML description at runtime. Libglade uses the XML
file format used by the GLADE user interface builder GLADE, so
libglade acts as an alternative to GLADE's code generation
approach. Libglade also provides a simple interface for connecting
handlers to the various signals in the interface (on platforms where
the gmodule library works correctly, it is possible to connect all the
handlers with a single function call). Once the interface has been
instantiated, libglade gives no overhead, so other than the short
initial interface loading time, there is no performance tradeoff.

%package devel
Summary: The files needed for libglade application development
Requires: %{name} = %{version}-%{release}

%description devel
The libglade-devel package contains the libraries and include files
that you can use to develop libglade applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libglade-%{version}

%patch -P1 -p1 -b .nowarning
%patch -P2 -p1 -b .secondary

%build
%configure --disable-gtk-doc --disable-static
make %{?_smp_mflags}

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/libglade/2.0
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README
%{_libdir}/lib*.so.*
%dir %{_libdir}/libglade
%dir %{_libdir}/libglade/2.0
%{_datadir}/xml/libglade

%files devel
%doc test-libglade.c
# Python2 script, anything that needed/wanted to convert to Glade2 would have done so long ago
%exclude %{_bindir}/libglade-convert
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/gtk-doc/html/libglade

%changelog
%autochangelog
