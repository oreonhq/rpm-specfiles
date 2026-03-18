# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kamoso
Summary: Application for taking pictures and videos from a webcam
Version: 25.12.3
Release: 1%{?dist}

License: GFDL-1.2-or-later AND GPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later
URL:     https://userbase.kde.org/Kamoso

Source0: https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros

BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(libaccounts-glib)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Quick)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Purpose)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)

%if 0%{?tests}
BuildRequires: mesa-libGL
BuildRequires: time
BuildRequires: xorg-x11-server-Xvfb
%endif
BuildRequires: make

# currently not linked, needs qml resources
Requires: kf6-purpose%{?_isa}
Requires: kf6-kirigami%{?_isa}
Requires: qt6-qtdeclarative%{?_isa}

%description
Kamoso is an application to take pictures and videos out of your webcam.


%prep
%autosetup -p1


%build
%cmake_kf6 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{!?tests:OFF} -Wno-dev

%cmake_build


%install
%cmake_install

%find_lang kamoso --with-html


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kamoso.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kamoso.desktop
%if 0%{?tests}
xvfb-run -a bash -c "%ctest"
%endif


%files -f kamoso.lang
%doc AUTHORS
%license LICENSES/*
%{_kf6_metainfodir}/org.kde.kamoso.appdata.xml
%{_kf6_datadir}/applications/org.kde.kamoso.desktop
%{_kf6_bindir}/kamoso
%{_kf6_datadir}/icons/hicolor/*/apps/kamoso.*
%{_kf6_datadir}/icons/hicolor/*/actions/*
%{_kf6_datadir}/knotifications6/%{name}*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
