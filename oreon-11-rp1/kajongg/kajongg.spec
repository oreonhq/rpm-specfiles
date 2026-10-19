%global stable_kf6 stable
%global source0_hash b24ebbc30e68f5fd52d180cd2cc2734d481b3d793f084dd6bfc4a19ac3264b99
ExcludeArch: %{ix86}
Name:    kajongg
Summary:        Classical Mah Jongg game for four players
Version: 25.12.3
Release:        1%{?dist}
License: GPL-2.0-only AND GFDL-1.1-or-later
URL:     https://apps.kde.org/kajongg/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
BuildArch: noarch
Patch1: kajongg-20.04.1-KDEPython_paths.patch
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
Requires:      libkmahjongg-data >= %{majmin_ver}
Requires:      python3-twisted >= 16.6.0
Requires: python3-pyqt6
Requires: vorbis-tools
Requires: python3-QtPy
# oreon:deps
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KMahjongglib6)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  libappstream-glib
BuildRequires:  libkmahjongg-devel
BuildRequires:  python3-devel
BuildRequires:  python3-twisted
# /oreon:deps
%description
Kajongg is the ancient Chinese board game for 4 players. Kajongg can
be used in two different ways: Scoring a manual game where you play
as always and use Kajongg for the computation of scores and for
bookkeeping.  Or you can use Kajongg to play against any combination 
of other human players or computer players.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%py_byte_compile %{__python3} %{buildroot}%{_kf6_datadir}/%{name}
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
