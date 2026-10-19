%global source0_hash 521ff7bd62c459ff5372e269c223e2a6107a6a99a36afdc2ae634a973af70c59
Name:           ftgl
Version:        2.1.3
Release:        1%{?dist}
Summary:        OpenGL frontend to Freetype 2
License:        MIT
URL:            http://ftgl.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ftgl/ftgl-%{version}-rc5.tar.bz2
Patch0:         ftgl-2.1.3-rc5-ttf_font.patch
Patch1:         ftgl-2.1.3-rc5-ldflags.patch
Patch2:         fix-double-float-narrowing.patch
Patch3:         adapt-to-freetype-2.13.3-change.patch
Obsoletes: ftgl-utils < %{version}
# oreon:deps
BuildRequires:  cppunit-devel
BuildRequires:  doxygen
BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  make
# /oreon:deps
%description
FTGL is a free open source library to enable developers to use arbitrary
fonts in their OpenGL (www.opengl.org)  applications.
Unlike other OpenGL font libraries FTGL uses standard font file formats
so doesn't need a preprocessing step to convert the high quality font data
into a lesser quality, proprietary format.
FTGL uses the Freetype (www.freetype.org) font library to open and 'decode'
the fonts. It then takes that output and stores it in a format most 
efficient for OpenGL rendering.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
Requires:       freetype-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package docs
Summary:        Documentation for %{name}
%description docs
This package contains documentation files for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ftgl-%{version}~rc5
%patch -P 0 -p1 -b .destdir
%patch -P 1 -p1 -b .ldflags
%patch -P 2 -p1 -b .narrowing
# Fix for freetype 2.13.3
%patch -P 3 -p1 -b .freetype-2.13.3

%build

%configure \
  --enable-shared \
  --disable-static \
  --with-gl-inc=%{_includedir} \
  --with-gl-lib=%{_libdir} \
  --with-glut-inc=%{_includedir} \
  --with-glut-lib=%{_libdir} \
  --with-x
sed -i 's/2\.1\.3~rc5/2.1.3/' ftgl.pc
%make_build
%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mkdir -p __doc/html
install -pm 0644 %{buildroot}%{_datadir}/doc/ftgl/html/* __doc/html
rm -rf %{buildroot}%{_datadir}/doc
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ftgl-devel -f %{oreon_filedir}/ftgl-devel.list
%files -n ftgl-docs -f %{oreon_filedir}/ftgl-docs.list

%changelog

%autochangelog
