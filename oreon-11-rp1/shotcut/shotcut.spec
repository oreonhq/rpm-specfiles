%global source0_hash 756435135cff15129f720611e750fe8fedfc9c816c9356943f0079618b6f1c6f
%global org_name_shotcut org.%{name}.Shotcut
%global __provides_exclude_from ^%{_libdir}/%{name}/libCuteLogger\\.so
%global __requires_exclude ^libCuteLogger\\.so
Name:           shotcut
Version:        26.9.6
Release:        1%{?dist}
Summary:        A free, open source, cross-platform video editor
License:        GPL-3.0-or-later AND LGPL-2.1-only AND Apache-2.0 AND MIT
URL:            http://www.shotcut.org/
Source0:        https://github.com/mltframework/shotcut/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
%if %{undefined flatpak}
Requires:       gstreamer1-plugins-bad-free-extras
Requires:       frei0r-plugins
%endif
Requires:       qt6-qt5compat
Requires:       ladspa
Requires:       lame
Requires:       /usr/bin/ffmpeg
Suggests:       ladspa-swh-plugins
# oreon:deps
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fftw-devel
BuildRequires:  gcc-c++
BuildRequires:  hardlink
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(Qt6Charts)
BuildRequires:  pkgconfig(Qt6Concurrent)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Linguist)
BuildRequires:  pkgconfig(Qt6Multimedia)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6OpenGL)
BuildRequires:  pkgconfig(Qt6PrintSupport)
BuildRequires:  pkgconfig(Qt6Quick)
BuildRequires:  pkgconfig(Qt6QuickControls2)
BuildRequires:  pkgconfig(Qt6QuickWidgets)
BuildRequires:  pkgconfig(Qt6WebSockets)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(mlt++-7)
BuildRequires:  pkgconfig(mlt-framework-7)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  webvfx-devel
# /oreon:deps
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
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0

# Postmortem debugging tools for MinGW.
rm -rf drmingw
# remove due MLT 7
sed -i 's/^\(\s*\)s\.set_consumer(\*saveConsumer);/\1\/\/ s.set_consumer(*saveConsumer); \/\/ remove due MLT 7/' src/mltcontroller.cpp

%build

%set_build_flags
export LDFLAGS="%{build_ldflags} -Wl,-rpath,%{_libdir}/%{name}"
%cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
       -DUNIX_STRUCTURE=1 -GNinja \
       -DCMAKE_BUILD_TYPE=Release \
       -DSHOTCUT_VERSION=%{version} \
       -DDEFINES+=SHOTCUT_NOUPGRADE
