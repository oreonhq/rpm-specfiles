%global source1_hash 5f730df6f693410ef85dae08351748b0dc79dbe98f523cd9e116e59c2337f3eb
%global source0_hash 4cf89d91e429d2ece3110e78f7ef7011952b0412cb15011329516b46f21e98e2
%global framework karchive
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:           kf6-%{framework}
Version:        6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 1 addon with archive functions
License:        LGPL-2.0-or-later AND BSD-2-Clause
URL:            https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
Requires:       kf6-filesystem
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
KDE Frameworks 6 Tier 1 addon with archive functions.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       qt6-qtbase-devel
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
%find_lang_kf6 karchive6_qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-karchive-devel -f %{oreon_filedir}/kf6-karchive-devel.list

%changelog

%autochangelog
