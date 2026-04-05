
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    blinken 
Summary: Memory Enhancement Game 
Version: 25.12.3
Release:	2%{?dist}

License: GPL-2.0-or-later
URL:     https://apps.kde.org/blinken/
Source:  https://download.kde.org/%{stable_kf5}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gettext
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Multimedia)

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Crash)

BuildRequires: cmake(Phonon4Qt6)

Requires: hicolor-icon-theme
Requires: sj-stevehand-fonts

%description
%{summary}.


%prep
%autosetup


%build
%cmake_kf6

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-qt

## unpackaged files
# omit bundled steve font
rm -fv %{buildroot}%{_kf6_datadir}/blinken/fonts/steve.ttf


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop


%files -f %{name}.lang
%doc AUTHORS 
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
%{_kf6_datadir}/config.kcfg/%{name}.kcfg


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
