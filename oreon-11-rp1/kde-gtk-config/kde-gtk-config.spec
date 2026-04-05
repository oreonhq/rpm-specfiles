
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kde-gtk-config
Summary: Configure the appearance of GTK apps in KDE
Version: 6.6.2
Release:	2%{?dist}

License: BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/kde-gtk-config-%{version}.tar.xz
Source1: https://download.kde.org/%{stable_kf6}/plasma/%{version}/kde-gtk-config-%{version}.tar.xz.sig

# upstream patches

## upstreamable patches

BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel

BuildRequires:  cmake(KDecoration3)
BuildRequires:  cmake(KF6ColorScheme)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6WindowSystem)

BuildRequires:  gsettings-desktop-schemas-devel
BuildRequires:  gtk3-devel
BuildRequires:  gtk2-devel
BuildRequires:  sassc

# dir ownership
Requires:       breeze-gtk-common
# need kcmshell5 from kde-cli-tools
Requires:       kde-cli-tools

# runtime dep checked-for at buildtime
BuildRequires:  xsettingsd
# avoid hard dep for now -- rex
Recommends:     xsettingsd

%description
This is a System Settings configuration module for configuring the
appearance of GTK apps in KDE.


%prep
%autosetup -p1


%build
%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
%cmake_install_kf6
%files
%license LICENSES/*.txt
%{_libexecdir}/gtk3_preview
%{_libdir}/kconf_update_bin/gtk_theme
%{_datadir}/kconf_update/gtkconfig.upd
%{_datadir}/kconf_update/remove_window_decorations_from_gtk_css.sh
%{_libdir}/kconf_update_bin/remove_deprecated_gtk4_option_v2
%{_kf6_plugindir}/kded/gtkconfig.so
%{_libdir}/gtk-3.0/modules/libcolorreload-gtk-module.so
%{_libdir}/gtk-3.0/modules/libwindow-decorations-gtk-module.so
%{_datadir}/themes/Breeze/window_decorations.css
%{_datadir}/kcm-gtk-module/
%{_datadir}/qlogging-categories6/kde-gtk-config.categories


%changelog
* Sat Apr 04 2026 Oreon Packaging Team <packaging@oreonhq.com>
- KF6 packaging: use kf6 cmake build/install macros (no qt6 prepare_docs / forced install_html_docs)

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.2-1
- Prepare for Oreon 11 (RP1)
