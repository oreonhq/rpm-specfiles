%global source0_hash fd4089e2974a1a57f9ba209a0a47924ed157da9fc9a3d65f68a6b9fdca353ccc

Summary: A library for using real 3D models within a Clutter scene
Name: libmash
Version: 0.2.0
Release: 42%{?dist}
URL: http://clutter-project.github.com/mash/
Source0: https://github.com/downloads/clutter-project/mash/mash-%{version}.tar.xz

# Already sent upstream for review,
# see http://lists.clutter-project.org/pipermail/clutter-devel-list/2011-March/000196.html
Patch0:		0001-Use-the-system-version-of-rply-if-available.patch

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
BuildRequires: libtool
BuildRequires: glib2-devel >= 2.16
BuildRequires: clutter-devel
BuildRequires: gtk-doc
BuildRequires: rply-devel
BuildRequires: gobject-introspection-devel
BuildRequires: make

# Do not BR: mx-devel, as the lighting example isn't actually installed

%description
Mash is a small library for using real 3D models within a Clutter
scene. Models can be exported from Blender or other 3D modeling
software as PLY files and then used as actors. It also supports a
lighting model with animatable lights.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains libraries and header files needed for
development of programs using %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mash-%{version}
#%patch0 -p1 -b .use-system-rply

%build
autoconf

export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing"
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc README COPYING.LIB NEWS AUTHORS
%{_libdir}/libmash-0.2.so.*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%dir %{_includedir}/mash-0.2
%{_includedir}/mash-0.2/*
%{_libdir}/libmash-0.2.so
%{_libdir}/pkgconfig/mash-0.2.pc
%dir %{_datadir}/gtk-doc/html/mash
%{_datadir}/gtk-doc/html/mash/*
%{_datadir}/gir-1.0/*.gir
%dir %{_datadir}/gir-1.0

%changelog
%autochangelog
