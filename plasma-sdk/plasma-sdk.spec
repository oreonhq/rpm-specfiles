
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    plasma-sdk
Version: 6.6.2
Release: 1%{?dist}
Summary: Development tools for Plasma 6

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{name}

Source0:        http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        http://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig


BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(Qt6Core5Compat)

BuildRequires:  cmake(Plasma5Support)
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6SyntaxHighlighting)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6GuiAddons)

BuildRequires:  cmake(Plasma)

# Desktop file verification, and appstream validation
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

# lookandfeelexplorer deps
BuildRequires:  cmake(KF6Kirigami2)
Requires:       kf6-filesystem
Requires:       hicolor-icon-theme

# Little lie: this package does not provide the actual plasmate tool yet (but
# eventually it will), but it still has some tools that were part of the KDE4
# plasmate package (and which are useless in Plasma 5)
Obsoletes:      plasmate < 5.2
Provides:       plasmate = %{version}-%{release}

%description
Plasma SDK contains tools for plasma development

%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang plasmasdk6 --with-man --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.themeexplorer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.iconexplorer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasmaengineexplorer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasmoidviewer.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop

%files -f plasmasdk6.lang
%license LICENSES/*.txt
%{_bindir}/lookandfeelexplorer
%{_bindir}/plasmaengineexplorer
%{_bindir}/plasmathemeexplorer
%{_bindir}/plasmoidviewer
%{_bindir}/iconexplorer
%{_bindir}/kqml
%{_kf6_plugindir}/ktexteditor/iconexplorerplugin.so
%{_kf6_datadir}/applications/org.kde.plasma.lookandfeelexplorer.desktop
%{_kf6_datadir}/kpackage/genericqml/org.kde.plasma.themeexplorer
%{_kf6_datadir}/plasma/shells/org.kde.plasma.plasmoidviewershell
%{_kf6_datadir}/applications/org.kde.iconexplorer.desktop
%{_kf6_datadir}/applications/org.kde.plasma.themeexplorer.desktop
%{_kf6_datadir}/applications/org.kde.plasmaengineexplorer.desktop
%{_kf6_datadir}/applications/org.kde.plasmoidviewer.desktop
%{_kf6_datadir}/metainfo/org.kde.plasmaengineexplorer.appdata.xml
%{_kf6_datadir}/metainfo/org.kde.plasmoidviewer.appdata.xml
%{_kf6_datadir}/zsh/site-functions/_plasmoidviewer
%{_kf6_datadir}/zsh/site-functions/_kqml
%{_kf6_metainfodir}/org.kde.plasma.iconexplorer.appdata.xml
%{_mandir}/man1/plasmaengineexplorer.1*
%{_mandir}/man1/plasmoidviewer.1*
%{_mandir}/man1/kqml.1.gz
%{_datadir}/icons/hicolor/scalable/apps/org.kde.iconexplorer.svg

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
