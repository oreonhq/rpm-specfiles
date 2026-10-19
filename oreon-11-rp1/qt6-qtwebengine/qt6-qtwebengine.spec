%global source0_hash 61257967afd9803a1db6403e86ea25c4efff8fad479bda365a9d81bfd709f621
%global source20_hash 809668ffc296043779c984f53461c2b3987a45b7a25eb2f0a1d11d9f23ba4055
%global qt_module qtwebengine
%global _hardened_build 1
%undefine _package_note_file
%global use_system_re2 1
%global use_system_libicu 1
%global use_system_libwebp 1
%global use_system_opus 1
%global use_system_ffmpeg 0
%global use_system_libvpx 0
%global use_system_snappy 1
%global use_system_glib 1
%global use_system_zlib 1
%global use_system_minizip 1
%global use_system_libevent 1
%global use_system_libxml 1
%global use_system_lcms2 1
%global use_system_libpng 1
%global use_system_libtiff 1
%global use_system_libjpeg 1
%global use_system_libopenjpeg2 1
%global use_system_harfbuzz 1
%global use_system_freetype 1
%global use_system_libpci 1
%global use_system_libudev 1
%if 0%{?rhel} && 0%{?rhel} == 9 || (0%{?oreon} >= 11)
%global use_system_re2 0
%global use_system_libicu 0
%global use_system_minizip 0
%global use_system_harfbuzz 0
%endif
%if 0%{?rhel} && 0%{?rhel} == 10 || (0%{?oreon} >= 11)
%global use_system_zlib 0
%endif
%ifarch ppc64le
%global enable_pdf_v8 0
%else
%global enable_pdf_v8 1
%endif
%if 0%{?fedora} && 0%{?fedora} >= 39 || (0%{?oreon} >= 11)
%global use_system_py_six 1
%endif
%ifarch %{arm} aarch64
%global debug_config %{nil}
%else
%global debug_config force_debug_info
%endif
%global _qtwebengine_dictionaries_dir %{_qt6_datadir}/qtwebengine_dictionaries
%global __provides_exclude ^lib.*plugin\\.so.*$
%global __provides_exclude_from ^%{_qt6_plugindir}/.*\\.so$
%global unstable 1
%if 0%{?unstable}
%global prerelease rc
%endif
%global examples 1
Summary:        Qt6 - QtWebEngine components
Name:    qt6-qtwebengine
Version: 6.140.0
Release:        1%{?dist}
License: (LGPLv2 with exceptions or GPLv3 with exceptions) and BSD and LGPLv2+ and ASL 2.0 and IJG and MIT and GPLv2+ and ISC and OpenSSL and (MPLv1.1 or GPLv2 or LGPLv2)
URL:     http://www.qt.io
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)
%if 0%{?unstable}
Source0:        https://download.qt.io/development_releases/%{qt_module}/%{version}-%{prerelease}/%{qt_module}-everywhere-s%{prerelease}-%{version}-%{prerelease}.tar.xz
%else
%endif
Source2:        clean_qtwebengine.sh
Source3:        clean_ffmpeg.sh
Source4:        get_free_ffmpeg_source_files.py
Source10:        macros.qt6-qtwebengine
Source20:        https://www.freedesktop.org/software/pulseaudio/releases/pulseaudio-12.2.tar.xz
Patch1:        qtwebengine-SIOCGSTAMP.patch
Patch2:        qtwebengine-link-pipewire.patch
Patch3:        qtwebengine-aarch64-new-stat.patch
Patch4:        qtwebengine-use-openh264.patch
Patch5:        qtwebengine-chromium-141-glibc-2.42-SYS_SECCOMP.patch
Patch80:        qtwebengine-fix-arm-build.patch
Patch101:        qtwebengine-fix-build-against-gcc16.patch
Patch102:        qtwebengine-fix-delay-signature.patch
Patch200:        qtwebengine-6.9-ppc64.patch
Patch201:        qtwebengine-chromium-ppc64.patch
Patch202:        qtwebengine-chromium-ppc64-highway.patch
Patch203:        qtwebengine-chromium-ppc64-skia-musttail.patch
ExclusiveArch: %{qt6_qtwebengine_arches}
%{?_qt6_version:Requires: qt6-qtbase%{?_isa} = %{_qt6_version}}
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
%if 0%{?use_system_re2}
%else
Provides: bundled(re2)
%endif
%if 0%{?use_system_libicu}
%endif
%if 0%{?use_system_libwebp}
%endif
%if 0%{?use_system_opus}
%endif
%if %{?use_system_ffmpeg}
%endif
%if %{?use_system_libvpx}
%endif
%if 0%{?use_system_snappy}
%endif
%if 0%{?use_system_glib}
%endif
%if %{?use_system_zlib}
%endif
%if 0%{?use_system_minizip}
%else
Provides: bundled(minizip) = 2.8.1
%endif
%if 0%{?use_system_libevent}
%endif
%if %{?use_system_libxml}
%else
Provides: bundled(libxml2) = 2.9.13
Provides: bundled(libxslt) = 1.1.3
%endif
%if 0%{?use_system_lcms2}
%endif
%if 0%{?use_system_libpng}
%endif
%if 0%{?use_system_libtiff}
%endif
%if 0%{?use_system_libjpeg}
%endif
%if 0%{?use_system_libopenjpeg2}
%endif
%if 0%{?use_system_harfbuzz}
%endif
%if 0%{?use_system_freetype}
%endif
%if 0%{?use_system_libpci}
%endif
%if 0%{?use_system_libudev}
%endif
%if 0%{?fedora} && 0%{?fedora} >= 39 || (0%{?oreon} >= 11)
%endif
Requires: qt6-qtpdf%{?_isa} = %{version}-%{release}
Provides: bundled(chromium) = 118.0.5993.220
Provides: bundled(angle)
Provides: bundled(boringssl)
Provides: bundled(brotli)
Provides: bundled(ffmpeg) = 7.1
Provides: bundled(hunspell) = 1.6.0
Provides: bundled(iccjpeg)
Provides: bundled(khronos_headers)
Provides: bundled(leveldb) = 1.23
Provides: bundled(libjingle)
Provides: bundled(libsrtp) = 2.4.0
Provides: bundled(libyuv) = 1819
Provides: bundled(modp_b64)
Provides: bundled(ots)
Provides: bundled(protobuf) = 3.13.0.1
Provides: bundled(qcms) = 4
Provides: bundled(skia)
Provides: bundled(SMHasher) = 0-147
Provides: bundled(sqlite) = 3.39.4
Provides: bundled(usrsctp)
Provides: bundled(webrtc) = 90
%ifarch %{ix86} x86_64
Provides: bundled(x86inc)
%endif
Provides: bundled(dynamic_annotations) = 4384
Provides: bundled(superfasthash) = 0
Provides: bundled(symbolize)
Provides: bundled(valgrind.h)
Provides: bundled(xdg-mime)
Provides: bundled(xdg-user-dirs) = 0.10
Provides: bundled(mozilla_security_manager) = 1.9.2
Provides: bundled(nsURLParsers)
Provides: bundled(mojo)
Provides: bundled(v8) = 11.8.172.18
Provides: bundled(fdlibm) = 5.3
# oreon:deps
BuildRequires:  /usr/bin/node
BuildRequires:  /usr/bin/python3.15
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gperf
BuildRequires:  krb5-devel
BuildRequires:  libatomic
BuildRequires:  libicu-devel
BuildRequires:  libstdc++-static
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  nodejs
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(minizip)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(re2)
BuildRequires:  pkgconfig(snappy)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xshmfence)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-html5lib
BuildRequires:  python3-zombie-imp
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qthttpserver-devel
BuildRequires:  qt6-qtlocation-devel
BuildRequires:  qt6-qtquickcontrols2-devel
BuildRequires:  qt6-qtsensors-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-static
BuildRequires:  qt6-qtwebchannel-devel
BuildRequires:  qt6-qtwebsockets-devel
BuildRequires:  qt6-srpm-macros
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
Requires: qt6-qtpdf-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-devtools = %{version}-%{release}
%description devel
%{summary}.

