%global source0_hash 76fda84a231a8e5e59a507c9b5a5526c4e6a41f96faa63bb50e98cf7de01bc6b
Name:          maui-mauikit-arca
Version:       1.0.0
Release:        1%{?dist}
License:       LGPL-3.0-only
Summary:        Maui Archiver for compressed files
URL:           https://apps.kde.org/%{name}/
Source0:        https://download.kde.org/stable/maui/arca/%{version}/arca-%{version}.tar.xz
Requires:      hicolor-icon-theme
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(MauiKit4)
BuildRequires:  cmake(MauiKitArchiver4)
BuildRequires:  cmake(MauiKitFileBrowsing4)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir arca-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.arca.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
