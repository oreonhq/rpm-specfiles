%global source0_hash 366b325101ab1a9a4ee79fbdb8e3dd9e78bcc0a21c0f9b1966313aaed3d33502

%global libzen_version  0.4.41

Name:           mediainfo
Version:        25.10
Release:        2%{?dist}
Summary:        Supplies technical and tag information about a video or audio file (CLI)

License:        BSD-2-Clause
URL:            http://mediaarea.net/MediaInfo
Source0:        http://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
Source1:        mediainfo-qt.desktop
Source2:        mediainfo-qt.kde4.desktop

ExclusiveArch:  %qt6_qtwebengine_arches

BuildRequires:  make
BuildRequires:  pkgconfig(libmediainfo) >= %{version}
BuildRequires:  pkgconfig(libzen) >= %{libzen_version}
BuildRequires:  wxWidgets-devel
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libtool
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  perl(Pod::Man)
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  pkgconfig(Qt6Gui)
BuildRequires:  pkgconfig(Qt6Network)
BuildRequires:  pkgconfig(Qt6Xml)
BuildRequires:  pkgconfig(Qt6WebEngineWidgets)
BuildRequires:  qt6-linguist
BuildRequires:  libappstream-glib

%description
MediaInfo CLI (Command Line Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, S-MI

%package gui
Summary:    Supplies technical and tag information about a video or audio file (GUI)
Requires:   libzen%{?_isa} >= %{libzen_version}
Requires:   libmediainfo%{?_isa} >= %{version}
Requires:   hicolor-icon-theme

%description gui
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%package qt
Summary:    Supplies technical and tag information about a video or audio file (Qt GUI)
Requires:   libzen%{?_isa} >= %{libzen_version}
Requires:   libmediainfo%{?_isa} >= %{version}

%description qt
MediaInfo (Graphical User Interface).

What information can I get from MediaInfo?
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

What format (container) does MediaInfo support?
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MediaInfo

sed -i 's/\r$//' *.txt *.html Release/*.txt

find Source -type f -exec chmod 644 {} ';'
chmod 644 *.html *.txt Release/*.txt

#https://fedorahosted.org/FedoraReview/wiki/AutoTools
sed -i 's/AC_PROG_LIBTOOL/LT_INIT/' Project/GNU/*/configure.ac

pushd Project/GNU/CLI
    autoreconf -fiv
    sed -i 's/enable_unicode="$(pkg-config --variable=Unicode libzen)"/enable_unicode=yes/' configure
popd

pushd Project/GNU/GUI
    autoreconf -fiv
    sed -i 's/enable_unicode="$(pkg-config --variable=Unicode libzen)"/enable_unicode=yes/' configure
popd

sed -i 's|TARGET = "mediainfo-gui"|TARGET = "mediainfo-qt"|' Project/QMake/GUI/MediaInfoQt.pro
sed -i 's|-ldl|-ldl -lmediainfo -lzen|' Project/QMake/GUI/MediaInfoQt.pro

pushd Source/GUI/Qt/Qt_Translations_Updater
    sed -i -e 's|lupdate|lupdate-qt6|' \
        -e 's|lrelease|lrelease-qt6|' update_Qt_translations.sh
    chmod +x ./update_Qt_translations.sh
    ./update_Qt_translations.sh
popd

%build
# build CLI
pushd Project/GNU/CLI
    %configure --enable-static=no
    %make_build
popd

# now build GUI
pushd Project/GNU/GUI
    %configure --enable-static=no
    %make_build
popd

# now build Qt GUI
pushd Project/QMake/GUI
    %{qmake_qt6}
    %make_build
popd

# generate manpages
pushd debian
    for i in *.pod; do
        pod2man --center "User Commands" --release="MediaInfo %{version}" \
            $i >../${i/%pod/1}
    done
popd

%install
pushd Project/GNU/CLI
    %make_install
popd

pushd Project/GNU/GUI
    %make_install
popd

pushd Project/QMake/GUI
#     make install INSTALL_ROOT=%{buildroot}
    install -m 755 %{name}-qt %{buildroot}%{_bindir}
popd

# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 -p Source/Resource/Image/MediaInfo.png \
    %{buildroot}%{_datadir}/pixmaps/%{name}.png

# menu-entry
install -dm 755 %{buildroot}%{_datadir}/applications
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" \
Project/GNU/GUI/%{name}-gui.desktop
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" %{SOURCE1}
install -m 644 -p %{SOURCE2} %{buildroot}%{_datadir}/kservices5/ServiceMenus/%{name}-qt.desktop
rm -rf %{buildroot}%{_datadir}/kde4
rm %{buildroot}%{_datadir}/kservices5/ServiceMenus/%{name}-gui.desktop

mkdir %{buildroot}%{_datadir}/appdata
mv %{buildroot}%{_datadir}/metainfo/%{name}-gui.metainfo.xml %{buildroot}%{_datadir}/appdata/%{name}-gui.appdata.xml
rm -rf %{buildroot}%{_datadir}/metainfo

# manpages
install -dm 755 %{buildroot}%{_mandir}/man1
install -m 644 -p %{name}*.1 %{buildroot}%{_mandir}/man1/

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/appdata/*.appdata.xml

%files
%doc Release/ReadMe_CLI_Linux.txt History_CLI.txt
%license License.html
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%files gui
%doc Release/ReadMe_GUI_Linux.txt History_GUI.txt
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/apps/konqueror/servicemenus/%{name}-gui.desktop
%{_datadir}/appdata/%{name}-gui.appdata.xml
%{_mandir}/man1/%{name}-gui.1*

%files qt
%doc Release/ReadMe_GUI_Linux.txt History_GUI.txt
%{_bindir}/%{name}-qt
%{_datadir}/applications/%{name}-qt.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/kservices5/ServiceMenus/%{name}-qt.desktop

%changelog
%autochangelog
