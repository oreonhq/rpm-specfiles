%global source0_hash daa49490600ef3a3dbd9d1ccd94e72870f6c099ae425a1c2982e014555509775

Name:          xdg-desktop-portal-lxqt
Version:       1.3.0
Release:       2%{?dist}
Summary:       A backend implementation for xdg-desktop-portal that is using Qt/KF5/libfm-qt
License:       LGPL-2.0-or-later
URL:           https://lxqt-project.org
Source0:       https://github.com/lxqt/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(libfm-qt6)
BuildRequires: cmake(KF6WindowSystem)

BuildRequires: pkgconfig(Qt5X11Extras)

BuildRequires: libexif-devel
Requires:      dbus-common
Requires:      xdg-desktop-portal

%description
%{summary}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake
%cmake_build

%install
%cmake_install

%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service

%postun
%systemd_user_postun_with_restart %{name}.service
%systemd_user_postun_with_reload %{name}.service
%systemd_user_postun %{name}.service

%files
%doc CHANGELOG README.md
%license LICENSE
%dir %{_datadir}/xdg-desktop-portal
%dir %{_datadir}/xdg-desktop-portal/portals
%{_datadir}/xdg-desktop-portal/portals/lxqt.portal
%{_datadir}/dbus-1/services/org.freedesktop.impl.portal.desktop.lxqt.service
%{_datadir}/applications/org.freedesktop.impl.portal.desktop.lxqt.desktop
%{_datadir}/xdg-desktop-portal/lxqt-portals.conf
%{_libexecdir}/xdg-desktop-portal-lxqt
%{_userunitdir}/%{name}.service

%changelog
%autochangelog
