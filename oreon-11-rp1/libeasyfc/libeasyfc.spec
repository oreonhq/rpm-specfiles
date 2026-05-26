Name:		libeasyfc
Version:	0.14.1
Release:	7%{?dist}
Summary:	Easy configuration generator interface for fontconfig

License:	LGPL-3.0-or-later
URL:		https://gitlab.com/tagoh/libeasyfc/
Source0:	https://bitbucket.org/tagoh/libeasyfc/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-freetype.patch
# oreon url source checksums begin
%global source0_sha256 87d4a5ddcfa74e4ace3a7333749d87ea25855de4a31a78a4f8e6212831432d31
%global source0_file libeasyfc-0.14.1.tar.bz2
# oreon url source checksums end

BuildRequires:	glib2-devel gobject-introspection-devel libxml2-devel fontconfig-devel >= 2.12.93 harfbuzz-devel
BuildRequires:	gettext
BuildRequires: make
Requires:	fontconfig >= 2.12.93

%description
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

%package	gobject
Summary:	GObject interface for libeasyfc
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description	gobject
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains an interface for GObject.

%package	devel
Summary:	Development files for libeasyfc
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Requires:	fontconfig-devel glib2-devel

%description	devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc.

%package	gobject-devel
Summary:	Development files for libeasyfc-gobject
Requires:	%{name}-gobject%{?_isa} = %{version}-%{release}
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}
Requires:	pkgconfig
Requires:	glib2-devel

%description	gobject-devel
libeasyfc aims to provide an easy interface to generate
fontconfig configuration on demand.

This package contains the development files to make any
applications with libeasyfc-gobject.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libeasyfc-0.14.1.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "87d4a5ddcfa74e4ace3a7333749d87ea25855de4a31a78a4f8e6212831432d31" || { echo "oreon: Source0 SHA256 mismatch for libeasyfc-0.14.1.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
%configure --disable-static
make %{?_smp_mflags} V=1


%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets
%ldconfig_scriptlets	gobject

%files
%doc README AUTHORS ChangeLog
%license COPYING
%{_libdir}/libeasyfc.so.*

%files	gobject
%{_libdir}/libeasyfc-gobject.so.*
%{_libdir}/girepository-*/Easyfc-*.typelib

%files	devel
%{_includedir}/libeasyfc
%exclude %{_includedir}/libeasyfc/ezfc-gobject.h
%{_libdir}/libeasyfc.so
%{_libdir}/pkgconfig/libeasyfc.pc
%{_datadir}/gtk-doc/html/libeasyfc

%files	gobject-devel
%{_includedir}/libeasyfc/ezfc-gobject.h
%{_libdir}/libeasyfc-gobject.so
%{_libdir}/pkgconfig/libeasyfc-gobject.pc
%{_datadir}/gir-*/Easyfc-*.gir

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.1-7
- Import
