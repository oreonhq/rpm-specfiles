%global source0_hash 52badaaa51052470cc604ac32ccb3f993d17933ab0e7af17d2ab1613d77d09ea
%global framework kcompletion
Name:           kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon with auto completion widgets and classes
License:        CC0-1.0 AND LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  cmake(Qt5UiPlugin)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kconfig-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(Qt5Widgets)
# /oreon:deps
%description
KCompletion provides widgets with advanced completion support as well as a
lower-level completion class which can be used with your own widgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(Qt5Widgets)
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang_kf5 kcompletion5_qt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kcompletion-devel -f %{oreon_filedir}/kf5-kcompletion-devel.list

%changelog

%autochangelog
