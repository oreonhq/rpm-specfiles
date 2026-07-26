%global source0_hash b5c840a459eaf4ad9e0ad7a02d782678207f9102cfce7f129f413fe2c0cb3ca8

%global org_name_shotcut org.%{name}.Shotcut
%global __provides_exclude_from ^%{_libdir}/%{name}/libCuteLogger\\.so
%global __requires_exclude ^libCuteLogger\\.so

Name:           shotcut
Version:        26.2.26
Release:        1%{?dist}
Summary:        A free, open source, cross-platform video editor
# Main code is GPLv3+
License:        GPL-3.0-or-later AND LGPL-2.1-only AND Apache-2.0 AND MIT
# LGPL-2.1-only:
# CuteLogger/include/AbstractAppender.h
# CuteLogger/include/AbstractStringAppender.h
# CuteLogger/include/ConsoleAppender.h
# CuteLogger/include/FileAppender.h
# CuteLogger/include/Logger.h
# CuteLogger/include/OutputDebugAppender.h
# CuteLogger/src/AbstractAppender.cpp
# CuteLogger/src/AbstractStringAppender.cpp
# CuteLogger/src/ConsoleAppender.cpp
# CuteLogger/src/FileAppender.cpp
# CuteLogger/src/Logger.cpp
# CuteLogger/src/OutputDebugAppender.cpp

# Apache-2.0:
# src/spatialmedia/box.cpp
# src/spatialmedia/box.h
# src/spatialmedia/constants.h
# src/spatialmedia/container.cpp
# src/spatialmedia/container.h
# src/spatialmedia/mpeg4_container.cpp
# src/spatialmedia/mpeg4_container.h
# src/spatialmedia/sa3d.cpp
# src/spatialmedia/sa3d.h
# src/spatialmedia/spatialmedia.cpp
# src/spatialmedia/spatialmedia.h

# MIT:
# doc/html/clipboard.js
# doc/html/dynsections.js
# doc/html/jquery.js:
# doc/html/menu.js
# doc/html/menudata.js
# doc/html/resize.js

URL:            http://www.shotcut.org/
Source0:        https://github.com/mltframework/shotcut/archive/v%{version}/%{name}-%{version}.tar.gz

ExcludeArch:    %{ix86}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core) >= 6.4.0
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(mlt++-7) >= 7.36.0
BuildRequires:  pkgconfig(mlt-framework-7) >= 7.36.0
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  webvfx-devel
BuildRequires:  fftw-devel

%if %{undefined flatpak}
Requires:       gstreamer1-plugins-bad-free-extras
Requires:       frei0r-plugins
%endif
Requires:       qt6-qt5compat
Requires:       ladspa
Requires:       lame
Requires:       /usr/bin/ffmpeg
# Remove duplicate files and create hardlinks
BuildRequires: hardlink

# audio filters
Suggests:       ladspa-swh-plugins

%description
Shotcut is a free and open-source cross-platform video editing application for
Windows, OS X, and Linux. 

Shotcut supports many video, audio, and image formats via FFmpeg and screen, 
webcam, and audio capture. It uses a time-line for non-linear video editing of 
multiple tracks that may be composed of various file formats. Scrubbing and 
transport control are assisted by OpenGL GPU-based processing and a number of 
video and audio filters are available.

%package        doc
Summary:        Documentation files for %{name}
BuildArch:      noarch

%description    doc
The %{name}-doc package contains html documentation
that use %{name}.

