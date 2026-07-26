%global source0_hash 94972bdd03c9707cb5b3638c12b1c9c9c149762d6984ab8d0de29ba78ee0535a

%global framework mailimporter

Name:    kf5-%{framework}
Version: 23.08.5
Release: 5%{?dist}
Summary: Mail importer library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/pim/%{framework}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0:        http://download.kde.org/%{stable}/release-service/%{version}/src/%{framework}-%{version}.tar.xz

# handled by qt5-srpm-macros, which defines %%qt5_qtwebengine_arches
%{?qt5_qtwebengine_arches:ExclusiveArch: %{qt5_qtwebengine_arches}}

BuildRequires:  cmake(Grantlee5)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5Test)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)

%global kf5_ver 5.89.0
BuildRequires:  extra-cmake-modules >= %{kf5_ver}
BuildRequires:  kf5-rpm-macros >= %{kf5_ver}
BuildRequires:  kf5-karchive-devel >= %{kf5_ver}
BuildRequires:  kf5-ki18n-devel >= %{kf5_ver}
BuildRequires:  kf5-kconfig-devel >= %{kf5_ver}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{kf5_ver}
BuildRequires:  kf5-ktextwidgets-devel >= %{kf5_ver}

#global majmin_ver %(echo %{version} | cut -d. -f1,2)
%global majmin_ver %{version}
BuildRequires:  kf5-akonadi-contacts-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-mime-devel >= %{majmin_ver}
BuildRequires:  kf5-akonadi-server-devel >= %{majmin_ver}
BuildRequires:  kf5-libkdepim-devel >= %{majmin_ver}
BuildRequires:  kf5-pimcommon-devel >= %{majmin_ver}
BuildRequires:  kf5-kmime-devel >= %{majmin_ver}
BuildRequires:  cmake(KF5PimTextEdit)

Obsoletes:      kdepim-libs < 7:16.04.0
Conflicts:      kdepim-libs < 7:16.04.0

%description
%{summary}.

%package        akonadi
Summary:        The MailImporterAkondi runtime library
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description akonadi
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KF5Archive)
# akonadi
Requires:       %{name}-akonadi%{?_isa} = %{version}-%{release}
%description    devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

# Rename translation files to avoid conflict with KF6
find ./po -type f -execdir mv {} libmailimporter5.po \;
sed -i "/TRANSLATION_DOMAIN/ s/libmailimporter/libmailimporter5/" CMakeLists.txt
sed -i "s/libmailimporter/libmailimporter5/" src/Messages.sh

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name

%ldconfig_scriptlets

%files -f %{name}.lang
%license LICENSES/*
%{_kf5_datadir}/qlogging-categories5/*%{framework}.*
%{_kf5_libdir}/libKPim5MailImporter.so.*

%ldconfig_scriptlets akonadi

%files akonadi
%{_kf5_libdir}/libKPim5MailImporterAkonadi.so.*

%files devel
%{_kf5_libdir}/libKPim5MailImporter.so
%{_kf5_archdatadir}/mkspecs/modules/qt_MailImporter.pri
# akonadi
%{_kf5_libdir}/libKPim5MailImporterAkonadi.so
%{_kf5_libdir}/cmake/KPim5MailImporterAkonadi/
%{_kf5_libdir}/cmake/KPim5MailImporter/
%{_includedir}/KPim5/MailImporterAkonadi/
%{_includedir}/KPim5/MailImporter/
%{_kf5_archdatadir}/mkspecs/modules/qt_MailImporterAkonadi.pri

%changelog
%autochangelog
