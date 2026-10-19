%global source0_hash 96157f988d261b7368e5340afa1a0cad943768f35929c22841f62c25b17bf7f0
%{?mingw_package_header}
%global mingw_build_win32 1
%global mingw_build_win64 1
%global mingw_pkg_name wxWidgets3
%global majorver 3
%global minorver 0
Summary:        MinGW port of the wxWidgets GUI library
Name:          mingw-%{mingw_pkg_name}
Version:       %{majorver}.%{minorver}.4
Release:        20%{?dist}
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:           http://wxwidgets.org
Source0:        https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/wxWidgets-%{version}.tar.bz2
Patch0:         %{name}-3.0.3-abicheck.patch
Patch1:         fix-filename-test.patch
Patch2:         fix-vararg-test.patch
Patch3:         fix-glcanvas-crash-wayland.patch
Patch1000:      %{name}-%{version}-winsock2.patch
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

%autosetup -n wxWidgets-%{version} -p1

# patch some installed files to avoid conflicts with 2.8.*
sed -i -e 's|aclocal)|aclocal/wxwin%{majorver}.m4)|' Makefile.in
sed -i -e 's|wxstd.mo|wxstd%{majorver}.mo|' Makefile.in
sed -i -e 's|wxmsw.mo|wxmsw%{majorver}.mo|' Makefile.in

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
  --enable-intl \
  --enable-no_deps \
  --disable-rpath \
  --enable-ipv6 \
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
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw32_libdir}/wx/config/%{mingw32_target}-*-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw64_libdir}/wx/config/%{mingw64_target}-*-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/bakefile
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/bakefile
mv $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config-%{majorver}.%{minorver}
mv $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config-%{majorver}.%{minorver}
%find_lang wxstd%{majorver}
%find_lang wxmsw%{majorver}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-wxWidgets3 -f %{oreon_filedir}/mingw32-wxWidgets3.list
%files -n mingw64-wxWidgets3 -f %{oreon_filedir}/mingw64-wxWidgets3.list
%files -n mingw32-wxWidgets3-static -f %{oreon_filedir}/mingw32-wxWidgets3-static.list
%files -n mingw64-wxWidgets3-static -f %{oreon_filedir}/mingw64-wxWidgets3-static.list

%changelog

%autochangelog
