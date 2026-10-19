%global source0_hash a8e1e054f16760e90d4c830b96d62ed066404f71c01f33e99f472795f9119565
%undefine __cmake_in_source_build
%global framework kwidgetsaddons
Name:           kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with various classes on top of QtWidgets
License:        CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-only AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND LGPL-3.0-or-later AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:            https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Requires:       kf5-filesystem >= %{majmin}
# oreon:deps
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-qttools-static
# /oreon:deps
%description
KDE Frameworks 5 Tier 1 addon with various classes on top of QtWidgets.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{framework}-%{version}

%build

%cmake_kf5
%cmake_build
%install
%cmake_install
%find_lang_kf5 kwidgetsaddons5_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-kwidgetsaddons-devel -f %{oreon_filedir}/kf5-kwidgetsaddons-devel.list

%changelog

%autochangelog
