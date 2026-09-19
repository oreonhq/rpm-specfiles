%global source0_hash 63a1c9d86439938adc87d0acd86e69ff14f53c0a24a7114930c581c26046553c

Name:           screengrab
Summary:        Crossplatform tool for fast making screenshots
Version:        3.1.0
Release:        3%{?dist}
License:        GPL-2.0-only
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(qt6xdg)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  wayland-devel

BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)

BuildRequires:  perl

Requires:       hicolor-icon-theme

%description
An application for creating screenshots. ScreenGrab uses
the Qt framework and thus, it is independent from any
desktop environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
# TODO: Please submit an issue to upstream (rhbz#2381657)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/screengrab.desktop

%files -f %{name}.lang
%license COPYING
%doc AUTHORS CHANGELOG README.md
%{_bindir}/screengrab
%{_datadir}/applications/screengrab.desktop
%{_datadir}/icons/hicolor/scalable/apps/screengrab.svg
%{_metainfodir}/screengrab.metainfo.xml
%{_datadir}/screengrab/screengrab.conf

%changelog
%autochangelog
