%global source0_hash 5515b2610361ef34580b6b976635119f6dedb4f0a79d54662fa5fe6186a45ed5
Summary:        Decode camera RAW files
Name:		libopenraw
Version:	0.3.7
Release:        1%{?dist}
License:	LGPL-3.0-or-later
URL:		http://libopenraw.freedesktop.org/wiki
Source0:        http://libopenraw.freedesktop.org/download/%{name}-%{version}.tar.bz2
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cargo
BuildRequires:  gcc-c++
BuildRequires:  libjpeg-devel
BuildRequires:  make
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libxml-2.0)
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup
# this may be installed into a different prefix than gdk-pixbuf2 (e.g. flatpaks)
sed -i -e '/gdk_pixbuf_moduledir/s/PKG_CONFIG/& --define-variable=prefix=${prefix}/' configure

%build

%configure --disable-static --enable-gnome --disable-silent-rules
sed --in-place --expression 's! -shared ! -Wl,--as-needed\0!g' libtool
%{make_build}
%check

make check
%install
%make_install
find $RPM_BUILD_ROOT -type f -name "*.la" -delete
%ldconfig_scriptlets
%ldconfig_scriptlets gnome
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.*

%files -f %{oreon_filedir}/main.list
%files -n libopenraw-gnome -f %{oreon_filedir}/libopenraw-gnome.list
%files -n libopenraw-devel -f %{oreon_filedir}/libopenraw-devel.list
%files -n libopenraw-gnome-devel -f %{oreon_filedir}/libopenraw-gnome-devel.list
%files -n libopenraw-pixbuf-loader -f %{oreon_filedir}/libopenraw-pixbuf-loader.list

%changelog

%autochangelog
