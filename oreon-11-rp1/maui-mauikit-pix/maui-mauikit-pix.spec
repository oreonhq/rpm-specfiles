%global source0_hash 5b404113a5a397c85a3ef133bf68696e205e54377571837c96964a011174adf3

Name:          maui-mauikit-pix
Version:       4.0.0
Release:       4%{?dist}
License:       GPL-3.0-or-later AND BSD-3-Clause AND MIT
Summary:       Image gallery manager built on the maui framework
URL:           https://mauikit.org/apps/pix/

# Doesn't build on i686.
ExcludeArch:   %{ix86}

Source0:       https://download.kde.org/stable/maui/pix/%{version}/maui-pix-%{version}.tar.xz

# One license in LICENSES/ is no longer used and one was missing.
# https://invent.kde.org/maui/maui-pix/-/merge_requests/16
Patch0:        16.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKitImageTools4)
BuildRequires: cmake(MauiKit4)
BuildRequires: pkgconfig(exiv2)

Requires:      hicolor-icon-theme

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n maui-pix-%{version}

%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.pix.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%find_lang pix --with-man --with-qt --all-name

%files -f pix.lang
%license LICENSES/*
%{_datadir}/icons/hicolor/scalable/apps/pix.svg
%{_datadir}/applications/org.kde.pix.desktop
%{_metainfodir}/org.kde.pix.appdata.xml
%{_kf6_bindir}/pix

%changelog
%autochangelog
