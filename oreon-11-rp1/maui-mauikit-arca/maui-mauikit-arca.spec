%global source0_hash 76fda84a231a8e5e59a507c9b5a5526c4e6a41f96faa63bb50e98cf7de01bc6b

Name:          maui-mauikit-arca
Version:       1.0.0
Release:       4%{?dist}
# SPDX licenses missing from project, using license in licenses/
License:       LGPL-3.0-only
Summary:       Maui Archiver for compressed files
URL:           https://apps.kde.org/%{name}/

Source0:       https://download.kde.org/stable/maui/arca/%{version}/arca-%{version}.tar.xz

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKitArchiver4)
BuildRequires: cmake(MauiKit4)

Requires:      hicolor-icon-theme

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n arca-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.arca.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%files
%license licenses/*
%{_kf6_bindir}/arca
%{_kf6_datadir}/applications/org.kde.arca.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/arca.svg
%{_metainfodir}/org.kde.arca.appdata.xml

%changelog
%autochangelog
