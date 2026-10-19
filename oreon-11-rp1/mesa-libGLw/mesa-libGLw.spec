%global source0_hash 84671643a479182b35a77756af9042070950d4a05f96cbf073fa5848622083da
Summary:        Xt / Motif OpenGL widgets
Name: mesa-libGLw
Version: 8.0.0
Release:        1%{?dist}
License: SGI-OpenGL
URL: http://www.mesa3d.org
%global gitver b060a0782f09ebe4f60c8fd4564c11ba043c331f
Source0:        https://gitlab.freedesktop.org/mesa/glw/-/archive/b060a0782f09ebe4f60c8fd4564c11ba043c331f/glw-b060a0782f09ebe4f60c8fd4564c11ba043c331f.tar.bz2
Provides: libGLw
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libGL-devel
BuildRequires:  libXt-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  motif-devel
# /oreon:deps
%description
Mesa libGLw runtime library.

%package devel
Summary: Mesa libGLw development package
Requires: %{name} = %{version}-%{release}
Requires: libGL-devel
Requires: motif-devel
Provides: libGLw-devel
%description devel
Mesa libGLw development package.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n glw-%{gitver}

%build

autoreconf -f -i -v
%configure --disable-static --enable-motif
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name \*.la | xargs rm -f
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%ldconfig_post
%ldconfig_postun
%files -f %{oreon_filedir}/main.list
%files -n mesa-libGLw-devel -f %{oreon_filedir}/mesa-libGLw-devel.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 8.0.0-33
- Prepare for Oreon 11 (RP1)
