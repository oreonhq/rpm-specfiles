%global source0_hash 7a813f9ea815a09c1e733d0e7dc879c64eee85f075389e87e6aab99cf0c1c1ff

%global app_id org.kde.kexi

# koffice version to Obsolete
%global koffice_ver 3:2.3.70

%bcond_with bootstrap

%if %{without bootstrap}
# some known failures, ping upstream
%global tests 1
%endif

Name:    kexi
Summary: An integrated environment for managing data
Version: 3.2.0
Release: 15%{?dist}
License: LGPL-2.0-or-later AND GFDL-1.2-or-later
Url:     https://kexi-project.org/
Source0: https://download.kde.org/%{stable_kf5}/%{name}/src/%{name}-%{version}.tar.xz

## upstream patches (lookaside cache)
Patch8: 0008-cmake-find-PostgreSQL-12.patch
Patch13: 0013-Fix-build-with-Qt-5.13.patch
Patch31: 0031-add-override-where-needed.patch
Patch36: 0036-TRIVIAL-Move-Q_REQUIRED_RESULT-to-correct-place.patch
Patch50: 0050-cmake-find-PostgreSQL-13.patch
Patch80: 0080-cmake-find-PostgreSQL-14.patch
Patch504: 0504-Fix-glib-include-position.patch
Patch543: 0543-Fix-build-with-GCC-12-standard-attributes-in-middle-.patch

BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(Qt5PrintSupport)
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Qml)

BuildRequires: cmake(Qt5UiTools)
#BuildRequires: cmake(Qt5WebKit)
#BuildRequires: cmake(Qt5WebKitWidgets)

BuildRequires: cmake(KF5Archive)
BuildRequires: cmake(KF5Codecs)
BuildRequires: cmake(KF5Completion)
BuildRequires: cmake(KF5Config)
BuildRequires: cmake(KF5ConfigWidgets)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5Crash)
BuildRequires: cmake(KF5GuiAddons)
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5IconThemes)
BuildRequires: cmake(KF5ItemViews)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5TextEditor)
BuildRequires: cmake(KF5TextWidgets)
BuildRequires: cmake(KF5WidgetsAddons)
BuildRequires: cmake(KF5XmlGui)

BuildRequires: cmake(KF5DocTools)
#BuildRequires: doxygen

BuildRequires: breeze-icon-theme-rcc
# needed at runtime too, apparently -- rex
Requires: breeze-icon-theme-rcc

# kdb/kproperty/kreport and kexi are all tied together
BuildRequires: cmake(KDb) >= %{version}
BuildRequires: cmake(KPropertyWidgets) >= %{version}
BuildRequires: cmake(KReport) >= %{version}

Requires: kdb%{?_isa} >= %{version}
Requires: kproperty%{?_isa} >= %{version}
Requires: kreport%{?_isa} >= %{version}

## mapbrowser currently disabled in sources
#BuildRequires: cmake(Marble)

## DB engines
BuildRequires: glib2-devel
BuildRequires: mariadb-connector-c-devel
# this shouldn't be needed, but the build system configuration seems to
# mistakenly detect server-related headers
BuildRequires: postgresql-server-devel

%if 0%{?tests}
BuildRequires: cmake(Qt5Test)
BuildRequires: xorg-x11-server-Xvfb
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

Obsoletes: koffice-kexi < %{koffice_ver}
Obsoletes: koffice-kexi-libs < %{koffice_ver}

Obsoletes: calligra-kexi < 3.0.0
Provides:  calligra-kexi = %{version}-%{release}

Obsoletes: calligra-kexi-map-form-widget < 3.0.0
#Provides:  calligra-kexi-map-form-widget = %{version}-%{release}

%description
Kexi is an integrated data management application.  It can be used for
creating database schemas, inserting data, performing queries, and
processing data. Forms can be created to provide a custom interface to
your data. All database objects – tables, queries and forms – are
stored in the database, making it easy to share data and design.

For additional database drivers take a look at kexi-driver-*

%package  libs
Summary:  Runtime libraries for %{name}
Obsoletes: calligra-kexi-libs < 3.0.0
Provides:  calligra-kexi-libs = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package spreadsheet-import
Summary: Spreadsheet-to-Kexi-table import plugin
Obsoletes: calligra-kexi-spreadsheet-import < 3.0.0
Provides:  calligra-kexi-spreadsheet-import = %{version}-%{release}
Requires: %{name} = %{version}-%{release}
%description spreadsheet-import
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf5 \
  -DBUILD_TESTING:BOOL=%{?tests:ON}%{?!tests:OFF}

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

## versioning silliness
# compat symlink
ln -s kexi-%{majmin_ver_kf5} %{buildroot}%{_bindir}/kexi
# rename appdata/.desktop
mv %{buildroot}%{_metainfodir}/%{app_id}-%{majmin_ver_kf5}.appdata.xml \
   %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
mv %{buildroot}%{_datadir}/applications/%{app_id}-%{majmin_ver_kf5}.desktop \
   %{buildroot}%{_datadir}/applications/%{app_id}.desktop

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
## tests have known failures, TODO: consult upstream
%if 0%{?tests}
export CTEST_OUTPUT_ON_FAILURE=1
#xvfb-run -a \
%make_build ARGS="--output-on-failure --timeout 20" -C %{_target_platform} ||:
%endif

%files -f %{name}.lang
%license COPYING.LIB COPYING.DOC
%doc AUTHORS README.md
%{_bindir}/kexi
%{_bindir}/kexi-%{majmin_ver_kf5}
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/kexi/
%{_datadir}/icons/hicolor/*/*/kexi-%{majmin_ver_kf5}.*

%ldconfig_scriptlets libs

%files libs
%license COPYING.LIB
%{_libdir}/libkexi*
%{_libdir}/libkformdesigner*
%{_qt5_plugindir}/kexi/

%changelog
%autochangelog
