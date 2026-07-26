%global source0_hash f5b00c302955a67fa5fb1f2d3f2583767cdc61fdbc6fd843c0c7c9d95c5629e3

Name:           lib3ds
Version:        1.3.0
Release:        47%{?dist}

Summary:        3D Studio file format library

License:        LGPL-2.1-or-later
URL:            http://lib3ds.sourceforge.net
Source:         http://downloads.sourceforge.net/lib3ds/lib3ds-%{version}.zip
# Extracted from Debian's lib3ds_1.3.0-1.diff.gz
Patch0:         lib3ds-1.3.0-lib3ds-file.h.diff
# Address https://bugzilla.redhat.com/show_bug.cgi?id=633475
Patch1:         lib3ds-1.3.0-lib3ds-mesh.c.diff

Patch2:         lib3ds-1.2.0-pkgconfig.diff

BuildRequires:  gcc
BuildRequires: make
# RHBZ 1987639: rpm corrupts older libtool sources
BuildRequires: autoconf automake libtool

%description
lib3ds is a free ANSI-C library for working with the popular "3ds" 3D model
format.

Supported platforms include GNU (autoconf, automake, libtool, make, GCC) on
Unix and Cygwin, and MS Visual C++ 6.0. lib3ds loads and saves Atmosphere
settings, Background settings, Shadow map settings, Viewport setting,
Materials, Cameras, Lights, Meshes, Hierarchy, Animation keyframes. It also
contains useful matrix, vector and quaternion mathematics tools. lib3ds
usually integrates well with OpenGL. In addition, some diagnostic and
conversion tools are included.

%package        tools
Summary:        %summary

%description    tools
Some tools to process 3ds files.

%files          tools
%doc AUTHORS ChangeLog README
%license COPYING
%{_bindir}/3dsdump
%{_mandir}/man1/3dsdump.1*

%package        devel
Summary:        %summary
Requires:	pkgconfig
Requires:	lib3ds = %{version}-%{release}

%description    devel
Development files for lib3ds

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1

autoreconf -fi

%build
%configure  --disable-static

%{make_build}

sed -e 's,@prefix@,%{_prefix},' \
  -e 's,@exec_prefix@,%{_exec_prefix},' \
  -e 's,@libdir@,%{_libdir},' \
  -e 's,@includedir@,%{_includedir},' \
  -e 's,@VERSION@,%{version},' \
  lib3ds.pc.in > lib3ds.pc

%install
%{make_install}

install -d ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig
install lib3ds.pc -m 0644 ${RPM_BUILD_ROOT}%{_libdir}/pkgconfig

## Remove libtool archive
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la

%files
%doc AUTHORS ChangeLog README
%license COPYING
%{_libdir}/*.so.*

%ldconfig_scriptlets

%files devel
%{_bindir}/lib3ds-config
%{_libdir}/*.so
%{_libdir}/pkgconfig/lib3ds.pc
%{_mandir}/man1/lib3ds-config.1*
%{_includedir}/lib3ds
%{_datadir}/aclocal/*

%changelog
%autochangelog
