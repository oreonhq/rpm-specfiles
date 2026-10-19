%global source0_hash aa9dfe316cddcb2451f0195ce4f8c5b0d3e17504574c8d00db6adeef36cdcfa6
Name:           deepin-image-viewer
Version:        6.0.48
Release:        1%{?dist}
Summary:        Deepin Image Viewer
License:        GPL-3.0-only
URL:            https://github.com/linuxdeepin/deepin-image-viewer
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{name}-appdata.xml
Patch0:         libraw.patch
Patch1:         includes.patch
Requires:       hicolor-icon-theme
Recommends:     deepin-manual
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  freeimage-devel
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5OpenGL)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  pkgconfig(gio-qt)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(libexif)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xext)
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  udisks2-qt5-devel
# /oreon:deps
%description
%{summary}.

%prep
%oreon_prep
%build

export PATH=%{_qt5_bindir}:$PATH
%qmake_qt5 PREFIX=%{_prefix}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dm644 %SOURCE1 %{buildroot}%{_metainfodir}/%{name}.appdata.xml
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop ||:
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
