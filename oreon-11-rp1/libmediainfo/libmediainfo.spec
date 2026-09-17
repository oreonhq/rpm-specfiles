%global source0_hash ad13d9797b046ce39d0c65a6f81d2aef2429734c21865a6a4c592c7c01f249dd

%global libzen_version  0.4.41

Name:           libmediainfo
Version:        25.10
Release:        2%{?dist}
Summary:        Library for supplies technical and tag information about a video or audio file

License:        BSD-2-Clause
URL:            https://github.com/MediaArea/MediaInfo
Source0:        http://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libzen) >= %{libzen_version}
BuildRequires:  pkgconfig(zlib)
BuildRequires:  doxygen
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(tinyxml2)

Provides:       bundled(md5-plumb)

%description
This package contains the shared library for MediaInfo.
MediaInfo supplies technical and tag information about a video or
audio file.

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

%package        devel
Summary:        Include files and mandatory libraries for development
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libzen-devel%{?_isa} >= %{libzen_version}

%description    devel
Include files and mandatory libraries for development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n MediaInfoLib

cp           Release/ReadMe_DLL_Linux.txt ReadMe.txt
mv           History_DLL.txt History.txt
sed -i 's/.$//' *.txt Source/Example/*

find . -type f -exec chmod 644 {} ';'

rm -rf Project/MSCS20*
rm -rf Source/ThirdParty/tinyxml2

%build
pushd Source/Doc/
    doxygen -u Doxyfile
    doxygen Doxyfile
popd
cp Source/Doc/*.html ./

pushd Project/CMake
    %cmake
    %cmake_build
popd

%install
pushd Project/CMake
    %cmake_install
popd

install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.cs %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.JNA.java %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.JNative.java %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL.py %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 -p Source/MediaInfoDLL/MediaInfoDLL3.py %{buildroot}%{_includedir}/MediaInfoDLL

rm -f %{buildroot}%{_libdir}/%{name}.la

%files
%doc History.txt ReadMe.txt
%license License.html
%{_libdir}/%{name}.so.*

%files    devel
%doc Changes.txt Documentation.html Doc Source/Example
%{_includedir}/MediaInfo
%{_includedir}/MediaInfoDLL
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/cmake/mediainfolib/

%changelog
%autochangelog
