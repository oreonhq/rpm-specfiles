%global source1_hash 65a15a70f8b993d1e915b189ac7733cea4b9ca5e02bc50d4e11aeb90c2ca8b53
%global source0_hash b7641d15996f590df27d8f820dffc79d83ce9e4e19a88f03bb1d8651faa25887
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    sddm-kcm
Version:        6.7.5
Release:        1%{?dist}
Summary:        SDDM KDE configuration module
License: GPL-2.0-or-later AND GPL-3.0-only AND CC0-1.0 AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Requires:       sddm
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libxcb-devel
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  xcb-util-image-devel
# /oreon:deps
%description
This is a System Settings configuration module for configuring the
SDDM Display Manager

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kcmsddm6_qt --with-qt --all-name
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
