%global source0_hash b24ebbc30e68f5fd52d180cd2cc2734d481b3d793f084dd6bfc4a19ac3264b99

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    kajongg
Summary: Classical Mah Jongg game for four players
Version: 25.12.3
Release: 1%{?dist}

License: GPL-2.0-only AND GFDL-1.1-or-later
URL:     https://apps.kde.org/kajongg/
Source0: https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildArch: noarch

## upstream patches

## upstreamble patches
# NEEDSWORK: KDEPython.cmake assumes relative paths
Patch1: kajongg-20.04.1-KDEPython_paths.patch

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6SvgWidgets)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KMahjongglib6)
%global majmin_ver %(echo %{version} | cut -d. -f1,2)
# versioned dep often not strictly required -- rex
BuildRequires: libkmahjongg-devel >= %{majmin_ver}
Requires:      libkmahjongg-data >= %{majmin_ver}

BuildRequires: python3-devel
# https://bugzilla.redhat.com/show_bug.cgi?id=1460506
# strictly only a runtime dep, but checked at buildtime for sanity -- rex
BuildRequires: python3-twisted >= 16.6.0
Requires:      python3-twisted >= 16.6.0

# Previously, 'python3-pyqt6-base' was enough, but it isn't any longer.
# It looks for 'PyQt6.QtSvgWidgets' which is not in the base package.
Requires: python3-pyqt6
# for ogg123
Requires: vorbis-tools
Requires: python3-QtPy

%description
Kajongg is the ancient Chinese board game for 4 players. Kajongg can
be used in two different ways: Scoring a manual game where you play
as always and use Kajongg for the computation of scores and for
bookkeeping.  Or you can use Kajongg to play against any combination 
of other human players or computer players.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install
%py_byte_compile %{__python3} %{buildroot}%{_kf6_datadir}/%{name}

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license COPYING*
%license voices/female2/COPYRIGHT
%{_kf6_bindir}/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/

%changelog
%autochangelog
