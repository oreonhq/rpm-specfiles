%global stable_kf6 stable
%global source0_hash fad2b53162bf0cd1bb751fcf6d6c88b1cd2f8ff43c7257657eeb0802646227ac
ExcludeArch: %{ix86}
Name:    kmag
Version: 25.12.3
Release:        1%{?dist}
Summary:        A screen magnifier
License: CC0-1.0 AND GPL-2.0-or-later AND GFDL-1.2-only AND BSD-3-Clause
URL:     https://invent.kde.org/accessibility/kmag
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Conflicts: kdeaccessibility < 1:4.7.80
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(QAccessibilityClient6)
BuildRequires:  cmake(Qt6PrintSupport)
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
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
