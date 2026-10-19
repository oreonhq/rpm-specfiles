%global source0_hash 74abe7c2c800fa77783b23e86741a1e9051a94b5d8f2c6c24df765a13c94fe03
Name:           kdecoration5
Summary:        A plugin-based library to create window decorations
Version:        5.27.11
Release:        1%{?dist}
License:        LGPL-2.1-only OR LGPL-3.0-only
URL:            https://invent.kde.org/plasma/kdecoration
Source0:        https://invent.kde.org/plasma/kdecoration/-/archive/v5.27.11/kdecoration-v5.27.11.tar.bz2
Requires:       kf5-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir kdecoration-v%{version}
%oreon_prep
%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang kdecoration
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n kdecoration5-devel -f %{oreon_filedir}/kdecoration5-devel.list
%files -n kdecoration5-lang -f %{oreon_filedir}/kdecoration5-lang.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.27.11-1
- Prepare for Oreon 11 (RP1)
