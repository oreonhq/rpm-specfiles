%global framework kdewebkit

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 3 integration module for QtWebKit

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/portingAids/%{framework}-%{version}.tar.xz


# Temporary revert commit that introduces a dependency on kf6 extra-cmake-modules
Patch0: revert_feature_summary_ecm.patch


BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kio-devel >= %{majmin}
BuildRequires:  kf5-kjobwidgets-devel >= %{majmin}
BuildRequires:  kf5-kparts-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-kwallet-devel >= %{majmin}
BuildRequires:  kf5-rpm-macros >= %{majmin}

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtwebkit-devel

# designer plugin
BuildRequires:  cmake(Qt5UiPlugin)

%description
KDE Frameworks 5 Tier 3 integration module for the HTML rendering engine WebKit.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtwebkit-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{framework}-%{version}


%build
%cmake_kf5

%cmake_build


%install
%cmake_install


%ldconfig_scriptlets

%files
%doc README.md
%license COPYING.LIB
%{_kf5_libdir}/libKF5WebKit.so.*
# designer plugin
%{_kf5_qtplugindir}/designer/kdewebkit5widgets.so

%files devel

%{_kf5_includedir}/KDEWebKit/
%{_kf5_libdir}/libKF5WebKit.so
%{_kf5_libdir}/cmake/KF5WebKit/
%{_kf5_archdatadir}/mkspecs/modules/qt_KDEWebKit.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.116.0-6
- Prepare for Oreon 11 (RP1)
