%global source0_hash c08b2d87b2fb5edb4526c2a8a317eb1f2cff44807e4631a037ca9f9a1d455054
%global libzen_version  0.4.41
Name:           libmediainfo
Version:        26.05
Release:        1%{?dist}
Summary:        Library for supplies technical and tag information about a video or audio file
License:        BSD-2-Clause
URL:            https://github.com/MediaArea/MediaInfo
Source0:        http://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
Provides:       bundled(md5-plumb)
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libzen)
BuildRequires:  pkgconfig(tinyxml2)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libmediainfo-devel -f %{oreon_filedir}/libmediainfo-devel.list

%changelog

%autochangelog
