%global source0_hash efb719d6659c39a03b165dca3b6c84f729a833290fc44e7e1f99625690b6115a

%global framework kio

%bcond kf6_compat %[0%{?fedora} >= 40 || 0%{?rhel} >= 10]
%bcond_with bootstrap

Name:    kf5-%{framework}
Version: 5.116.0
Release: 6%{?dist}
Summary: KDE Frameworks 5 Tier 3 solution for filesystem abstraction

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT
URL:     https://invent.kde.org/frameworks/%{framework}

%global majmin %majmin_ver_kf5
%global stable %stable_kf5
Source0: http://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz

## upstream patches (lookaside)

## upstreamable patches

%if 0%{?flatpak}
# Disable the help: and ghelp: protocol for Flatpak builds, to avoid depending
# on the docbook stack.
Patch101: kio-no-help-protocol.patch
%endif

# filter plugin provides
%global __provides_exclude_from ^(%{_kf5_qtplugindir}/.*\\.so)$

BuildRequires:  extra-cmake-modules >= %{majmin}
BuildRequires:  kf5-rpm-macros
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires: gcc-toolset-12
%endif
# core
BuildRequires:  kf5-karchive-devel >= %{majmin}
BuildRequires:  kf5-kconfig-devel >= %{majmin}
BuildRequires:  kf5-kcoreaddons-devel >= %{majmin}
BuildRequires:  kf5-kcrash-devel >= %{majmin}
BuildRequires:  kf5-kdoctools-devel >= %{majmin}
BuildRequires:  kf5-kdbusaddons-devel >= %{majmin}
BuildRequires:  kf5-kguiaddons-devel >= %{majmin}
BuildRequires:  kf5-ki18n-devel >= %{majmin}
BuildRequires:  kf5-kservice-devel >= %{majmin}
BuildRequires:  kf5-solid-devel >= %{majmin}
# extras
BuildRequires:  kf5-kbookmarks-devel >= %{majmin}
BuildRequires:  kf5-kcompletion-devel >= %{majmin}
BuildRequires:  kf5-kconfigwidgets-devel >= %{majmin}
BuildRequires:  kf5-kiconthemes-devel >= %{majmin}
BuildRequires:  kf5-kitemviews-devel >= %{majmin}
BuildRequires:  kf5-kjobwidgets-devel >= %{majmin}
BuildRequires:  kf5-kwindowsystem-devel >= %{majmin}
# others
BuildRequires:  kf5-knotifications-devel >= %{majmin}
BuildRequires:  kf5-ktextwidgets-devel >= %{majmin}
BuildRequires:  kf5-kwallet-devel >= %{majmin}
BuildRequires:  kf5-kwidgetsaddons-devel >= %{majmin}
BuildRequires:  kf5-kxmlgui-devel >= %{majmin}

BuildRequires:  krb5-devel
BuildRequires:  libacl-devel
%if !0%{?flatpak}
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
%endif
BuildRequires:  pkgconfig(blkid)
BuildRequires:  pkgconfig(mount)
BuildRequires:  zlib-devel

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  cmake(Qt5Qml)
BuildRequires:  switcheroo-control

%if %{without bootstrap}
# really runtime dep, but will make cmake happier when building
BuildRequires: kf5-kded-devel
# (apparently?) requires org.kde.klauncher5 service provided by kf5-kinit -- rex
# not versioned to allow update without bootstrap
# <skip!>
BuildRequires:  kf5-kinit-devel
%endif

Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-file-widgets%{?_isa} = %{version}-%{release}
Requires:       %{name}-ntlm%{?_isa} = %{version}-%{release}
Requires:       %{name}-gui%{?_isa} = %{version}-%{release}

Requires: kf5-kded

%description
KDE Frameworks 5 Tier 3 solution for filesystem abstraction

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       kf5-kbookmarks-devel >= %{majmin}
Requires:       kf5-kcompletion-devel >= %{majmin}
Requires:       kf5-kconfig-devel >= %{majmin}
Requires:       kf5-kcoreaddons-devel >= %{majmin}
Requires:       kf5-kitemviews-devel >= %{majmin}
Requires:       kf5-kjobwidgets-devel >= %{majmin}
Requires:       kf5-kservice-devel >= %{majmin}
Requires:       kf5-solid-devel >= %{majmin}
Requires:       kf5-kxmlgui-devel >= %{majmin}
Requires:       kf5-kwindowsystem-devel >= %{majmin}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Requires:       %{name}-core = %{version}-%{release}
Obsoletes:      kf5-kio-doc < 5.11.0-3
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%package        core
Summary:        Core components of the KIO Framework
## org.kde.klauncher5 service referenced from : src/core/slave.cpp
%{?kf5_kinit_requires}
Requires:       %{name}-core-libs%{?_isa} = %{version}-%{release}
Requires:       %{name}-doc = %{version}-%{release}
Recommends:     switcheroo-control
%description    core
KIOCore library provides core non-GUI components for working with KIO.

%package        core-libs
Summary:        Runtime libraries for KIO Core
Requires:       %{name}-core = %{version}-%{release}
%description    core-libs
%{summary}.

