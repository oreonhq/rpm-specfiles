%global source0_hash 4330d3e4b70cf5f8d7b341b665a63b47f02e12270946ce6991971315298c4625
%global framework libkleo
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        KDE PIM cryptographic library
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1)
URL:     https://invent.kde.org/frameworks/%{framework}/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
Obsoletes:      kdepim-libs < 7:16.04.0
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%if 0%{?fedora} < 26 && 0%{?rhel} < 8 && 0%{?oreon} < 11
Requires:       pinentry-gui
%else
Recommends:     pinentry-gui
%endif
Conflicts: kde-l10n < 17.03
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  gpgmepp-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libassuan-devel
BuildRequires:  qgpgme-devel
# /oreon:deps
%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Requires:       cmake(Gpgmepp)
Requires:       cmake(QGpgme)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libkleopatra5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libkleopatra/libkleopatra5/" src/CMakeLists.txt
sed -i "s/libkleopatra/libkleopatra5/" src/Messages.sh

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-libkleo-libs -f %{oreon_filedir}/kf5-libkleo-libs.list
%files -n kf5-libkleo-devel -f %{oreon_filedir}/kf5-libkleo-devel.list

%changelog

%autochangelog
