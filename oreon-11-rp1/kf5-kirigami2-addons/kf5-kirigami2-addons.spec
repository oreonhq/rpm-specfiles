%global source0_hash 0939bbd80af5f3c64574660ace513884b7331bee8f9886f5dbc8894ca44255fe

%global orig_name kirigami-addons

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kf5-kirigami2-addons
Version:        0.11.0
Release:        9%{?dist}
Epoch:          1
License:        BSD-2-Clause AND CC-BY-SA-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
Summary:        Convergent visual components ("widgets") for Kirigami-based applications
Url:            https://invent.kde.org/libraries/kirigami-addons
Source:         https://invent.kde.org/libraries/%{orig_name}/-/archive/v%{version}/%{orig_name}-v%{version}.tar.gz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf5-rpm-macros
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5Kirigami2)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Quick)
BuildRequires:  cmake(Qt5QuickControls2)

Obsoletes: kf5-kirigami2-addons-dateandtime < 1:0.11.0-2
Provides:  kf5-kirigami2-addons-dateandtime = %{epoch}:%{version}-%{release}
Provides:  kf5-kirigami2-addons-dateandtime%{?_isa} = %{epoch}:%{version}-%{release}

Obsoletes: kf5-kirigami2-addons-treeview < 1:0.11.0-2
Provides:  kf5-kirigami2-addons-treeview = %{epoch}:%{version}-%{release}
Provides:  kf5-kirigami2-addons-treeview%{?_isa} = %{epoch}:%{version}-%{release}

%description
A set of "widgets" i.e visual end user components along with a
code to support them. Components are usable by both touch and
desktop experiences providing a native experience on both, and
look native with any QQC2 style (qqc2-desktop-theme, Material
or Plasma).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{orig_name}-v%{version}

%build
%cmake_kf5
%cmake_build

%install
%cmake_install
%find_lang %{orig_name} --all-name

%files -f %{orig_name}.lang
%doc README.md
%license LICENSES/
%dir %{_kf5_qmldir}/org/kde
%{_kf5_qmldir}/org/kde/kirigamiaddons
%{_kf5_libdir}/cmake/KF5KirigamiAddons

%changelog
%autochangelog
