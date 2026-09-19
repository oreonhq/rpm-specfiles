%global source0_hash 9aa486a65f311c4e6b4013fa446780f08bc889658724e0c51c479bdf9d945a7b


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    mailcommon
Version: 26.04.3
Release: 1%{?dist}
Summary: Mail applications support library

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/pim/%{name}/

Source0:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Multimedia)

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake

BuildRequires:  cmake(Gpgmepp)
BuildRequires:  cmake(QGpgmeQt6)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6TextWidgets)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6TextTemplate)

BuildRequires:  cmake(KPim6Akonadi)
BuildRequires:  cmake(KPim6AkonadiMime)
BuildRequires:  cmake(KPim6Libkdepim)
BuildRequires:  cmake(KPim6MailImporter)
BuildRequires:  cmake(KPim6MailTransport)
BuildRequires:  cmake(KPim6MessageComposer)
BuildRequires:  cmake(KPim6MessageList)
BuildRequires:  cmake(KPim6MessageCore)
BuildRequires:  cmake(KPim6MessageViewer)
BuildRequires:  cmake(KPim6Mime)
BuildRequires:  cmake(KPim6PimCommonAkonadi)
BuildRequires:  cmake(KPim6TemplateParser)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(KPim6AkonadiContactWidgets)
BuildRequires:  cmake(KPim6IdentityManagementCore)
BuildRequires:  cmake(KF6TextCustomEditor)

%description
%{summary}.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       cmake(KPim6Akonadi)
Requires:       cmake(KPim6AkonadiMime)
Requires:       cmake(KPim6MessageComposer)
Requires:       cmake(KPim6PimCommonAkonadi)
%description    devel
%{summary}.

%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch
%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_libdir}/libKPim6MailCommon.so.*

%files devel
%{_includedir}/KPim6/MailCommon/
%{_kf6_libdir}/cmake/KPim6MailCommon/
%{_kf6_libdir}/libKPim6MailCommon.so
%{_qt6_plugindir}/designer/mailcommon6widgets.so

%files doc

%changelog
%autochangelog

