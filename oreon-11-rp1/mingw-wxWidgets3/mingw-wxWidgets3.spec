%global source0_hash none

%{?mingw_package_header}

%global mingw_build_win32 1
%global mingw_build_win64 1

%global mingw_pkg_name wxWidgets3
%global majorver 3
%global minorver 0

Summary:       MinGW port of the wxWidgets GUI library
Name:          mingw-%{mingw_pkg_name}
Version:       %{majorver}.%{minorver}.4
Release:       20%{?dist}
License:       LGPL-2.0-or-later WITH WxWindows-exception-3.1

URL:           http://wxwidgets.org
Source:        https://github.com/wxWidgets/wxWidgets/releases/download/v%{version}/wxWidgets-%{version}.tar.bz2
# https://bugzilla.redhat.com/show_bug.cgi?id=1225148
# remove abort when ABI check fails
# Backport from wxGTK
Patch0:         %{name}-3.0.3-abicheck.patch
Patch1:         fix-filename-test.patch
Patch2:         fix-vararg-test.patch
Patch3:         fix-glcanvas-crash-wayland.patch
# Use winsock2
Patch1000:      %{name}-%{version}-winsock2.patch

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
Summary: %{summary}

%description -n mingw32-%{mingw_pkg_name}
wxWidgets is the C++ cross-platform GUI library, offering classes for all
common GUI controls as well as a comprehensive set of helper classes for most
common application tasks, ranging from networking to HTML display and image
manipulation.

# Mingw64
%package -n mingw64-%{mingw_pkg_name}
Summary: %{summary}

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

#========= Shared Libraries ==========
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
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw32_libdir}/wx/config/%{mingw32_target}-*-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config
wx_config_filename=$(basename $RPM_BUILD_ROOT%{mingw64_libdir}/wx/config/%{mingw64_target}-*-[0-9]*)
ln -sf ../lib/wx/config/$wx_config_filename $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config

# remove bakefiles for now until we have a working bakefile setup for mingw32
rm -rf $RPM_BUILD_ROOT%{mingw32_datadir}/bakefile
rm -rf $RPM_BUILD_ROOT%{mingw64_datadir}/bakefile

mv $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config $RPM_BUILD_ROOT%{mingw32_bindir}/wx-config-%{majorver}.%{minorver}
mv $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config $RPM_BUILD_ROOT%{mingw64_bindir}/wx-config-%{majorver}.%{minorver}

# find locale files
%find_lang wxstd%{majorver}
%find_lang wxmsw%{majorver}

%files -n mingw32-%{mingw_pkg_name} -f wxstd%{majorver}.lang -f wxmsw%{majorver}.lang
%license docs/licence.txt docs/licendoc.txt docs/lgpl.txt docs/gpl.txt
%{mingw32_bindir}/wx-config-%{majorver}.%{minorver}
%{mingw32_bindir}/wxbase%{majorver}%{minorver}u_gcc_custom.dll
%{mingw32_bindir}/wxbase%{majorver}%{minorver}u_net_gcc_custom.dll
%{mingw32_bindir}/wxbase%{majorver}%{minorver}u_xml_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_adv_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_aui_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_core_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_gl_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_html_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_media_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_propgrid_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_qa_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_ribbon_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_richtext_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_stc_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_webview_gcc_custom.dll
%{mingw32_bindir}/wxmsw%{majorver}%{minorver}u_xrc_gcc_custom.dll
%{mingw32_includedir}/wx-%{majorver}.%{minorver}
%{mingw32_libdir}/libwx_baseu-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_baseu_net-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_baseu_xml-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_adv-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_aui-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_core-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_gl-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_html-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_media-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_propgrid-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_qa-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_ribbon-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_richtext-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_stc-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_webview-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%{mingw32_libdir}/libwx_mswu_xrc-%{majorver}.%{minorver}-%{mingw32_target}.dll.a
%dir %{mingw32_libdir}/wx
%dir %{mingw32_libdir}/wx/config
%{mingw32_libdir}/wx/config/%{mingw32_target}-msw-unicode-%{majorver}.%{minorver}
%dir %{mingw32_libdir}/wx/include
%{mingw32_libdir}/wx/include/%{mingw32_target}-msw-unicode-%{majorver}.%{minorver}
%{mingw32_datadir}/aclocal/wxwin%{majorver}.m4
#{mingw32_datadir}/bakefile
#{mingw32_datadir}/bakefile/presets
#{mingw32_datadir}/bakefile/presets/wx.bkl
#{mingw32_datadir}/bakefile/presets/wx_unix.bkl
#{mingw32_datadir}/bakefile/presets/wx_win32.bkl

