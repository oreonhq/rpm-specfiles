%global source0_hash 68b61bca8a07c0b9bf0a812544ba46e8d52b799a9dc15fad5b25e6beb80e4cd4
%global stable_kf6 stable
%global bundle_font 1
ExcludeArch: %{ix86}
Name:    kiten
Summary:        Japanese Reference/Study Tool
Version: 26.08.1
Release:        1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND BSD-3-Clause AND CC-BY-SA-3.0 AND CC-BY-SA-4.0
URL:     https://apps.kde.org/kiten/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%if !0%{?bundle_font}
Requires: kanjistrokeorders-fonts
%endif
# oreon:deps
BuildRequires:  cmake(KF6Archive)
BuildRequires:  cmake(KF6Completion)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6ConfigWidgets)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gettext
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
# /oreon:deps
%description
%{summary}.

%package  libs
Summary:  Runtime files for %{name}
Requires: %{name} = %{version}-%{release}
License: LGPL-2.0-or-later
%description libs
%{summary}.

%package devel
Summary:  Development files for %{name}
License: LGPL-2.0-or-later
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
%description devel
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%if !0%{?bundle_font}
rm -fv %{buildroot}%{_datadir}/fonts/kanjistrokeorders/KanjiStrokeOrders.ttf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%endif
%check

for f in %{buildroot}%{_kf6_datadir}/applications/org.kde.kiten*.desktop ; do
desktop-file-validate $f
done
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kiten.appdata.xml
%files -f %{oreon_filedir}/main.list
%files -n kiten-libs -f %{oreon_filedir}/kiten-libs.list
%files -n kiten-devel -f %{oreon_filedir}/kiten-devel.list

%changelog

%autochangelog
