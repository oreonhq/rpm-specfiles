%global source0_hash none

Summary:        Cross platform C++ game library
Name:           ClanLib
Version:        2.3.7
Release:        37%{?dist}
License:        zlib
URL:            http://www.clanlib.org/
Source0:        http://www.clanlib.org/download/releases-2.0/%{name}-%{version}.tgz
# This is http://clanlib.org/docs/clanlib-2.3/reference_doxygen.zip renamed
# to reflect the exact version for which it was downloaded
Source1:        ClanLib-%{version}-generated-docs.zip
Patch1:         ClanLib-2.3.4-gcc47.patch
Patch2:         ClanLib-2.3.4-non-x86.patch
Patch3:         ClanLib-2.3.7-no-wm_type-in-fs.patch
Patch4:         ClanLib-2.3.7-no-ldflags-for-conftest.patch
Patch5:         ClanLib-2.3.7-gcc7.patch
Patch6:         ClanLib-2.3.7-ftbfs.patch
Patch7:         ClanLib-2.3.7-link-pthread.patch
BuildRequires:  make gcc-c++
BuildRequires:  libX11-devel libXi-devel libXmu-devel libGLU-devel libICE-devel
BuildRequires:  libXext-devel libXxf86vm-devel libXt-devel xorg-x11-proto-devel
BuildRequires:  libvorbis-devel mikmod-devel alsa-lib-devel
BuildRequires:  libpng-devel libjpeg-devel fontconfig-devel
BuildRequires:  libXrender-devel sqlite-devel libtool
Provides:       clanlib = %{version}-%{release}

%description
ClanLib is a cross platform C++ game library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libGLU-devel xorg-x11-proto-devel libXrender-devel
Requires:       fontconfig-devel libjpeg-devel libpng-devel libXxf86vm-devel
Requires:       mikmod-devel alsa-lib-devel sqlite-devel pcre-devel
Provides:       clanlib-devel = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1 -a 1
./autogen.sh
mv reference_doxygen html

%build
%configure --disable-dependency-tracking --disable-static --disable-docs \
  --disable-clanRegExp   \
  --enable-clanDisplay   \
  --enable-clanGL        \
  --enable-clanGL1       \
  --enable-clanSound     \
  --enable-clanDatabase  \
  --enable-clanSqlite    \
  --enable-clanNetwork   \
  --enable-clanGUI       \
  --enable-clanCSSLayout \
  --enable-clanSWRender  \
  --enable-clanMikMod    \
  --enable-clanVorbis

# Don't use rpath!
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%make_build

%install
%make_install
rm $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc CREDITS
%license COPYING
%{_libdir}/libclan23*.so.*

%files devel
%doc README html
%{_libdir}/libclan23*.so
%{_includedir}/%{name}-2.3
%{_libdir}/pkgconfig/clan*-2.3.pc

%changelog
%autochangelog
