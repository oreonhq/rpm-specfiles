%global source0_hash aba4679a5b1f2bf62482eba6e8814a94de7ffc86de5f8587ba199fcc61b4a04f

Name:		allegro5
Version:	5.2.11.3
Release:	1%{?dist}
Summary:	A game programming library
License:	zlib
URL:		http://liballeg.org/
Source0:	https://github.com/liballeg/allegro5/releases/download/%{version}/allegro-%{version}.tar.gz
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	dumb-devel
BuildRequires:	enet-devel
BuildRequires:	flac-devel
BuildRequires:	freeimage-devel
BuildRequires:	freetype-devel
BuildRequires:	gtk3-devel
BuildRequires:	libICE-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libopenmpt-devel
BuildRequires:	libpng-devel
BuildRequires:	libtheora-devel
BuildRequires:	libvorbis-devel
BuildRequires:	libwebp-devel
BuildRequires:	libXcursor-devel
BuildRequires:	libXext-devel
BuildRequires:	libXxf86vm-devel
BuildRequires:	libXrandr-devel
BuildRequires:	libXinerama-devel
BuildRequires:	libXpm-devel
BuildRequires:	mesa-libGL-devel
BuildRequires:	mesa-libGLU-devel
BuildRequires:	openal-soft-devel
BuildRequires:	physfs-devel
BuildRequires:	pulseaudio-libs-devel
BuildRequires:	opus-devel
BuildRequires:	opusfile-devel

%global so_version %(c="%{version}"; echo "${c%.*}")

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

%autosetup -p1 -n allegro-%{version}

%build
# TODO: Remove in the next version
# https://github.com/liballeg/allegro5/pull/1632
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake -DWANT_DOCS=OFF
%cmake_build

%install
%cmake_install

mkdir %buildroot/%{_sysconfdir}
install -p -m 644 allegro5.cfg %buildroot/%{_sysconfdir}/allegro5rc
# install man pages
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

%files
%config(noreplace) %{_sysconfdir}/allegro5rc
%doc CHANGES-5.?.txt CONTRIBUTORS.txt README.txt
%license LICENSE.txt
%{_libdir}/liballegro.so.5.2
%{_libdir}/liballegro.so.%{so_version}
%{_libdir}/liballegro_color.so.5.2
%{_libdir}/liballegro_color.so.%{so_version}
%{_libdir}/liballegro_font.so.5.2
%{_libdir}/liballegro_font.so.%{so_version}
%{_libdir}/liballegro_main.so.5.2
%{_libdir}/liballegro_main.so.%{so_version}
%{_libdir}/liballegro_memfile.so.5.2
%{_libdir}/liballegro_memfile.so.%{so_version}
%{_libdir}/liballegro_primitives.so.5.2
%{_libdir}/liballegro_primitives.so.%{so_version}

%files devel
%doc docs/html/refman
%{_includedir}/allegro5
%exclude %{_includedir}/allegro5/allegro_acodec.h
%exclude %{_includedir}/allegro5/allegro_audio.h
%exclude %{_includedir}/allegro5/allegro_native_dialog.h
%exclude %{_includedir}/allegro5/allegro_image.h
%exclude %{_includedir}/allegro5/allegro_physfs.h
%exclude %{_includedir}/allegro5/allegro_ttf.h
%exclude %{_includedir}/allegro5/allegro_vidio.h
%{_libdir}/liballegro.so
%{_libdir}/liballegro_color.so
%{_libdir}/liballegro_font.so
%{_libdir}/liballegro_main.so
%{_libdir}/liballegro_memfile.so
%{_libdir}/liballegro_primitives.so
%{_libdir}/cmake/allegro/
%{_libdir}/pkgconfig/allegro-5*.pc
%{_libdir}/pkgconfig/allegro_color-5*.pc
%{_libdir}/pkgconfig/allegro_font-5*.pc
%{_libdir}/pkgconfig/allegro_main-5*.pc
%{_libdir}/pkgconfig/allegro_memfile-5*.pc
%{_libdir}/pkgconfig/allegro_primitives-5*.pc
%{_mandir}/man3/ALLEGRO_*.3*
%{_mandir}/man3/al_*.3*

%files addon-acodec
%{_libdir}/liballegro_acodec.so.5.2
%{_libdir}/liballegro_acodec.so.%{so_version}

%files addon-acodec-devel
%{_includedir}/allegro5/allegro_acodec.h
%{_libdir}/liballegro_acodec.so
%{_libdir}/pkgconfig/allegro_acodec-5*.pc

%files addon-audio
%{_libdir}/liballegro_audio.so.5.2
%{_libdir}/liballegro_audio.so.%{so_version}

%files addon-audio-devel
%{_includedir}/allegro5/allegro_audio.h
%{_libdir}/liballegro_audio.so
%{_libdir}/pkgconfig/allegro_audio-5*.pc

%files addon-dialog
%{_libdir}/liballegro_dialog.so.5.2
%{_libdir}/liballegro_dialog.so.%{so_version}

%files addon-dialog-devel
%{_includedir}/allegro5/allegro_native_dialog.h
%{_libdir}/liballegro_dialog.so
%{_libdir}/pkgconfig/allegro_dialog-5*.pc

%files addon-image
%{_libdir}/liballegro_image.so.5.2
%{_libdir}/liballegro_image.so.%{so_version}

%files addon-image-devel
%{_includedir}/allegro5/allegro_image.h
%{_libdir}/liballegro_image.so
%{_libdir}/pkgconfig/allegro_image-5*.pc

%files addon-physfs
%{_libdir}/liballegro_physfs.so.5.2
%{_libdir}/liballegro_physfs.so.%{so_version}

%files addon-physfs-devel
%{_includedir}/allegro5/allegro_physfs.h
%{_libdir}/liballegro_physfs.so
%{_libdir}/pkgconfig/allegro_physfs-5*.pc

%files addon-ttf
%{_libdir}/liballegro_ttf.so.5.2
%{_libdir}/liballegro_ttf.so.%{so_version}

%files addon-ttf-devel
%{_includedir}/allegro5/allegro_ttf.h
%{_libdir}/liballegro_ttf.so
%{_libdir}/pkgconfig/allegro_ttf-5*.pc

%files addon-video
%{_libdir}/liballegro_video.so.5.2
%{_libdir}/liballegro_video.so.%{so_version}

%files addon-video-devel
%{_includedir}/allegro5/allegro_video.h
%{_libdir}/liballegro_video.so
%{_libdir}/pkgconfig/allegro_video-5*.pc

%changelog
%autochangelog
