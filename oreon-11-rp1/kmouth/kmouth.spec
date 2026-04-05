
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kmouth
Version: 25.12.3
Release:	2%{?dist}
Summary: A program that speaks for you 

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kmouth/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6TextToSpeech)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Widgets)

%description
Program that allows people who have lost their voice to let their
computer speak for them.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kmouth.desktop


%files -f %{name}.lang
%license COPYING*
%{_kf6_sysconfdir}/xdg/kmouthrc
%{_kf6_bindir}/kmouth
%{_kf6_datadir}/kmouth/
%{_kf6_datadir}/applications/org.kde.kmouth.desktop
%{_kf6_metainfodir}/org.kde.kmouth.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/*.1*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
