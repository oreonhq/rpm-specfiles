
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kompare
Summary: Diff tool
Version: 25.12.3
Release:	2%{?dist}

License: GFDL-1.2-or-later AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://apps.kde.org/kompare/

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Codecs)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6TextEditor)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6I18n)

BuildRequires:  cmake(KompareDiff2)

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

Provides:       mergetool

%description
Tool to visualize changes between two versions of a file

%package libs
Summary: Runtime libraries for %{name}
Requires:  libkomparediff2%{?_isa}
%description libs
This package contains shared libraries for %{name}.

%package devel
Summary: Developer files for %{name}
Requires:  %{name}-libs%{?_isa} = %{version}-%{release}
Requires:  qt6-qtbase-devel
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kompare.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kompare.appdata.xml


%files -f %{name}.lang
%doc README
%license LICENSES/*
%{_bindir}/kompare
%{_datadir}/applications/org.kde.kompare.desktop
%{_datadir}/icons/hicolor/*/apps/kompare.*
%{_datadir}/kio/servicemenus/kompare.desktop
%{_kf6_datadir}/qlogging-categories6/kompare.categories
%{_kf6_metainfodir}/org.kde.kompare.appdata.xml

%files libs
%{_libdir}/libkomparedialogpages.so.*
%{_libdir}/libkompareinterface.so.*
%{_kf6_plugindir}/parts/komparenavtreepart.so
%{_kf6_plugindir}/parts/komparepart.so

%files devel
%{_includedir}/kompare/
%{_libdir}/libkompareinterface.so


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
