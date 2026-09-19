%global source0_hash 088b44471b0fec80fb5099c69bc737b67a4e68a08a3d52f901821417defdc865

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kcolorchooser
Summary: A color chooser 
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD 
URL:     https://apps.kde.org/kcolorchooser/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Widgets)

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

%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/kcolorchooser.*

%changelog
%autochangelog