%package        widgets
Summary:        Widgets for KIO Framework
## org.kde.klauncher5 service referenced from : widgets/krun.cpp
## included here for completeness, even those -core already has a dependency.
%{?kf5_kinit_requires}
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
%description    widgets
KIOWidgets contains classes that provide generic job control, progress
reporting, etc.

%package        widgets-libs
Summary:        Runtime libraries for KIO Widgets library
Requires:       %{name}-widgets = %{version}-%{release}
%description    widgets-libs
%{summary}.

%package        file-widgets
Summary:        Widgets for file-handling for KIO Framework
Requires:       %{name}-widgets%{?_isa} = %{version}-%{release}
%description    file-widgets
The KIOFileWidgets library provides the file selection dialog and
its components.

%package        gui
Summary:        Gui components for the KIO Framework
Requires:       %{name}-core%{?_isa} = %{version}-%{release}
Recommends:     switcheroo-control
%description    gui
%{summary}.

%package        ntlm
Summary:        NTLM support for KIO Framework
%description    ntlm
KIONTLM provides support for NTLM authentication mechanism in KIO

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build
%if 0%{?rhel} && 0%{?rhel} < 9    
. /opt/rh/gcc-toolset-12/enable    
%endif 
%cmake_kf5

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-man --with-html

%if %{with kf6_compat}
rm %{buildroot}%{_datadir}/applications/kcm_trash.desktop
%endif

%files
%license LICENSES/*.txt
%doc README.md

%files core
%{_kf5_sysconfdir}/xdg/accept-languages.codes
%{_kf5_datadir}/qlogging-categories5/*categories
%{_kf5_libexecdir}/kio_http_cache_cleaner
%{_kf5_libexecdir}/kpac_dhcp_helper
%{_kf5_libexecdir}/kioexec
%{_kf5_libexecdir}/kioslave5
%{_kf5_libexecdir}/kiod5
%{_kf5_bindir}/ktelnetservice5
%{_kf5_bindir}/kcookiejar5
%{_kf5_bindir}/ktrash5
%{_kf5_plugindir}/kio/
%{_kf5_plugindir}/kded/
%{_kf5_qtplugindir}/kcm_*.so
%{_kf5_plugindir}/kiod/
%{_kf5_datadir}/kservices5/*.desktop
%{_kf5_datadir}/knotifications5/proxyscout.*
%{_kf5_datadir}/kf5/kcookiejar/domain_info
%if %{without kf6_compat}
%{_kf5_datadir}/applications/kcm_trash.desktop
%endif
%{_kf5_datadir}/applications/ktelnetservice5.desktop
%{_kf5_datadir}/kconf_update/*
%{_datadir}/dbus-1/services/org.kde.*.service

## omitted since 5.45, security concerns? -- rex
%if 0
# file_helper
%{_kf5_sysconfdir}/dbus-1/system.d/org.kde.kio.file.conf
%{_kf5_libexecdir}/kauth/file_helper
%{_kf5_datadir}/dbus-1/system-services/org.kde.kio.file.service
%{_kf5_datadir}/polkit-1/actions/org.kde.kio.file.policy
%endif

%files core-libs
%{_kf5_libdir}/libKF5KIOCore.so.*

%files doc -f %{name}.lang
%{_kf5_mandir}/man8/kcookiejar5.8*
%if !0%{?_with_html:1}
%{_kf5_docdir}/HTML/*/*
%endif

%files gui
%{_kf5_libdir}/libKF5KIOGui.so.*

%files widgets
#{_kf5_datadir}/kservices5/fixhosturifilter.desktop
#{_kf5_datadir}/kservices5/kshorturifilter.desktop
#{_kf5_datadir}/kservices5/kuriikwsfilter.desktop
#{_kf5_datadir}/kservices5/kurisearchfilter.desktop
#{_kf5_datadir}/kservices5/localdomainurifilter.desktop
%config %{_kf5_sysconfdir}/xdg/kshorturifilterrc
%dir %{_kf5_plugindir}/urifilters/
%{_kf5_datadir}/kservices5/searchproviders
%{_kf5_datadir}/kservices5/webshortcuts.desktop
%{_kf5_datadir}/kservicetypes5/*.desktop
%{_kf5_plugindir}/urifilters/*.so
%{_kf5_qtplugindir}/kcm_webshortcuts.so
%{_kf5_qtplugindir}/plasma/kcms/systemsettings/kcm_smb.so
%{_kf5_qtplugindir}/plasma/kcms/systemsettings_qwidgets/kcm_*.so

%files widgets-libs
%{_kf5_libdir}/libKF5KIOWidgets.so.*

%files file-widgets
%{_kf5_libdir}/libKF5KIOFileWidgets.so.*

%files ntlm
%{_kf5_libdir}/libKF5KIONTLM.so.*

%files devel
%{_datadir}/dbus-1/interfaces/*.xml
%{_kf5_bindir}/protocoltojson
%{_kf5_includedir}/*
%{_kf5_libdir}/*.so
%{_kf5_libdir}/cmake/KF5KIO/
%{_kf5_archdatadir}/mkspecs/modules/qt_*.pri
%{_kf5_datadir}/kdevappwizard/templates/kioworker.tar.bz2
%{_kf5_qtplugindir}/designer/kio5widgets.so

%changelog
%autochangelog
