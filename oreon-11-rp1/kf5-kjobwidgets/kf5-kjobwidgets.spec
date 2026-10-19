%global source0_hash eac37f7d02183f8d4347ab1d86608ee66007a3482a061169e4808caf853dbe87
%undefine __cmake_in_source_build
%global framework kjobwidgets
Name:           kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 2 addon for KJobs
License:        CC0-1.0 AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-3.0-only AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-kcoreaddons-devel
BuildRequires:  kf5-kwidgetsaddons-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qtx11extras-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 2 addon for KJobs

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
Requires:       kf5-kcoreaddons-devel >= %{version}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%find_lang_kf5 kjobwidgets5_qt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kjobwidgets-devel -f %{oreon_filedir}/kf5-kjobwidgets-devel.list

%changelog

%autochangelog