%define         lang_subpkg() \
%package        langpack-%{1}\
Summary:        %{2} language data for %{name}\
BuildArch:      noarch \
Requires:       %{name} = %{version}-%{release}\
Supplements:    (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description    langpack-%{1}\
%{2} language data for %{name}.\
\
%files          langpack-%{1}\
%{_datadir}/%{name}/translations/%{name}_%{1}*.qm

%lang_subpkg ar Arabic
%lang_subpkg ca Catalan
%lang_subpkg cs Czech
%lang_subpkg da Danish
%lang_subpkg de German
%lang_subpkg el Greek
%lang_subpkg en_GB "(Great Britain)"
%lang_subpkg en English
%lang_subpkg es Spanish
%lang_subpkg et Estonian
%lang_subpkg eu Euskara
%lang_subpkg fi Finnish
%lang_subpkg fr_CA "(Canadian French)"
%lang_subpkg fr French
%lang_subpkg ga "(Irish Gaeilge)"
%lang_subpkg gd "(Scottish Gaelic)"
%lang_subpkg gl Galician
%lang_subpkg he_IL Hebrew
%lang_subpkg hu Hungarian
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg ko Korean
%lang_subpkg lt Lithuanian
%lang_subpkg nb Norwegian
%lang_subpkg ne Nepali
%lang_subpkg nl Dutch
%lang_subpkg nn Norwegian
%lang_subpkg oc Occitan
%lang_subpkg pl Polish
%lang_subpkg pt_BR "Portuguese (Brazil)"
%lang_subpkg pt_PT "Portuguese (Portugal)"
%lang_subpkg ro Romanian
%lang_subpkg ru Russian
%lang_subpkg sk Slovakian
%lang_subpkg sl Slovenian
%lang_subpkg sv Swedish
%lang_subpkg th Thai
%lang_subpkg tr Turkish
%lang_subpkg uk Ukrainian
%lang_subpkg zh_CN "Chinese (S)"
%lang_subpkg zh_TW "Chinese (T)"

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# Postmortem debugging tools for MinGW.
rm -rf drmingw
# remove due MLT 7
sed -i 's/^\(\s*\)s\.set_consumer(\*saveConsumer);/\1\/\/ s.set_consumer(*saveConsumer); \/\/ remove due MLT 7/' src/mltcontroller.cpp

%build
%set_build_flags
# Add RUNPATH pointing to %%{_libdir}/shotcut
export LDFLAGS="%{build_ldflags} -Wl,-rpath,%{_libdir}/%{name}"
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DUNIX_STRUCTURE=1 -GNinja \
       -DCMAKE_BUILD_TYPE=Release \
       -DSHOTCUT_VERSION=%{version} \
       -DDEFINES+=SHOTCUT_NOUPGRADE
%cmake_build

# update Doxyfile
doxygen -u CuteLogger/Doxyfile
# build docs
doxygen CuteLogger/Doxyfile

%install
%cmake_install
chmod a+x %{buildroot}/%{_datadir}/shotcut/qml/export-edl/rebuild.sh
chmod a+x %{buildroot}/%{_datadir}/shotcut/qml/export-chapters/rebuild.sh

# Install language files
langlist="$PWD/%{name}.lang"
langdir="%{_datadir}/%{name}/translations"
basedir=$(basename "$langdir")
pushd $basedir
        for ts in *.ts; do
                [ -e "$ts" ] || continue
                lupdate-qt6 "$ts" && lrelease-qt6 "$ts"
        done
        for qm in *.qm; do
                [ -e "$qm" ] || continue
                if ! grep -wqs "%dir $langdir" "$langlist"; then
                        echo "%dir $langdir" >>"$langlist"
                fi
                install -Dm0644 "$qm" "%{buildroot}/$langdir/$qm"
                lang="${qm%.qm}"
                echo "%lang($lang) $langdir/$qm" >>"$langlist"
        done
popd

# A shared library without SONAME in %%{_libdir} should be moved out of linker search path
# Move the shared library to a package-specific directory
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/libCuteLogger.so %{buildroot}%{_libdir}/%{name}/

# Remove duplicate files and create hardlinks
hardlink -v %{buildroot}%{_datadir}/shotcut/qml/filters

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{org_name_shotcut}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{org_name_shotcut}.metainfo.xml

%files
%doc README.md
%license COPYING
%{_bindir}/%{name}
%{_libdir}/%{name}/libCuteLogger.so
%{_datadir}/%{name}/
%exclude %{_datadir}/%{name}/translations
%{_datadir}/applications/%{org_name_shotcut}.desktop
%{_datadir}/icons/hicolor/*/apps/%{org_name_shotcut}.png
%{_metainfodir}/%{org_name_shotcut}.metainfo.xml
%{_datadir}/mime/packages/%{org_name_shotcut}.xml
%{_mandir}/man1/%{name}.1.*

%files doc
%license COPYING
%doc doc

%changelog
%autochangelog
