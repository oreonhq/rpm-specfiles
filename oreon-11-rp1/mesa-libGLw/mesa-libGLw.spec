# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 84671643a479182b35a77756af9042070950d4a05f96cbf073fa5848622083da
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Summary: Xt / Motif OpenGL widgets
Name: mesa-libGLw
Version: 8.0.0
Release: 33%{?dist}
License: SGI-OpenGL
URL: http://www.mesa3d.org
# archived project
%global gitver b060a0782f09ebe4f60c8fd4564c11ba043c331f
Source0: https://gitlab.freedesktop.org/mesa/glw/-/archive/%{gitver}/glw-%{gitver}.tar.bz2

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
%oreon_verify_sources
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
