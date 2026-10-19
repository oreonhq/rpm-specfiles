%global source0_hash da37af29e9a1a8d5947cbdc7ccfbdd749d3ef5257e4cc778eb8f0069fe50ddf8
%global framework messagelib
Name:    kf5-%{framework}
Version: 23.08.5
Release:        1%{?dist}
Summary:        KDE Message libraries
License: BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/stable/release-service/%{version}/src/%{framework}-%{version}.tar.xz
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}
%global kf5_ver 5.28
%global majmin_ver %{version}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-addons < 16.12
# oreon:deps
BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextAutoCorrectionWidgets)
BuildRequires:  cmake(QGpgme)
BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-akonadi-mime-devel
BuildRequires:  kf5-akonadi-notes-devel
BuildRequires:  kf5-akonadi-search-devel
BuildRequires:  kf5-grantleetheme-devel
BuildRequires:  kf5-karchive-devel
BuildRequires:  kf5-kcodecs-devel
BuildRequires:  kf5-kcompletion-devel
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kcontacts-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kiconthemes-devel
BuildRequires:  kf5-kidentitymanagement-devel
BuildRequires:  kf5-kitemviews-devel
BuildRequires:  kf5-kldap-devel
BuildRequires:  kf5-kmailtransport-devel
BuildRequires:  kf5-kmbox-devel
BuildRequires:  kf5-kmime-devel
BuildRequires:  kf5-kpimtextedit-devel
BuildRequires:  kf5-ktextwidgets-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-kxmlgui-devel
BuildRequires:  kf5-libgravatar-devel
BuildRequires:  kf5-libkdepim-devel
BuildRequires:  kf5-libkleo-devel
BuildRequires:  kf5-pimcommon-devel
BuildRequires:  kf5-rpm-macros
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
Requires:       cmake(KF5Akonadi)
Requires:       cmake(KF5AkonadiMime)
Requires:       cmake(KF5Contacts)
Requires:       cmake(KF5IdentityManagement)
Requires:       cmake(KF5Libkleo)
Requires:       cmake(KPim5MessageCore)
Requires:       cmake(KPim5Mime)
Requires:       cmake(KPim5PimCommon)
Requires:       cmake(Qt5WebEngine)
%description    devel
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

# Rename translation files to avoid conflict with KF6
find ./po -type f -name libmessagecomposer.po -execdir mv {} libmessagecomposer5.po \;
find ./po -type f -name libmessagecore.po -execdir mv {} libmessagecore5.po \;
find ./po -type f -name libmessagelist.po -execdir mv {} libmessagelist5.po \;
find ./po -type f -name libmessageviewer.po -execdir mv {} libmessageviewer5.po \;
find ./po -type f -name libmimetreeparser.po -execdir mv {} libmimetreeparser5.po \;
find ./po -type f -name libtemplateparser.po -execdir mv {} libtemplateparser5.po \;
find ./po -type f -name libwebengineviewer.po -execdir mv {} libwebengineviewer5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libmessagecomposer/libmessagecomposer5/" messagecomposer/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmessagecore/libmessagecore5/" messagecore/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmessagelist/libmessagelist5/" messagelist/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmessageviewer/libmessageviewer5/" messageviewer/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libmimetreeparser/libmimetreeparser5/" mimetreeparser/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libtemplateparser/libtemplateparser5/" templateparser/src/CMakeLists.txt
sed -i "/TRANSLATION_DOMAIN/ s/libwebengineviewer/libwebengineviewer5/" webengineviewer/src/CMakeLists.txt
sed -i "s/libmessagecomposer/libmessagecomposer5/" messagecomposer/src/Messages.sh
sed -i "s/libmessagecore/libmessagecore5/" messagecore/src/Messages.sh
sed -i "s/libmessagelist/libmessagelist5/" messagelist/src/Messages.sh
sed -i "s/libmessageviewer/libmessageviewer5/" messageviewer/src/Messages.sh
sed -i "s/libmimetreeparser/libmimetreeparser5/" mimetreeparser/Messages.sh
sed -i "s/libtemplateparser/libtemplateparser5/" templateparser/src/Messages.sh
sed -i "s/libwebengineviewer/libwebengineviewer5/" webengineviewer/src/Messages.sh

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%ldconfig_scriptlets
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-messagelib-libs -f %{oreon_filedir}/kf5-messagelib-libs.list
%files -n kf5-messagelib-devel -f %{oreon_filedir}/kf5-messagelib-devel.list

%changelog

%autochangelog
