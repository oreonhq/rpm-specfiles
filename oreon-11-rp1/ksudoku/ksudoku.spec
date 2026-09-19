%global source0_hash 9bbcfa9353f106350b4e9d9782d4b93ce5353106ff97fc5a929292c8ba9a4ff3

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    ksudoku
Summary: A logic-based symbol placement puzzle
Version: 25.12.3
Release: 1%{?dist}

# Automatically converted from old format: GPLv2+ and GFDL - review is highly recommended.
License: GPL-2.0-or-later AND LicenseRef-Callaway-GFDL
URL:     https://invent.kde.org/games/%{name}

%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches (lookaside cache)

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: extra-cmake-modules
BuildRequires: cmake(KF6Archive)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6IconThemes)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6NewStuff)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6XmlGui)

%global majmin_ver %(echo %{version} | cut -d. -f1,2)
BuildRequires: libkdegames-devel >= %{majmin_ver}
BuildRequires: libkdegames-private-devel

BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)

BuildRequires: pkgconfig(gl) pkgconfig(glu)

%description
KSudoku is a logic-based symbol placement puzzle.  The player has to
fill a grid with symbols so that each column, row and block on the game
board contains only one instance of each symbol. In KSudoku the symbols
are usually the numbers 1 to 9, but may be the letters A to P or A to
Y in larger puzzles. Puzzles start with the board partially filled and
it is your job to fill in the rest.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%license COPYING*
%doc README
%{_kf6_bindir}/%{name}*
%{_kf6_metainfodir}/org.kde.%{name}.*.xml
%{_kf6_datadir}/applications/org.kde.%{name}.desktop
%{_kf6_datadir}/icons/hicolor/*/*/*
%{_kf6_datadir}/%{name}/
#{_kf6_datadir}/config.kcfg/%{name}.kcfg
#{_kf6_datadir}/knotifications6/%{name}.notifyrc
%{_kf6_sysconfdir}/xdg/ksudokurc

%changelog
%autochangelog
