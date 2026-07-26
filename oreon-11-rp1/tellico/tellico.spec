%global source0_hash 3c00d5213d36fb6faa16d57dba42568e801505f25846e41b342c159c1b3b66a5

Name:           tellico
Version:        4.1.2
Release:        5%{?dist}
Summary:        A collection manager

License:        GPL-2.0-or-later
URL:            https://tellico-project.org/
Source0:        https://tellico-project.org/files/tellico-%{version}.tar.xz

ExclusiveArch:  %{qt6_qtwebengine_arches}

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6PrintSupport)

BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6TextWidgets)
#BuildRequires:  cmake(KF6Wallet)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)

BuildRequires:  cmake(Qt6WebEngineWidgets)

# optional (non mandatory)
BuildRequires:  cmake(Qt6Charts)
BuildRequires:  cmake(KF6FileMetaData)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KSaneWidgets6)
BuildRequires:  cmake(KCddb6)

BuildRequires:  libxslt-devel
BuildRequires:  libxml2-devel
BuildRequires:  gettext
BuildRequires:  taglib-devel
BuildRequires:  libyaz-devel
BuildRequires:  poppler-qt6-devel
BuildRequires:  exempi-devel
# required for btparse (as this package has the btparse.h header file)
BuildRequires:  perl-Text-BibTeX
BuildRequires:  libcdio-devel
BuildRequires:  libcsv-devel
BuildRequires:  libv4l-devel

Requires: python3

%description
Tellico is a collection manager by KDE. It includes default collections for
books, bibliographies, comic books, videos, music, coins, stamps, trading
cards, and wines, and also allows custom collections. Unlimited user-defined
fields are allowed. Filters are available to limit the visible entries by
definable criteria. Full customization for printing is possible through
editing the default XSLT file. It can import CSV, Bibtex, and Bibtexml and
export CSV, HTML, Bibtex, Bibtexml, and PilotDB. Entries may be imported
directly from Amazon.com.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# There are just two scripts
sed \
  -i.python \
  -e "s|^#!/usr/bin/env python$|#!%{__python3}|g" \
  src/fetch/scripts/*.py

%build
%{cmake_kf6} -DENABLE_WEBCAM:BOOL=ON
%cmake_build

%install
%cmake_install

%find_lang %{name} --with-kde --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.tellico.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.tellico.appdata.xml

%files -f %{name}.lang
%doc AUTHORS ChangeLog
%license COPYING
%{_kf6_bindir}/tellico
%{_kf6_datadir}/applications/org.kde.tellico.desktop
%{_kf6_datadir}/kconf_update/*
%{_kf6_datadir}/tellico/
%{_kf6_datadir}/config.kcfg/tellico_config.kcfg
%{_sysconfdir}/xdg/tellicorc
%{_kf6_datadir}/knsrcfiles/tellico-template.knsrc
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/mime/packages/tellico.xml
%{_kf6_metainfodir}/org.kde.tellico.appdata.xml

%changelog
%autochangelog
