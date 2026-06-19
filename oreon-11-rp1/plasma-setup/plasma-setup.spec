%global source0_hash none

%global stable_kf6 stable
%global maj_ver_kf6 6
%global min_ver_kf6 7
%global bug_ver_kf6 0
%global qt6_minver 6.6.0
%global kf6_minver 6.5.0

%global orgname org.kde.plasmasetup

# Respect distro compiler hardening flags.
%global _hardened_build 1

Name:           plasma-setup
Version: 6.7.0
Release: 1%{?dist}
Summary:        Initial setup for systems using KDE Plasma
License:        (GPL-2.0-or-later or GPL-3.0-or-later) and GPL-2.0-or-later and GPL-3.0-or-later and (LGPL-2.0-or-later or LGPL-3.0-or-later) and (LGPL-2.1-or-later or LGPL-3.0-or-later) and LGPL-2.1-or-later and BSD-2-Clause and CC0-1.0
URL:            https://invent.kde.org/plasma/%{name}

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{maj_ver_kf6}.%{min_ver_kf6}.%{bug_ver_kf6}/%{name}-%{version}.tar.xz.sig

# Backported changes

# Proposed changes
# https://invent.kde.org/plasma/plasma-setup/-/merge_requests/101
# https://bugzilla.redhat.com/show_bug.cgi?id=2453216
Patch503:       101.patch

# Downstream only changes
Patch1001:      plasma-setup-load-oreon-wallpaper.patch
Patch1002:      plasma-setup-select-oreon-lookandfeel.patch

BuildRequires:  cmake(Qt6Core) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Gui) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Qml) >= %{qt6_minver}
BuildRequires:  cmake(Qt6QuickControls2) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Svg) >= %{qt6_minver}
BuildRequires:  cmake(Qt6Widgets) >= %{qt6_minver}
BuildRequires:  cmake(Qt6DBus) >= %{qt6_minver}
BuildRequires:  cmake(KF6I18n) >= %{kf6_minver}
BuildRequires:  cmake(KF6Package) >= %{kf6_minver}
BuildRequires:  cmake(KF6Auth) >= %{kf6_minver}
BuildRequires:  cmake(KF6CoreAddons) >= %{kf6_minver}
BuildRequires:  cmake(KF6Config) >= %{kf6_minver}
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cracklib-devel
BuildRequires:  extra-cmake-modules >= %{kf6_minver}
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  systemd-rpm-macros
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  system-backgrounds-kde
BuildRequires:  qt6qml(org.kde.plasma.private.kcm_keyboard)

Requires:       qt6qml(org.kde.plasma.private.kcm_keyboard)

Requires:       dbus-common
Requires:       kf6-filesystem
Requires:       kf6-kauth

# Oreon look and feel package
Requires:       oreon-plasmaconfig
Requires:       system-backgrounds-kde

# Renamed from KDE Initial System Setup / kiss
Obsoletes:      kiss < %{version}-%{release}
Provides:       kiss = %{version}-%{release}
Provides:       kiss%{?_isa} = %{version}-%{release}

ExcludeArch:    %{ix86}

# Do not check .so files in an application-specific library directory
%global __provides_exclude_from ^%{_kf6_qmldir}/org/kde/plasmasetup/.*\\.so.*$


%description
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
# e.g. RHEL 10 has .png, not .jxl
if [ -f /usr/share/wallpapers/Default/contents/images/3840x2160.png ]; then
sed -i -e 's|\.jxl|.png|' src/qml/LandingComponent.qml
fi


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%find_lang %{orgname} --all-name
rm -fv %{buildroot}%{_kf6_libdir}/libcomponentspluginplugin.a


%preun
%systemd_preun %{name}.service


%post
%systemd_post %{name}.service


%postun
%systemd_postun %{name}.service


%files -f %{orgname}.lang
%license LICENSES/*
%config(noreplace) %{_sysconfdir}/xdg/plasmasetuprc
%{_libexecdir}/%{name}*
%{_kf6_libexecdir}/kauth/%{name}*
%{_kf6_qmldir}/org/kde/plasmasetup/
%{_kf6_plugindir}/packagestructure/plasmasetup.so
%{_kf6_datadir}/plasma/packages/%{orgname}.*/
%license %{_kf6_datadir}/plasma/packages/%{orgname}.finished/contents/ui/konqi-calling.png.license
%{_unitdir}/%{name}*
%{_sysusersdir}/%{name}*
%{_tmpfilesdir}/%{name}*
%{_datadir}/dbus-1/*/%{orgname}.*
%{_datadir}/polkit-1/actions/%{orgname}.*
%{_datadir}/polkit-1/rules.d/%{name}*
%{_datadir}/qlogging-categories6/plasmasetup.categories
%{_datadir}/%{name}/


%changelog
* Mon May 25 2026 Brandon Lester <boostyconnect@oreonproject.org> - 6.6.5-1
- Update to KDE Plasma 6.6.5

* Mon Apr 27 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.4-7
- Rebrand downstream defaults for Oreon look and feel

