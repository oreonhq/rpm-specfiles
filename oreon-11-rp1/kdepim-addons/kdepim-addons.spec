%global source0_hash 0eebf8a6aee397b53ce1365ed6a27af5f7a348865c575ba7ac0f88787f7fa979

# adblock requires rust and corrosion
%bcond adblock 1

Name:    kdepim-addons
Version: 25.12.3
Release: 1%{?dist}
Summary: Additional plugins for KDE PIM applications
# Cargo license summary:
# MIT
# MIT OR Apache-2.0
# MIT OR Apache-2.0 OR Zlib
# MPL-2.0
# Unlicense OR MIT
# Zlib OR Apache-2.0 OR MIT
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:     https://invent.kde.org/pim/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:   %{ix86}
%endif

## upstream patches

## upstream patches (master)

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
# libphonenumber is not build for i686 anymore (i686 is not in
# %%{java_arches}), see https://fedoraproject.org/wiki/Changes/Drop_i686_JDKs
# Since libphonenumber is a transitive dependency of this package, we must
# drop i686 support as well
%{?qt6_qtwebengine_arches:ExclusiveArch: %(echo %{qt6_qtwebengine_arches} | sed -e 's/i686//g')}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Test)

BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6KCMUtils)

BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6WebEngineViewer)
BuildRequires:  cmake(KPim6TemplateParser)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6AddressbookImportExport)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KF6TextGrammarCheck)
BuildRequires:  cmake(KF6TextTranslator)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6IncidenceEditor)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6MessageList)
BuildRequires:  cmake(KPim6CalendarSupport)
BuildRequires:  cmake(KPim6EventViews)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6Gravatar)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6KSieveUi)
BuildRequires:  cmake(KPim6LdapWidgets)

BuildRequires:  cmake(KPim6Tnef)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6ImportWizard)
BuildRequires:  cmake(KPim6MailImporterAkonadi)
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(KPim6Itinerary)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  pkgconfig(libmarkdown)

%if %{with adblock}
BuildRequires:  cmake(Corrosion)
BuildRequires:  cargo-rpm-macros >= 24
%endif

Conflicts:      kdepim-common < 16.04.0

# at least until we have subpkgs for each -- rex
Supplements:    kaddressbook
Supplements:    kmail
Supplements:    korganizer

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
%if %{with adblock}
pushd plugins/webengineurlinterceptor/adblock
%cargo_prep
popd
%endif

%if %{with adblock}
%generate_buildrequires
pushd plugins/webengineurlinterceptor/adblock > /dev/null
%cargo_generate_buildrequires
popd > /dev/null
%endif

%build
%cmake_kf6 \
  -DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=FALSE

%cmake_build

%if %{with adblock}
# Rust dependency handling
pushd plugins/webengineurlinterceptor/adblock
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
popd
%endif

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%if %{with adblock}
%license plugins/webengineurlinterceptor/adblock/LICENSE.dependencies
%endif
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%if %{with adblock}
%{_kf6_libdir}/libadblockplugin.so.*
%endif
%{_kf6_libdir}/libakonadidatasetools.so.*
%{_kf6_libdir}/libdkimverifyconfigure.so.*
%{_kf6_libdir}/libexpireaccounttrashfolderconfig.so.*
%{_kf6_libdir}/libfolderconfiguresettings.so.*
%{_kf6_libdir}/libkmailconfirmbeforedeleting.so.*
%{_kf6_libdir}/libopenurlwithconfigure.so.*
%{_kf6_qmldir}/org/kde/plasma/PimCalendars/
%{_kf6_qtplugindir}/pim6/mailtransport/mailtransport_sendplugin.so
%{_kf6_qtplugindir}/plasmacalendarplugins/pimevents.so
%{_kf6_qtplugindir}/plasmacalendarplugins/pimevents/
%{_kf6_qtplugindir}/pim6/webengineviewer/
%{_kf6_qtplugindir}/pim6/contacteditor/editorpageplugins/cryptopageplugin.so
%{_kf6_qtplugindir}/pim6/kcms/kleopatra/kcm_kmail_gnupgsystem.so
%{_kf6_qtplugindir}/pim6/ldapactivities/kldapactivitiesplugin.so
%{_kf6_qtplugindir}/pim6/mailtransportactivities/kmailtransportactivitiesplugin.so
%{_kf6_libdir}/libkaddressbookmergelibprivate.so*
%{_kf6_qtplugindir}/pim6/kaddressbook/
%{_kf6_libdir}/libKPim6AutoGenerateText.so.*

# KMail
%{_kf6_bindir}/kmail_*.sh
%{_kf6_libdir}/libkmailmarkdown.so.*
%{_kf6_libdir}/libkmailquicktextpluginprivate.so.*
%{_kf6_qtplugindir}/pim6/akonadi/
%{_kf6_qtplugindir}/pim6/importwizard/
%{_kf6_qtplugindir}/pim6/kmail/
%{_kf6_qtplugindir}/pim6/libksieve/
%{_kf6_qtplugindir}/pim6/templateparser/
%{_kf6_sysconfdir}/xdg/kmail.antispamrc
%{_kf6_sysconfdir}/xdg/kmail.antivirusrc

# PimCommon
%{_kf6_libdir}/libshorturlpluginprivate.so*
%{_kf6_qtplugindir}/pim6/pimcommon/

# BodyPartFormatter, MessageViewer, MessageViewer_headers
%{_kf6_qtplugindir}/pim6/messageviewer/

%changelog
%autochangelog
