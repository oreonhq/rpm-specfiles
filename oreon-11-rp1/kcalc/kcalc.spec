%global stable_kf6 stable

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kcalc 
Summary: Scientific Calculator 
Version: 25.12.3
Release:	2%{?dist}

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://invent.kde.org/utils/%{name}

Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstreamable patches
# fix arithmetic fault in mod, factorial
## FIXME: review if still needed, rebase, upstream -- rdieter
#Patch100: kcalc-4.9.90-misc.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Core5Compat)

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: gmp-devel
BuildRequires: mpfr-devel
BuildRequires: libmpc-devel

%description
KCalc is a calculator which offers many more mathematical
functions than meet the eye on a first glance.


%prep
%autosetup -p1


%build
%cmake_kf6 %{?flatpak:-DINSTALL_ICONS=ON}

%{__cmake} --build \"%{__cmake_builddir}\" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%find_lang %{name} --all-name --with-html --with-man


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop ||:


%files -f %{name}.lang
%license LICENSES/*
#doc README
%{_kf6_bindir}/%{name}
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/kglobalaccel/org.kde.%{name}.desktop
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/kconf_update/%{name}*
%{_kf6_datadir}/config.kcfg/%{name}.kcfg
%if 0%{?flatpak}
%{_kf6_datadir}/icons/hicolor/*/*/accessories-calculator.*
%endif


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