%package devtools
Summary: WebEngine devtools_resources
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devtools
Support for remote debugging.

%if 0%{?examples}
%package examples
Summary: Example files for %{name}
%description examples
%{summary}.
%endif

%package -n qt6-qtpdf
Summary: Qt6 - QtPdf components
%description -n qt6-qtpdf
%{summary}.

%package -n qt6-qtpdf-devel
Summary: Development files for qt6-qtpdf
Requires: qt6-qtpdf%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
Requires: qt6-qtdeclarative-devel%{?_isa}
%description -n qt6-qtpdf-devel
%{summary}.

%package -n qt6-qtpdf-examples
Summary: Example files for qt6-qtpdf
Requires: qt6-qtsvg%{?_isa}
%description -n qt6-qtpdf-examples
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source20_hash}" = "none" || { f="%{SOURCE20}"; test -f "$f" || { echo "oreon: missing Source20 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source20_hash}" || { echo "oreon: Source20 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{qt_module}-everywhere-src-%{qt_version}
mkdir -p pulse
tar -xJf %{SOURCE20} pulseaudio-12.2/src/pulse
mv pulseaudio-12.2/src/pulse pulse
rm -rf pulseaudio-12.2

cp -p %{SOURCE4} get_free_ffmpeg_source_files.py
bash %{SOURCE3} src/3rdparty/chromium
find src/3rdparty/chromium/third_party/openh264/src -type f -not -name '*.h' -delete
rm get_free_ffmpeg_source_files.py

