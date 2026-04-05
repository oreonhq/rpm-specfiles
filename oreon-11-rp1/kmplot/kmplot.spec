%undefine __cmake_in_source_build


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kmplot
Summary: Mathematical Function Plotter 
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later
URL:     https://cgit.kde.org/%{name}.git
Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

BuildRequires: git
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6TextWidgets)

# when split occurred
Conflicts: kdeedu-math < 4.7.0-10

%description
%{summary}.


%prep
%autosetup -p1


%build
%cmake_kf6 \
	-DQT_MAJOR_VERSION=6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man --with-qt


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/apps/%{name}.*
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%{_kf6_plugindir}/parts/%{name}part.so
%{_datadir}/dbus-1/interfaces/org.kde.%{name}.*.xml
%{_mandir}/man1/kmplot.*


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
