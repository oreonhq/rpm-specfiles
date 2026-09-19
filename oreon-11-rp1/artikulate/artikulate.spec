%global source0_hash d837d477075779ab2ac0501e2d1a8069a761fc1cfc43a68ec5bbc5d81c0c9ebc

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    artikulate
Summary: Improve your pronunciation by listening to native speakers
Version: 25.12.3
Release: 1%{?dist}

License: BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND MIT
URL:     https://invent.kde.org/education/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: kf6-filesystem
BuildRequires: cmake(Qt6Sql)
BuildRequires: cmake(Qt6Multimedia)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Xml)

BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6DocTools)

BuildRequires: libappstream-glib

Requires: %{name}-libs%{?_isa} = %{version}-%{release}

%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
%description libs
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html --with-qt

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README*
%license LICENSES/*
%{_kf6_bindir}/artikulate
%{_kf6_bindir}/artikulate_editor
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/applications/org.kde.artikulate.desktop
%{_kf6_metainfodir}/org.kde.artikulate.appdata.xml
%{_kf6_datadir}/config.kcfg/artikulate.kcfg
%{_kf6_datadir}/knsrcfiles/artikulate.knsrc

%files libs
%{_kf6_libdir}/libartikulatecore.so.0
%{_kf6_libdir}/libartikulatelearnerprofile.so.0

%changelog
%autochangelog
