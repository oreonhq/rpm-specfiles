Name:    kmenuedit
Summary: KDE menu editor
Version: 6.6.2
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig

BuildRequires:  qt6-qtbase-devel

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6Sonnet)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  libappstream-glib

# when split out from kde-workspace-4.11.x
Conflicts:      kde-workspace < 4.11.15-3

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang kmenuedit5 --with-html --all-name


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kmenuedit.desktop
# commented out until upstream fixes a duplicate entries problem
#appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files -f kmenuedit5.lang
%license LICENSES/*
%{_bindir}/kmenuedit
%{_datadir}/kmenuedit/
%{_datadir}/applications/org.kde.kmenuedit.desktop
%{_datadir}/icons/hicolor/*/apps/kmenuedit.*
%{_kf6_datadir}/qlogging-categories6/kmenuedit.categories
%{_kf6_datadir}/metainfo/org.kde.kmenuedit.appdata.xml

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
