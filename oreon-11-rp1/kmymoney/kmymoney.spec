%global source0_hash 40b6639e6a216100d20248ed74fa154202f9ccdfbc335227cedc1bef8ea5d377
%global kbanking 1
%if !0%{?bootstrap}
%global tests 1
%endif
Summary:        Personal finance
Name:    kmymoney
Version: 5.2.2
Release:        1%{?dist}
License: GPL-2.0-or-later
Url:     https://kmymoney.org/
Source0:        https://download.kde.org/stable/kmymoney/%{version}/kmymoney-%{version}.tar.xz
ExcludeArch: %{ix86}
%global sqlcipher 1
%if 0%{?kbanking}
%endif
%if 0%{?tests}
%endif
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  cmake(KChart6)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(LibAlkimia6)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6QuickWidgets)
BuildRequires:  cmake(Qt6Sql)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(gwengui-qt6)
BuildRequires:  cppunit-devel
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  gmp-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  libEGL
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  opensp-devel
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(aqbanking)
BuildRequires:  pkgconfig(libical-glib)
BuildRequires:  pkgconfig(libofx)
BuildRequires:  pkgconfig(sqlcipher)
BuildRequires:  python3-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  time
BuildRequires:  xwayland-run
# /oreon:deps
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
Requires:  %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 \
  -DBUILD_WITH_QT6:BOOL=ON \
  %{?tests:-DBUILD_TESTING:BOOL=ON}
%cmake_build
%install
%cmake_install
%find_lang kmymoney --with-html --without-mo && mv kmymoney.lang kmymoney-doc.lang
%find_lang kmymoney --with-man
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kmymoney.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kmymoney.desktop
%if 0%{?tests}
%global __ctest xwfb-run -- %{__ctest}
%ctest
%endif
%files -f %{oreon_filedir}/main.list
%files -n kmymoney-libs -f %{oreon_filedir}/kmymoney-libs.list
%files -n kmymoney-devel -f %{oreon_filedir}/kmymoney-devel.list
%files -n kmymoney-doc -f %{oreon_filedir}/kmymoney-doc.list

%changelog

%autochangelog