mv pulse src/3rdparty/chromium/

pushd src/3rdparty/chromium
popd

%patch -P1 -p1 -b .SIOCGSTAMP
%patch -P2 -p1 -b .link-pipewire
%patch -P3 -p1 -b .aarch64-new-stat
%patch -P4 -p1 -b .use-openh264
%if 0%{?fedora} > 43 || 0%{?rhel} > 10 || (0%{?oreon} >= 11)
%patch -P5 -p1 -b .chromium-141-glibc-2.42-SYS_SECCOMP
%endif

## upstream patches
%patch -P80 -p1 -b .fix-arm-build

## upstreamable patches
%patch -P101 -p1 -b .fix-build-against-gcc16
%patch -P102 -p1 -b .fix-delay-signature

# ppc64le support
%patch -P200 -p1
%patch -P201 -p1
%patch -P202 -p1
%patch -P203 -p1

# delete all "toolprefix = " lines from build/toolchain/linux/BUILD.gn, as we
# never cross-compile in native Fedora RPMs, fixes ARM and aarch64 FTBFS
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' \
  src/3rdparty/chromium/build/toolchain/linux/BUILD.gn

%if 0%{?use_system_py_six}
rm src/3rdparty/chromium/third_party/six/src/six.py
rm src/3rdparty/chromium/third_party/catapult/third_party/six/six.py
rm src/3rdparty/chromium/third_party/wpt_tools/wpt/tools/third_party/six/six.py

ln -s /usr/lib/python%{python3_version}/site-packages/six.py src/3rdparty/chromium/third_party/six/src/six.py
ln -s /usr/lib/python%{python3_version}/site-packages/six.py src/3rdparty/chromium/third_party/catapult/third_party/six/six.py
ln -s /usr/lib/python%{python3_version}/site-packages/six.py src/3rdparty/chromium/third_party/wpt_tools/wpt/tools/third_party/six/six.py
%endif

#%%if 0%%{?use_system_re2}
# http://bugzilla.redhat.com/1337585
# can't just delete, but we'll overwrite with system headers to be on the safe side
#cp -bv /usr/include/re2/*.h src/3rdparty/chromium/third_party/re2/src/re2/
#%%endif

# copy the Chromium license so it is installed with the appropriate name
cp -p src/3rdparty/chromium/LICENSE LICENSE.Chromium

# use system libraries not handled by cmake options correctly
system_libs=()
%if %{?use_system_ffmpeg}
system_libs+=(ffmpeg)
%endif
system_libs+=(openh264)
# Use system libraries
src/3rdparty/chromium/build/linux/unbundle/replace_gn_files.py --system-libraries ${system_libs[@]}

# consider doing this as part of the tarball creation step instead?  rdieter
# fix/workaround
# fatal error: QtWebEngineCore/qtwebenginecoreglobal.h: No such file or directory
# if [ ! -f "./include/QtWebEngineCore/qtwebenginecoreglobal.h" ]; then
# {_qt6_libexecdir}/syncqt -version {version}
# fi
#
# # abort if this doesn't get created by syncqt.pl
# test -f "./include/QtWebEngineCore/qtwebenginecoreglobal.h"

%build

