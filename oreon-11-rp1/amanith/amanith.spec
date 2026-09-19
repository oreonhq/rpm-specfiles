%global source0_hash 2e92dde6e56abef0f5146fd61ad0310e176d25578673353afe4def99c6bdaa1a

Name:          amanith
Version:       0.3
Release:       60%{?dist}
Summary:       Crossplatform framework for 2d/3d vector graphics
# Automatically converted from old format: QPL - review is highly recommended.
License:       QPL-1.0
URL:           http://www.amanith.org
# Upstream no longer offers this code
# It originally came from: http://www.amanith.org/download/files/amanith_03.tar.gz
Source0:       amanith_03.tar.gz
BuildRequires:  gcc-c++
BuildRequires: qt3-devel, freetype-devel, libjpeg-devel, libpng-devel, zlib-devel
BuildRequires: libXmu-devel, glew-devel, mesa-libGLU-devel
BuildRequires: mesa-libGL-devel, pkgconfig
BuildRequires: make
Patch0:        amanith-0.3-nothirdpartystatic.patch
Patch1:        amanith-0.3-system-glew.patch
Patch3:        amanith-0.3-gcc-C++fix.patch
Patch4:        amanith-0.3-system-libjpeg.patch
Patch5:        amanith-0.3-system-libpng.patch
Patch6:        amanith-0.3-freetype-fix.patch
Patch7:        amanith-0.3-system-freetype.patch
Patch8:        amanith-0.3-gcc43.patch
Patch9:        amanith-0.3-gcc44.patch
Patch10:       amanith-0.3-fix-DSO.patch
Patch11:       amanith-0.3-gcc-constructor-fix.patch
Patch12:       amanith-0.3-libpng15-fix.patch

%description
Amanith is an OpenSource C++ CrossPlatform framework designed for 2d & 3d 
vector graphics.  All the framework is heavily based on a light plug-in 
system.

%package devel
Summary:       Development files for amanith
Requires:      glew-devel
Requires:      %{name} = %{version}-%{release}

%description devel
Development libraries and headers for developing programs that use amanith.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}
%patch -P0 -p1 -b .system
%patch -P1 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1 -b .DSO
%patch -P11 -p1 -b .constructor
%patch -P12 -p1 -b .pngfix
# Boo. Hiss. SGI Free B and GLX files.
rm -rf include/GL/
# Don't need the 3rdpart stuff either.
rm -rf 3rdpart/
chmod -x include/amanith/*.h include/amanith/1d/*.h \
         include/amanith/2d/*.h include/amanith/lang/*.h \
         include/amanith/numerics/*.h include/amanith/geometry/*.h \
         include/amanith/rendering/*.h include/amanith/support/*.h \
         FAQ CHANGELOG INSTALL README LICENSE.QPL doc/amanith.chm \
         src/1d/*.cpp src/2d/*.cpp src/support/*.cpp src/rendering/*.cpp \
         src/*.cpp src/geometry/*.cpp plugins/jpeg/*.cpp src/numerics/*.cpp \
         plugins/fonts/*.cpp plugins/png/*.cpp \
         plugins/jpeg/*.h plugins/png/*.h plugins/fonts/*.h
# convert to utf-8, fix end of line encoding
for i in FAQ CHANGELOG INSTALL README LICENSE.QPL; do
  sed -i -e 's|\r||g' $i
  iconv -f iso-8859-1 -t utf-8 -o $i{.utf8,} 
  mv $i{.utf8,}
done

%build
export AMANITHDIR=$(pwd)
export LD_LIBRARY_PATH=$AMANITHDIR/lib:$LD_LIBRARY_PATH
source %{_sysconfdir}/profile.d/qt.sh
qmake amanith.pro
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}

# We're using cp instead of install because the symlinks are already
# created correctly.
cp -a lib/*.so* $RPM_BUILD_ROOT%{_libdir}
cp -a plugins/*.so* $RPM_BUILD_ROOT%{_libdir}
cp -a include/amanith $RPM_BUILD_ROOT%{_includedir}

%ldconfig_scriptlets

%files
%doc CHANGELOG FAQ LICENSE.QPL README doc/*
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_includedir}/amanith/

%changelog
%autochangelog
