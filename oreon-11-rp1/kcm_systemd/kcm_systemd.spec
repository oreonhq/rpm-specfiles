%global source0_hash 51960f4d3b4a1ceae28737c172c35aec8c1f4e534327fbc6dda76f1c17341389

%undefine __cmake_in_source_build
Name:           kcm_systemd
Version:        1.2.1
Release:        26%{?dist}
Summary:        Systemd control module for KDE

License:        GPLv2+
URL:            http://kde-apps.org/content/show.php/Kcmsystemd?content=161871
Source0:        http://download.kde.org/stable/systemd-kcm/systemd-kcm-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  systemd-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  kf5-kconfigwidgets-devel
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-ki18n-devel
BuildRequires:  kf5-kauth-devel
BuildRequires:  kf5-kcrash-devel
BuildRequires:  kf5-kio-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros

# for /usr/share/kservices5/settings-system-administration.desktop
# That file was previously shipped in this package, but now upstreamed to
# plasma-systemsettings 5.16.90.
Requires:       plasma-systemsettings >= 5.16.90

%description
Systemd control module for KDE. It provides a graphical frontend for the systemd
daemon, which allows for viewing and controlling systemd units, as well as
modifying configuration files. In integrates in the System Settings dialogue in
KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n systemd-kcm-%{version}

%build
%{cmake_kf5}
%cmake_build

%install
%cmake_install
%find_lang systemd-kcm
# fix file conflict with plasma-systemsettings >= 5.16.90
rm -f %{buildroot}%{_kf5_datadir}/kservices5/settings-system-administration.desktop

%files -f systemd-kcm.lang
%license COPYING
%doc NEWS README.md
%{_kf5_qtplugindir}/kcm_systemd.so
%{_kf5_libexecdir}/kauth/kcmsystemdhelper
%{_kf5_datadir}/dbus-1/system.d/org.kde.kcontrol.kcmsystemd.conf
%{_kf5_datadir}/dbus-1/system-services/org.kde.kcontrol.kcmsystemd.service
%{_kf5_datadir}/kservices5/kcm_systemd.desktop
%{_kf5_datadir}/polkit-1/actions/org.kde.kcontrol.kcmsystemd.policy

%changelog
%autochangelog