export STRIP=strip
export NINJAFLAGS="%{__ninja_common_opts}"
export NINJA_PATH=%{__ninja}
%cmake_qt6 -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
  -DCMAKE_TOOLCHAIN_FILE:STRING="%{_libdir}/cmake/Qt6/qt.toolchain.cmake" \
  -DFEATURE_webengine_build_gn:BOOL=ON \
  -DFEATURE_webengine_jumbo_build:BOOL=ON \
  -DFEATURE_webengine_developer_build:BOOL=OFF \
  -DFEATURE_qtwebengine_build:BOOL=ON \
  -DFEATURE_qtwebengine_core_build:BOOL=ON \
  -DFEATURE_qtwebengine_widgets_build:BOOL=ON \
  -DFEATURE_qtwebengine_quick_build:BOOL=ON \
  -DFEATURE_qtpdf_build:BOOL=ON \
  -DFEATURE_qtpdf_widgets_build:BOOL=ON \
  -DFEATURE_qtpdf_quick_build:BOOL=ON \
  -DFEATURE_webengine_system_re2:BOOL=%{?use_system_re2} \
  -DFEATURE_webengine_system_icu:BOOL=%{?use_system_libicu} \
  -DFEATURE_webengine_system_libwebp:BOOL=%{?use_system_libwebp} \
  -DFEATURE_webengine_system_opus:BOOL=%{?use_system_opus} \
  -DFEATURE_webengine_system_ffmpeg:BOOL=%{?use_system_ffmpeg} \
  -DFEATURE_webengine_system_libvpx:BOOL=%{?use_system_libvpx} \
  -DFEATURE_webengine_system_snappy:BOOL=%{?use_system_snappy} \
  -DFEATURE_webengine_system_glib:BOOL=%{?use_system_glib} \
  -DFEATURE_webengine_system_zlib:BOOL=%{?use_system_zlib} \
  -DFEATURE_webengine_system_minizip:BOOL=%{?use_system_minizip} \
  -DFEATURE_webengine_system_libevent:BOOL=%{?use_system_libevent} \
  -DFEATURE_webengine_system_libxml:BOOL=%{?use_system_libxml} \
  -DFEATURE_webengine_system_lcms2:BOOL=%{?use_system_lcms2} \
  -DFEATURE_webengine_system_libpng:BOOL=%{?use_system_libpng} \
  -DFEATURE_webengine_system_libtiff:BOOL=%{?use_system_libtiff} \
  -DFEATURE_webengine_system_libjpeg:BOOL=%{?use_system_libjpeg} \
  -DFEATURE_webengine_system_libopenjpeg2:BOOL=%{?use_system_libopenjpeg2} \
  -DFEATURE_webengine_system_harfbuzz:BOOL=%{?use_system_harfbuzz} \
  -DFEATURE_webengine_system_freetype:BOOL=%{?use_system_freetype} \
  -DFEATURE_webengine_system_libpci:BOOL=%{?use_system_libpci} \
  -DFEATURE_webengine_system_libudev:BOOL=%{?use_system_libudev} \
  -DFEATURE_webengine_embedded_build:BOOL=OFF \
  -DFEATURE_webengine_pepper_plugins:BOOL=ON \
  -DFEATURE_webengine_printing_and_pdf:BOOL=ON \
  -DFEATURE_webengine_proprietary_codecs:BOOL=ON \
  -DFEATURE_webengine_spellchecker:BOOL=ON \
  -DFEATURE_webengine_native_spellchecker:BOOL=OFF \
  -DFEATURE_webengine_webrtc:BOOL=ON \
  -DFEATURE_webengine_webrtc_pipewire:BOOL=ON \
  -DFEATURE_webengine_geolocation:BOOL=ON \
  -DFEATURE_webengine_webchannel:BOOL=ON \
  -DFEATURE_webengine_kerberos:BOOL=ON \
  -DFEATURE_webengine_extensions:BOOL=ON \
  -DFEATURE_webengine_ozone_x11:BOOL=ON \
  -DFEATURE_webengine_vulkan:BOOL=ON \
  -DFEATURE_webengine_vaapi:BOOL=ON \
  -DFEATURE_webengine_system_alsa:BOOL=ON \
  -DFEATURE_webengine_system_pulseaudio:BOOL=ON \
  -DFEATURE_webengine_system_gbm:BOOL=ON \
  -DFEATURE_webengine_v8_context_snapshot:BOOL=ON \
  -DFEATURE_webenginedriver:BOOL=ON \
  -DFEATURE_pdf_v8:BOOL=%{?enable_pdf_v8} \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}
%cmake_build
%install
%cmake_install
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{_rpmmacrodir}/macros.qt6-qtwebengine
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{_rpmmacrodir}/macros.qt6-qtwebengine
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
rm -fv Qt6WebEngineCore.la
popd
mkdir -p %{buildroot}%{_qtwebengine_dictionaries_dir}
%global lesser_version $(echo -e "%{version}\\n%{_qt6_version}" | sort -V | head -1)
sed -i -e "s|%{version} \${_Qt6WebEngine|%{lesser_version} \${_Qt6WebEngine|" \
  %{buildroot}%{_qt6_libdir}/cmake/Qt6WebEngine*/Qt6WebEngine*Config.cmake
%filetriggerin -- %{_datadir}/hunspell
while read filename ; do
  case "$filename" in
    *.dic)
      bdicname=%{_qtwebengine_dictionaries_dir}/`basename -s .dic "$filename"`.bdic
      %{_qt6_libdir}/qt6/libexec/qwebengine_convert_dict "$filename" "$bdicname" &> /dev/null || :
      ;;
  esac
done
%oreon_autofiles qt6-qtpdf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles qt6-qtpdf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles qt6-qtpdf-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt6-qtwebengine-devel -f %{oreon_filedir}/qt6-qtwebengine-devel.list
%files -n qt6-qtwebengine-devtools -f %{oreon_filedir}/qt6-qtwebengine-devtools.list
%files -n qt6-qtwebengine-examples -f %{oreon_filedir}/qt6-qtwebengine-examples.list
%files -n qt6-qtpdf -f %{oreon_filedir}/qt6-qtpdf.list
%files -n qt6-qtpdf-devel -f %{oreon_filedir}/qt6-qtpdf-devel.list
%files -n qt6-qtpdf-examples -f %{oreon_filedir}/qt6-qtpdf-examples.list

%changelog

%autochangelog
