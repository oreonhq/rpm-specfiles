%global source0_hash 2be1891bf498cb38030ca5db1ad022c502557c1c0b8ff6ac3fdac8254a5bb76b

%undefine __cmake_in_source_build

Name:    okteta
Summary: Binary/hex editor
Epoch:   1
Version: 0.26.25
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/okteta/%{version}/src/%{name}-%{version}.tar.xz
Patch0: okteta-gcc11.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kbookmarks-devel
BuildRequires: kf5-kcodecs-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kdbusaddons-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kparts-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kxmlgui-devel

BuildRequires: pkgconfig(qca2-qt5)
BuildRequires: pkgconfig(Qt5Designer)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Network)
BuildRequires: pkgconfig(Qt5PrintSupport)
BuildRequires: pkgconfig(Qt5Script)
BuildRequires: pkgconfig(Qt5ScriptTools)
BuildRequires: pkgconfig(Qt5Test)
BuildRequires: pkgconfig(Qt5Widgets)
BuildRequires: pkgconfig(Qt5Xml)

Requires: kio-extras-kf5

# translations moved here
Conflicts: kde-l10n < 17.03

Conflicts:      kdesdk-common < 4.10.80
Obsoletes:      kdesdk-okteta < 4.10.80
Provides:       kdesdk-okteta = %{epoch}:%{version}-%{release}

Requires:       %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
# struct2osd.sh deps
%if 0%{?fedora} > 20  || 0%{?rhel} > 7
Recommends: castxml libxslt
%else
Requires: castxml libxslt
%endif

%description
Okteta is a binary/hex editor for KDE

%package libs
Summary: Runtime libraries and kpart plugins for %{name}
Obsoletes: kdesdk-okteta-libs < 4.10.80
Provides:  kdesdk-okteta-libs = %{epoch}:%{version}-%{release}
Provides:  okteta5-part = %{epoch}:%{version}-%{release}
Provides:  okteta5-part%{?_isa} = %{epoch}:%{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Developer files for %{name}
Obsoletes: kdesdk-okteta-devel < 4.10.80
Provides:  kdesdk-okteta-devel = %{epoch}:%{version}-%{release}
Provides:  okteta5-devel = %{epoch}:%{version}-%{release}
Requires:  %{name}-libs%{?_isa} = %{epoch}:%{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf5_metainfodir}/org.kde.okteta.appdata.xml ||:
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.okteta.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_bindir}/okteta
%{_bindir}/struct2osd
%{_datadir}/mime/packages/okteta.xml
%{_kf5_metainfodir}/org.kde.okteta.appdata.xml
%{_kf5_datadir}/knsrcfiles/okteta-structures.knsrc
%{_datadir}/applications/org.kde.okteta.desktop
#{_datadir}/kxmlgui5/okteta/
%{_datadir}/icons/hicolor/*/apps/okteta.*

%ldconfig_scriptlets libs

%files libs
%dir %{_datadir}/okteta/
%{_datadir}/okteta/structures/
%{_datadir}/config.kcfg/structureviewpreferences.kcfg
%{_libdir}/libKasten4*.so.*
%{_libdir}/libOkteta3*.so.*
# part
%{_kf5_plugindir}/parts/oktetapart.so
%{_kf5_datadir}/kservices5/oktetapart.desktop

%files devel
%{_includedir}/Okteta*/
%{_includedir}/Kasten*/
%{_libdir}/libKasten4*.so
%{_libdir}/libOkteta3*.so
%{_libdir}/cmake/KastenControllers/
%{_libdir}/cmake/KastenCore/
%{_libdir}/cmake/KastenGui/
%{_libdir}/cmake/OktetaCore/
%{_libdir}/cmake/OktetaGui/
%{_libdir}/cmake/OktetaKastenControllers/
%{_libdir}/cmake/OktetaKastenCore/
%{_libdir}/cmake/OktetaKastenGui/
%{_libdir}/pkgconfig/Okteta*.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_Okteta*.pri
%{_qt5_plugindir}/designer/oktetawidgets.so

%changelog
%autochangelog
