%global source0_hash 197c94f7d46269a7fc261a3c8c943f03a9807acf65381944489a538fd8b5dd21
%{?mingw_package_header}
%global mingw_build_win32 1
%global mingw_build_win64 1
%global mingw_pkg_name wxWidgets
Summary:        MinGW port of the wxWidgets GUI library
Name:          mingw-%{mingw_pkg_name}
Version:       2.8.12
Release:        1%{?dist}
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:           http://wxwidgets.org
Source0:        http://prdownloads.sourceforge.net/wxwindows/wxWidgets-%{version}.tar.gz
Patch0:        wxWidgets-2.8.12-mingw64-1.patch
Patch1:        wxWidgets-2.8.12-strtoull.patch
BuildArch:     noarch
# oreon:deps
BuildRequires:  gettext
BuildRequires:  make
BuildRequires:  mingw32-expat
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libjpeg
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-expat
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libjpeg
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:        MinGW port of the wxWidgets GUI library
%description -n mingw32-%{mingw_pkg_name}
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:        MinGW port of the wxWidgets GUI library
%description -n mingw64-%{mingw_pkg_name}
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw32 static
%package -n mingw32-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw32-%{mingw_pkg_name} development
Requires: mingw32-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw32-%{mingw_pkg_name}-static
The mingw32-%{mingw_pkg_name}-static package contains static library for
mingw32-%{mingw_pkg_name} development.

# Mingw64 static
%package -n mingw64-%{mingw_pkg_name}-static
Summary:  Static libraries for mingw64-%{mingw_pkg_name} development
Requires: mingw64-%{mingw_pkg_name} = %{version}-%{release}
%description -n mingw64-%{mingw_pkg_name}-static
The mingw64-%{mingw_pkg_name}-static package contains static library for
mingw64-%{mingw_pkg_name} development.

%{?mingw_debug_package}

%prep

%setup -q -n wxWidgets-%{version}
%patch -P0 -p1 -b .mingw64
%patch -P1 -p1 -b .strtoull

#==========================================
%build

export MINGW32_CXXFLAGS="%{mingw32_cflags} -Wno-narrowing"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -Wno-narrowing"
export MINGW_BUILDDIR_SUFFIX=_shared
%mingw_configure --enable-shared \
  --with-msw \
  --with-sdl \
  --enable-unicode \
  --enable-optimise \
  --with-regex=builtin \
  --disable-rpath \
  --without-subdirs
sed -e 's|^CXXFLAGS = |CXXFLAGS = -fpermissive -fno-keep-inline-dllexport |' < build_win64_shared/Makefile > build_win64_shared/Makefile.xx
mv build_win64_shared/Makefile.xx build_win64_shared/Makefile
%mingw_make %{?_smp_mflags}
export MINGW_BUILDDIR_SUFFIX=_static
%mingw_configure --disable-shared \
  --with-msw \
  --with-sdl \
  --enable-unicode \
  --enable-optimise \
  --with-regex=builtin \
  --disable-rpath \
  --without-subdirs
%mingw_make %{?_smp_mflags}
make -C locale allmo
%install
export MINGW_BUILDDIR_SUFFIX=_shared
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
export MINGW_BUILDDIR_SUFFIX=_static
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
if ls $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll ; then
  mv $RPM_BUILD_ROOT%{mingw32_libdir}/*.dll $RPM_BUILD_ROOT%{mingw32_bindir}
else
  echo "No 32bit shared libraries found."
fi
if ls $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll ; then
  mv $RPM_BUILD_ROOT%{mingw64_libdir}/*.dll $RPM_BUILD_ROOT%{mingw64_bindir}
else
  echo "No 32bit shared libraries found."
fi
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw32_libdir}/wx/config/%{mingw32_target}-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw64_libdir}/wx/config/%{mingw64_target}-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/bakefile
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/bakefile
%find_lang wxstd
%find_lang wxmsw
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-wxWidgets -f %{oreon_filedir}/mingw32-wxWidgets.list
%files -n mingw64-wxWidgets -f %{oreon_filedir}/mingw64-wxWidgets.list
%files -n mingw32-wxWidgets-static -f %{oreon_filedir}/mingw32-wxWidgets-static.list
%files -n mingw64-wxWidgets-static -f %{oreon_filedir}/mingw64-wxWidgets-static.list

%changelog

%autochangelog
