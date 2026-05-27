%global source0_hash 6405634f555849eb01cb028e2a63936e7b841151ea2a1571ac5b5b10431cfab9

Summary:	Decode camera RAW files
Name:		libopenraw
Version:	0.1.3
Release:	21%{?dist}
License:	LGPL-3.0-or-later
URL:		http://libopenraw.freedesktop.org/wiki
Source0:	http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2

BuildRequires:  boost-devel
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.5.0
BuildRequires: make

%description
libopenraw is an ongoing project to provide a free software
implementation for camera RAW files decoding. One of the main reason is
that dcraw is not suited for easy integration into applications, and
there is a need for an easy to use API to build free software digital
image processing application.

%package gnome
Summary:	GUI components of %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description gnome 
The %{name}-gnome package contains gui components of %{name}.

%package devel
Summary:	Development files for %{name}
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package gnome-devel
Summary:	Development files for %{name}-gnome
Requires:	%{name}-gnome%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description    gnome-devel
The %{name}-gnome-devel package contains libraries and header files for
developing applications that use %{name}-gnome.

%package pixbuf-loader
Summary:	RAW image loader for GTK+ applications
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description pixbuf-loader
%{name}-pixbuf-loader contains a plugin to load RAW images, as created by
digital cameras, in GTK+ applications.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup
# this may be installed into a different prefix than gdk-pixbuf2 (e.g. flatpaks)
sed -i -e '/gdk_pixbuf_moduledir/s/PKG_CONFIG/& --define-variable=prefix=${prefix}/' configure

%build
%configure --disable-static --enable-gnome --disable-silent-rules

# Omit unused direct shared library dependencies.
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool

%{make_build}

%check
make check

%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%ldconfig_scriptlets

%ldconfig_scriptlets gnome


%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/%{name}.so.*

%files gnome
%{_libdir}/%{name}gnome.so.*

%files devel
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}-0.1.pc

%dir %{_includedir}/%{name}-0.1
%{_includedir}/%{name}-0.1/%{name}/*.h

%files gnome-devel
%{_libdir}/%{name}gnome.so
%{_libdir}/pkgconfig/%{name}-gnome-0.1.pc

%dir %{_includedir}/%{name}-0.1/%{name}-gnome
%{_includedir}/%{name}-0.1/%{name}-gnome/gdkpixbuf.h

%files pixbuf-loader
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.3-21
- Prepare for Oreon 11 (RP1)
