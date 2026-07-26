%global source0_hash none

# Compile options:
# invoke with: rpmbuild --with ffmpeg --with local_ffmpeg audacity.spec to use local ffmpeg
%bcond_without  ffmpeg
%bcond_with     local_ffmpeg

#global commit0 53a5c930a4b5b053ab06a8b975458fc51cf41f6c
#global shortcommit0 #(c=#{commit0}; echo ${c:0:7})

# Ignore these libraries because they are internal-only and should never be exposed in the RPM database
%global __requires_exclude ^lib-.*.so
%global __provides_exclude ^lib-.*.so

Name: audacity

Version: 3.7.7
Release: 5%{?dist}
Summary: Multitrack audio editor
License: GPL-2.0-or-later AND GPL-3.0-only AND CC-BY-3.0
URL:     https://www.audacityteam.org/

Source0: https://github.com/audacity/audacity/releases/download/Audacity-%{version}/%{name}-sources-%{version}.tar.gz
# Temporary, 3.7.7 didn't release a manual
#Source1: https://github.com/audacity/audacity/releases/download/Audacity-%{version}/%{name}-manual-%{version}.tar.gz
Source1: https://github.com/audacity/audacity/releases/download/Audacity-3.7.6/%{name}-manual-3.7.6.tar.gz

Patch0: fix_data_path.patch
Patch1: rapidjson.patch

BuildRequires: cmake
BuildRequires: gettext-devel

%if 0%{?rhel} == 7
BuildRequires: devtoolset-7-toolchain, devtoolset-7-libatomic-devel
%endif
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: chrpath

BuildRequires: alsa-lib-devel
BuildRequires: desktop-file-utils
BuildRequires: expat-devel
BuildRequires: flac-devel
BuildRequires: git
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: lame-devel
BuildRequires: libid3tag-devel
BuildRequires: libmpg123-devel
BuildRequires: taglib-devel
%if 0%{?rhel} && 0%{?rhel} == 8
#note: epel-8 currently doesn't have twolame-devel.
%else
BuildRequires: twolame-devel
%endif
BuildRequires: libogg-devel
BuildRequires: libsndfile-devel
BuildRequires: libvorbis-devel
BuildRequires: libuuid-devel
BuildRequires: portaudio-devel >= 19-16
BuildRequires: portmidi-devel
BuildRequires: soundtouch-devel
BuildRequires: soxr-devel
BuildRequires: sqlite-devel >= 3.32
BuildRequires: vamp-plugin-sdk-devel >= 2.0
BuildRequires: wavpack-devel
BuildRequires: zip
BuildRequires: zlib-devel
BuildRequires: python3
BuildRequires: rapidjson-devel
BuildRequireS: opusfile-devel
BuildRequires: libjpeg-turbo-devel turbojpeg
# We need /usr/bin/wx-config so that configure can detect the wx-config version:
#if 0#{?rhel} || 0#{?fedora} < 28
#BuildRequires: wxGTK3-devel
#endif
# But we will actually use the --toolkit=gtk2 version using --with-wx-version
#BuildRequires: compat-wxGTK3-gtk2-devel
BuildRequires: wxGTK-devel
%if 0%{?rhel} >= 8 || 0%{?fedora}
BuildRequires: libappstream-glib
%endif

%if %{with ffmpeg}
%if ! %{with local_ffmpeg}
BuildRequires: ffmpeg-free-devel
%endif
%endif

# LV2 interface and the plugins used
BuildRequires: lv2-devel >= 1.16
BuildRequires: lilv-devel >= 0.24.6
BuildRequires: serd-devel >= 0.30.2
BuildRequires: sord-devel >= 0.16.4
BuildRequires: sratom-devel >= 0.6.4
BuildRequires: suil-devel  >= 0.10.6

# For new symbols in portaudio
Requires:      portaudio%{?_isa} >= 19-16

# We force the GDK backend to be X11 in the launcher, so we need to ensure we have Xwayland available
%if !0%{?flatpak}
Requires:      xorg-x11-server-Xwayland
%endif

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86} s390x

%description
Audacity is a cross-platform multitrack audio editor. It allows you to
record sounds directly or to import files in various formats. It features
a few simple effects, all of the editing features you should need, and
unlimited undo. The GUI was built with wxWidgets and the audio I/O
supports PulseAudio, OSS and ALSA under Linux.

%package manual
Summary: Manual for Audacity - Offline Install
BuildArch: noarch
# -manual suits either audacity or audacity-freeworld; both create the path:
%if 0%{?fedora} || 0%{?rhel} >= 9
Requires: (audacity or audacity-freeworld)
%else
Requires: /usr/bin/audacity
%endif

%description manual
Audacity Manual can be installed locally if preferred, or accessed on-line
if internet connection is available.
For the most up to date manual content, use the on-line manual.

%prep
%setup -q -n %{name}-sources-%{version}

%patch -P 0 -p1
%patch -P 1 -p1

