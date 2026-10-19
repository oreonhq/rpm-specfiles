%global source0_hash 1663e3c970b84063ece7f28548a87c97bc7592e79da0a0afaa4f6354f8dea30a
%undefine __cmake_in_source_build
%global framework karchive
Name:           kf5-%{framework}
Version: 5.116.0
Release:        1%{?dist}
Summary:        KDE Frameworks 5 Tier 1 addon with archive functions
License:        BSD-2-Clause AND CC0-1.0 AND LGPL-2.0-or-later
URL:            https://invent.kde.org/frameworks/%{framework}
%global majmin 5.116
%global stable stable
Source0:        https://download.kde.org/%{stable}/frameworks/%{majmin}/%{framework}-%{version}.tar.xz
Requires:       kf5-filesystem >= %{majmin}
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  extra-cmake-modules
BuildRequires:  kf5-rpm-macros
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KDE Frameworks 5 Tier 1 addon with archive functions.

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

%{cmake_kf5}
%cmake_build
%install
%cmake_install
%find_lang_kf5 karchive5_qt
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf5-karchive-devel -f %{oreon_filedir}/kf5-karchive-devel.list

%changelog

%autochangelog
