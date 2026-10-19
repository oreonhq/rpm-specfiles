%global source0_hash 16bd736074f6b14180f206b7e91263fc721b49912ea3258ab5f094cfa5497f51
%define api_version		1.0
Summary:        OpenGL Extension to GTK
Name:		gtkglext
Version:	1.2.0
Release:        1%{?dist}
License:	GPL-2.0-or-later OR LGPL-2.0-or-later
URL:		http://gtkglext.sourceforge.net/
Source0:        https://download.gnome.org/sources/gtkglext/1.2/gtkglext-%{version}.tar.bz2
Patch0:		0001-gtkglext-1.2.0-bz677457.patch
Patch1:		0002-GCC-8-fixes.patch
Patch2:		gtkglext-1.2.0-no-pangox.patch
Patch3:		gtkglext-1.2.0-fedora-c99.patch
Requires(postun):	/sbin/ldconfig
Requires(post):		/sbin/ldconfig
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gtk2-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  make
# /oreon:deps
%description
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package libs
Summary:	OpenGL Extension to GTK
License:	LGPL-2.0-or-later
%description libs
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package devel
Summary:	Development tools for GTK-based OpenGL applications
License:	LGPL-2.0-or-later
Requires:	%{name}-libs%{?_isa} = %{version}-%{release}
Requires:	gtk2-devel
Requires:	libGL-devel
Requires:	libGLU-devel
Requires:	libXmu-devel
%description devel
The gtkglext-devel package contains the header files, static libraries,
and developer docs for GtkGLExt.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n gtkglext-%{version}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1 -b .nopangox
%patch -P3 -p1

%build

%configure --disable-gtk-doc --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}
%install
%{make_install}
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gtkglext-libs -f %{oreon_filedir}/gtkglext-libs.list
%files -n gtkglext-devel -f %{oreon_filedir}/gtkglext-devel.list

%changelog

%autochangelog
