%global source0_hash 7556eb98e2d156aca08913ec91d1180aaef3f7e73397f5ec54304d6e82a5a869
%global libmediainfo_version    23.10
%global libzen_version          0.4.41
Name:           mediaconch
Version:        25.04
Release:        2%{?dist}
Summary:        Most relevant technical and tag data for video and audio files (CLI)
License:        LicenseRef-Callaway-BSD
URL:            https://mediaarea.net/MediaConch/
Source0:        https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
Patch0:         https://github.com/MediaArea/MediaConch_SourceCode/pull/803.patch
ExclusiveArch:  %{qt6_qtwebengine_arches}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  pkgconfig(jansson)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(libmediainfo)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libxslt)
BuildRequires:  pkgconfig(libzen)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtwebengine-devel
BuildRequires:  systemd
# /oreon:deps
%description
MediaConch is an implementation checker, policy checker, reporter,
and fixer that targets preservation-level audiovisual files
(specifically Matroska, Linear Pulse Code Modulation (LPCM)
and FF Video Codec 1 (FFV1)).

This project is maintained by MediaArea and funded by PREFORMA.

This package includes the command line interface.

%package gui
Summary:    Supplies technical and tag information about a video or audio file (GUI)
Requires:   hicolor-icon-theme
%description gui
MediaConch is an implementation checker, policy checker, reporter,
and fixer that targets preservation-level audiovisual files
(specifically Matroska, Linear Pulse Code Modulation (LPCM)
and FF Video Codec 1 (FFV1)).

This project is maintained by MediaArea and funded by PREFORMA.

This package includes the graphical user interface.

%package server
Summary:    Supplies technical and tag information about a video or audio file (Server)
%{?systemd_requires}
%description server
MediaConch is an implementation checker, policy checker, reporter,
and fixer that targets preservation-level audiovisual files
(specifically Matroska, Linear Pulse Code Modulation (LPCM)
and FF Video Codec 1 (FFV1)).

This project is maintained by MediaArea and funded by PREFORMA.

This package includes the server.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MediaConch -p1
rm -rf Source/ThirdParty/sqlite
sed -i 's/.$//' *.txt *.html Release/*.txt

sed -i 's/AC_PROG_LIBTOOL/LT_INIT([disable-static])/' Project/GNU/CLI/configure.ac
sed -i 's/AC_PROG_LIBTOOL/LT_INIT([disable-static])/' Project/GNU/Server/configure.ac

pushd Project/GNU/CLI
    autoreconf -fiv
popd

pushd Project/GNU/Server
    autoreconf -fiv
popd

%build

pushd Project/GNU/CLI
    %configure --enable-static=no
    %make_build
popd
pushd Project/GNU/Server
    %configure --enable-static=no
    %make_build
popd
pushd Project/Qt
    %{qmake_qt6}
    %make_build
popd
%install
pushd Project/GNU/CLI
    %make_install
popd
pushd Project/GNU/Server
    %make_install
popd
pushd Project/Qt
    install -dm 755 %{buildroot}%{_bindir}
    install -m 755 -p mediaconch-gui %{buildroot}%{_bindir}
popd
install -dm 755 %{buildroot}%{_datadir}/icons/hicolor/256x256/apps
install -m 644 -p Source/Resource/Image/MediaConch.png %{buildroot}%{_datadir}/icons/hicolor/256x256/apps/%{name}.png
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 -p Source/Resource/Image/MediaConch.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -dm 755 %{buildroot}%{_datadir}/applications
install -m 644 -p Project/GNU/GUI/mediaconch-gui.desktop %{buildroot}%{_datadir}/applications
desktop-file-install --dir="%{buildroot}%{_datadir}/applications" -m 644 Project/GNU/GUI/mediaconch-gui.desktop
install -dm 755 %{buildroot}%{_datadir}/appdata/
install -m 644 -p Project/GNU/GUI/mediaconch-gui.metainfo.xml %{buildroot}%{_datadir}/appdata/mediaconch-gui.appdata.xml
install -dm 755 %{buildroot}%{_unitdir}
install -m 644 -p Project/GNU/Server/mediaconchd.service  %{buildroot}%{_unitdir}/mediaconchd.service
install -dm 755 %{buildroot}%{_sysconfdir}/%{name}
install -m 644 -p Project/GNU/Server/MediaConch.rc  %{buildroot}%{_sysconfdir}/%{name}/MediaConch.rc
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml
%post server

%systemd_post mediaconchd.service
%preun server

%systemd_preun mediaconchd.service
%postun server

%systemd_postun_with_restart mediaconchd.service
%files -f %{oreon_filedir}/main.list
%files -n mediaconch-gui -f %{oreon_filedir}/mediaconch-gui.list
%files -n mediaconch-server -f %{oreon_filedir}/mediaconch-server.list

%changelog

%autochangelog
