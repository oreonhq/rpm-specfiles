%global source0_hash 6a97ac76c006dcd0ccdb33933ab71c611b79cc9ae20666deb8074a8ac43993ce
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:          kjournald
Version:       26.04.3
Release:        1%{?dist}
Summary:        Framework for interacting with systemd-journald
License:       BSD-3-Clause and CC0-1.0 and MIT and LGPL-2.1-or-later and MIT
URL:           https://invent.kde.org/system/%{name}
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires:      kf6-kirigami%{?_isa}
Requires:      %{name}-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  systemd-devel
# /oreon:deps
%description
%{summary}.

%package       libs
Summary:       Library files for kjournald
%description   libs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6 -DQT_QML_NO_CACHEGEN=ON
%cmake_build
%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name
rm -f %{buildroot}%{_kf6_libdir}/libkjournald.so
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.kjournaldbrowser.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kjournaldbrowser.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kjournald-libs -f %{oreon_filedir}/kjournald-libs.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
