%global source1_hash b99692a68fb2a52868a8bd12c226b35b1a9d484b478afa551f66be29a683ee59
%global source0_hash b17f8242309e1502119c48b1ef5059a396a3068596a84fb79fdef6d9e2cd4f49
%global framework kcrash
%global stable_kf6 stable
%global majmin_ver_kf6 6.30
Name:    kf6-%{framework}
Version: 6.30.0
Release:        1%{?dist}
Summary:        KDE Frameworks 6 Tier 2 addon for handling application crashes
License: CC0-1.0 AND LGPL-2.0-or-later
URL:     https://invent.kde.org/frameworks/%{framework}
Source0:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/frameworks/%{majmin_ver_kf6}/%{framework}-%{version}.tar.xz.sig
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  qt6-qtbase-devel
# /oreon:deps
%description
KCrash provides support for intercepting and handling application crashes.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n kf6-kcrash-devel -f %{oreon_filedir}/kf6-kcrash-devel.list

%changelog

%autochangelog
