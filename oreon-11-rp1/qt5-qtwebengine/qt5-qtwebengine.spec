%global source0_hash 06627d8c6f10e06c25b42a7e88a6c61b4afc255914ca1a55bc72909899d36c2b
%global qt_module qtwebengine
%global _hardened_build 1
%undefine _package_note_file
%ifarch %{arm} aarch64
%global debug_config %{nil}
%else
%global debug_config force_debug_info
%endif
%global _qtwebengine_dictionaries_dir %{_qt5_datadir}/qtwebengine_dictionaries
%global rpm_macros_dir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)
%global __provides_exclude ^lib.*plugin\\.so.*$
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\\.so$
Summary:        Qt5 - QtWebEngine components
Name:    qt5-qtwebengine
Version: 5.15.19
Release:        1%{?dist}
License: (LGPL-2.0-or-later WITH FLTK-exception OR LicenseRef-Callaway-GPLv3-with-exceptions) AND LicenseRef-Callaway-BSD AND LicenseRef-Callaway-LGPLv2+ AND Apache-2.0 AND IJG AND LicenseRef-Callaway-MIT AND GPL-2.0-or-later AND ISC AND OpenSSL AND (LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-only OR LicenseRef-Callaway-LGPLv2)
URL:     http://www.qt.io
Source0:        https://download.qt.io/archive/qt/5.15/%{version}/submodules/qtwebengine-everywhere-opensource-src-%{version}.tar.xz
Source1: qtwebengine-release.sh
Source2: clean_qtwebengine.sh
Source3: clean_ffmpeg.sh
Source4: get_free_ffmpeg_source_files.py
Source10: macros.qt5-qtwebengine
Patch2:  qtwebengine-opensource-src-5.12.4-fix-extractcflag.patch
Patch3:  qtwebengine-opensource-src-5.9.0-no-neon.patch
Patch4:  qtwebengine-SIOCGSTAMP.patch
Patch5:  qtwebengine-5.15.0-QT_DEPRECATED_VERSION.patch
Patch6:  chromium-angle-nullptr.patch
Patch7:  chromium-hunspell-nullptr.patch
Patch8:  qtwebengine-everywhere-5.15.8-libpipewire-0.3.patch
Patch24: qtwebengine-everywhere-src-5.11.3-aarch64-new-stat.patch
Patch32: qtwebengine-skia-missing-includes.patch
Patch34: qtwebengine-fix-build.patch
Patch35: qt5-qtwebengine-c99.patch
Patch36: qtwebengine-chromium-141-glibc-2.42-SYS_SECCOMP.patch
Patch60: qtwebengine-ffmpeg5.patch
Patch61: qt5-qtwebengine-ffmpeg7.patch
Patch62: qt5-qtwebengine-ffmpeg8.patch
Patch70: qtwebengine-5.15.13_p20240322-ninja1.12.patch
Patch71: fix_build_pdf_extension_util.patch
Patch73: python3.12-six.patch
Patch80: qtwebengine-icu75.patch
Patch100: riscv-v8.patch
Patch101: riscv.patch
Patch102: riscv-breakpad.patch
Patch103: riscv-crashpad.patch
Patch104: riscv-sandbox.patch
ExclusiveArch: %{qt5_qtwebengine_arches}
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
%if 0%{?use_system_libicu}
%endif
%if 0%{?pipewire}
%endif
BuildConflicts: minizip-devel
Provides: bundled(minizip) = 1.2
%if 0%{?use_system_libvpx}
%endif
Provides: bundled(chromium) = 87.0.4280.144
Provides: bundled(angle) = 2422
Provides: bundled(boringssl)
Provides: bundled(brotli)
Provides: bundled(ffmpeg) = 4.3
Provides: bundled(hunspell) = 1.6.0
Provides: bundled(iccjpeg)
Provides: bundled(khronos_headers)
Provides: bundled(leveldb) = 1.22
Provides: bundled(libjingle)
Provides: bundled(libsrtp) = 2.2.0
%if !0%{?use_system_libvpx}
Provides: bundled(libvpx) = 1.8.2
%endif
Provides: bundled(libxml2) = 2.9.10
Provides: bundled(libxslt) = 1.1.34
Provides: bundled(libXNVCtrl) = 302.17
Provides: bundled(libyuv) = 1768
Provides: bundled(modp_b64)
Provides: bundled(ots)
Provides: bundled(re2)
Provides: bundled(protobuf) = 3.9.0
Provides: bundled(qcms) = 4
Provides: bundled(skia)
Provides: bundled(SMHasher) = 0-147
Provides: bundled(sqlite) = 3.35.5
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
Provides: bundled(v8) = 8.7.220.35
Provides: bundled(fdlibm) = 5.3
%{?_qt5_version:Requires: qt5-qtbase%{?_isa} = %{_qt5_version}}
%if 0%{?use_system_icu}
Conflicts: qt5-qtwebengine-freeworld < 5.15.2-2
%endif
# oreon:deps
BuildRequires:  /usr/bin/python3.11
BuildRequires:  bison
BuildRequires:  cmake
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  gperf
BuildRequires:  krb5-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libnsl2
BuildRequires:  libstdc++-static
BuildRequires:  libtirpc
BuildRequires:  make
BuildRequires:  ninja-build
BuildRequires:  nodejs
BuildRequires:  perl-interpreter
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(egl)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(harfbuzz)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libpci)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(nss)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(poppler-cpp)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbfile)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python-rpm-macros
BuildRequires:  python3-html5lib
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qt5-qtquickcontrols2-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-static
BuildRequires:  qt5-qtwebchannel-devel
BuildRequires:  qt5-qtxmlpatterns-devel
BuildRequires:  snappy-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
Requires: %{name}-devtools = %{version}-%{release}
%description devel
%{summary}.

