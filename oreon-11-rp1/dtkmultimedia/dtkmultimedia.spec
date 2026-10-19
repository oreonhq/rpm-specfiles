%global source0_hash 443024907176e232a4e7d5157f30b34bb3c79ab45c56d405bc60e9b94f022c82
%global sover 1
Name:           dtkmultimedia
Version:        6.0.4
Release:        1%{?dist}
Summary:        Development Tool Kit Multimedia
License:        Apache-2.0 AND BSL-1.0 AND GPL-2.0-or-later AND LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/dtkmultimedia
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         drop-set_vulkan_compute.patch
Patch1:         https://github.com/linuxdeepin/dtkmultimedia/pull/72.patch
Patch2:         https://github.com/linuxdeepin/dtkmultimedia/pull/78.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(Dtk6Core)
BuildRequires:  cmake(Dtk6Widget)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6GuiPrivate)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6MultimediaWidgets)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6OpenGLWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gstreamer1-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  libXtst-devel
BuildRequires:  libusb1-devel
BuildRequires:  libv4l-devel
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libffmpegthumbnailer)
BuildRequires:  pkgconfig(mpv)
BuildRequires:  pkgconfig(ncnn)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  portaudio-devel
BuildRequires:  systemd-devel
# /oreon:deps
%description
Development Tool Kit (DtkMultimedia) is the base development tool of all C++/Qt
Developer work on Deepin.

%package -n     libdtk6multimedia
Summary:        Deepin Multimedia Toolkit libraries
%description -n libdtk6multimedia
Deepin Multimedia Toolkit is the base devlopment tool of all C++/Qt Developer
work on Deepin.

%package -n     libdtk6multimediawidgets
Summary:        Deepin Multimedia Widgets Toolkit libraries
%description -n libdtk6multimediawidgets
Deepin Multimedia Widgets Toolkit is the base devlopment tool of all C++/Qt
Developer work on Deepin.

%package -n     libdtk6ocr
Summary:        Deepin Multimedia OCR Toolkit libraries
Requires:       libdtk6ocr-data = %{version}-%{release}
%description -n libdtk6ocr
Deepin Multimedia OCR Toolkit is the base devlopment tool of all C++/Qt
Developer work on Deepin.

%package -n     libdtk6ocr-data
Summary:        Data files for libdtk6ocr
BuildArch:      noarch
%description -n libdtk6ocr-data
This package contains data files for libdtk6ocr.

%package        devel
Summary:        Development files for dtkmultimedia
Requires:       libdtk6multimedia%{?_isa} = %{version}-%{release}
Requires:       libdtk6multimediawidgets%{?_isa} = %{version}-%{release}
Requires:       libdtk6ocr%{?_isa} = %{version}-%{release}
%description    devel
This package contains development files for dtkmultimedia.

%prep

%autosetup -p1

# '-Wl,--as-needed' already included in LDFLAGS when building on Fedora
sed -i '/-Wl,--as-needed/d' CMakeLists.txt

sed -i 's/opencv_mobile/opencv4/' src/ocr/CMakeLists.txt

%build

export CFLAGS="%{build_cflags} -std=gnu17"
%cmake -DENABLE_Qt6=ON \
    -DQCH_INSTALL_DESTINATION=%{_qt6_docdir}
%cmake_build
%install
%cmake_install
%oreon_autofiles libdtk6multimedia usr/*/lib*.so.*
%oreon_autofiles libdtk6multimediawidgets usr/*/lib*.so.*
%oreon_autofiles libdtk6ocr usr/*/lib*.so.*
%oreon_autofiles libdtk6ocr-data usr/*/lib*.so.*
%oreon_autofiles main usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libdtk6multimedia -f %{oreon_filedir}/libdtk6multimedia.list
%files -n libdtk6multimediawidgets -f %{oreon_filedir}/libdtk6multimediawidgets.list
%files -n libdtk6ocr -f %{oreon_filedir}/libdtk6ocr.list
%files -n libdtk6ocr-data -f %{oreon_filedir}/libdtk6ocr-data.list
%files -n dtkmultimedia-devel -f %{oreon_filedir}/dtkmultimedia-devel.list

%changelog

%autochangelog
