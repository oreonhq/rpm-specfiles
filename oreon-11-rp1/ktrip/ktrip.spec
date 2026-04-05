
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:          ktrip
Version:       25.12.3
Release:	2%{?dist}
Summary:       Public transport navigation, allows you to find journeys between specified locations, departures for a specific station and shows real-time delay and disruption information.

License:       GPL-2.0-or-later
Url:           https://invent.kde.org/utilities/ktrip

Source0:       https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake 
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6QQC2DesktopStyle)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KPublicTransport)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: cmake(KF6Crash)

BuildRequires: pkgconfig(zlib)

# QML module dependencies
Requires:      kf6-ki18n%{?_isa}
Requires:      kf6-kirigami2%{?_isa}
Requires:      kf6-kirigami2-addons%{?_isa}
Requires:      kpublictransport%{?_isa}

%description
%{summary}.

%prep
%autosetup

%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name}
desktop-file-install --dir=%{buildroot}%{_kf6_datadir}/applications/ %{buildroot}/%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/org.kde.%{name}.*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
