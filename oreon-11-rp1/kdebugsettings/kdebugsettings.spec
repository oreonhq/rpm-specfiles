%global source0_hash none

%global stable_kf6 stable


# 
ExcludeArch: %{ix86}

Name:    kdebugsettings
Summary: Configure debug output from Qt6 applications
Version: 26.04.1
Release: 1%{?dist}

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
URL:     https://apps.kde.org/kdebugsettings/

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6WindowSystem)

%description
An application to enable/disable qCDebug


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup


%build
%cmake_kf6

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man


%check
## currently fails on all RHEL releases
# RHEL8: https://bugzilla.redhat.com/show_bug.cgi?id=2107277
# RHEL9: https://bugzilla.redhat.com/show_bug.cgi?id=2107278
%if !0%{?rhel} || (0%{?oreon} >= 11)
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.kdebugsettings.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kdebugsettings.*.xml
%endif


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/kdebugsettings
%{_kf6_datadir}/applications/org.kde.kdebugsettings.desktop
%{_kf6_datadir}/kdebugsettings/
%{_kf6_metainfodir}/org.kde.kdebugsettings.*.xml
%{_kf6_datadir}/qlogging-categories6/kde*
%{_kf6_libdir}/libkdebugsettings.so.*
%{_kf6_libdir}/libkdebugsettingscore.so.*


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
