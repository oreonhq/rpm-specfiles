%global source0_hash 521ff7bd62c459ff5372e269c223e2a6107a6a99a36afdc2ae634a973af70c59

Name:           ftgl
Version:        2.1.3
Release:        %autorelease
Summary:        OpenGL frontend to Freetype 2

License:        MIT
URL:            http://ftgl.wiki.sourceforge.net/
Source0:        http://downloads.sourceforge.net/ftgl/ftgl-%{version}-rc5.tar.bz2
Patch0:         ftgl-2.1.3-rc5-ttf_font.patch
Patch1:         ftgl-2.1.3-rc5-ldflags.patch
Patch2:         fix-double-float-narrowing.patch
Patch3:         adapt-to-freetype-2.13.3-change.patch

BuildRequires:  gcc-c++
BuildRequires:  doxygen

BuildRequires:  freeglut-devel
BuildRequires:  freetype-devel
BuildRequires:  libXi-devel
BuildRequires:  libXmu-devel
BuildRequires:  cppunit-devel
BuildRequires: make

Obsoletes: ftgl-utils < %{version}

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

# Remove the ~rc5 from the pc file, as this causes rpm to add a
# Requires: rpmlib(TildeInVersions) <= 4.10.0-1 
# Which breaks installing ftgl-devel into a koji buildroot (rhbz#843460)
sed -i 's/2\.1\.3~rc5/2.1.3/' ftgl.pc

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'

# Doc fixes
mkdir -p __doc/html
install -pm 0644 %{buildroot}%{_datadir}/doc/ftgl/html/* __doc/html
rm -rf %{buildroot}%{_datadir}/doc

%ldconfig_scriptlets

%files
%doc AUTHORS BUGS ChangeLog NEWS README TODO
%license COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/FTGL/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%files docs
%doc __doc/*

%changelog
%autochangelog
