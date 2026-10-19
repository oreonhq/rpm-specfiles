%global source0_hash f3b4448904f1656d6d7cd5a557d22fe1c50624eb32ed369f34726beff9ce0589
Name:          ktextaddons-qt5
Version:       2.1.2
Release:        1%{?dist}
Summary:        Various text handling addons
License:       CC0-1.0 AND LGPL-2.0-or-later AND GPL-2.0-or-later AND BSD-3-Clause
URL:           https://invent.kde.org/libraries/%{name}
Source0:        http://download.kde.org/stable/ktextaddons/ktextaddons-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5Sonnet)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Keychain)
BuildRequires:  cmake(Qt5TextToSpeech)
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros
# /oreon:deps
%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n ktextaddons-%{version} -p1
# allow parallel installability with newer qt6-only ktextaddons
sed -i -e '/DTRANSLATION_DOMAIN/s/libtext[[:alpha:]]\+/&5/' text*/CMakeLists.txt
rename .po 5.po po/*/*.po

%build

%cmake_kf5 -DQT_MAJOR_VERSION=5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ktextaddons-qt5-devel -f %{oreon_filedir}/ktextaddons-qt5-devel.list

%changelog

%autochangelog
