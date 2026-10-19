%global source0_hash aba4679a5b1f2bf62482eba6e8814a94de7ffc86de5f8587ba199fcc61b4a04f
Name:		allegro5
Version:	5.2.11.3
Release:        1%{?dist}
Summary:        A game programming library
License:	zlib
URL:		http://liballeg.org/
Source0:        https://github.com/liballeg/allegro5/releases/download/%{version}/allegro-%{version}.tar.gz
%global so_version %(c="%{version}"; echo "${c%.*}")
# oreon:deps
BuildRequires:  alsa-lib-devel
BuildRequires:  cmake
BuildRequires:  dumb-devel
BuildRequires:  enet-devel
BuildRequires:  flac-devel
BuildRequires:  freeimage-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk3-devel
BuildRequires:  libICE-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXpm-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libopenmpt-devel
BuildRequires:  libpng-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libwebp-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  openal-soft-devel
BuildRequires:  opus-devel
BuildRequires:  opusfile-devel
BuildRequires:  physfs-devel
BuildRequires:  pulseaudio-libs-devel
# /oreon:deps
%description
Allegro is a cross-platform library intended for use in computer games
and other types of multimedia programming. Allegro 5 is the latest major
revision of the library, designed to take advantage of modern hardware
(e.g. hardware acceleration using 3D cards) and operating systems.
Although it is not backwards compatible with earlier versions, it still
occupies the same niche and retains a familiar style.

%package devel
Summary:	Development files for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description devel
This package is needed to build programs using the Allegro 5 library.
Contains header files and man-page documentation.

%package addon-acodec
Summary:	Audio codec addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-acodec
This package provides the audio codec addon for the Allegro 5 library.
This addon allows you to load audio sample formats.

%package addon-acodec-devel
Summary:	Header files for the Allegro 5 audio codec addon
Requires:	%{name}-addon-acodec = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-acodec-devel
This package is required to build programs that use the Allegro 5 audio
codec addon.

%package addon-audio
Summary:	Audio addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-audio
This package provides the audio addon for the Allegro 5 library. This
addon allows you to play sounds in your Allegro 5 programs.

%package addon-audio-devel
Summary:	Header files for the Allegro 5 audio addon
Requires:	%{name}-addon-audio = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-audio-devel
This package is required to build programs that use the Allegro 5 audio
addon.

%package addon-dialog
Summary:	Dialog addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-dialog
This package provides the dialog addon for the Allegro 5 library. This
addon allows you to show dialog boxes.

%package addon-dialog-devel
Summary:	Header files for the Allegro 5 dialog addon
Requires:	%{name}-addon-dialog = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-dialog-devel
This package is required to build programs that use the Allegro 5 dialog
addon.

%package addon-image
Summary:	Image addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-image
This package provides the image addon for the Allegro 5 library. Provides
support for loading image file formats.

%package addon-image-devel
Summary:	Header files for the Allegro 5 image addon
Requires:	%{name}-addon-image = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-image-devel
This package is required to build programs that use the Allegro 5 image
addon.

%package addon-physfs
Summary:	Physfs addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-physfs
This package provides the physfs addon for the Allegro 5 library. This
addon provides an interface to the PhysicsFS library, allowing you to
mount virtual file-systems (e.g., archives) and access files as if they
were physically on the file-system.

%package addon-physfs-devel
Summary:	Header files for the Allegro 5 physfs addon
Requires:	%{name}-addon-physfs = %{version}-%{release}
%description addon-physfs-devel
This package is required to build programs that use the Allegro 5 physfs
addon.

%package addon-ttf
Summary:	TTF addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-ttf
This package provides the ttf addon for the Allegro 5 library. This addon
allows you to load and use TTF fonts in your Allegro 5 programs.

%package addon-ttf-devel
Summary:	Header files for the Allegro 5 TTF addon
Requires:	%{name}-addon-ttf = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-ttf-devel
This package is required to build programs that use the Allegro 5 ttf
addon.

%package addon-video
Summary:	Video addon for the Allegro 5 library
Requires:	%{name} = %{version}-%{release}
%description addon-video
This package provides the video addon for the Allegro 5 library. This
addon allows you to play theora videos in your Allegro 5 programs.

%package addon-video-devel
Summary:	Header files for the Allegro 5 video addon
Requires:	%{name}-addon-video = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
%description addon-video-devel
This package is required to build programs that use the Allegro 5 video
addon.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir allegro-%{version}
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DWANT_DOCS=OFF
%cmake_build
%install
%cmake_install
mkdir %buildroot/%{_sysconfdir}
install -p -m 644 allegro5.cfg %buildroot/%{_sysconfdir}/allegro5rc
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man3
install -p -m 644 docs/man/*.3 $RPM_BUILD_ROOT%{_mandir}/man3
%ldconfig_scriptlets
%ldconfig_scriptlets addon-acodec
%ldconfig_scriptlets addon-audio
%ldconfig_scriptlets addon-dialog
%ldconfig_scriptlets addon-image
%ldconfig_scriptlets addon-physfs
%ldconfig_scriptlets addon-ttf
%ldconfig_scriptlets addon-video
%oreon_autofiles allegro5-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-acodec usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-acodec-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-audio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-audio-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-dialog usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-dialog-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-image usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-image-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-physfs usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-physfs-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-ttf usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-ttf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles allegro5-addon-video usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles allegro5-addon-video-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n allegro5-devel -f %{oreon_filedir}/allegro5-devel.list
%files -n allegro5-addon-acodec -f %{oreon_filedir}/allegro5-addon-acodec.list
%files -n allegro5-addon-acodec-devel -f %{oreon_filedir}/allegro5-addon-acodec-devel.list
%files -n allegro5-addon-audio -f %{oreon_filedir}/allegro5-addon-audio.list
%files -n allegro5-addon-audio-devel -f %{oreon_filedir}/allegro5-addon-audio-devel.list
%files -n allegro5-addon-dialog -f %{oreon_filedir}/allegro5-addon-dialog.list
%files -n allegro5-addon-dialog-devel -f %{oreon_filedir}/allegro5-addon-dialog-devel.list
%files -n allegro5-addon-image -f %{oreon_filedir}/allegro5-addon-image.list
%files -n allegro5-addon-image-devel -f %{oreon_filedir}/allegro5-addon-image-devel.list
%files -n allegro5-addon-physfs -f %{oreon_filedir}/allegro5-addon-physfs.list
%files -n allegro5-addon-physfs-devel -f %{oreon_filedir}/allegro5-addon-physfs-devel.list
%files -n allegro5-addon-ttf -f %{oreon_filedir}/allegro5-addon-ttf.list
%files -n allegro5-addon-ttf-devel -f %{oreon_filedir}/allegro5-addon-ttf-devel.list
%files -n allegro5-addon-video -f %{oreon_filedir}/allegro5-addon-video.list
%files -n allegro5-addon-video-devel -f %{oreon_filedir}/allegro5-addon-video-devel.list

%changelog

%autochangelog
