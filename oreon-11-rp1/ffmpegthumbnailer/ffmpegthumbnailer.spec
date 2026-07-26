%global source0_hash ddf561e294385f07d0bd5a28d0aab9de79b8dbaed29b576f206d58f3df79b508

%global forgeurl https://github.com/dirkvdb/ffmpegthumbnailer
Version:        2.3.0
%global tag v%{version}
%forgemeta

Name:           ffmpegthumbnailer
Release:        %autorelease
Summary:        Lightweight video thumbnailer that can be used by file managers
License:        GPL-2.0-or-later
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)

Requires:       %{name}-libs%{?isa} = %{version}-%{release}

%description
FFmpegthumbnailer is a lightweight video thumbnailer that can be used by file
managers to create thumbnails for your video files. The thumbnailer uses ffmpeg
to decode frames from the video files, so supported videoformats depend on the
configuration flags of ffmpeg.

%package        libs
Summary:        Library for %{name}

%description    libs
This package contains the library for %{name}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?isa} = %{version}-%{release}

%description    devel
This package contains the development files for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build
%cmake \
    -DENABLE_GIO=ON \
    -DENABLE_THUMBNAILER=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license COPYING
%doc README
%{_bindir}/ffmpegthumbnailer
%{_mandir}/man1/ffmpegthumbnailer.1*
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/ffmpegthumbnailer.thumbnailer

%files libs
%license COPYING
%{_libdir}/libffmpegthumbnailer.so.4*

%files devel
%{_includedir}/libffmpegthumbnailer/
%{_libdir}/libffmpegthumbnailer.so
%{_libdir}/pkgconfig/libffmpegthumbnailer.pc

%changelog
%autochangelog
