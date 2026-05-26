# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7d254573de29330bd47cb332de97a824e0ea23bcabc516cc917ba16823a40c80
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           kwrited
Version:        6.6.3
Release:        3%{?dist}
Summary:        KDE daemon for wall and write messages
License:        GPL-2.0-or-later
URL:            https://invent.kde.org/plasma/kwrited
Source0:        https://download.kde.org/stable/plasma/%{version}/kwrited-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Pty)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

Requires:       kf6-filesystem

%description
%{summary}.


%prep
%oreon_verify_sources
%autosetup -n kwrited-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install


%files
%license LICENSES/*
%{_kf6_plugindir}/kded/kwrited.so
%{_kf6_datadir}/knotifications6/kwrited.notifyrc


%changelog
* Fri Apr 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-2
- Add kwrited for Plasma workspace
