
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ktouch
Summary: Touch Typing Tutor
Version: 25.12.3
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://www.kde.org/applications/education/ktouch/

%global kf5_dl_bug %(echo %{version} | cut -d. -f3)
%if 0%{?kf5_dl_bug} >= 50
%global kf5_dl_stable unstable
%else
%global kf5_dl_stable stable
%endif

Source0: http://download.kde.org/%{kf5_dl_stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 88ed5ef0c492321be6c926bc3af3b573c4a7d2fba0b65568b5ad50b40a48c790
%global source0_file ktouch-25.12.3.tar.xz
# oreon url source checksums end

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: qt6-qtbase-private-devel

BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
%if 0%{?fedora} > 19
BuildRequires: libappstream-glib
%endif
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbfile)
BuildRequires: cmake(libxml2)

Requires:      kqtquickcharts%{?_isa}

# when split occurred
Conflicts: kdeedu < 4.7.0-10

%description
%{summary}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/ktouch-25.12.3.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "88ed5ef0c492321be6c926bc3af3b573c4a7d2fba0b65568b5ad50b40a48c790" || { echo "oreon: Source0 SHA256 mismatch for ktouch-25.12.3.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup


%build
%{cmake_kf6} \
  -DCOMPILE_QML:BOOL=OFF
%cmake_build


%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-man


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS
%license LICENSES/*
%{_kf6_bindir}/ktouch
%{_kf6_datadir}/ktouch/
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/config.kcfg/ktouch.kcfg
%{_kf6_datadir}/icons/hicolor/*/*/ktouch.*
%{_mandir}/man1/ktouch.*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
