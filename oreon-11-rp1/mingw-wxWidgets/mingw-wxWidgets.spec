%global source0_hash none

%{?mingw_package_header}

%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name wxWidgets

Summary:       MinGW port of the wxWidgets GUI library
Name:          mingw-%{mingw_pkg_name}
Version:       2.8.12
Release:       43%{?dist}
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1

URL:           http://wxwidgets.org
Source:        http://prdownloads.sourceforge.net/wxwindows/wxWidgets-%{version}.tar.gz
Patch0:        wxWidgets-2.8.12-mingw64-1.patch
Patch1:        wxWidgets-2.8.12-strtoull.patch
BuildArch:     noarch
BuildRequires: make
BuildRequires: mingw32-filesystem >= 68
BuildRequires: mingw64-filesystem >= 68
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw32-expat
BuildRequires: mingw64-expat
BuildRequires: mingw32-libjpeg
BuildRequires: mingw64-libjpeg
BuildRequires: mingw32-libpng
BuildRequires: mingw64-libpng
BuildRequires: mingw32-libtiff
BuildRequires: mingw64-libtiff
BuildRequires: mingw32-zlib
BuildRequires: mingw64-zlib
BuildRequires: gettext

%description
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw32
%package -n mingw32-%{mingw_pkg_name}
Summary:		%{summary}

%description -n mingw32-%{mingw_pkg_name}
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary:		%{summary}

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

#========= Shared Libraries ==========
export MINGW_BUILDDIR_SUFFIX=_shared
%mingw_configure --enable-shared \
  --with-msw \
  --with-sdl \
  --enable-unicode \
  --enable-optimise \
  --with-regex=builtin \
  --disable-rpath \
  --without-subdirs

#Try to reduce linker memory footprint
sed -e 's|^CXXFLAGS = |CXXFLAGS = -fpermissive -fno-keep-inline-dllexport |' < build_win64_shared/Makefile > build_win64_shared/Makefile.xx
mv build_win64_shared/Makefile.xx build_win64_shared/Makefile

%mingw_make %{?_smp_mflags}

#========= Static Libraries ==========
export MINGW_BUILDDIR_SUFFIX=_static
%mingw_configure --disable-shared \
  --with-msw \
  --with-sdl \
  --enable-unicode \
  --enable-optimise \
  --with-regex=builtin \
  --disable-rpath \
  --without-subdirs

#TODO verify this doesn't overwrite anything from the shared build
%mingw_make %{?_smp_mflags}

#========= Locale ====================
make -C locale allmo

#==========================================
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

# we need to modify the absolute wx-config link to be relative or rpm complains
# (and our package wouldn't be relocatable)
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw32_libdir}/wx/config/%{mingw32_target}-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw64_libdir}/wx/config/%{mingw64_target}-*-release-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config

# remove bakefiles for now until we have a working bakefile setup for mingw32
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/bakefile
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/bakefile

# find locale files
%find_lang wxstd
%find_lang wxmsw

%files -n mingw32-%{mingw_pkg_name} -f wxstd.lang -f wxmsw.lang
%doc docs/licence.txt docs/licendoc.txt docs/lgpl.txt docs/gpl.txt
%{mingw32_bindir}/wx-config
%{mingw32_bindir}/wxbase28u_gcc_custom.dll
%{mingw32_bindir}/wxbase28u_net_gcc_custom.dll
%{mingw32_bindir}/wxbase28u_xml_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_adv_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_aui_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_core_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_html_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_qa_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_richtext_gcc_custom.dll
%{mingw32_bindir}/wxmsw28u_xrc_gcc_custom.dll
%{mingw32_includedir}/wx-2.8
%{mingw32_libdir}/libwx_baseu-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_baseu_net-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_baseu_xml-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_adv-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_aui-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_core-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_html-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_qa-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_richtext-2.8-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_xrc-2.8-%{mingw32_target}.dll.a
%dir %{mingw32_libdir}/wx
%dir %{mingw32_libdir}/wx/config
%{mingw32_libdir}/wx/config/%{mingw32_target}-msw-unicode-release-2.8
%dir %{mingw32_libdir}/wx/include
%{mingw32_libdir}/wx/include/%{mingw32_target}-msw-unicode-release-2.8
%{mingw32_datadir}/aclocal/wxwin.m4
#{mingw32_datadir}/bakefile
#{mingw32_datadir}/bakefile/presets
#{mingw32_datadir}/bakefile/presets/wx.bkl
#{mingw32_datadir}/bakefile/presets/wx_unix.bkl
#{mingw32_datadir}/bakefile/presets/wx_win32.bkl

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libwx_baseu-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_baseu_net-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_baseu_xml-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_adv-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_aui-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_core-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_html-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_qa-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_richtext-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_xrc-2.8-%{mingw32_target}.a
%{mingw32_libdir}/libwxregexu-2.8-%{mingw32_target}.a
%{mingw32_libdir}/wx/config/%{mingw32_target}-msw-unicode-release-static-2.8
%{mingw32_libdir}/wx/include/%{mingw32_target}-msw-unicode-release-static-2.8

%files -n mingw64-%{mingw_pkg_name} -f wxstd.lang -f wxmsw.lang
%doc docs/licence.txt docs/licendoc.txt docs/lgpl.txt docs/gpl.txt
%{mingw64_bindir}/wx-config
%{mingw64_bindir}/wxbase28u_gcc_custom.dll
%{mingw64_bindir}/wxbase28u_net_gcc_custom.dll
%{mingw64_bindir}/wxbase28u_xml_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_adv_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_aui_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_core_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_html_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_qa_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_richtext_gcc_custom.dll
%{mingw64_bindir}/wxmsw28u_xrc_gcc_custom.dll
%{mingw64_includedir}/wx-2.8
%{mingw64_libdir}/libwx_baseu-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_baseu_net-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_baseu_xml-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_adv-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_aui-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_core-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_html-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_qa-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_richtext-2.8-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_xrc-2.8-%{mingw64_target}.dll.a
%dir %{mingw64_libdir}/wx
%dir %{mingw64_libdir}/wx/config
%{mingw64_libdir}/wx/config/%{mingw64_target}-msw-unicode-release-2.8
%dir %{mingw64_libdir}/wx/include
%{mingw64_libdir}/wx/include/%{mingw64_target}-msw-unicode-release-2.8
%{mingw64_datadir}/aclocal/wxwin.m4
#{mingw64_datadir}/bakefile
#{mingw64_datadir}/bakefile/presets
#{mingw64_datadir}/bakefile/presets/wx.bkl
#{mingw64_datadir}/bakefile/presets/wx_unix.bkl
#{mingw64_datadir}/bakefile/presets/wx_win32.bkl

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libwx_baseu-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_baseu_net-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_baseu_xml-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_adv-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_aui-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_core-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_html-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_qa-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_richtext-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_xrc-2.8-%{mingw64_target}.a
%{mingw64_libdir}/libwxregexu-2.8-%{mingw64_target}.a
%{mingw64_libdir}/wx/config/%{mingw64_target}-msw-unicode-release-static-2.8
%{mingw64_libdir}/wx/include/%{mingw64_target}-msw-unicode-release-static-2.8

%changelog
%autochangelog
