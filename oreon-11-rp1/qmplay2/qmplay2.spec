%global source0_hash 26ed1b33e38cc39635d363e2860a36dbc8b97b5e35f4b4dc7dffd6192fecf498
%global pname QMPlay2
%global __provides_exclude_from ^%{_libdir}/%{name}/modules/.*$
%undefine _strict_symbol_defs_build
Name:           qmplay2
Version:        26.08.02
Release:        1%{?dist}
Summary:        A Qt based media player, streamer and downloader
License:        LGPL-3.0-or-later AND MIT AND LicenseRef-Fedora-Public-Domain
URL:            https://github.com/zaps166/QMPlay2
Source0:        https://github.com/zaps166/%{pname}/releases/download/%{version}/%{pname}-src-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:       hicolor-icon-theme
Requires:       kde-filesystem
Requires:       shared-mime-info
Recommends:     yt-dlp
Provides:       bundled(libbs2b) = 3.1.0
Provides:       bundled(libmodplug)
Provides:       bundled(qmvk)
Obsoletes:      %{name}-kde-integration < %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  glslc
BuildRequires:  libappstream-glib
BuildRequires:  ninja-build
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libcddb)
BuildRequires:  pkgconfig(libcdio)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libpulse-simple)
BuildRequires:  pkgconfig(libsidplayfp)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(rubberband)
BuildRequires:  pkgconfig(taglib)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xv)
# /oreon:deps
%description
%{name} is a video player, it can play and stream all formats supported by
ffmpeg and libmodplug (including J2B). It has an integrated Youtube browser.

%package        devel
Summary:        %{pname} development files
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
It's a development package for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pname}-src-%{version}
# unbundle vulkan headers
find src/qmplay2/vulkan/headers -delete
# subproject and bundled license files
cp src/qmvk/LICENSE LICENSE.qmvk
cp src/modules/Modplug/libmodplug/COPYING COPYING.libmodplug

%build

%cmake \
    -G Ninja \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_UPDATES=OFF \
    -DSOLID_ACTIONS_INSTALL_PATH=%{_datadir}/solid/actions
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-qt
rm -f %{buildroot}%{_datadir}/qmplay2/{LICENSE,README.md}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{pname}*.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{pname}.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n qmplay2-devel -f %{oreon_filedir}/qmplay2-devel.list

%changelog

%autochangelog