%cmake_build
doxygen -u CuteLogger/Doxyfile
doxygen CuteLogger/Doxyfile
%install
%cmake_install
chmod a+x %{buildroot}/%{_datadir}/shotcut/qml/export-edl/rebuild.sh
chmod a+x %{buildroot}/%{_datadir}/shotcut/qml/export-chapters/rebuild.sh
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
mkdir -p %{buildroot}%{_libdir}/%{name}
mv %{buildroot}%{_libdir}/libCuteLogger.so %{buildroot}%{_libdir}/%{name}/
hardlink -v %{buildroot}%{_datadir}/shotcut/qml/filters
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{org_name_shotcut}.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_metainfodir}/%{org_name_shotcut}.metainfo.xml
%files -f %{oreon_filedir}/main.list
%files -n shotcut-doc -f %{oreon_filedir}/shotcut-doc.list
%files -n shotcut-langpack-ar -f %{oreon_filedir}/shotcut-langpack-ar.list
%files -n shotcut-langpack-ca -f %{oreon_filedir}/shotcut-langpack-ca.list
%files -n shotcut-langpack-cs -f %{oreon_filedir}/shotcut-langpack-cs.list
%files -n shotcut-langpack-da -f %{oreon_filedir}/shotcut-langpack-da.list
%files -n shotcut-langpack-de -f %{oreon_filedir}/shotcut-langpack-de.list
%files -n shotcut-langpack-el -f %{oreon_filedir}/shotcut-langpack-el.list
%files -n shotcut-langpack-en_GB -f %{oreon_filedir}/shotcut-langpack-en_GB.list
%files -n shotcut-langpack-en -f %{oreon_filedir}/shotcut-langpack-en.list
%files -n shotcut-langpack-es -f %{oreon_filedir}/shotcut-langpack-es.list
%files -n shotcut-langpack-et -f %{oreon_filedir}/shotcut-langpack-et.list
%files -n shotcut-langpack-eu -f %{oreon_filedir}/shotcut-langpack-eu.list
%files -n shotcut-langpack-fi -f %{oreon_filedir}/shotcut-langpack-fi.list
%files -n shotcut-langpack-fr_CA -f %{oreon_filedir}/shotcut-langpack-fr_CA.list
%files -n shotcut-langpack-fr -f %{oreon_filedir}/shotcut-langpack-fr.list
%files -n shotcut-langpack-ga -f %{oreon_filedir}/shotcut-langpack-ga.list
%files -n shotcut-langpack-gd -f %{oreon_filedir}/shotcut-langpack-gd.list
%files -n shotcut-langpack-gl -f %{oreon_filedir}/shotcut-langpack-gl.list
%files -n shotcut-langpack-he_IL -f %{oreon_filedir}/shotcut-langpack-he_IL.list
%files -n shotcut-langpack-hu -f %{oreon_filedir}/shotcut-langpack-hu.list
%files -n shotcut-langpack-it -f %{oreon_filedir}/shotcut-langpack-it.list
%files -n shotcut-langpack-ja -f %{oreon_filedir}/shotcut-langpack-ja.list
%files -n shotcut-langpack-ko -f %{oreon_filedir}/shotcut-langpack-ko.list
%files -n shotcut-langpack-lt -f %{oreon_filedir}/shotcut-langpack-lt.list
%files -n shotcut-langpack-nb -f %{oreon_filedir}/shotcut-langpack-nb.list
%files -n shotcut-langpack-ne -f %{oreon_filedir}/shotcut-langpack-ne.list
%files -n shotcut-langpack-nl -f %{oreon_filedir}/shotcut-langpack-nl.list
%files -n shotcut-langpack-nn -f %{oreon_filedir}/shotcut-langpack-nn.list
%files -n shotcut-langpack-oc -f %{oreon_filedir}/shotcut-langpack-oc.list
%files -n shotcut-langpack-pl -f %{oreon_filedir}/shotcut-langpack-pl.list
%files -n shotcut-langpack-pt_BR -f %{oreon_filedir}/shotcut-langpack-pt_BR.list
%files -n shotcut-langpack-pt_PT -f %{oreon_filedir}/shotcut-langpack-pt_PT.list
%files -n shotcut-langpack-ro -f %{oreon_filedir}/shotcut-langpack-ro.list
%files -n shotcut-langpack-ru -f %{oreon_filedir}/shotcut-langpack-ru.list
%files -n shotcut-langpack-sk -f %{oreon_filedir}/shotcut-langpack-sk.list
%files -n shotcut-langpack-sl -f %{oreon_filedir}/shotcut-langpack-sl.list
%files -n shotcut-langpack-sv -f %{oreon_filedir}/shotcut-langpack-sv.list
%files -n shotcut-langpack-th -f %{oreon_filedir}/shotcut-langpack-th.list
%files -n shotcut-langpack-tr -f %{oreon_filedir}/shotcut-langpack-tr.list
%files -n shotcut-langpack-uk -f %{oreon_filedir}/shotcut-langpack-uk.list
%files -n shotcut-langpack-zh_CN -f %{oreon_filedir}/shotcut-langpack-zh_CN.list
%files -n shotcut-langpack-zh_TW -f %{oreon_filedir}/shotcut-langpack-zh_TW.list

%changelog

%autochangelog
