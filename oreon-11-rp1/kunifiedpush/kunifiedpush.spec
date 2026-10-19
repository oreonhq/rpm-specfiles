%global source0_hash 247ccc7bcc4277e2fc63a753c367d0ca10efe3b4916f60a44d9ca2da403c4fe5
Name:           kunifiedpush
Version:        26.04.3
Release:        2%{?dist}
Summary:        UnifiedPush client library and distributor daemon
License:        BSD-2-Clause AND CC0-1.0 AND BSD-3-Clause AND LGPL-2.0-or-later
URL:            https://invent.kde.org/libraries/kunifiedpush
Source :        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6WebSockets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  openssl-devel
BuildRequires:  systemd-rpm-macros
# /oreon:deps
%description
%{summary}.

%package devel
Summary:        %{name} development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Required headers to build components based
on %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6 -DKDE_INSTALL_SYSTEMDUSERUNITDIR=%{_userunitdir}
%cmake_build
%install
%cmake_install
%find_lang kcm_push_notifications
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/kcm_push_notifications.desktop
%files -f %{oreon_filedir}/main.list
%files -n kunifiedpush-devel -f %{oreon_filedir}/kunifiedpush-devel.list

%changelog

%autochangelog

