%global source0_hash 4330d3e4b70cf5f8d7b341b665a63b47f02e12270946ce6991971315298c4625

%global framework libkleo

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: KDE PIM cryptographic library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND LGPL-2.0-or-later AND (GPL-3.0-or-later WITH GCC-exception-3.1)
URL:     https://invent.kde.org/frameworks/%{framework}/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        https://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

BuildRequires:  boost-devel

BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  gpgmepp-devel >= 1.7.1
BuildRequires:  qgpgme-devel
# workaround gpgmepp-devel missing Requires: libassuan-devel for now
BuildRequires:  libassuan-devel
# kf5
BuildRequires:  extra-cmake-modules >= 5.19.0
BuildRequires:  kf5-rpm-macros >= 5.19.0
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5TextEditor)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
# kde-apps
%global majmin_ver %(echo %{version} | cut -d. -f1,2)

Obsoletes:      kdepim-libs < 7:16.04.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

# gpg support ui
%if 0%{?fedora} < 26 && 0%{?rhel} < 8
Requires:       pinentry-gui
%else
Recommends:     pinentry-gui
%endif

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%package        libs
Summary:        Only the linkable libraries for %{name}
%description    libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
# INTERFACE_LINK_LIBRARIES "QGpgme;Gpgmepp"
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

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_sysconfdir}/xdg/libkleopatrarc
%{_kf5_datadir}/libkleopatra/

%files libs
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5Libkleo.so.*

%files devel
%{_kf5_libdir}/libKPim5Libkleo.so
%{_kf5_libdir}/cmake/KF5Libkleo/
%{_kf5_libdir}/cmake/KPim5Libkleo/
%{_includedir}/KPim5/Libkleo/
%{_kf5_archdatadir}/mkspecs/modules/qt_Libkleo.pri

%changelog
%autochangelog
