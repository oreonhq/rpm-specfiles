
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    rocs
Summary: Graph Theory IDE
Version: 25.12.3
Release:	2%{?dist}

License: BSD-2-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/education/rocs

Source0: http://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: kf6-rpm-macros

BuildRequires: boost-devel >= 1.43
BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemViews)
BuildRequires: cmake(KF6TextEditor)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: libappstream-glib

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
# when split occurred
Conflicts: kdeedu-math-libs < 4.7.0-10
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%package devel
Summary:  Development files for %{name}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/actions/*
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_qt6_plugindir}/rocs/

%files libs
%{_kf6_libdir}/librocsgraphtheory.so.*

%files devel
%{_kf6_libdir}/librocsgraphtheory.so
%{_includedir}/rocs/


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
