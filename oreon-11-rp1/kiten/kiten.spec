# kanjistrokeorders-fonts was retired since F34
%global bundle_font 1


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kiten
Summary: Japanese Reference/Study Tool
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0
URL:     https://apps.kde.org/kiten/
Source:  https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6XmlGui)

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%if !0%{?bundle_font}
Requires: kanjistrokeorders-fonts
%endif


%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
License: LGPL-2.0-or-later
%description libs
%{summary}.

%package devel
Summary:  Development files for %{name}
License: LGPL-2.0-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6

%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html

## unpackaged files
%if !0%{?bundle_font}
rm -fv %{buildroot}%{_datadir}/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf
%endif


%check
for f in %{buildroot}%{_kf6_datadir}/applications/org.kde.kiten*.desktop ; do
desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kiten.appdata.xml


%files -f %{name}.lang
%license COPYING*
%license LICENSES/*
%doc AUTHORS README.md TODO
%{_kf6_bindir}/kiten
%{_kf6_bindir}/kitenkanjibrowser
%{_kf6_bindir}/kitenradselect
%{_kf6_datadir}/kiten/
%{_kf6_metainfodir}/org.kde.kiten.appdata.xml
%{_kf6_datadir}/applications/org.kde.kiten*.desktop
%{_kf6_datadir}/config.kcfg/kiten.kcfg
%{_kf6_datadir}/icons/hicolor/*/*/kiten.*
%if 0%{?bundle_font}
%{_datadir}/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf
%endif

%files libs
%{_kf6_libdir}/libkiten.so.6{,.*}

%files devel
%{_kf6_libdir}/libkiten.so
%{_includedir}/libkiten/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
