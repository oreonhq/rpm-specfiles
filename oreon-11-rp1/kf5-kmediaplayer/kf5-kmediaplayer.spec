%undefine __cmake_in_source_build
%global framework kmediaplayer

Name:    kf5-%{framework}
Version: 5.116.0
Release: 5%{?dist}
Summary: KDE Frameworks 5 Tier 3 module with interface for media player features

# The project has no SPDX tags on files. The LICENSE file points to X11 License, soooooo...
License: X11
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/portingAids/%{framework}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kparts-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros

BuildRequires:  qt5-qtbase-devel

%description
KDE Frameworks 5 Tier 3 module with plugin interfaces for media player features.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kparts-devel >= %{majmin}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%{cmake_kf5}
%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license LICENSE
%{_kf5_libdir}/libKF5MediaPlayer.so.*
%{_kf5_datadir}/kservicetypes5/*.desktop

%files devel

%{_kf5_includedir}/KMediaPlayer/
%{_kf5_libdir}/libKF5MediaPlayer.so
%{_kf5_libdir}/cmake/KF5MediaPlayer/
%{_kf5_datadir}/dbus-1/interfaces/*.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-5
- Prepare for Oreon 11 (RP1)
