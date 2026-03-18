Name:           kdecoration5
Summary:        A plugin-based library to create window decorations
Version:        5.27.11
Release:        %autorelease
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/kdecoration
Source0:        %{url}/-/archive/v%{version}/kdecoration-v%{version}.tar.bz2

BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5CoreAddons)

Requires:       kf5-filesystem

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      kdecoration-devel

%description    devel
This package contains development files for %{name}.

%package        lang
Summary:        Translations for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Conflicts:      kdecoration

%description    lang
This package contains translations for %{name}.

%prep
%autosetup -p1 -n kdecoration-v%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang kdecoration

%files
%license LICENSES/*.txt
%{_libdir}/libkdecorations2.so.*
%{_libdir}/libkdecorations2private.so.*

%files devel
%{_libdir}/libkdecorations2.so
%{_libdir}/libkdecorations2private.so
%{_libdir}/cmake/KDecoration2/
%{_kf5_includedir}/kdecoration2_version.h
%{_includedir}/KDecoration2

%files lang -f kdecoration.lang

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.27.11-1
- Prepare for Oreon 11 (RP1)
