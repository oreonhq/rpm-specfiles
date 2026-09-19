%global source0_hash eae7f687f76950b8e490420747076087bf3fb04da15df6b04b663586b2550f81

# uncomment to enable bootstrap mode
%global bootstrap 1

%if !0%{?bootstrap}
%global tests 1
%endif

%global framework sieveeditor

Name:    pim-sieve-editor
Summary: Sieve Editor
Version: 25.12.3
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://invent.kde.org/pim/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# Uses QtWebEngine: KPim6KSieveUi
# handled by qt6-srpm-macros, which defines %%qt6_qtwebengine_arches
%{?qt6_qtwebengine_arches:ExclusiveArch: %{qt6_qtwebengine_arches}}

## Upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gettext
BuildRequires: perl-generators

BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Bookmarks)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6UserFeedback)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KPim6MailTransport)
BuildRequires: cmake(KPim6PimCommon)
BuildRequires: cmake(KPim6KSieveUi)
BuildRequires: cmake(KPim6IMAP)
BuildRequires: cmake(Qt6Keychain)

# split from kdepim/kmail
Conflicts: kmail < 16.12

%description
Sieve Editor is an editor for Sieve scripts used for email filtering
on a mail server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.sieveeditor.desktop

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_datadir}/qlogging-categories6/*%{framework}.*
%{_kf6_bindir}/sieveeditor
%{_kf6_datadir}/applications/org.kde.sieveeditor.desktop
%{_kf6_metainfodir}/org.kde.sieveeditor.appdata.xml
%{_kf6_datadir}/config.kcfg/sieveeditorglobalconfig.kcfg
%{_kf6_libdir}/libsieveeditor.so.*
%{_kf6_datadir}/icons/hicolor/16x16/apps/sieveeditor.png
%{_kf6_datadir}/icons/hicolor/22x22/apps/sieveeditor.png
%{_kf6_datadir}/icons/hicolor/32x32/apps/sieveeditor.png
%{_kf6_datadir}/icons/hicolor/48x48/apps/sieveeditor.png
%{_kf6_datadir}/icons/hicolor/64x64/apps/sieveeditor.png
%{_kf6_datadir}/icons/hicolor/scalable/apps/sieveeditor.svg

%changelog
%autochangelog
