%global source0_hash 532de277f27c11a631144aead5687ec8caa8dc8e404ce319ff4de7bc669d9648
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    kmouth
Version: 26.08.1
Release:        1%{?dist}
Summary:        A program that speaks for you
License: GPL-2.0-or-later
URL:     https://apps.kde.org/kmouth/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6TextToSpeech)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib
# /oreon:deps
%description
Program that allows people who have lost their voice to let their
computer speak for them.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kmouth.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
