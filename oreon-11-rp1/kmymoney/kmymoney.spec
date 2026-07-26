%global source0_hash 40b6639e6a216100d20248ed74fa154202f9ccdfbc335227cedc1bef8ea5d377

%global kbanking 1

# uncomment to enable bootstrap mode
#global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

Summary: Personal finance
Name:    kmymoney
Version: 5.2.2
Release: 1%{?dist}

# kmm itself is GPLv2+
# bundled kdchart is GPLv2 or GPLv3, but currently not using it
License: GPL-2.0-or-later
Url:     https://kmymoney.org/
Source0: https://download.kde.org/stable/kmymoney/%{version}/kmymoney-%{version}.tar.xz

## backports from upstream

## upstreamable patches

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

BuildRequires: make
BuildRequires: boost-devel
BuildRequires: cppunit-devel
BuildRequires: desktop-file-utils
BuildRequires: doxygen
BuildRequires: gettext

BuildRequires: libappstream-glib
BuildRequires: perl-generators

# kf6
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: cmake(QGpgmeQt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(PlasmaActivities)

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6IdentityManagementCore)

BuildRequires: cmake(Qt6Keychain)
BuildRequires: cmake(LibAlkimia6)
BuildRequires: cmake(KChart6)

BuildRequires: pkgconfig(libofx)
BuildRequires: opensp-devel

## NEEDSWORK?
%global sqlcipher 1
BuildRequires: qt6-qtbase-private-devel
BuildRequires: pkgconfig(sqlcipher)
%if 0%{?kbanking}
BuildRequires: pkgconfig(aqbanking) >= 6.5.0
BuildRequires: cmake(gwengui-qt6) >= 5.10.1
%endif
BuildRequires: python3-devel
BuildRequires: pkgconfig(libical-glib)

## FIXME/TODO:
# kmymoney/payeeidentifier/ibanandbic/ibanbic.cpp includes gmpxx.h
BuildRequires: gmp-devel

%if 0%{?tests}
BuildRequires: libEGL
BuildRequires: time
BuildRequires: xwayland-run
%endif

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
KMyMoney strives to be the best personal finance manager.
The ultimate objectives of KMyMoney are...
* Accuracy.  Using time tested double entry accounting principles
  helps ensure that your finances are kept in correct order.
* Ease of use.  Strives to be the easiest open source personal
  finance manager to use, especially for the non-technical user.
* Familiar Features.  Intends to provide all important features
  found in the commercially-available, personal finance managers.

%package libs
Summary: Run-time libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary: Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%package doc
Summary: Application handbook, documentation, translations
# for upgrade path
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=ON \
  %{?tests:-DBUILD_TESTING:BOOL=ON}

%cmake_build

%install
%cmake_install

%find_lang kmymoney --with-html --without-mo && mv kmymoney.lang kmymoney-doc.lang
%find_lang kmymoney --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kmymoney.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kmymoney.desktop
%if 0%{?tests}
%global __ctest xwfb-run -- %{__ctest}
%ctest
%endif

%files -f kmymoney.lang
%doc README.md
%license LICENSES/GPL-2.0-or-later.txt
%{_kf6_bindir}/kmymoney
%{_kf6_metainfodir}/org.kde.kmymoney.appdata.xml
%{_kf6_datadir}/applications/org.kde.kmymoney.desktop
%{_kf6_datadir}/checkprinting/
%{_kf6_datadir}/config.kcfg/k*.kcfg
%{_kf6_datadir}/kconf_update/kmymoney.upd
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/mime/packages/x-kmymoney.xml
%{_mandir}/man1/kmymoney.1*

%files libs
%{_kf6_qtplugindir}/kmymoney_plugins/
%if 0%{?sqlcipher}
# adds dep on qt6 private api
%{_kf6_qtplugindir}/sqldrivers/qsqlcipher.so
%endif
%{_kf6_libdir}/libkmm_*.so.5{,.*}
%{_kf6_libdir}/libonlinetask_interfaces.so.5{,.*}

%files devel
%{_includedir}/kmymoney/
%{_kf6_libdir}/libkmm_*.so
%{_kf6_libdir}/libonlinetask_interfaces.so

%files doc -f kmymoney-doc.lang

%changelog
%autochangelog
