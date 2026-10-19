%global source0_hash 63a1c9d86439938adc87d0acd86e69ff14f53c0a24a7114930c581c26046553c
Name:           screengrab
Summary:        Crossplatform tool for fast making screenshots
Version:        3.1.0
Release:        1%{?dist}
License:        GPL-2.0-only
URL:            https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(qt6xdg)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  perl
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpng16)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  wayland-devel
# /oreon:deps
%description
An application for creating screenshots. ScreenGrab uses
the Qt framework and thus, it is independent from any
desktop environment.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-qt
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml
desktop-file-validate %{buildroot}/%{_datadir}/applications/screengrab.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
