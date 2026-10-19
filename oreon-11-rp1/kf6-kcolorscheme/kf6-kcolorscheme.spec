%global source1_hash 96e4573e5827cf93f9a53adf4935ac1245636dc666b083073875abba6b227bde
%global source0_hash a4128e82e47cd474c777754c4dd8af28a00a57ecf388da1a62f8173d898890d0
%global framework kcolorscheme
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        Classes to read and interact with KColorScheme
License: BSD-2-Clause and CC0-1.0 and LGPL-2.0-or-later and LGPL-2.1-only and LGPL-3.0-only and (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6GuiAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-private-devel
# /oreon:deps
%description
%summary.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{framework}-%{version} -p1

%build

%cmake_kf6
%{__cmake} --build "%{__cmake_builddir}" %{?_smp_mflags} --verbose
%install
DESTDIR="%{buildroot}" %{__cmake} --install "%{__cmake_builddir}" --verbose
%find_lang kcolorscheme6 --all-name
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kcolorscheme-devel -f %{oreon_filedir}/kf6-kcolorscheme-devel.list

%changelog

%autochangelog
