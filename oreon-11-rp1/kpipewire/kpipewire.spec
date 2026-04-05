Name:    kpipewire
Summary: Set of convenient classes to use PipeWire in Qt projects
Version: 6.6.2
Release:	2%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND LGPL-2.1-only AND LGPL-3.0-only
URL:     https://invent.kde.org/plasma/%{name}
Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Patch0:  %{name}-ffmpeg8.patch

# Compile Tools
BuildRequires:  cmake
BuildRequires:  gcc-c++

# Fedora
BuildRequires:  kf6-rpm-macros
Requires:       kf6-filesystem

# KDE Frameworks
BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)

# Misc
BuildRequires:  libdrm-devel
BuildRequires:  libepoxy-devel
BuildRequires:  mesa-libgbm-devel
BuildRequires:  pipewire-devel
BuildRequires:  wayland-devel
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  pkgconfig(libva)

# Plasma
BuildRequires:  plasma-wayland-protocols-devel

# Qt
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtwayland-devel

%description
It is developed in C++ and it's main use target is QML components.
As it's what's been useful, this framework focuses on graphical PipeWire
features. If it was necessary, these could be included.

At the moment we offer two main components:

- KPipeWire: offers the main components to connect to and render
PipeWire into your app.
- KPipeWireRecord: using FFmpeg, helps to record a PipeWire video stream
into a file.

%package        devel
Summary:        Development files for %{name}
# This requires pipewire headers to be installed
Requires:       pipewire-devel
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       kpipewire-devel = %{version}-%{release}
Provides:       kpipewire-devel%{?_isa} = %{version}-%{release}
Obsoletes:      kpipewire-devel <= 1:5.2.0

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -p1 -n %{name}-%{version}

%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --with-qt --all-name

%files -f %{name}.lang
%license LICENSES/*
%{_libdir}/libKPipeWire.so.6
%{_libdir}/libKPipeWire.so.%{version}
%{_libdir}/libKPipeWireRecord.so.6
%{_libdir}/libKPipeWireRecord.so.%{version}
%{_libdir}/libKPipeWireDmaBuf.so.6
%{_libdir}/libKPipeWireDmaBuf.so.%{version}
%{_qt6_qmldir}/org/kde/pipewire/*
%{_kf6_datadir}/qlogging-categories6/*.categories

%files devel
%{_libdir}/libKPipeWire.so
%{_libdir}/libKPipeWireRecord.so
%{_libdir}/libKPipeWireDmaBuf.so
%dir %{_includedir}/KPipeWire
%{_includedir}/KPipeWire/*
%dir %{_libdir}/cmake/KPipeWire
%{_libdir}/cmake/KPipeWire/*.cmake

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