%package devtools
Summary: WebEngine devtools_resources
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devtools
Support for remote debugging.

%package examples
Summary: Example files for %{name}
%description examples
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{qt_module}-everywhere-src-%{version}%{?prerelease:-%{prerelease}}

cp %{SOURCE4} . && chmod +x get_free_ffmpeg_source_files.py
bash %{SOURCE3} src/3rdparty/chromium
rm -rf src/3rdparty/chromium/third_party/openh264/src

%patch -P2 -p1 -b .fix-extractcflag
%if !0%{?arm_neon}
%patch -P3 -p1 -b .no-neon
%endif
%patch -P4 -p1 -b .SIOCGSTAMP
%patch -P5 -p1 -b .QT_DEPRECATED_VERSION
%patch -P6 -p1 -b .angle_nullptr
%patch -P7 -p1 -b .hunspell_nullptr
#if 0%{?pipewire}
%patch -P8 -p1 -b .libpipewire-0.3
#endif

## upstream patches
%patch -P24 -p1 -b .aarch64-new-stat
%patch -P32 -p1 -b .skia-missing-includes
%patch -P34 -p1 -b .fix-build
%patch -P35 -p1 -b .c99

%patch -P60 -p1
%patch -P61 -p1
%patch -P62 -p1 -b .ffmpeg8
%patch -P70 -p1
%patch -P71 -p1
%patch -P73 -p1

%patch -P80 -p1

# RISC-V support patches
%patch -P100 -p1 -b .riscv64-v8
%patch -P101 -p1 -b .riscv64
%patch -P102 -p1 -b .riscv64-breakpad
%patch -P103 -p1 -b .riscv64-crashpad
%patch -P104 -p1 -b .riscv64-sandbox

# delete all "toolprefix = " lines from build/toolchain/linux/BUILD.gn, as we
# never cross-compile in native Fedora RPMs, fixes ARM and aarch64 FTBFS
sed -i -e '/toolprefix = /d' -e 's/\${toolprefix}//g' \
  src/3rdparty/chromium/build/toolchain/linux/BUILD.gn

# copy the Chromium license so it is installed with the appropriate name
cp -p src/3rdparty/chromium/LICENSE LICENSE.Chromium

# consider doing this as part of the tarball creation step instead?  rdieter
# fix/workaround
# fatal error: QtWebEngineCore/qtwebenginecoreglobal.h: No such file or directory
if [ ! -f "./include/QtWebEngineCore/qtwebenginecoreglobal.h" ]; then
%_qt5_bindir/syncqt.pl -version %{version}
fi

# abort if this doesn't get created by syncqt.pl
test -f "./include/QtWebEngineCore/qtwebenginecoreglobal.h"

%build

export STRIP=strip
export NINJAFLAGS="%{__ninja_common_opts}"
export NINJA_PATH=%{__ninja}
%{qmake_qt5} \
  %{?debug_config:CONFIG+="%{debug_config}}" \
  CONFIG+="link_pulseaudio" \
  QMAKE_EXTRA_ARGS+="-system-webengine-ffmpeg -system-webengine-webp -system-webengine-opus" \
  QMAKE_EXTRA_ARGS+="-webengine-kerberos -webengine-python-version python3" \
  %{?use_system_libicu:QMAKE_EXTRA_ARGS+="-system-webengine-icu"} \
  %{?pipewire:QMAKE_EXTRA_ARGS+="-webengine-webrtc-pipewire"} \
  .
make %{?_smp_mflags}
%install
make install INSTALL_ROOT=%{buildroot}
install -p -m644 -D %{SOURCE10} \
  %{buildroot}%{rpm_macros_dir}/macros.qt5-qtwebengine
sed -i \
  -e "s|@@NAME@@|%{name}|g" \
  -e "s|@@EPOCH@@|%{?epoch}%{!?epoch:0}|g" \
  -e "s|@@VERSION@@|%{version}|g" \
  -e "s|@@EVR@@|%{?epoch:%{epoch:}}%{version}-%{release}|g" \
  %{buildroot}%{rpm_macros_dir}/macros.qt5-qtwebengine
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
rm -fv Qt5WebEngineCore.la
popd
mkdir -p %{buildroot}%{_qtwebengine_dictionaries_dir}
%global lesser_version $(echo -e "%{version}\\n%{_qt5_version}" | sort -V | head -1)
sed -i -e "s|%{version} \${_Qt5WebEngine|%{lesser_version} \${_Qt5WebEngine|" \
  %{buildroot}%{_qt5_libdir}/cmake/Qt5WebEngine*/Qt5WebEngine*Config.cmake
%ldconfig_scriptlets
%filetriggerin -- %{_datadir}/myspell
while read filename ; do
  case "$filename" in
    *.dic)
      bdicname=%{_qtwebengine_dictionaries_dir}/`basename -s .dic "$filename"`.bdic
      %{_qt5_bindir}/qwebengine_convert_dict "$filename" "$bdicname" &> /dev/null || :
      ;;
  esac
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtwebengine-devel -f %{oreon_filedir}/qt5-qtwebengine-devel.list
%files -n qt5-qtwebengine-devtools -f %{oreon_filedir}/qt5-qtwebengine-devtools.list
%files -n qt5-qtwebengine-examples -f %{oreon_filedir}/qt5-qtwebengine-examples.list

%changelog

%autochangelog
