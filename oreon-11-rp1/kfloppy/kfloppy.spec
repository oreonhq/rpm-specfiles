%global source0_hash 9d247ce63ba98bf52e5f13fb7d6ec181f489f1f0aa71e9f3abca9c71b75c63e0

%undefine __cmake_in_source_build
Name:    kfloppy
Summary: Floppy formatting tool 
Version: 23.04.3
Release: 10%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     http://utils.kde.org/projects/%{name}
#URL:    https://cgit.kde.org/%{name}.git

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: cmake(KF5I18n)
BuildRequires: cmake(KF5CoreAddons)
BuildRequires: cmake(KF5KIO)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(KF5KDELibs4Support)
BuildRequires: cmake(KF5XmlGui)

# translations moved here
Conflicts: kde-l10n < 17.03

# when split occured
Conflicts: kdeutils-common < 6:4.7.80

Obsoletes: kdeutils-kfloppy < 6:4.7.80
Provides:  kdeutils-kfloppy = 6:%{version}-%{release}

%description
KFloppy is a utility that provides a straightforward graphical means
to format 3.5" and 5.25" floppy disks.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf5_datadir}/applications/org.kde.kfloppy.desktop

%files -f %{name}.lang
%license COPYING
%doc README
%{_kf5_bindir}/kfloppy
%{_kf5_datadir}/qlogging-categories5/%{name}*
%{_kf5_metainfodir}/org.kde.kfloppy.appdata.xml
%{_kf5_datadir}/applications/org.kde.kfloppy.desktop
%{_kf5_datadir}/icons/hicolor/*/apps/kfloppy.*

%changelog
%autochangelog
