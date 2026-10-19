%global source0_hash 87d4a5ddcfa74e4ace3a7333749d87ea25855de4a31a78a4f8e6212831432d31
Name:		libeasyfc
Version:	0.14.1
Release:        7%{?dist}
Summary:        Easy configuration generator interface for fontconfig
License:	LGPL-3.0-or-later
URL:		https://gitlab.com/tagoh/libeasyfc/
Source0:        https://bitbucket.org/tagoh/libeasyfc/downloads/%{name}-%{version}.tar.bz2
Patch0:		%{name}-freetype.patch
Requires:	fontconfig >= 2.12.93
# oreon:deps
BuildRequires:  fontconfig-devel
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  harfbuzz-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libeasyfc-0.14.1
%oreon_prep
%build

%configure --disable-static
make %{?_smp_mflags} V=1
%install
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="/usr/bin/install -p"
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%ldconfig_scriptlets
%ldconfig_scriptlets	gobject
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libeasyfc-gobject -f %{oreon_filedir}/libeasyfc-gobject.list
%files -n libeasyfc-devel -f %{oreon_filedir}/libeasyfc-devel.list
%files -n libeasyfc-gobject-devel -f %{oreon_filedir}/libeasyfc-gobject-devel.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.14.1-7
- Import
