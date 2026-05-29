%global source0_hash none

# 
ExcludeArch: %{ix86}

Name:    kgeography
Summary: Geography Trainer 
Version: 26.04.1
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://invent.kde.org/education/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)

BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)


%description
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

## unpackaged files
# locale/LC_SCRIPT junk, need to keep? -- rex
rm -fv %{buildroot}%{_kf6_datadir}/locale/*/LC_SCRIPTS/kgeography/*


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license COPYING*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