%files -n mingw32-%{mingw_pkg_name}-static
%{mingw32_libdir}/libwx_baseu-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_baseu_net-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_baseu_xml-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_adv-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_aui-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_core-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_gl-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_html-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_media-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_propgrid-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_qa-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_ribbon-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_richtext-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_stc-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_webview-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwx_mswu_xrc-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwxregexu-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/libwxscintilla-%{majorver}.%{minorver}-%{mingw32_target}.a
%{mingw32_libdir}/wx/config/%{mingw32_target}-msw-unicode-static-%{majorver}.%{minorver}
%{mingw32_libdir}/wx/include/%{mingw32_target}-msw-unicode-static-%{majorver}.%{minorver}

%files -n mingw64-%{mingw_pkg_name} -f wxstd%{majorver}.lang -f wxmsw%{majorver}.lang
%license docs/licence.txt docs/licendoc.txt docs/lgpl.txt docs/gpl.txt
%{mingw64_bindir}/wx-config-%{majorver}.%{minorver}
%{mingw64_bindir}/wxbase%{majorver}%{minorver}u_gcc_custom.dll
%{mingw64_bindir}/wxbase%{majorver}%{minorver}u_net_gcc_custom.dll
%{mingw64_bindir}/wxbase%{majorver}%{minorver}u_xml_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_adv_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_aui_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_core_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_gl_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_html_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_media_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_propgrid_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_qa_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_ribbon_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_richtext_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_stc_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_webview_gcc_custom.dll
%{mingw64_bindir}/wxmsw%{majorver}%{minorver}u_xrc_gcc_custom.dll
%{mingw64_includedir}/wx-%{majorver}.%{minorver}
%{mingw64_libdir}/libwx_baseu-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_baseu_net-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_baseu_xml-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_adv-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_aui-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_core-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_gl-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_html-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_media-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_propgrid-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_qa-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_ribbon-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_richtext-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_stc-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_webview-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%{mingw64_libdir}/libwx_mswu_xrc-%{majorver}.%{minorver}-%{mingw64_target}.dll.a
%dir %{mingw64_libdir}/wx
%dir %{mingw64_libdir}/wx/config
%{mingw64_libdir}/wx/config/%{mingw64_target}-msw-unicode-%{majorver}.%{minorver}
%dir %{mingw64_libdir}/wx/include
%{mingw64_libdir}/wx/include/%{mingw64_target}-msw-unicode-%{majorver}.%{minorver}
%{mingw64_datadir}/aclocal/wxwin%{majorver}.m4
#{mingw64_datadir}/bakefile
#{mingw64_datadir}/bakefile/presets
#{mingw64_datadir}/bakefile/presets/wx.bkl
#{mingw64_datadir}/bakefile/presets/wx_unix.bkl
#{mingw64_datadir}/bakefile/presets/wx_win32.bkl

%files -n mingw64-%{mingw_pkg_name}-static
%{mingw64_libdir}/libwx_baseu-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_baseu_net-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_baseu_xml-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_adv-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_aui-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_core-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_gl-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_html-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_media-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_propgrid-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_qa-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_ribbon-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_richtext-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_stc-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_webview-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwx_mswu_xrc-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwxregexu-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/libwxscintilla-%{majorver}.%{minorver}-%{mingw64_target}.a
%{mingw64_libdir}/wx/config/%{mingw64_target}-msw-unicode-static-%{majorver}.%{minorver}
%{mingw64_libdir}/wx/include/%{mingw64_target}-msw-unicode-static-%{majorver}.%{minorver}

%changelog
%autochangelog
