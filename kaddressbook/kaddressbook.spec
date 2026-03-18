Name:    kaddressbook
Summary: Contact Manager
Version: 25.12.3
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://www.kde.org/applications/office/kaddressbook

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz


BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: libappstream-glib
BuildRequires: perl-generators

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)

# kf5
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6IconThemes)

Obsoletes: kdepim-apps-libs < 20.11.90

BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6KontactInterface)
BuildRequires: cmake(KPim6Libkdepim)
BuildRequires: cmake(KPim6PimCommonAkonadi)
BuildRequires: cmake(KPim6AkonadiSearch)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6GrantleeTheme)
BuildRequires: cmake(KPim6LdapCore)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
KAddressBook stores all the personal details of your family, friends
and other contacts.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes: kdepim-apps-libs-devel < 20.11.90
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kaddressbook-importer.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/kaddressbook-view.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml


%files -f %{name}.lang
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_bindir}/kaddressbook
%{_kf6_metainfodir}/org.kde.kaddressbook.appdata.xml
%{_kf6_datadir}/applications/org.kde.kaddressbook.desktop
%{_kf6_datadir}/applications/kaddressbook-importer.desktop
%{_kf6_datadir}/applications/kaddressbook-view.desktop
%{_kf6_datadir}/icons/hicolor/*/apps/kaddressbook.*
%{_kf6_datadir}/kaddressbook/

%files libs
%{_kf6_libdir}/libkaddressbookprivate.so.*
%{_kf6_qtplugindir}/kaddressbookpart.so
%{_qt6_plugindir}/pim6/kcms/kaddressbook/
%{_kf6_qtplugindir}/pim6/kontact/kontact_kaddressbookplugin.so
%{_kf6_libdir}/libKPim6AddressbookImportExport.so.*

%files devel
%{_kf6_libdir}/libKPim6AddressbookImportExport.so
%{_includedir}/KPim6/
%{_libdir}/cmake/KPim6AddressbookImportExport/


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
