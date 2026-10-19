%global source0_hash 5c5f3790f6f70977f3573b9d039372d5b85bddc46f8944244a6225a79891acf2
%define _lto_cflags %{nil}
%global soversion 28
%bcond openh264 0
%global skip_tests Clip:verify parent Timeline|\\\
Clip:time remapping|\\\
Clip:resample_audio_8000_to_48000_reverse|\\\
FFmpegWriter:Options_Overloads|\\\
FrameMapper:resample_audio_mapper|\\\
FrameMapper:resample_audio_48000_to_41000|\\\
SphericalMetadata:SphericalMetadata_Test|\\\
SphericalMetadata:SphericalMetadata_FullOrientation|\\\
Timeline:Multi-threaded Timeline Add/Remove Effect
%if %{without openh264}
%global skip_openh264_tests |\AudioWaveformer:Extract waveform data sintel|\\\
AudioWaveformer:Extract waveform continues if caller closes original reader|\\\
AudioWaveformer:Channel selection returns data and rejects invalid channel|\\\
AudioWaveformer:Extract waveform data clip slowed by time curve|\\\
AudioWaveformer:Extract waveform waits for reader reopen|\\\
AudioWaveformer:Waveform extraction does not mutate source reader video flag|\\\
Clip:effects|\\\
Clip:verify parent Timeline|\\\
Clip:has_video|\\\
FFmpegReader:DisplayInfo|\\\
FFmpegReader:Multiple_Open_and_Close|\\\
FFmpegReader:verify parent Timeline|\\\
FFmpegReader:Seek|\\\
FFmpegReader:Frame_Rate|\\\
FFmpegReader:Duration_Strategy_Audio_Preferred|\\\
FFmpegReader:Duration_And_Length|\\\
FFmpegReader:Duration_Strategy_Video_Preferred|\\\
FFmpegReader:Duration_Strategy_Longest_Stream|\\\
FFmpegWriter:DisplayInfo|\\\
FFmpegWriter:Webm|\\\
FFmpegWriter:Gif|\\\
Frame:Convert_Image|\\\
Frame:Data_Access|\\\
KeyFrame:AttachToObject|\\\
Timeline:ApplyJSONDiff Update Reader Info|\\\
Timeline:Multi-threaded Timeline Add/Remove Clip|\\\
Timeline:Multi-threaded Timeline GetFrame|\\\
VideoCacheThread:prefetchWindow: interrupt on userSeeked flag|\\\
VideoCacheThread:prefetchWindow: backward caching with FFmpegReader & CacheMemory|\\\
VideoCacheThread:prefetchWindow: forward caching with FFmpegReader & CacheMemory|\\\
ImageWriter:Gif
%else
%global skip_openh264_tests %nil
%endif
%ifarch s390x
%global skip_s390x_tests |\Clip:Speed up time curve|\\\
ColorMap:3D LUT obeys DOMAIN_MIN and DOMAIN_MAX|\\\
ColorMap:1D LUT obeys DOMAIN_MIN and DOMAIN_MAX|\\\
AnalogTape:AnalogTape stripe lifts bottom|\\\
CVOutline:Outline_Tests
%else
%global skip_s390x_tests %nil
%endif
Name:           libopenshot
Version:        1.0.0
Release:        1%{?dist}
Summary:        Library for creating and editing videos
License:        LGPL-3.0-or-later and BSD-3-Clause
URL:            http://www.openshot.org/
Source0:        https://github.com/OpenShot/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-ffmpeg8.patch
Patch1:         %{name}-fix-babl-detection.patch
ExcludeArch:    ppc64le
%if %{with openh264}
%endif
# oreon:deps
BuildRequires:  ImageMagick-c++-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  babl-devel
BuildRequires:  catch-devel
BuildRequires:  cmake
BuildRequires:  cppzmq-devel
BuildRequires:  ffmpeg-free-devel
BuildRequires:  gcc-c++
BuildRequires:  jsoncpp-devel
BuildRequires:  libopenshot-audio-devel
BuildRequires:  opencv-devel
BuildRequires:  protobuf-devel
BuildRequires:  python3-devel
BuildRequires:  python3-distutils-extra
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  ruby-devel
BuildRequires:  swig
BuildRequires:  unittest-cpp-devel
BuildRequires:  zeromq-devel
# /oreon:deps
%description
OpenShot Library (libopenshot) is an open-source project
dedicated to delivering high quality video editing, animation,
and playback solutions to the world.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python%{python3_pkgversion}-%{name}
Summary:        Python bindings for %{name}
BuildRequires:  swig >= 3.0
BuildRequires:  python%{python3_pkgversion}-libs
BuildRequires:  python%{python3_pkgversion}-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      python-%{name} < 0.1.1-2
Provides:       python-%{name} = %{version}-%{release}
%description -n python%{python3_pkgversion}-%{name}
The python-%{name} package contains python bindings for
applications that use %{name}.

%package -n     ruby-%{name}
Summary:        Ruby bindings for %{name}
BuildRequires:  ruby-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description -n ruby-%{name}
The ruby-%{name} package contains ruby bindings for
applications that use %{name}.

%prep

%autosetup -p1

rm -rf third_party/jsoncpp

%build

%cmake -Wno-dev -DCMAKE_BUILD_TYPE:STRING=Release
%cmake_build
%check

export QT_QPA_PLATFORM=offscreen
%ctest --exclude-regex "%{skip_tests}%{skip_openh264_tests}%{skip_s390x_tests}"
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n libopenshot-devel -f %{oreon_filedir}/libopenshot-devel.list
%files -n python3-libopenshot -f %{oreon_filedir}/python3-libopenshot.list
%files -n ruby-libopenshot -f %{oreon_filedir}/ruby-libopenshot.list

%changelog

%autochangelog
