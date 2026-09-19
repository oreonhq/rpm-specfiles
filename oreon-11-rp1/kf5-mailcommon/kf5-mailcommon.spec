%global source0_hash 65dd3b8c9f8233fbdbde5a6f6f65539c061920e34140bd8f97d0efde5fd60fc0

%global framework mailcommon

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kf5-%{framework}
Version: 23.08.5
Release: 6%{?dist}
Summary: Mail applications support library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}/

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake(Qt5Designer)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)

%global kf5_ver 5.89.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5Archive)
BuildRequires:  cmake(KF5Codecs)
BuildRequires:  cmake(KF5Completion)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5DBusAddons)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5IconThemes)
BuildRequires:  cmake(KF5ItemModels)
BuildRequires:  cmake(KF5ItemViews)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextWidgets)
BuildRequires:  cmake(KF5WidgetsAddons)
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5XmlGui)
BuildRequires:  cmake(KPim5MessageViewer)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-kldap-devel >= %{majmin_ver}
BuildRequires:  kf5-kmailtransport-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires:  kf5-mailimporter-devel >= %{majmin_ver}
BuildRequires:  cmake(KPim5MessageCore)
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

BuildRequires:  pkgconfig(libxslt)
BuildRequires:  phonon-qt5-devel >= 4.11

Obsoletes:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KPim5MessageComposer)
Requires:       cmake(KPim5PimCommon)
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libmailcommon5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libmailcommon/libmailcommon5/" src/CMakeLists.txt
sed -i "s/libmailcommon/libmailcommon5/" src/Messages.sh

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5MailCommon.so.*
%{_qt5_plugindir}/designer/mailcommon5widgets.so

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_MailCommon.pri
%{_includedir}/KPim5/MailCommon/
%{_kf5_libdir}/cmake/KF5MailCommon/
%{_kf5_libdir}/cmake/KPim5MailCommon/
%{_kf5_libdir}/libKPim5MailCommon.so

%changelog
%autochangelog
