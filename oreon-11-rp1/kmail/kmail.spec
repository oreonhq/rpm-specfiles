%global source0_hash 2e5035d0f4219f7ec77a1859d483e8f902663db9bcc1c2fdd0a2a4337cc7bf89
%global stable_kf6 stable
Name:    kmail
Summary:        Mail client
Version: 26.08.1
Release:        1%{?dist}
License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://www.kde.org/applications/internet/kmail
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}
Obsoletes: pim-storage-service-manager < 17.03
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: akonadi-import-wizard
Requires: grantlee-editor
Requires: kdepim-runtime
Requires: kmail-account-wizard
Requires: pim-data-exporter
Requires: pim-sieve-editor
# oreon:deps
BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(KF6Bookmarks)
BuildRequires:  cmake(KF6CalendarCore)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6NotifyConfig)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6TextAutoCorrectionWidgets)
BuildRequires:  cmake(KF6TextCustomEditor)
BuildRequires:  cmake(KF6TextEditTextToSpeech)
BuildRequires:  cmake(KF6TextTemplate)
BuildRequires:  cmake(KF6TextUtils)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6UserFeedback)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6AkonadiSearch)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KPim6Gravatar)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KPim6KSieveUi)
BuildRequires:  cmake(KPim6KontactInterface)
BuildRequires:  cmake(KPim6LdapWidgets)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6Libkleo)
BuildRequires:  cmake(KPim6MailCommon)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MailTransportDBusService)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6MessageList)
BuildRequires:  cmake(KPim6MessageViewer)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KPim6TemplateParser)
BuildRequires:  cmake(KPim6TextEdit)
BuildRequires:  cmake(KPim6Tnef)
BuildRequires:  cmake(QGpgmeQt6)
BuildRequires:  cmake(Qt6Keychain)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  perl-generators
BuildRequires:  pkgconfig(cups)
# /oreon:deps
%description
%{summary}.

%package libs
Summary: Runtime libraries for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

for f in %{buildroot}%{_kf6_datadir}/applications/*.desktop ; do
  desktop-file-validate $f
done
for f in %{buildroot}%{_kf6_metainfodir}/*.appdata.xml ; do
appstream-util validate-relax --nonet $f
done
%files -f %{oreon_filedir}/main.list
%files -n kmail-libs -f %{oreon_filedir}/kmail-libs.list

%changelog

%autochangelog
