%global source0_hash fad2b53162bf0cd1bb751fcf6d6c88b1cd2f8ff43c7257657eeb0802646227ac

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kmag
Version: 25.12.3
Release: 1%{?dist}
Summary: A screen magnifier

License: CC0-1.0 AND GPL-2.0-or-later AND GFDL-1.2-only AND BSD-3-Clause
URL:     https://invent.kde.org/accessibility/kmag
	
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6Crash)

BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(QAccessibilityClient6)

# when split occured
Conflicts: kdeaccessibility < 1:4.7.80

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc ChangeLog
%license LICENSES/*
%{_kf6_bindir}/%{name}*
%{_kf6_datadir}/%{name}
%{_kf6_metainfodir}/org.kde.%{name}.metainfo.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_mandir}/man1/*.1*

%changelog
%autochangelog