# fix building translations with gettext-0.22 (#2225711), fixed in 3.4
sed -i -e 's|%hs|%s|g' locale/*.po

%build
export CFLAGS="$CFLAGS -std=gnu17"
%if 0%{?rhel} == 7
export WX_CONFIG=wx-config-3.0
%endif

%if 0%{?rhel} == 7
. /opt/rh/devtoolset-7/enable
%endif

%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DwxWidgets_CONFIG_EXECUTABLE="$(which wx-config-3.2)" \
    -DAUDACITY_BUILD_LEVEL:STRING=2 \
    -Daudacity_conan_enabled=Off \
    -Daudacity_has_networking=Off \
    -Daudacity_has_crashreports=Off \
    -Daudacity_has_updates_check=Off \
    -Daudacity_has_sentry_reporting=Off \
    -Daudacity_has_vst3=Off \
    -Daudacity_lib_preference=system \
    -Daudacity_obey_system_dependencies=On \
    -Daudacity_use_wxwidgets=system \
    -Daudacity_use_uuid=system \
    -Daudacity_use_sqlite=system \
    -Daudacity_use_libsndfile=system \
    -Daudacity_use_soxr=system \
    -Daudacity_use_lame=system \
%if 0%{?rhel} == 8
    -Daudacity_use_twolame=off \
%else
    -Daudacity_use_twolame=system \
%endif
    -Daudacity_use_libflac=system \
    -Daudacity_use_ladspa=on \
    -Daudacity_use_libvorbis=system \
    -Daudacity_use_libid3tag=system \
    -Daudacity_use_expat=system \
    -Daudacity_use_soundtouch=system \
    -Daudacity_use_vamp=system \
    -Daudacity_use_lv2=system \
    -Daudacity_use_portaudio=system \
    -Daudacity_use_midi=system \
    -Daudacity_use_libogg=system \
%if %{with ffmpeg}
%if ! %{with local_ffmpeg}
    -Daudacity_use_ffmpeg=loaded \
%endif
%else
    -Daudacity_use_ffmpeg=off \
%endif
    -Daudacity_use_portsmf=local \
    -Daudacity_use_sbsms=local \
    -Daudacity_use_wavpack=system \

%cmake_build

%install
%cmake_install

rm -Rf %{buildroot}%{_datadir}/%{name}/include
rm -Rf %{buildroot}%{_bindir}/../%{name}

# Remove the RPATH from all the private libraries provided with Audacity and
# make them all executable so that debug symbol extraction happens.
# CMake could do this on its own using the install target for the library,
# but the Audacity build system manually copies around the libraries so it
# doesn't use the install target. This is very involved to fix in the code,
# so this work around is easier and more maintainable than patching the build
# system.
pushd %{buildroot}%{_libdir}/%{name}
for libFile in *;
do
    if [[ ! -d $libFile ]];
    then
        chrpath --delete $libFile
        chmod 755 $libFile
    fi
done
popd

pushd %{buildroot}%{_libdir}/%{name}/modules
for libFile in *;
do
    if [[ ! -d $libFile ]];
    then
        chrpath --delete $libFile
        chmod 755 $libFile
    fi
done
popd

%if 0%{?rhel} >= 8 || 0%{?fedora}
if appstream-util --help | grep -q replace-screenshots ; then
# Update the screenshot shown in the software center
#
# NOTE: It would be *awesome* if this file was pushed upstream.
#
# See http://people.freedesktop.org/~hughsient/appdata/#screenshots for more details.
#
appstream-util replace-screenshots %{buildroot}%{_metainfodir}/audacity.appdata.xml \
  https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/audacity/a.png
fi
%endif

# audacity manual must be extracted to correct location
pushd %{buildroot}%{_datadir}/%{name}
gzip -dc %{SOURCE1} | tar -xvvf -
#unzip %{SOURCE1}
#mv %{name}-manual-%{version}/* .
mv help/manual/* .
#rmdir %{name}-manual-%{version}
rmdir -p help/manual
popd

%{find_lang} %{name}

desktop-file-install --dir %{buildroot}{_datadir}/applications \
        %{buildroot}%{_datadir}/applications/audacity.desktop

mkdir %{buildroot}%{_datadir}/doc/%{name}/nyquist
cp -pr lib-src/libnyquist/nyquist/license.txt %{buildroot}%{_datadir}/doc/%{name}/nyquist
cp -pr lib-src/libnyquist/nyquist/Readme.txt %{buildroot}%{_datadir}/doc/%{name}/nyquist
rm %{buildroot}%{_datadir}/doc/%{name}/LICENSE.txt

%files -f %{name}.lang
%{_bindir}/%{name}
%{_libdir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/EffectsMenuDefaults.xml
%{_datadir}/%{name}/nyquist/
%{_datadir}/%{name}/plug-ins/
%exclude %{_datadir}/%{name}/favicon.ico
%exclude %{_datadir}/%{name}/index.html
%exclude %{_datadir}/%{name}/quick_help.html
%exclude %{_datadir}/%{name}/man/
%exclude %{_datadir}/%{name}/m/
%{_mandir}/man*/*
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/*/%{name}.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/mime/packages/*
%{_datadir}/doc/%{name}
%license LICENSE.txt

%files manual
%{_datadir}/%{name}/favicon.ico
%{_datadir}/%{name}/index.html
%{_datadir}/%{name}/quick_help.html
%{_datadir}/%{name}/man/
%{_datadir}/%{name}/m/

%changelog
%autochangelog
