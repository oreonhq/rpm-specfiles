%global source0_hash f9cfeef7d4ddde78ad8978876cb3525843a302504f547c225e9c22c81d710760

%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10
%bcond_without kf6
%endif
# keep this in sync with phonon-backend-gstreamer
%global gstversion 1.0

%global __provides_exclude_from ^%{_libdir}/kid3/plugins/.*\\.so$

Name:           kid3
Version:        3.9.7
Release:        1%{?dist}
Summary:        Efficient KDE ID3 tag editor

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://kid3.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
%if %{with kf6}
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6DocTools)
%else
BuildRequires:  kf5-rpm-macros
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  cmake(Qt5Multimedia)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Svg)
BuildRequires:  cmake(Qt5QuickControls2)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5DocTools)
%endif
BuildRequires:  cmake
BuildRequires:  id3lib-devel
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  flac-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  pkgconfig(gstreamer-%{gstversion})
BuildRequires:  readline-devel
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  gcc-c++
Requires:       %{name}-common = %{version}-%{release}

%description
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC, MPC,
MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, and AIFF files
(e.g. full albums) without typing the same information again and again
and have control over both ID3v1 and ID3v2 tags, then Kid3 is the
program you are looking for.

%package        common
Summary:        Efficient command line ID3 tag editor
Recommends:     xdg-utils

%description    common
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC, MPC,
MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, and AIFF files
(e.g. full albums) without typing the same information again and again
and have control over both ID3v1 and ID3v2 tags, then Kid3 is the
program you are looking for.  The %{name}-common package provides Kid3
command line tool and files shared between all Kid3 variants.

%package        qt
Summary:        Efficient Qt ID3 tag editor
Requires:       %{name}-common = %{version}-%{release}

%description    qt
If you want to easily tag multiple MP3, Ogg/Vorbis, FLAC, MPC,
MP4/AAC, MP2, Speex, TrueAudio, WavPack, WMA, WAV, and AIFF files
(e.g. full albums) without typing the same information again and again
and have control over both ID3v1 and ID3v2 tags, then Kid3 is the
program you are looking for.  The %{name}-qt package provides Kid3
built without KDE dependencies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# lib64 stuff: //bugzilla.redhat.com/show_bug.cgi?id=1425064
%if %{with kf6}
%cmake_kf6 \
    -DBUILD_WITH_QT6=ON \
%else
%cmake_kf5 \
%endif
%if "%{?_lib}" == "lib64"
    %{?_cmake_lib_suffix64} \
%endif
    -DWITH_GSTREAMER=ON \
    -DWITH_GSTREAMER_VERSION=%{gstversion} \
    -DWITH_NO_MANCOMPRESS=ON
%cmake_build

%install

%cmake_install

install -dm 755 $RPM_BUILD_ROOT%{_pkgdocdir}
install -pm 644 AUTHORS ChangeLog README $RPM_BUILD_ROOT%{_pkgdocdir}

%find_lang %{name} --with-html --with-man
mv %{name}.lang %{name}-kde.lang
%find_lang %{name}-qt --with-man
%find_lang %{name}-cli --with-man
%find_lang %{name} --with-qt
cat %{name}.lang >> %{name}-cli.lang
cat <<EOF >> %{name}-cli.lang
%%dir %%{_datadir}/kid3/
%%dir %%{_datadir}/kid3/translations/
EOF

%check
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml

%files -f %{name}-kde.lang
%{_bindir}/kid3
%{_datadir}/metainfo/org.kde.kid3.appdata.xml
%{_datadir}/icons/hicolor/*x*/apps/kid3.png
%{_datadir}/icons/hicolor/scalable/apps/kid3.svgz
%{_datadir}/applications/org.kde.kid3.desktop
%{_datadir}/kxmlgui5/%{name}

%files common -f %{name}-cli.lang
%{_bindir}/kid3-cli
%{_libdir}/kid3/
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/kid3/qml/
%{_mandir}/man1/kid3.1*
%{_mandir}/man1/kid3-cli.1*
%license COPYING LICENSE
%{_pkgdocdir}/

%files qt -f %{name}-qt.lang
%{_bindir}/kid3-qt
%{_datadir}/metainfo/org.kde.kid3-qt.appdata.xml
%{_datadir}/applications/org.kde.kid3-qt.desktop
%{_datadir}/icons/hicolor/*x*/apps/kid3-qt.png
%{_datadir}/icons/hicolor/scalable/apps/kid3-qt.svg
%dir %{_docdir}/kid3-qt/
%lang(de) %{_docdir}/kid3-qt/kid3_de.html
%lang(en) %{_docdir}/kid3-qt/kid3_en.html
%lang(pt) %{_docdir}/kid3-qt/kid3_pt.html
%lang(ca) %{_docdir}/kid3-qt/kid3_ca.html
%lang(it) %{_docdir}/kid3-qt/kid3_it.html
%lang(nl) %{_docdir}/kid3-qt/kid3_nl.html
%lang(sv) %{_docdir}/kid3-qt/kid3_sv.html
%lang(uk) %{_docdir}/kid3-qt/kid3_uk.html
%lang(ru) %{_docdir}/kid3-qt/kid3_ru.html
%{_mandir}/man1/kid3-qt.1*

%changelog
%autochangelog
