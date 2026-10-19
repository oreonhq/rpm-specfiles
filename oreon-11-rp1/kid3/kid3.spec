%global source0_hash 020c357c74c39c931435b49e7409328d0b7f6da5491b58c2f732ed7236ea9a45
%if 0%{?fedora} >= 40 || 0%{?rhel} >= 10 || 0%{?oreon} >= 11
%bcond_without kf6
%endif
%global gstversion 1.0
%global __provides_exclude_from ^%{_libdir}/kid3/plugins/.*\\.so$
Name:           kid3
Version:        3.10.1
Release:        1%{?dist}
Summary:        Efficient KDE ID3 tag editor
License:        GPL-2.0-or-later
URL:            https://kid3.kde.org/
Source0:        https://download.kde.org/stable/%{name}/%{version}/%{name}-%{version}.tar.xz
%if %{with kf6}
%else
%endif
Requires:       %{name}-common = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  extra-cmake-modules
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  id3lib-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  libchromaprint-devel
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  readline-devel
BuildRequires:  taglib-devel
# /oreon:deps
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
%oreon_prep
%build

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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT%{_datadir}/metainfo/*.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kid3-common -f %{oreon_filedir}/kid3-common.list
%files -n kid3-qt -f %{oreon_filedir}/kid3-qt.list

%changelog

%autochangelog
