%global source0_hash 6a97ac76c006dcd0ccdb33933ab71c611b79cc9ae20666deb8074a8ac43993ce

%global stable_kf6 stable


# 
ExcludeArch: %{ix86}

Name:          kjournald
Version:       26.04.3
Release:       1%{?dist}
Summary:       Framework for interacting with systemd-journald

License:       BSD-3-Clause and CC0-1.0 and MIT and LGPL-2.1-or-later and MIT
URL:           https://invent.kde.org/system/%{name}

Source:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: systemd-devel
BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6KirigamiAddons)
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: cmake(KF6Crash)

# QML module dependencies
Requires:      kf6-kirigami%{?_isa}

Requires:      %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package       libs
Summary:       Library files for kjournald
%description   libs

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n kjournald-26.04.1

%build
# Building on Qt 6.9.1 crashed the qml compiler. This is a (...temporary?) workaround.
%cmake_kf6 -DQT_QML_NO_CACHEGEN=ON
%cmake_build

%install
%cmake_install
%find_lang %{name} --with-kde --with-man --all-name
# unpackaged (headers not installed, no stable API)
rm -f %{buildroot}%{_kf6_libdir}/libkjournald.so

%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.kjournaldbrowser.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kjournaldbrowser.appdata.xml

%files -f %{name}.lang
%license LICENSES/*
%doc README.md
%{_kf6_bindir}/kjournaldbrowser
%{_kf6_datadir}/applications/org.kde.kjournaldbrowser.desktop
%{_kf6_metainfodir}/org.kde.kjournaldbrowser.appdata.xml
%{_kf6_datadir}/qlogging-categories6/kjournald.categories
%{_kf6_qmldir}/org/kde/kjournald/

%files libs
%{_kf6_libdir}/libkjournald.so.0
%{_kf6_libdir}/libkjournald.so.%{version}

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.04.1-1
- Import
