Summary: Xt / Motif OpenGL widgets
Name: mesa-libGLw
Version: 8.0.0
Release: 33%{?dist}
License: SGI-OpenGL
URL: http://www.mesa3d.org
# archived project
%global gitver b060a0782f09ebe4f60c8fd4564c11ba043c331f
Source0: https://gitlab.freedesktop.org/mesa/glw/-/archive/%{gitver}/glw-%{gitver}.tar.bz2
# oreon url source checksums begin
%global source0_sha256 84671643a479182b35a77756af9042070950d4a05f96cbf073fa5848622083da
%global source0_file glw-b060a0782f09ebe4f60c8fd4564c11ba043c331f.tar.bz2
# oreon url source checksums end

BuildRequires: make
BuildRequires: autoconf automake libtool
BuildRequires: gcc
BuildRequires: libXt-devel
BuildRequires: libGL-devel
%if 0%{?rhel}
BuildRequires: openmotif-devel
%else
BuildRequires: motif-devel
%endif

Provides: libGLw

%description
Mesa libGLw runtime library.

%package devel
Summary: Mesa libGLw development package
Requires: %{name} = %{version}-%{release}
Requires: libGL-devel
%if 0%{?rhel}
Requires: openmotif-devel
%else
Requires: motif-devel
%endif
Provides: libGLw-devel

%description devel
Mesa libGLw development package.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/glw-b060a0782f09ebe4f60c8fd4564c11ba043c331f.tar.bz2; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "84671643a479182b35a77756af9042070950d4a05f96cbf073fa5848622083da" || { echo "oreon: Source0 SHA256 mismatch for glw-b060a0782f09ebe4f60c8fd4564c11ba043c331f.tar.bz2" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n glw-%{gitver}

%build
autoreconf -f -i -v
%configure --disable-static --enable-motif
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%check

%ldconfig_post
%ldconfig_postun

%files
%doc README
%{_libdir}/libGLw.so.1
%{_libdir}/libGLw.so.1.0.0

%files devel
%{_libdir}/libGLw.so
%{_libdir}/pkgconfig/glw.pc
%{_includedir}/GL/GLwDrawA.h
%{_includedir}/GL/GLwDrawAP.h
%{_includedir}/GL/GLwMDrawA.h
%{_includedir}/GL/GLwMDrawAP.h

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.0.0-33
- Prepare for Oreon 11 (RP1)
