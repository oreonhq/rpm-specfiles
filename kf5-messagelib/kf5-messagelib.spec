%global framework messagelib

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: KDE Message libraries

License: BSD-3-Clause AND BSL-1.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
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

## upstream patches

BuildRequires:  cmake(Grantlee5)

BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Positioning)
BuildRequires:  cmake(Qt5Qml) cmake(Qt5Quick)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebChannel)
BuildRequires:  cmake(Qt5WebEngine)
BuildRequires:  cmake(Qt5Widgets)

BuildRequires:  cmake(Qca-qt5)
BuildRequires:  cmake(QGpgme)

%global kf5_ver 5.28
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-karchive-devel >= %{kf5_ver}
BuildRequires:  kf5-kcodecs-devel >= %{kf5_ver}
BuildRequires:  kf5-kcompletion-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-kiconthemes-devel >= %{kf5_ver}
BuildRequires:  kf5-kitemviews-devel >= %{kf5_ver}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_ver}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-kxmlgui-devel >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}

BuildRequires:  cmake(KF5NewStuff)
BuildRequires:  cmake(KF5SyntaxHighlighting)
BuildRequires:  cmake(KF5TextAutoCorrectionWidgets)

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-notes-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-search-devel >= %{majmin_ver}
BuildRequires:  kf5-grantleetheme-devel >= %{majmin_ver}
BuildRequires:  kf5-kcontacts-devel >= %{majmin_ver}
BuildRequires:  kf5-kidentitymanagement-devel >= %{majmin_ver}
BuildRequires:  kf5-kldap-devel >= %{majmin_ver}
BuildRequires:  kf5-kmailtransport-devel >= %{majmin_ver}
BuildRequires:  kf5-kmbox-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  kf5-kpimtextedit-devel >= %{majmin_ver}
BuildRequires:  kf5-libgravatar-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires:  kf5-libkleo-devel >= %{majmin_ver}, cmake(QGpgme)
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes:      kdepim-libs < 7:16.04.0

# messageviewer_defaultgrantleeheaderstyleplugin.so moved here
Conflicts:      kdepim-addons < 16.12

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

%files
%license LICENSES/*
%{_kf5_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_kf5_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg
%{_kf5_datadir}/knotifications5/messageviewer.notifyrc
%{_kf5_datadir}/knsrcfiles/messageviewer_header_themes.knsrc
%{_kf5_datadir}/libmessageviewer/
%{_kf5_datadir}/messagelist/
%{_kf5_datadir}/messageviewer/
%{_kf5_qtplugindir}/pim5/messageviewer/grantlee/5.0/messageviewer_grantlee_extension.so
%{_kf5_qtplugindir}/pim5/messageviewer/headerstyle/messageviewer_defaultgrantleeheaderstyleplugin.so
## check this -- rex
%dir %{_kf5_datadir}/org.kde.syntax-highlighting/
%{_kf5_datadir}/org.kde.syntax-highlighting/syntax/kmail-template.xml

%files libs -f %{name}.lang
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5MessageComposer.so.*
%{_kf5_libdir}/libKPim5MessageCore.so.*
%{_kf5_libdir}/libKPim5MessageList.so.*
%{_kf5_libdir}/libKPim5MessageViewer.so.*
%{_kf5_libdir}/libKPim5MimeTreeParser.so.*
%{_kf5_libdir}/libKPim5TemplateParser.so.*
%{_kf5_libdir}/libKPim5WebEngineViewer.so.*

%files devel
%{_kf5_archdatadir}/mkspecs/modules/qt_MessageComposer.pri
%{_includedir}/KPim5/MessageComposer/
%{_kf5_libdir}/cmake/KPim5MessageComposer/
%{_kf5_libdir}/libKPim5MessageComposer.so

%{_kf5_archdatadir}/mkspecs/modules/qt_MessageCore.pri
%{_includedir}/KPim5/MessageCore/
%{_kf5_libdir}/cmake/KPim5MessageCore/
%{_kf5_libdir}/libKPim5MessageCore.so

%{_kf5_archdatadir}/mkspecs/modules/qt_MessageList.pri
%{_includedir}/KPim5/MessageList/
%{_kf5_libdir}/cmake/KPim5MessageList/
%{_kf5_libdir}/libKPim5MessageList.so

%{_kf5_archdatadir}/mkspecs/modules/qt_MessageViewer.pri
%{_includedir}/KPim5/MessageViewer/
%{_kf5_libdir}/cmake/KPim5MessageViewer/
%{_kf5_libdir}/libKPim5MessageViewer.so

%{_includedir}/KPim5/MimeTreeParser/
%{_kf5_libdir}/cmake/KPim5MimeTreeParser/
%{_kf5_libdir}/libKPim5MimeTreeParser.so
#{_kf5_archdatadir}/mkspecs/modules/qt_MimeTreeParser.pri

%{_kf5_archdatadir}/mkspecs/modules/qt_TemplateParser.pri
%{_includedir}/KPim5/TemplateParser/
%{_kf5_libdir}/cmake/KPim5TemplateParser/
%{_kf5_libdir}/libKPim5TemplateParser.so

%{_kf5_archdatadir}/mkspecs/modules/qt_WebEngineViewer.pri
%{_includedir}/KPim5/WebEngineViewer/
%{_kf5_libdir}/cmake/KPim5WebEngineViewer/
%{_kf5_libdir}/libKPim5WebEngineViewer.so


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 23.08.5-5
- Prepare for Oreon 11 (RP1)
