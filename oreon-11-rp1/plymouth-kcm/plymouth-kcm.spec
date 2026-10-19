%global source1_hash 60ef1e6ebd75b3d156b2e3687a1e15d05b427085ba24ee3f327960739a2a507d
%global stable_kf6 stable
%global source0_hash ce723d67e6b8cd71b6eb353e87c10f698a095ea7d455bee703d8ba59e793e57e
%global base_name    plymouth-kcm
ExcludeArch: %{ix86}
Name:    plymouth-kcm
Summary:        Plymouth configuration module for systemsettings
Version: 6.7.5
Release:        1%{?dist}
License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/plasma/%{base_name}
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{base_name}-%{version}.tar.xz.sig
Patch1:         0001-fedora.patch
Requires:   plymouth
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6NewStuff)
BuildRequires:  cmake(KF6NewStuffCore)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-kcmutils
BuildRequires:  kf6-rpm-macros
BuildRequires:  plymouth-devel
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
This is a System Settings configuration module for configuring the
plymouth splash screen.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{base_name}-%{version} -p1

%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang kcm_plymouth --all-name --with-html
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
