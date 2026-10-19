%global stable_kf6 stable
%global source0_hash 09a604e46cbacde0cc99848e18f51ae64019382beb1da11e94319bc48cc8937d
%bcond adblock 1
Name:    kdepim-addons
Version: 26.08.1
Release:        1%{?dist}
Summary:        Additional plugins for KDE PIM applications
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only) AND MIT AND (MIT OR Apache-2.0) AND (MIT OR Apache-2.0 OR Zlib) AND MPL-2.0 AND (Unlicense OR MIT) AND (Zlib OR Apache-2.0 OR MIT)
URL:     https://invent.kde.org/pim/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:   %{ix86}
%endif
%{?qt6_qtwebengine_arches:ExclusiveArch: %(echo %{qt6_qtwebengine_arches} | sed -e 's/i686//g')}
%if %{with adblock}
%endif
Conflicts:      kdepim-common < 16.04.0
Supplements:    kaddressbook
Supplements:    kmail
Supplements:    korganizer
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  cmake(Corrosion)
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Holidays)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Prison)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextAddonsWidgets)
BuildRequires:  cmake(KF6TextGrammarCheck)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextTranslator)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6AddressbookImportExport)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiCalendar)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6AkonadiNotes)
BuildRequires:  cmake(KPim6CalendarSupport)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6EventViews)
BuildRequires:  cmake(KPim6GrantleeTheme)
BuildRequires:  cmake(KPim6Gravatar)
BuildRequires:  cmake(KPim6IMAP)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6ImportWizard)
BuildRequires:  cmake(KPim6IncidenceEditor)
BuildRequires:  cmake(KPim6Itinerary)
BuildRequires:  cmake(KPim6KSieveUi)
BuildRequires:  cmake(KPim6LdapWidgets)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailImporterAkonadi)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6MessageList)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KPim6PkPass)
BuildRequires:  cmake(KPim6TemplateParser)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6Tnef)
BuildRequires:  cmake(KPim6WebEngineViewer)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebEngineWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libmarkdown)
# /oreon:deps
%description
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1
%if %{with adblock}
pushd plugins/webengineurlinterceptor/adblock
popd
%endif

%if %{with adblock}
%build

%cmake_kf6 \
  -DKDEPIMADDONS_BUILD_EXAMPLES:BOOL=FALSE
%cmake_build
%if %{with adblock}
pushd plugins/webengineurlinterceptor/adblock
%cargo_license_summary
%{cargo_license} > LICENSE.dependencies
popd
%endif
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
%endif
